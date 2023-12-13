#!/bin/bash

# Run the Python script to create the CloudFormation stack
# create-stack.py 스크립트 파일이 ml 폴더 안에 있음
python ml/create-stack.py

# Replace YourStackName with the actual name of your CloudFormation stack
STACK_NAME="endpoint-one-model-test3"

# Check the status of the CloudFormation stack creation
# You can replace "YourStackName" with your actual stack name
aws cloudformation wait stack-create-complete --stack-name $STACK_NAME

# Fetch the necessary information from the CloudFormation stack outputs
ENDPOINT_ID=$(aws cloudformation describe-stacks --stack-name $STACK_NAME --query 'Stacks[0].Outputs[?OutputKey==`EndpointId`].OutputValue' --output text)
ENDPOINT_NAME=$(aws cloudformation describe-stacks --stack-name $STACK_NAME --query 'Stacks[0].Outputs[?OutputKey==`EndpointName`].OutputValue' --output text)


# Set environment variables
export REQUEST_PATH="/endpoints/$ENDPOINT_NAME/invocations"

# Run docker-compose up -d
docker-compose up -d