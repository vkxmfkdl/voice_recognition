# 프로젝트 소개

1. 프로젝트 명 : voice_recognition

2. 팀원:  박경민, 고민재, 공민철

3. 프로젝트 소개: 음성인식을 통한 회의 내용 기록 프로그램

4. 개발기간: 2019.09~2019.10

5. 데모영상: https://www.youtube.com/watch?v=MR41moiE5rA

## 구글 Cloud 음성인식 API

https://webnautes.tistory.com/1247 참조

# 실행화면

<b>메인페이지</b>

<img src="https://user-images.githubusercontent.com/37204852/79060111-2e421500-7cbc-11ea-8d7b-47c806cc2bdf.png"/>

<b>회의기록, 감성분석</b>

<img src="https://user-images.githubusercontent.com/37204852/79060202-2df64980-7cbd-11ea-8f40-7404b85c1416.png"/>

<b> 분석결과 1</b>

<img src="https://user-images.githubusercontent.com/37204852/79060239-cc82aa80-7cbd-11ea-8b9a-f7c97c168342.png"/>

<b> 분석결과 2</b>

<img src="https://user-images.githubusercontent.com/37204852/79060259-0358c080-7cbe-11ea-9f09-9d84485a595c.png"/>

## 실행법

윈도우 환경에서 작성되었습니다.

1. 아나콘다3 파이썬이 설치되어 있어야합니다.

2. `conda env create -f requirements.yml` 명령어로 가상환경을 설치합니다

3. `conda activate voiceenv` 명령어로 가상환경을 실행시킵니다.

4. 음성인식을 구동시키려면 개인 컴퓨터에 구글 음성인식 api가 설치되어 있어야합니다.

5. 음성분석을 하기 위해서는 uploadproject 폴더로 들어가 `python manage.py runserver` 명령어를 실행하면 됩니다.

6. 웹 페이지 접속 기본 url은 localhost:8000 입니다. 이는 실행하는 사람의 환경에 따라 다를 수도 있습니다.

* 음성인식api를 사용하지 않고 테스트하고자 하시면  voice_recognition\uploadproject\media 에 오늘 날짜로 폴더를 만들고 
  다른 폴더에 있는 .json파일을 복사하시면 테스트할 수 있습니다.
