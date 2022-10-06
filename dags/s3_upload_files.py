from s3_connectors import s3_cl
from itr_creator import itr
from decouple import config

def upload_file_to_s3(bucket_name, s3_client, file):
    """upload data from folder to S3 buket, deleting files from local folder"""
    s3_client.upload_file('/home/ivannikalayeu/Documents/GitHub/Task_8/data/' + file.name, bucket_name, file.name)


def main_upload():
    s3_client = s3_cl()
    bucket_name = config('bucket_name', default='')
    for file in itr():
        upload_file_to_s3(bucket_name, s3_client,file)