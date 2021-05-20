# 오픈 채팅방

def solution(record):
    answer = []
    id_name = dict()
    # 아이디당 이름을 저장하기 위한 반복문
    for x in record :
        info = x.split()
        # enter, change의 경우에는 아이디를 키, 이름을 value로 저장
        # 아이디가 중복될 경우에는 마지막으로 등록된 이름이 저장된다
        if info[0] == 'Enter' or info[0] == 'Change' :
            id_name[info[1]] = info[2]

    # 출력을 하기 위한 반복문
    for x in record:
        out_info = x.split()
        # 채팅방 enter시 등록된 id, name으로 출력함
        if out_info[0] == 'Enter' :
            answer.append("%s님이 들어왔습니다." %(id_name[out_info[1]]))
        # 채팅방 leave시 등록된 id,name으로 출력함
        elif out_info[0] == 'Leave' :
            answer.append("%s님이 나갔습니다." %(id_name[out_info[1]]))
    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))