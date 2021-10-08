# 단속카메라

def solution(routes):
    answer = []
    routes.sort(key=lambda x: x[0])
    answer.append(routes[0])
    for route in routes:
        prior_st, prior_en = answer[-1]
        new_st, new_en = route
        if new_st <= prior_en:
            answer[-1] = [new_st, min(prior_en, new_en)]
        else:
            answer.append(route)

    return len(answer)

