# sam-ssm
Creates a Lambda function and SNS Topic which runs SSM Document on AWS EC2 instance to configure Iptable rules. 

avish-port.yaml --> AWS SSM Document
example.yaml --> Lambda SAM Template with versioning.
index.py --> Script to run SSM Doc on EC2 base on SNS trigger ACCEPT/DROP.
pipelinejobconfig --> Jenkins pipeline job config.
version.sh --> Script to create aliases for previous versions of Lambda.
