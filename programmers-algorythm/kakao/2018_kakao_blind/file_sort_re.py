# 파일명 정렬

def file_sort(files):
    answer = []
    file_split = []
    for file in files:
        number_idx, tail_idx = 0,0
        for idx, word in enumerate(file):
            if word.isdigit():
                number_idx = idx
                break
        for idx in range(number_idx, len(file)):
            if not file[idx].isdigit():
                tail_idx = idx
                break
        if tail_idx == 0: # tail이 없는 경우
            file_split.append([file[:number_idx], file[number_idx:], ''])
        else: # tail이 있는 경우
            file_split.append([file[:number_idx], file[number_idx:tail_idx], file[tail_idx:]])

    file_split.sort(key=lambda x : (x[0].lower(),int(x[1])))

    return [''.join(file) for file in file_split]

files = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
print(file_sort(files))

