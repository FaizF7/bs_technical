

numbers = [3,5,1]

def and_list(numbers):
    output = numbers[0]
    for number in numbers[1:]:
        output = output&number
    return output

def xor_list(numbers):
    output = numbers[0]
    for number in numbers[1:]:
        output = output^number
    return output

print (and_list(numbers))
print (xor_list(numbers))


def f(numbers):

    contiguous_sublists=[]

    length = len(numbers)
    #loop through each index
    for i in range(length):
        #for each index i increment up to the end of the array
        for j in range(i,length):
            #append the sliced list after every incrementation using the two pointers
            contiguous_sublists.append( numbers[i:j+1])

    #initiate list to hold xor values for each sublist
    xor_elements = []

    for sublist in contiguous_sublists:
        # populate with the xor of each sublist
        xor_elements.append(xor_list(sublist))

    print(xor_elements)
    print([bin(element) for element in xor_elements])

    #return and_list operation of the list of of xor_elements
    return and_list(xor_elements)


print(f(numbers))

def f_eff(numbers):
    
    #initiate xor_result as 0
    xor_result = 0
    and_result = numbers[0]
    length = len(numbers)

    for i, number in enumerate(numbers):
        xor_result = xor_result ^ number * (length-i)*(i+1)
        and_result = and_result&numbers[i]

    return and_result & xor_result

def f(numbers):
    xor_result = 0
    and_result = numbers[0]
    length = len(numbers)

    for i in range(length):
        # Update the bitwise AND result
        and_result &= numbers[i]
        
        # Compute the XOR result
        xor_result ^= numbers[i] * (length - i) * (i + 1)

    return and_result & xor_result

# Example usage:
print(f_eff(numbers))


# a & (a^b) & b


# 011
# 101
# 001