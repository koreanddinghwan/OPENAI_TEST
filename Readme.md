# OpenAI Exercise

## Key Concepts

### 1. Prompt

GPT를 적절하게 사용하기위한 지침.  
적절하게 사용하기위해서는, 원하는 것을 정확하게 묘사해야한다.

<br>

1. Show and Tell

   - 명령어나 예시, 혹은 둘 모두를 혼합해서 원하는 것을 정확하게 말해야한다.

2. Provide Quality Data

   - 모델이 패턴을 따르도록 하려면 충분한 예제를 만들고, 이 예제를 교정해야한다.

3. Check your settings
   - 다양한 응답에 대해서는 temperature, top_p를 높게, 정답이 하나인 경우 응답을 원한다면 낮게설정한다.

이것이 ChatGPT로 프로그래밍하는 방법이며 이렇게 prompt가 설정되면 거의 모든 작업을 할 수 있다.

<br><br>

### 2. Tokens

문자열을 Token으로 나누어서 처리한다.  
Token은 단어, 혹은 문자열이 작게 나뉜 것이다.

`hamburger`와 같은 단어가 있다면, `ham`, `bur`, `gur`와 같은 token으로 나누어지며,

`pear`는 1개의 token으로 처리될 수 있다.

<br>

한 개의 API요청에서 처리되는 토큰의 수는 입-출력의 길이에 따라 달라진다.

대략, `1개 토큰은 4 character, 0.75word`정도이다.

대부분 모델의 경우, 2048개 토큰, 약 1500word를 넘지 않아야한다.

<br><br>

### 3. Models

openAI에는 다양한 기능, 가격대를 가진 모델이 있으며, GPT-4가 가장 강력한 최신모델이다.

<br>

GPT-3.5-turbo는 대화형에 최적화된 모델이다.

<br><br>

## Exercise01

<img width="1680" alt="스크린샷 2023-03-21 15 00 18" src="https://user-images.githubusercontent.com/76278794/226529240-4f8e130b-fd14-49d1-80a6-e49c3e40175c.png">
