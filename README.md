# 셀레니움을 활용한 웹 매크로

그래픽카드를 특가로 사기 위해 7일간 셀레니움 공부를 하게 되었습니다...

## 준비하기

### 1. Selenium 설치
+ pip 명령어를 사용해서 설치한다.
```
pip install selenium
```
### 2. WebDriver 설치
+ 크롬 버전 확인
  + ``` 더보기 → 설정 → Chrome 정보``` 로 크롬 버전을 확인한다.
 ![image](https://user-images.githubusercontent.com/88234731/155141104-55c61c19-4596-41d1-9955-ddc1d570c1f5.png)
+ WebDriver 설치
  + [chromedriver 링크](https://chromedriver.chromium.org/downloads)로 들어간다.
  + ```98.0.~~~``` 이므로 98버전을 설치한다.
  ![image](https://user-images.githubusercontent.com/88234731/155143294-68d71f09-030e-4f2b-bd3a-e98914e87acc.png)

## 셀레니움 시작
>### 다운받은 chromedriver.exe를 파일에 넣어준다.
>>![image](https://user-images.githubusercontent.com/88234731/160397814-24e6a884-2f7a-46ab-b0d0-e41a1c55ebe9.png)
>### 셀레니움 기본 코드(Import)를 입력한다.
>>![image](https://user-images.githubusercontent.com/88234731/160399597-829cc2c6-61ca-4312-8e04-996a8f9565db.png)
>### 크롤링 할 주소를 <b>browser.get</b>에 입력한다.
>>![image](https://user-images.githubusercontent.com/88234731/160399990-1418da89-5eb8-4726-91c1-2fb9afa2ac97.png)
>### 필요에 따라 이미지를 차단하는 코드도 입력한다.
>>![image](https://user-images.githubusercontent.com/88234731/160401146-543af412-fcb1-40a9-93ab-b41897ac0d99.png)
>### browser.find_element를 사용하여 클릭, 키보드입력 같은행동을 할 수 있다.
>>![image](https://user-images.githubusercontent.com/88234731/160405397-8e6f54cb-1c8a-4c1a-aab1-2ad54edecd77.png)
><br>
### 위 코드를 활용하여 인터파크 자동구매 매크로를 만들었습니다.
![image](https://user-images.githubusercontent.com/88234731/160406753-0fe4d72b-ebbc-4348-befe-50cf694e6c2c.png)

