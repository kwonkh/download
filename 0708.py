#6일차 실습

#1

def my_max(setnum):
    l = list(set(setnum))
    #숫자들의 모임 setnum을 입력 받아 집합으로 변환하여 중복값 제거 후 다시 리스트로 변환
    cn = 0
    for i in l:
        cn += 1 #리스트 l의 길이 구하기
    al = list(range(cn))
    for i in (range(cn)):
        al[i] = [l[i], 1]
    for i in (range(cn)):
        for j in (range(cn)):
            if (al[i][0] < al[j][0]):
                al[i][1] += 1
    for i in (range(cn)):
        if (al[i][1] == 1):
            return al[i][0]
            break

def my_max2(l):
    mx = l[0]
    for i in range(1,len(l)):
        if (l[i] > mx):
            mx = l[i]
    return mx

#2

def my_min(setnum):
    l = list(set(setnum))
    cn = 0
    for i in l:
        cn += 1
    al = list(range(cn))
    for i in (range(cn)):
        al[i] = [l[i], 1]
    for i in (range(cn)):
        for j in (range(cn)):
            if (al[i][0] < al[j][0]):
                al[i][1] += 1
    for i in (range(cn)):
        if (al[i][1] == cn):
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
