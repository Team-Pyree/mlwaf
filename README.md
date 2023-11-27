개요
==========
* docker-compose 를 이용하여, WAF/ML/WEB 3개의 container로 구성된 nginx lua API호출 예제 테스트베드


전체 구조
============
* 아래 3개의 container로 구성
  * WAF:
    * 웹 클라이언트의 웹 요청을 파싱하여, 헤더 요청 데이터를 추출하여, ML컨테이너에 REST API호출을 하고 호출 결과에 따라 차단하거나 혹은 원래 서버 (upstream server) 로 원본 클라이언트 요청을 그대로 전송
    * nginx 기반으로 lua script을 이용하여 구현
  * ML:
    * ML API endpoint emualation 컨테이너
    * WAF에서 호출된 rest API에 대해서 json 응답 ( 현재 예제는 항상 { result: ok } 값 return)
  * WEB:
    * 일반 웹서버 컨테이너. 웹 클라이언트의 정상적인 요청에 대한 사용자 컨텐츠를 응답하는 웹서버
    * nginx 로 구현


사용자 가이드
=============
* Linux 터미널 환경에서 docker-compose 명령을 실행 가능한 상태로 사전 준비
* 터미널에서 "docker-compose up -d" 명령 실행
* wget 명령을 이용하여 "wget http://127.0.0.1:9090/" 명령어로 정상 응답 확인 및 waf/logs/error.log 및 ml/logs/error.log 로그 파일에 정상적으로 로그가 남는지 확인


구현 관련 이슈
==============
* docker container의 내부 IP 주소를 lua 및 nginx 설정 파일에 반영
** envioronment variable => nginx 변수 생성 => nginx 설정 파일에서 nginx 변수 참조 및 lua script에서 nginx 변수 참고 api를 이용하여 변수 값 접근


개선 필요 사항
=============
* 본 구현 코드는 nginx lua의 기능 evaluation을 위한 POC 개념의 코드로, 대부분의 예외 처리에 대한 고려 및 성능/안정성에 대한 고려가 되어 있지 않으므로, 본격적으로 실망 사이트에 적용하기 위해서는 예외처리 향상이나 성능/안정성 등에 대한 추가 고려 및 구현이 필ㅇ
* lua libraray등의 static contents에 대해서는 Dockerfile 을 이용하여, 신규 이미지를 build 하여 배포 필요
