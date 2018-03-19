import boto3
import time
import json
import sys

def handler(event, context):

    ssm = boto3.client('ssm')
    message = event['Records'][0]['Sns']['Message']
    documentName = 'avish-port'
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()
    for r in response['Reservations']:
      for instance in r['Instances']:
        instanceid = instance['InstanceId']
        status = ssm.send_command(DocumentName=documentName,  Parameters={'Rule': [message.upper()]},  InstanceIds=[instanceid])
