# ml  
(mlwaf/ml)     



- svc_sklearn_jsonlist.ipynb
sagemaker notebook에서 실행     

- endpoint-one-model.yml     

aws cloudformation으로 앤드포인트 쉽게 deploy하기 위한 yml 파일
훈련작업 : svc-custom-sklearn-2023-12-02-16-15-36-841/
```
SAGEMAKER_SUBMIT_DIRECTORY: s3://sagemaker-ap-northeast-2-918934048065/svc-custom-sklearn-2023-12-02-16-15-36-841/source/sourcedir.tar.gz
```


- create-stack.py 
해당 탬플릿을  aws cloudformation에서 올릴수 있도록 하는 파이썬 코드
훈련작업 : svc-custom-sklearn-2023-12-02-16-15-36-841/
```
trainingJobName = "svc-custom-sklearn-2023-12-02-16-15-36-841"
```

endpoint-one-model.yml에 해당부분과 create-stack.py 훈련작업 일치해야함