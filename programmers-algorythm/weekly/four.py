from collections import defaultdict

def solution(table, languages, preference):
    answer = []
    table_dict = defaultdict(list)
    for i in range(len(table)):
        table[i] = table[i].split()
        table_dict[table[i][0]] = table[i][1:]

    score_dict = dict()
    for key, val in table_dict.items():
        total = 0
        for idx, lang in enumerate(languages):
            score = 0
            if lang in val:
                score = len(val) - val.index(lang)
            total += score * preference[idx]
        score_dict[key] = total

    max_score = max(score_dict.values())
    for key, val in score_dict.items():
        if val == max_score:
            answer.append(key)

    answer.sort()
    return answer[0]


table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["JAVA", "JAVASCRIPT"]
preference = [7, 5]
print(solution(table, languages, preference))