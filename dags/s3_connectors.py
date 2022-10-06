import boto3
from decouple import config


def s3_res(AWS_REGION = config('aws_region', default=''),
           AWS_ACCESS_KEY_ID= config('aws_access_key_id', default=''),
           AWS_SECRET_ACCESS_KEY=config('aws_secret_access_key', default='')):
    """creating .resource connection"""
    return boto3.resource("s3",
                          region_name=AWS_REGION,
                          endpoint_url='http://localhost:4566',
                          use_ssl=False,
                          aws_access_key_id=AWS_ACCESS_KEY_ID,
                          aws_secret_access_key=AWS_SECRET_ACCESS_KEY)



def s3_cl(AWS_REGION = config('aws_region', default=''),
           AWS_ACCESS_KEY_ID= config('aws_access_key_id', default=''),
           AWS_SECRET_ACCESS_KEY=config('aws_secret_access_key', default='')):
    """create .client connection"""
    return boto3.client("s3",
                        region_name=AWS_REGION,
                        endpoint_url='http://localhost:4566',
                        use_ssl=False,
                        aws_access_key_id=AWS_ACCESS_KEY_ID,
                        aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

