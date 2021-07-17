# 파일명 정렬

def solution(files):
    answer = []
    for file in files:
        tmp = []
        num_idx = -1
        for i,val in enumerate(file):
            if val.isdigit():
                num_idx = i
                break
        tail_idx = -1
        for i in range(num_idx, len(file)):
            if i > num_idx + 5:
                tail_idx = num_idx + 5
                break
            if not file[i].isdigit():
                tail_idx = i
                break
        if tail_idx == -1:
            tmp = [file[:num_idx], file[num_idx:]]
        else:
            tmp = [file[:num_idx], file[num_idx:tail_idx], file[tail_idx:]]
        answer.append(tmp)
    print(answer)
    answer.sort(key=lambda x : (x[0].lower(),int(x[1])))
    result = []
    for divided in answer:
        result.append("".join(divided))


    return result

files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
files = ["foo9.txt", "foo010bar020.zip", "F-15", "f -0111222"]
#files = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
print(solution(files))