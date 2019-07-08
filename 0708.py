#6일차 실습

#1

def length(a):
    a = list(set(a))
    cn = 0
    for i in a:
        cn += 1
    return cn

def my_max(setnum, th=1):
    l = list(set(setnum))
    cn = 0
    for i in a:
        cn += 1
    al = list(range(cn))
    for i in (range(cn)):
        al[i] = [l[i], 1]
    for i in (range(cn)):
        for j in (range(cn)):
            if (al[i][0] < al[j][0]):
                al[i][1] += 1
    for i in (range(cn)):
        if (al[i][1] == th):
            return al[i][0]
            break

def my_max2(l):
    mx = l[0]
    for i in range(1,len(l)):
        if (l[i] > mx):
            mx = l[i]
    return mx

#2

def my_min(setnum, th=1):
    l = list(set(setnum))
    cn = 0
    for i in l:
        cn += 1
    al = list(range(cn))
    for i in (range(cn)):
        al[i] = [l[i], 1]
    for i in (range(cn)):
        for j in (range(cn)):
            if (al[i][0] > al[j][0]):
                al[i][1] += 1
    for i in (range(cn)):
        if (al[i][1] == th):
            return al[i][0]
            break

def my_min2(l):
    mn = l[0]
    for i in range(1,len(l)):
        if (l[i] < mn):
            mn = l[i]
    return mn

#3

def my_sum(l):
    sm = 0
    for i in range(len(l)):
        sm += l[i]
    return sm

#4

def my_avg(l):
    sm = 0
    for i in range(len(l)):
        sm += l[i]
    return round(sm/len(l),2)

def len(l):
    cn = 0
    for i in l:
        cn += 1
    return cn

#1,2

def my_xn(setnum, xn, th=1):
    l = list(set(setnum))
    cn = 0
    for i in l:
        cn += 1
    if (th > cn):
        print('오류입니다. 입력하신 리스트 길이보다 작은 수를 세 번째 변수에 입력하세요.')
    al = list(range(cn))
    for i in (range(cn)):
        al[i] = [l[i], 1]
    if (xn == 'max'):
        for i in (range(cn)):
            for j in (range(cn)):
                if (al[i][0] < al[j][0]):
                    al[i][1] += 1
    elif (xn == 'min'):
        for i in (range(cn)):
            for j in (range(cn)):
                if (al[i][0] > al[j][0]):
                    al[i][1] += 1
    else:
        print('오류입니다. 구하려고 하는 것이 큰 순서이면 max, 작은 순서이면 min을 두번 째 변수에 입력하세요.')
    for i in (range(cn)):
        if (al[i][1] == th):
            return al[i][0]
            break
