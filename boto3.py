import boto3
s3 = boto3.client('s3')
DEST_BUCKET = "suraj-resized-results-unique"
def lambda_handler(event, context):
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    copy_source = {
        'Bucket': source_bucket,
        'Key': key
    }
    s3.copy_object(
        Bucket=DEST_BUCKET,
        CopySource=copy_source,
        Key="processed-" + key
    )
    return {
        "statusCode": 200,
        "body": "Image processed successfully"
    }
