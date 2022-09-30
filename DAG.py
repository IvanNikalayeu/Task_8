from airflow import DAG
from datetime import datetime

default_args = {
    'start_date': datetime(2022, 10, 1),
    'owner': 'airflow'
}

dag = DAG(
    'first_dag',
    default_args=default_args,
    schedule_interval=None
)
