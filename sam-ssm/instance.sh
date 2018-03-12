#!/bin/bash


ssh jenkins@10.0.1.2 "aws ec2 describe-instances --instance-ids  | grep -i instanceId | awk '{print$2}' | sed -e 's/\"//g' | sed -e 's/,//g'" > ./instance.txt
