# Project Codegay

![gay for my code](http://38.media.tumblr.com/125a0617d8986ad521772f0f42aa56db/tumblr_n68390DBXL1t9w6i8o1_500.gif)

## 규칙 (Updated at 2016. 10. 31)
- 매일 커밋 하나

## 기록
- 11/01: Retention은 보통 시간이 오래걸려서인지 배치잡을 선호하고, 앱당 리텐션 구하는데 하루 7000명 정도 Cohort면 mySQL로 2분, Redshift로 10초 정도 걸린다. 
- 11/01: `from datetime import datetime`에는 `dt.date()`, `dt.time()`이 있고, `from datetime import timedelta`를 사용해 `dt+timedelta(days=2)` 이런식으로 시간을 조작할 수 있다.
- 10/31: Udemy spark 강의를 듣다가, spark가 빠른 이유가 DAG(Directed Acyclic Graph) 때문이라고 들음. [DAG](https://github.com/HunjaeJung/py-dag) Github 소스를 찾아 Test 코드만 보고 [소스를 구현](https://github.com/HunjaeJung/codegay/data-structue/py-dag) 중. nose 테스트의 새로운 면모를 발견.
- 10/31: SQL 작성시 `DATE_FORMAT(..)` 이런식으로 Date formating 자꾸 해주기 귀찮은데 Function으로 만들어버릴 수 있다.
