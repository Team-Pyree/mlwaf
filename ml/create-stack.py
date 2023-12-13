import boto3
import os

# trainingJobName = "svc-custom-sklearn-2023-11-28-07-44-26-206"
trainingJobName = "svc-custom-sklearn-2023-12-02-16-15-36-841"
# trainingJobName = "svc-custom-sklearn-2023-12-02-16-15-36-841"

print(trainingJobName)
# use_custom_endpoint_name = True
sm = boto3.client("sagemaker")

job = sm.describe_training_job(TrainingJobName=trainingJobName)
trainingImage = job['AlgorithmSpecification']['TrainingImage']
modelDataUrl  = job['ModelArtifacts']['S3ModelArtifacts']
roleArn       = job['RoleArn']
program = job['HyperParameters']['sagemaker_program'].replace('"', '')
directory = job['HyperParameters']['sagemaker_submit_directory'].replace('"', '')

cf = boto3.client("cloudformation")

# with open("endpoint-one-model.yml", "r") as f:
with open("./ml/endpoint-one-model.yml", "r") as f:
	stack = cf.create_stack(StackName="endpoint-one-model-deploy", 
			TemplateBody=f.read(),
			Parameters=[
			{"ParameterKey":"ModelName",     "ParameterValue":trainingJobName},
			{"ParameterKey":"TrainingImage", "ParameterValue":trainingImage},
			{"ParameterKey":"ModelDataUrl",  "ParameterValue":modelDataUrl},
			{"ParameterKey":"ModelProgram",  "ParameterValue":program},
   			{"ParameterKey":"ModelDirectory",  "ParameterValue":directory},
			{"ParameterKey":"RoleArn",       "ParameterValue":roleArn}],
		Tags=[
			{"Key": "group", "Value": "pyree"}, ])
	print(stack)



# # Extract outputs from the stack
# outputs = stack.get('Outputs', [])
# print("Outputs:", outputs)

# # Set outputs as environment variables
# for output in outputs:
# 	key = output['OutputKey']
# 	value = output['OutputValue']
# 	os.environ[key] = value
# 	print(f"Set environment variable: {key}={value}")

# print("Stack created successfully.")
    
# waf_file_path = "../waf.env"  # Change this path based on your actual directory structure
# sagemaker_endpoint_name = os.environ.get('EndpointName', '')

# with open(waf_file_path, "r") as waf_file:
#     lines = waf_file.readlines()

# with open(waf_file_path, "w") as waf_file:
#     for line in lines:
#         if line.startswith("REQUEST_PATH="):
#             # Update the existing REQUEST_PATH line
#             waf_file.write(f"REQUEST_PATH=/endpoints/{sagemaker_endpoint_name}/invocations\n")
#         else:
#             # Keep other lines unchanged
#             waf_file.write(line)

# print(f"{waf_file_path} file updated with SAGEMAKER_ENDPOINT_NAME.")





"""[og_code]"""

# import boto3

# trainingJobName = "xgboost-2019-05-09-15-20-51-276" 

# print(trainingJobName)

# sm = boto3.client("sagemaker")

# job = sm.describe_training_job(TrainingJobName=trainingJobName)
# trainingImage = job['AlgorithmSpecification']['TrainingImage']
# modelDataUrl  = job['ModelArtifacts']['S3ModelArtifacts']
# roleArn       = job['RoleArn']

# cf = boto3.client("cloudformation")

# with open("endpoint-one-model.yml", "r") as f:
# 	stack = cf.create_stack(StackName="endpoint-one-model", 
# 		   TemplateBody=f.read(),
# 		   Parameters=[
# 			{"ParameterKey":"ModelName",     "ParameterValue":trainingJobName},
# 			{"ParameterKey":"TrainingImage", "ParameterValue":trainingImage},
# 			{"ParameterKey":"ModelDataUrl",  "ParameterValue":modelDataUrl},
# 			{"ParameterKey":"RoleArn",       "ParameterValue":roleArn} ])
# 	print(stack)

