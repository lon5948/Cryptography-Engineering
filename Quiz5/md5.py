import hashlib

inp = input()
byte = bytes.fromhex(inp)
md5 = hashlib.md5(byte)   
ans = md5.hexdigest()
MSB = ans[0:4]

num = 0
while(1):
    string = str(hex(num))[2:].zfill(32)
    byte = bytes.fromhex(string)
    md5 = hashlib.md5(byte)   
    ans = md5.hexdigest()
    msb = ans[0:4]
    if msb == MSB:
        print(MSB,string)
        break
    num += 1
    

