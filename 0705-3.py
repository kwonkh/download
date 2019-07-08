#weekend exercise

#1

def my_join(str1,str2):
    return str1 + str2

#2

def my_split(str,ch):
    return str.split(ch)

#6일차 실습

#1

def my_max(l,a):
    l = list(set(l))
    al = list(range(len(l)))
    for i in (range(len(l))):
        al[i] = [l[i], 1]
    for i in (range(len(l))):
        for j in (range(len(l))):
            if (al[i][0] < al[j][0]):
                al[i][1] += 1
    for i in (range(len(l))):
        if (al[i][1] == a):
            return al[i][0]

def my_max2(l):
    mx = l[0]
    for i in range(1,len(l)):
        if (l[i] > mx):
            mx = l[i]
    return mx

#2

def my_min(l):
    l = list(set(l))
    al = list(range(len(l)))
    for i in (range(len(l))):
        al[i] = [l[i], 1]
    for i in (range(len(l))):
        for j in (range(len(l))):
            if (al[i][0] < al[j][0]):
                al[i][1] += 1
    for i in (range(len(l))):
        if (al[i][1] == len(l)):
            return al[i][0]

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
