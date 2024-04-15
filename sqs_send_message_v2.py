import boto3

def send_message():
    sqs_client = boto3.client('sqs', region_name='us-east-1')
    queue_url='https://sqs.us-east-1.amazonaws.com/146270615771/myqueue'
    for x in range(3):
        response = sqs_client.send_message(
            QueueUrl=queue_url,
            DelaySeconds=10,
            MessageBody=(
                str(x)+" - mensagem"
            )
        )
        print(response)

if __name__ == '__main__':

    response = send_message()
