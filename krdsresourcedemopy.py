import boto3
iotanalytics = boto3.client("iotanalytics")

def handler(event, context):
    try:
        data = iotanalytics.batch_put_message(
            channelName="kiot",
            messages=[
                {
                    'messageId': "1",
                    'payload': "Test"
                }
            ]
        )
        print(data)
        
    except BaseException as e:
        print(e)
        raise(e)
    
    return {"message": "Successfully executed"}
