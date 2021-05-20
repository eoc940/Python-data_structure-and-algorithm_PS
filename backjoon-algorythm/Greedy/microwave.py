# 전자레인지

import sys

n = int(sys.stdin.readline())
# 각 버튼별로 횟수를 저장하기 위해 dictionary를 만듬
count_dict = dict()

# 만약 버튼 중 가장 작은 값인 10으로도 나누어지지 않는다면 -1를 출력
if n%10 != 0 :
    print(-1)
# 10으로 나누어지는 경우
else :
    # A버튼을 누른 횟수는 전체 초에서 5분(300초)로 나눈 몫이다
    count_dict['A'] = n//300
    # A라는 key로 값을 저장한 후 전체 계산할 초에서 앞서 들어간 값만큼 빼준다
    n = n-300*count_dict.get('A')

    # B버튼을 누른 횟수는 전체 초에서 1분(60초)로 나눈 몫이다
    count_dict['B'] = n // 60
    # B라는 key로 값을 저장한 후 전체 계산할 초에서 앞서 들어간 값만큼 빼준다
    n = n - 60 * count_dict.get('B')

    # C버튼을 누른 횟수는 전체 초에서 10초로 나눈 몫이다
    count_dict['C'] = n // 10
    # C라는 key로 값을 저장한 후 전체 계산할 초에서 앞서 들어간 값만큼 빼준다
    n = n - 10 * count_dict.get('C')

    # dictionary에 있는 value들을 출력한다
    for x in count_dict.values() :
        print(x, end=" ")




