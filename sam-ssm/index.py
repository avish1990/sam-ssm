import boto3
import time
import json

def lambda_handler(event, context):
    
    ssm = boto3.client('ssm')
    message = event['Records'][0]['Sns']['Message']
    instanceID = 'i-077cba0abb9f7d184'
    documentName = 'AWS-RunShellScript'
    commandopen = ['iptables -I INPUT -p tcp --dport 8080 -j ACCEPT']
    commandclose  = ['iptables -I INPUT -p tcp --dport 8080 -j DROP']

    if message.lower() == 'start':
        status = ssm.send_command(DocumentName=documentName, TimeoutSeconds=timeout, Parameters={'commands': commandopen}, InstanceIds=[instanceID])
    elif message.lower() == 'stop':
        status = ssm.send_command(DocumentName=documentName, TimeoutSeconds=timeout, Parameters={'commands': commandclose}, InstanceIds=[instanceID])
    else:
        print('Invalid Input')
