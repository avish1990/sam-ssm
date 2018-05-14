import boto3

def handler(event, context):    

  client = boto3.client('rds')
  message = event['Records'][0]['Sns']['Message']
  message = message.lower()
  if message == "start":
    response = client.start_db_instance(DBInstanceIdentifier='avishdb')
  elif message == "stop":
    response = client.stop_db_instance(DBInstanceIdentifier='avishdb')

