# handler.py



def handler(event, context):
    print(event)
    print(context)

    return {
        'statusCode': 200,
        'body': "success"
    }