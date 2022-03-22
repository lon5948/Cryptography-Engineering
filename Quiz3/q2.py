ave_freq = [8.167,1.492,2.782,4.253,12.702,2.228,2.015,6.094,6.966,0.153,0.772,4.025,2.406,6.749,7.507,1.929,0.095,5.987,6.327,9.056,2.758,0.978,2.360,0.150,1.974,0.074]

def find_k(group,ind):
    max_value = 0
    for k in range(26):
        value = 0
        for letter in range(26):
            value += group[ind][(letter+k)%26]*ave_freq[letter]
        if value>max_value:
            max_value = value
            max_k = k
    return max_k
        

def func(file,length):
    f = open(file,'r')
    msg = f.read()
    
    group = {}
    
    for i in range(length):
        group[i] = [0]*26
        
    for i in range(len(msg)):
        group[i%length][ord(msg[i])-ord('A')] += 1
        
    string = ""
    for i in range(length):
        string += chr(find_k(group,i)+ord('A'))
        
    print(file,":",string)
    return string

f = open('109550031_msg1.txt','a')
ans = func('message1.txt',5)
f.write(ans)
f.write('\n')
f.close()

f = open('109550031_msg2.txt','a')
ans = func('message2.txt',5)
f.write(ans)
f.write('\n')
f.close()

f = open('109550031_msg3.txt','a')
ans = func('message3.txt',6)
f.write(ans)
f.write('\n')
f.close()