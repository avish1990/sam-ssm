#!/bin/bash

#ssh jenkins@10.0.1.2 aws ec2 describe-instances --instance-ids  | grep -i instanceId | awk '{print$2}' | sed -e 's/\"//g' | sed -e 's/,//g' > ./instance.txt

ls ./sam-ssm/
#ssh jenkins@10.0.1.2 aws cloudformation package --template-file ./sam-ssm/example.yaml --output-template-file sam-ssm.yaml --s3-bucket snslambssm

#ssh jenkins@10.0.1.2 aws cloudformation deploy --template-file ./sam-ssm/sam-ssm.yaml --stack-name sam-ssm-lam-deploy --capabilities CAPABILITY_IAM
