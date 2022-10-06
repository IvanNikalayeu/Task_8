from airflow import DAG
from datetime import datetime, timedelta
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator

from spark_agg_upload import main_spark
from s3_create_bucket import s3_create_bucket
from s3_upload_files import main_upload
from del_file import main_del


default_args = {
    'owner': 'airflow',
    'start_date': days_ago(0),
    'depends_on_past': False,
}


with DAG(
    'S3_DAG',
    default_args=default_args,
    schedule_interval='@daily',
    start_date=days_ago(1)
) as dag:

    create_bucket = PythonOperator(
        task_id='create_bucket',
        python_callable=s3_create_bucket,

    )

    spark_agg = PythonOperator(
        task_id='spark_agg',
        python_callable=main_spark,

    )

    s3_upload = PythonOperator(
        task_id='s3_upload',
        python_callable=main_upload,
    )

    uploaded_del = PythonOperator(
        task_id='del_local_uploaded_file',
        python_callable=main_del
    )

    create_bucket >> \
    [spark_agg, s3_upload] >> uploaded_del
