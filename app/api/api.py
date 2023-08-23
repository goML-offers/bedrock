
import boto3
import json
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

AWS_ACCESS_KEY_ID = os.environ.get("aws_access_key_id")
AWS_SECRET_ACCESS_KEY_ID = os.environ.get("aws_secret_access_key")


bedrock = boto3.client(aws_access_key_id=AWS_ACCESS_KEY_ID, 
                      aws_secret_access_key=AWS_SECRET_ACCESS_KEY_ID,
                      service_name='bedrock',region_name='us-west-2',
                      endpoint_url='https://bedrock.us-west-2.amazonaws.com')

def aws_titan_summarisation(payload):
    text=payload['text']
    summary="write summary:"
    body = json.dumps({"inputText": summary+text})
    modelId = 'amazon.titan-tg1-large' # change this to use a different version from the model provider
    accept = 'application/json'
    contentType = 'application/json'

    response = bedrock.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)
    response_body = json.loads(response.get('body').read())

    result=response_body.get('results')[0].get('outputText')
    return {'output':result}
