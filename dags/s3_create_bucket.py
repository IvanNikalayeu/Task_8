from decouple import config
from s3_connectors import s3_res


def s3_create_bucket():
    """creating bucket"""
    s3_resource = s3_res()
    location = {'LocationConstraint': config('aws_region', default='')}
    bucket = s3_resource.create_bucket(
        Bucket=config('bucket_name', default=''),
        CreateBucketConfiguration=location)
