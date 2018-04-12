# Script to create aliases for previous version of Lambda.
#!/bin/bash

version=`aws lambda get-alias --name prod --function-name SSM | grep FunctionVersion | sed -e 's/\"//g' |  awk '{print$2}' | sed -e 's/,//g'`
prevversion=`expr $version - 1`
echo "$prevversion"
