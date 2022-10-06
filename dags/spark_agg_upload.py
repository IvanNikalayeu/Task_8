from io import StringIO
from pyspark.sql import SparkSession
from decouple import config
import pyspark.sql.functions as F
from itr_creator import itr
import s3_connectors
import os



def spark_df(spark, file):
    """reading csv file"""
    df = spark.read.csv('/home/ivannikalayeu/Documents/GitHub/Task_8/data/' + file.name, header=True)
    return df

def spark_transform(df):
    """aggregating df"""
    output = (
        df
        .groupBy('departure_id')
        .agg(
            F.count('departure').alias('num_of_dep'),
            F.count('return').alias('num_of_ret')
        )
        .toPandas()
    )
    return output


def df_upload_to_s3(output, file, bucket_name=config('bucket_name', default='')):
    """uploading file to S3"""
    csv_buffer = StringIO()
    output.to_csv(csv_buffer)
    s3_resource = s3_connectors.s3_res()
    s3_resource.Object(bucket_name, 'agg'+file.name).put(Body=csv_buffer.getvalue())


def main_spark():
    spark = SparkSession.builder.getOrCreate()
    for file in itr():
        df = spark_df(spark, file)
        output = spark_transform(df)
        df_upload_to_s3(output=output, file=file)



