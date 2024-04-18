import boto3

def list_s3():
    s3_client = boto3.resource('s3')
    print('Listando Buckets')
    for buckets in s3_client.buckets.all():
        print(f"\t{buckets.name}") 


if __name__ == '__main__': 
    response = list_s3()
