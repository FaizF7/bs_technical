list = [2,1]
list2 = [0,2,1]

def successor(trits):
    output  = trits.copy()
    if trits[0]<2:
        output[0]+=1

    else:
        i=0
        while i<len(trits)and trits[i]==2:
            output[i]=0
            i+=1
        if i==len(trits):
            output.append(1)
        else:
            output[i]+=1

    return output

print(successor(list))

def leq(list1, list2):

    if len(list2)>len(list1) and (1 in list2[len(list1):] or 2 in list2[len(list1):] ):
        return False
    
    if len(list1)>len(list2) and (1 in list1[len(list2):] or 2 in list1[len(list2):] ):
        return True

    for i in range(len(list1)-1,-1,-1):
        if list1[i]<list2[i]:
            return False
    
    return True

print(leq(list,list2))

def tritwise_min(list1, list2):

    if len(list2)<len(list1):
        list_min = list2
        list_max = list1
    else:
        list_min=list1
        list_max=list2
    # list_min = [0]*min(len(list1),len(list2))
    
    for i in range(len(list_min)):
        if list_max[i]<list_min[i]:
            list_min[i]=list_max[i]
    
    return list_min

print(tritwise_min(list, list2))

def f(A, B):
    current = A
    curr_min = A
    while current!=B:
        curr_min = tritwise_min(curr_min,successor(current))
        current = successor(current)

    return curr_min

print(f([2,0,1],[1,1,1,1]))

def f_eff(A,B):

    output= [0]*len(A)
    if len(B)>len(A) and (1 in B[len(A):] or 2 in B[len(A):] ):
        return output
    
    for i in range(len(A)-1,-1,-1):

        output[i]=A[i]

        if A[i]<B[i]:
            return output
        
    return A

    
# 211
# 011
# 111
# 211
# 021
# 002
    
print(f_eff([2,0,1],[1,0,2]))
