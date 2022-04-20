def Berlekamp_Massey_algorithm(sequence):
    
    length = len(sequence) # the length of sequence
    
    # find the first number which is one instead of zero
    for ind in range(length): # ind is the index of the number
        if sequence[ind] == 1:
            break
        
    l = ind + 1 # the next index of ind
    f = set([l,0]) # use a set to denote polynomial
    

    g = set([0]) # initial g which stores last f
    a = ind # initial a which stores last b
    b = 0 # the column which should be checked
    
    # n starts from one to (length of sequence)-1 
    for n in range(ind+1,length): 
        d = 0
        for ele in f: 
            d ^= sequence[ele + n - l] # count d to check if f need to be update
        if d == 0: # d is zero means f doesn't need to be update
            b += 1 # check next column
        else: # d is one means f need to be update
            if 2 * l > n: # according to Berlekamp Massey algorithm, check if 2*l > n
                f ^= set([a - b + ele for ele in g]) # update f
                b += 1 # check next column
            else:
                temp = f.copy() # store f in temp
                f = set([b - a + ele for ele in f]) ^ g # update f
                g = temp # update g with temp(last f)
                a = b # update a with b
                b = l # update b with l, it means next column which should be checked
                l = n + 1 - l # update l
        
    result = ''
    lis = sorted(f,reverse=True) # sort f from greater to smaller
    for i in lis:
        if i == 0:
            result += '1' # x^0 = 1
        else:
            result += 'x^'
            result += str(i)

        if i != lis[-1]: # last number doesn't need to add '+' anymore
            result += ' + '

    return result # return answer

if __name__ == '__main__':
    # input
    seq = (0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1) 
    print(Berlekamp_Massey_algorithm(seq)) # print the answer

    