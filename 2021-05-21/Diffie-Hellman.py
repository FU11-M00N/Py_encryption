
import random

# =============================================================================
# 소수 구하기
# =============================================================================
def is_prime(v):
    if v <2 :
        return False
    else:
        for a in range(2,v):
            if v % a ==0:
                return False
        return True
def get_prime(sv,ev):

    data = []

    for a in range(sv,ev+1):
        if is_prime(a):
            data.append(a)
    return data

def get_prime_random(sv,ev):
    count = 1000
    while count>0:

        v = random.randint(sv,ev)
        if is_prime(v):
            return v
        else:
            count -=1
    return -1

def test1():

    print(is_prime(111))
    data = get_prime(1,100)
    print(data)
    q = get_prime_random(1000,2000)
    print(q)

# test1()

 

# =============================================================================

# 원시근 구하기

# =============================================================================


def is_primitiveroot(p,p_v):
    total = 0
    data = []
    for i in range(1,p_v):
        if i == 1:
            total = p
        else:
            total = total * p

        v = total % p_v

        if v not in data:
            data.append(v)

    for i in range(1,p_v):
        if i not in data:
            return False

    return True

    

def get_primitiveroot(p_v):
    data = []

    if not is_prime(p_v):
        return data

    for i in range(2,p_v):
        if is_prime(i):
            if is_primitiveroot(i, p_v):
                data.append(i)
    return data


def get_primitiveroot_random(p_v):

    count = 1000
    while count>0:
        a = random.randint(2, p_v-1)
        if not is_prime(a):
            count -= 1
            continue
        if is_primitiveroot(a, p_v):
            return a
        else:
            count -= 1
    return -1

 
def test2():
    print(is_primitiveroot(5,11))
    data = get_primitiveroot(97)
    print(data)    
    a = get_primitiveroot_random(97)
    print(a)

# test2()

# =============================================================================
# 디피헬만 - 로컬버전
# =============================================================================

def get_qa_random(sv,ev):
    q = get_prime_random(sv, ev)
    a = get_primitiveroot_random(q)

    return q,a
def test3():

    q,a = get_qa_random(100,200)
    print(q,a)
    q =353
    a = 3

    #A

    xa = random.randint(1, q-1)
    ya = a**xa % q

    #B
    xb = random.randint(1, q-1)
    yb = a**xb % q 
    # 키 구하기

    ka = yb**xa % q

    kb = ya**xb % q

    print(ka)

    print(kb)

    

# test3()

 

def test4():

    q,a = get_qa_random(500, 1000)

    print(q,a)

    q = 877
    a = 683
    xa = random.randint(1, q-1)
    ya = a**xa % q

    yb= 663
    ka = yb**xa % q
    
    print(ya)
    print(ka)
#test4()

def test5():
    #q,a = get_qa_random(500, 1000)
    #print(q,a)
    q,a=619,614
    #xa = random.randint(1, q-1)
    xa=531
    ya = a**xa % q
    print(ya)

    yb = 423

    ka = yb**xa % q
    print(ka)
test5()