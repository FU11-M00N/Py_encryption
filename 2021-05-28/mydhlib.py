import random

#########################################################
# 소수 구하기
#########################################################
def is_prime(a):
    if a<2:
        return False
    else:
        for i in range(2,a):
            if a % i == 0:
                return False
        return True

#print(is_prime(8))

def get_prime_random(sv,ev):
    count = 1000
    while count >= 0:
        v = random.randint(sv,ev)
        if is_prime(v):
            return v
        else:
            count = count + 1
    return -1

#print(get_prime_random(100,200))

#########################################################
# 원시근 구하기
#########################################################
def is_primitiveRoot(p,p_v):
    total = 0
    data = []
    for i in range(1, p_v):
        if i ==1:
            total = p
        else:
            total = total * p
        v = total % p_v
        if v not in data:
            data.append(v)
    for i in range(1,p_v):
        if i not in data :
            return False
    return True

        

#print(is_primitiveRoot(2,11))

def get_primitiveroot_random(p_v):
    count = 1000
    
    while count > 0:
        a = random.randint(2,p_v-1)
        if not is_prime(a):
            count -=1
            continue
        if is_primitiveRoot(a, p_v):
            return a
        else: count -= 1
    return -1            
        
#print(get_primitiveroot_random(97))
#########################################################
# 디피헬만 키 교환
#########################################################

def get_qa_random(sv,ev):
    q = get_prime_random(sv,ev)
    a = get_primitiveroot_random(q)

    return q,a

#print(get_qa_random(100,200))

def get_df_key():
    # a,q 구하기
    q,a = get_qa_random(100,200)
    # A 값 구하기
    xa = random.randint(1, q-1)
    ya = a**xa % q 
    # B 값 구하기
    xb = random.randint(1,q-1)
    yb = a**xb & q

    # 키 계산하기
    ka = yb**xa & q
    kb = ya** xb & q
    print(q,a)
    print(ka,kb)
#get_df_key()