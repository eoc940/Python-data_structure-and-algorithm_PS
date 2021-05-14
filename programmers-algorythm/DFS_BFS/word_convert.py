# 단어 변환

def solution(begin, target, words):
    # 전역변수가 없을 때 함수 안에서 global을 써주면 전역변수가 된다
    global answer
    answer = 0
    # ch는 한번 탐색한 단어를 다시 탐색하지 않도록 체크하기 위한 리스트
    ch = [0]*len(words)

    def DFS(w,ans) :
        # 여기서의 global answer는 solution함수에서 선언된 전역변수 answer를 전역변수로 사용하겠다는 의미이다
        global answer

        # 탐색한 단어와 타겟이 같다면 탐색 횟수(ans)를 answer에 넣어준다
        if w==target :
            answer = ans
            return
        else :
            tmp = []
            for word in words :
                # 만약 탐색이 이미 이루어진 단어를 제외한다
                if ch[words.index(word)] != 0 :
                    continue

                cnt = 0
                # 탐색한 단어와 기준 단어에서 다른 알파벳이 나올때마다 cnt에 1을 더한다
                for i in range(len(w)) :
                    if w[i]!=word[i] :
                        cnt += 1
                # 알파벳 하나만 다를때 단어의 인덱스에 체크해주고 tmp에 단어를 넣어준다
                if cnt==1 :
                    ch[words.index(word)] = 1
                    tmp.append(word)
            # tmp에 있는 단어를 전부 dfs로 돌려준다. 이때 ans(탐색 횟수)를 1 증가시켜준다
            for x in tmp :
                DFS(x, ans+1)
    # 시작 문자와 탐색 횟수 즉 0을 초기값으로 넣고 dfs를 호출
    DFS(begin, 0)

    return answer


b ="hit"
t ="cog"
w =["hot", "dot", "dog", "lot", "log", "cog"]

print(solution(b,t,w))
print(answer)


