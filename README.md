# MLWAF 프로젝트

## 프로젝트 설명
**Nginx event driven/async IO 구조를 이용한 ML endpoint rest API 호출 및 MySQL 
DB Insert를 통한 고성능 방화벽 구현**


<img width="1170" alt="image" src="https://github.com/Choitim/mlwaf/assets/75467180/2a6150ee-93f2-49ff-98d5-32ceab6dd9a0">
<img width="1137" alt="image" src="https://github.com/Choitim/mlwaf/assets/75467180/7f97feff-5d06-47c6-a3d0-d17bb4e07961">
<img width="1125" alt="image" src="https://github.com/Choitim/mlwaf/assets/75467180/cc997a4e-2cdd-4f68-8132-424c6a210076">

## 개발 환경
<div>
  <img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white">
  <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white">
  <img src="https://img.shields.io/badge/lua-2C2D72?style=for-the-badge&logo=lua&logoColor=white">
  <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white">
  <img src="https://img.shields.io/badge/flask-000000?style=for-the-badge&logo=flask&logoColor=white">
  <img src="https://img.shields.io/badge/nginx-009639?style=for-the-badge&logo=nginx&logoColor=white">
  <img src="https://img.shields.io/badge/aws-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white">
  <img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white">
  <img src="https://img.shields.io/badge/sqlite-003B57?style=for-the-badge&logo=sqlite&logoColor=white">
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white">
</div>


## 설치 방법
이 프로젝트를 설치하기 위해서는 다음 단계를 따라야 합니다:
1. Git 저장소를 클론합니다: `git clone [repository-url]`
2. 필요한 환경 변수 파일(`.env`)을 설정합니다.
>- dash.env, waf.env, db.env 파일을 만들어서 환경변수를 설정해줍니다.
3. Docker를 사용하여 컨테이너를 구축 및 실행합니다: `docker-compose up` 또는  `docker-compose up -d`를 터미널에 입력합니다.

**AWS endpoint URL이 필수적으로 필요합니다**

## 사용 방법
이 프로젝트를 사용하기 위한 단계는 다음과 같습니다:
1. 웹 대시보드를 통해 사용자 인터페이스에 접근합니다.
2. 필요한 설정을 조정하고 프로젝트를 시작합니다.
3. 로그 및 보안 관련 데이터를 모니터링합니다.
4. AWS Endpoint를 호출하기 위해서는 WAF.env 파일에 aws api 정보를 입력한다
> 예시) <br/>
>- AWS_HOST= {your sagemaker host url} <br/>
>- AWS_KEY= {your key} <br/>
>- AWS_SECRET= {your secret Key}<br/>
>- AWS_REGION= {your location}<br/>
>- AWS_SERVIC=sagemaker<br/>
>- CONTENT_TYPE=application/json<br/>
>- REQUEST_METHOD=POST<br/>
>- REQUEST_PATH= {작성}<br/>

### 테스트 환경
- http://localhost:9090으로 접속하여 테스트 웹 환경을 띄운다.
- 로그인이나, 사진 업로드 기능에 공격구분을 넣어본다.
- http://localhost:9093 으로 접속하여 어떤 공격인지 확인해본다. 

## 시연
<a href="https://youtu.be/NP9f0EE6JF8">
<img src="https://img.shields.io/badge/youtube-FF0000?style=for-the-badge&logo=youtube&logoColor=white">
</a>
<br/>
<br/>

### 업데이트 된 대쉬보드
<img width="1440" alt="image" src="https://github.com/Choitim/mlwaf/assets/75467180/ffc40047-feac-4f2d-9002-906abb6455ed">

## 팀원

<table>
  <tr>
    <td>
      <strong>최경록(dev.choi28)</strong>
    </td>
    <td>
      <strong>장석희</strong>
    </td>
     <td>
      <strong>김소희</strong>
    </td>
     <td>
      <strong>박도은</strong>
    </td>
  </tr>
  <tr>
    <td>
        <a href="https://github.com/Choitim"><img src="https://github.com/Choitim/KISIA_2023_Hackathon_MCPG/assets/75467180/0ef0da9d-6b9c-4914-8a49-ad44478cca4f" width="280"/>
        </a>
    </td>
    <td>
      <img width="230" alt="image" src="https://github.com/Choitim/mlwaf/assets/75467180/9d2a3b0c-464f-47cc-84d3-7376dbf4b224">
    </td>
     <td>
      <img width="227" alt="image" src="https://github.com/Choitim/mlwaf/assets/75467180/ada89ed1-d570-4a99-b746-8b91449455e1">
    </td>
     <td>
      <img width="228" alt="image" src="https://github.com/Choitim/mlwaf/assets/75467180/8cb6f097-062c-4fbf-b121-e9a94fb4b916">
    </td>
    
  </tr>
  
  <tr>
    <td>
      - <strong>개발언어</strong>: Nginx, Lua, Django, Flask <br>
      - <strong>Nginx 기반 Waf 개발 </strong>
    </td>
    <td>
      - <strong>개발언어</strong>: Python, Lua, Jupyter Notebook <br>
      - <strong> ML 모델 개발 </strong>
    </td>
    <td>
      - <strong>개발언어</strong>: SQL, MySQL, Lua, python<br>
      - <strong> DB 설계, Infrastructure Design </strong>
    </td>
    <td>
      - <strong>개발언어</strong>: SQL, MySQL, Lua, python<br> <br>
      - <strong> ML 알고리즘 테스트 및 적용, DB 설계 </strong>
    </td>
    
  </tr>

  <tr>
    <td>
      <div>
        <a href="https://github.com/Choitim"><img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white"/></a>
      </div>
    </td>
    <td>
      <a href="https://github.com/seok-hee97"><img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white"/></a>
    </td>
    <td>
      <a href="https://github.com/so-heekim"><img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white"/></a>
    </td>
    <td>
      <a href="https://github.com/P-DOEUN"><img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white"/></a>
    </td>
  </tr>
</table>

## 라이선스
<img width="162" alt="image" src="https://github.com/Choitim/mlwaf/assets/75467180/d61d8ea4-b81e-45a6-8a1c-c52d0dbe0e5d"> </br>
Copyright (c)[2023][파이리]
