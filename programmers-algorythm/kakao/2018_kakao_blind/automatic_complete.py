# 자동완성

from collections import defaultdict

def make_trie(words):
    dic = dict()
    for word in words:
        cur_dic = dic
        for letter in word:
            # print(cur_dic)
            # print(dic)
            # print(id(dic), id(cur_dic))
            cur_dic.setdefault(letter, [0,{}])
            cur_dic[letter][0] += 1
            cur_dic = cur_dic[letter][1]
        # print(dic)
    return dic

def solution(words):
    answer = 0
    trie = make_trie(words)

    for word in words:
        tmp = trie
        for letter in word:
            answer += 1
            tmp = tmp[letter]
            if tmp[0] == 1:
                break
            tmp = tmp[1]

    return answer


words = ["go","gone","guild"]
# words = ["abc","def","ghi","jklm"]
words = ["word","war","warrior","world"]
print(solution(words))








