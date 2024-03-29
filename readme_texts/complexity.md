#### 복잡도(Complexity)
- 복잡도는 알고리즘의 성능을 나타내는 척도
- 시간 복잡도 : 특정한 크기의 입력에 대하여 알고리즘의 수행 시간 분석
- 공간 복잡도 : 특정한 크기의 입력에 대해서 알고리즘의 메모리 사용량 분석
- 동일한 기능을 수행하는 알고리즘이 있다면 일반적으로 복잡도가 낮을수록 좋은 알고리즘

#### 빅오 표기법(Big-O Notation)
- 가장 빠르게 증가하는 항만을 고려하는 표기법
- 함수의 상한만을 나타냄
- 예를 들어 연산 횟수가 3N<sup>3</sup> + 5N<sup>2</sup> + 100000인 경우 차수가 가장 큰 항만 남겨서 O(N<sup>3</sup>)으로 표현한다
- O(1) : 상수 시간, O(logN) : 로그 시간, O(N) : 선형 시간, O(NlogN) 로그 선형 시간, O(N<sup>2</sup>) : 이차 시간, O(N<sup>3</sup>) : 삼차 시간, O(2<sup>n</sup>) : 지수 시간 -> 뒤로 갈수록 나쁨

#### 수행 시간 측정
```
import time
start_time = time.time()

# 프로그램 소스코드
end_time = time.time()
print("time : ", end_time - start_time)
```
