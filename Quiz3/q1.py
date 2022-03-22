def ic_value(file,length):
    group = {}
    num = [0]*length
    for i in range(length):
        group[i] = [0]*26
        
    for i in range(len(file)):
        group[i%length][ord(file[i])-ord('A')] += 1
        num[i%length] += 1
        
    ic = 0
    for ind in range(length):
        for letter in range(26):
            ic += (group[ind][letter])*(group[ind][letter]-1)/num[ind]/(num[ind]-1)
    ic /= length
    return ic


def find_length(message):
    f = open(message,'r')
    msg = f.read()
    min_diff = 1
    for i in range(4,8):
        diff = abs(ic_value(msg,i)-0.066)
        if(diff<min_diff):
            min_diff = diff
            length = i
    print(message,":",length)
    return length


f = open('109550031_msg1.txt','w')
ans = find_length('message1.txt')
f.write(str(ans))
f.write('\n')
f.close()

f = open('109550031_msg2.txt','w')
ans = find_length('message2.txt')
f.write(str(ans))
f.write('\n')
f.close()

f = open('109550031_msg3.txt','w')
ans = find_length('message3.txt')
f.write(str(ans))
f.write('\n')
f.close()