#6일차 실습

#1,2

def length(l):
    l = list(set(l))
    cn = 0
    for i in l:
        cn += 1
    return cn

def my_xn(setnum, xn, th=1):
    l = list(set(setnum))
    cn = 0
    for i in l:
        cn += 1
    if (th > cn):
        print('세 번째 변수값 오류입니다. 입력하신 리스트 길이보다 작거나 같은 수를 입력하세요.')
    al = list(range(cn))
    for i in (range(cn)):
        al[i] = [l[i], 1]
    if (xn == 1):
        for i in (range(cn)):
            for j in (range(cn)):
                if (al[i][0] < al[j][0]):
                    al[i][1] += 1
    elif (xn == 2):
        for i in (range(cn)):
            for j in (range(cn)):
                if (al[i][0] > al[j][0]):
                    al[i][1] += 1
    else:
        print('두 번째 변수값 오류입니다. (큰 순서 : 1, 작은 순서 : 2)')
    for i in (range(cn)):
        if (al[i][1] == th):
            return al[i][0]
            break

#3, 4

def my_sa(l, sa, a=2):
    sm = 0
    cn = 0
    for i in l:
        cn += 1
    for i in range(cn):
        sm += l[i]
    if (sa == 1):
        return sm
    elif (sa == 2):
        return round(sm/cn, a)
    elif (sa == 3):
        print('합계 =',sm,', 평균 = ',round(sm/cn,a))
    else:
        print('두 번째 변수값 오류입니다. (합계 구하기 : 1, 평균 구하기 : 2, 둘다 구하기 : 3)')
