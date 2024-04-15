
import boto3

def consume_queue():
    sqs_client = boto3.client('sqs', region_name='us-east-1')
    while True:

        response = sqs_client.receive_message(
            QueueUrl="https://sqs.us-east-1.amazonaws.com/146270615771/myqueue",
            MaxNumberOfMessages=10,
            WaitTimeSeconds=10
        )
        
        if "Messages" not in response:
            print("fim das mensagens")
            break

        print("Recebendo Mensagens")
        messages = response['Messages'][0]
        receipt_handle = messages['ReceiptHandle']
        sqs_client.delete_message(
            QueueUrl="https://sqs.us-east-1.amazonaws.com/146270615771/myqueue",
            ReceiptHandle=receipt_handle
        )
        x = str(response)
        print(x)
        print (messages['Body'])
   

if __name__ == '__main__':

    response = consume_queue()
