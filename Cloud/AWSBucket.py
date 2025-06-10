import boto3
from botocore import UNSIGNED
from botocore.client import Config

s3 = boto3.client('s3', config=Config(signature_version=UNSIGNED))
bucket_obj = s3.list_objects_v2(Bucket="coderbytechallengesandbox")
for obj in bucket_obj:
    print(obj.contents)
    if obj.startswith("__cb__"):
        content = obj.get()['Body'].read()
        content += '4ez5amf76'
        print(content)
        newstr = ''.join("X" if i % 3 == 0 else char for i, char in enumerate(content, 1))
        print(newstr)
