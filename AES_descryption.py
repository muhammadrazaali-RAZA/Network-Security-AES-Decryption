# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 03:07:44 2021

@author: Raza_Jutt
"""
cipher_text = "29C3505F571420F6402299B31A02D73A"
key          = "5468617473206D79204B756E67204675"

sbox = ['63', '7C', '77', '7B', 'F2', '6B', '6F', 'C5', '30', '01', '67', '2B', 'FE', 'D7', 'AB', '76', 
        'CA', '82', 'C9', '7D', 'FA', '59', '47', 'F0', 'AD', 'D4', 'A2', 'AF', '9C', 'A4', '72', 'C0', 
        'B7', 'FD', '93', '26', '36', '3F', 'F7', 'CC', '34', 'A5', 'E5', 'F1', '71', 'D8', '31', '15', 
        '04', 'C7', '23', 'C3', '18', '96', '05', '9A', '07', '12', '80', 'E2', 'EB', '27', 'B2', '75', 
        '09', '83', '2C', '1A', '1B', '6E', '5A', 'A0', '52', '3B', 'D6', 'B3', '29', 'E3', '2F', '84', 
        '53', 'D1', '00', 'ED', '20', 'FC', 'B1', '5B', '6A', 'CB', 'BE', '39', '4A', '4C', '58', 'CF', 
        'D0', 'EF', 'AA', 'FB', '43', '4D', '33', '85', '45', 'F9', '02', '7F', '50', '3C', '9F', 'A8', 
        '51', 'A3', '40', '8F', '92', '9D', '38', 'F5', 'BC', 'B6', 'DA', '21', '10', 'FF', 'F3', 'D2', 
        'CD', '0C', '13', 'EC', '5F', '97', '44', '17', 'C4', 'A7', '7E', '3D', '64', '5D', '19', '73', 
        '60', '81', '4F', 'DC', '22', '2A', '90', '88', '46', 'EE', 'B8', '14', 'DE', '5E', '0B', 'DB', 
        'E0', '32', '3A', '0A', '49', '06', '24', '5C', 'C2', 'D3', 'AC', '62', '91', '95', 'E4', '79', 
        'E7', 'C8', '37', '6D', '8D', 'D5', '4E', 'A9', '6C', '56', 'F4', 'EA', '65', '7A', 'AE', '08', 
        'BA', '78', '25', '2E', '1C', 'A6', 'B4', 'C6', 'E8', 'DD', '74', '1F', '4B', 'BD', '8B', '8A', 
        '70', '3E', 'B5', '66', '48', '03', 'F6', '0E', '61', '35', '57', 'B9', '86', 'C1', '1D', '9E', 
        'E1', 'F8', '98', '11', '69', 'D9', '8E', '94', '9B', '1E', '87', 'E9', 'CE', '55', '28', 'DF', 
        '8C', 'A1', '89', '0D', 'BF', 'E6', '42', '68', '41', '99', '2D', '0F', 'B0', '54', 'BB', '16']

rsbox =['52', '09', '6A', 'D5', '30', '36', 'A5', '38', 'BF', '40', 'A3', '9E', '81', 'F3', 'D7', 'FB', 
        '7C', 'E3', '39', '82', '9B', '2F', 'FF', '87', '34', '8E', '43', '44', 'C4', 'DE', 'E9', 'CB', 
        '54', '7B', '94', '32', 'A6', 'C2', '23', '3D', 'EE', '4C', '95', '0B', '42', 'FA', 'C3', '4E', 
        '08', '2E', 'A1', '66', '28', 'D9', '24', 'B2', '76', '5B', 'A2', '49', '6D', '8B', 'D1', '25', 
        '72', 'F8', 'F6', '64', '86', '68', '98', '16', 'D4', 'A4', '5C', 'CC', '5D', '65', 'B6', '92', 
        '6C', '70', '48', '50', 'FD', 'ED', 'B9', 'DA', '5E', '15', '46', '57', 'A7', '8D', '9D', '84', 
        '90', 'D8', 'AB', '00', '8C', 'BC', 'D3', '0A', 'F7', 'E4', '58', '05', 'B8', 'B3', '45', '06', 
        'D0', '2C', '1E', '8F', 'CA', '3F', '0F', '02', 'C1', 'AF', 'BD', '03', '01', '13', '8A', '6B', 
        '3A', '91', '11', '41', '4F', '67', 'DC', 'EA', '97', 'F2', 'CF', 'CE', 'F0', 'B4', 'E6', '73', 
        '96', 'AC', '74', '22', 'E7', 'AD', '35', '85', 'E2', 'F9', '37', 'E8', '1C', '75', 'DF', '6E', 
        '47', 'F1', '1A', '71', '1D', '29', 'C5', '89', '6F', 'B7', '62', '0E', 'AA', '18', 'BE', '1B', 
        'FC', '56', '3E', '4B', 'C6', 'D2', '79', '20', '9A', 'DB', 'C0', 'FE', '78', 'CD', '5A', 'F4', 
        '1F', 'DD', 'A8', '33', '88', '07', 'C7', '31', 'B1', '12', '10', '59', '27', '80', 'EC', '5F', 
        '60', '51', '7F', 'A9', '19', 'B5', '4A', '0D', '2D', 'E5', '7A', '9F', '93', 'C9', '9C', 'EF', 
        'A0', 'E0', '3B', '4D', 'AE', '2A', 'F5', 'B0', 'C8', 'EB', 'BB', '3C', '83', '53', '99', '61', 
        '17', '2B', '04', '7E', 'BA', '77', 'D6', '26', 'E1', '69', '14', '63', '55', '21', '0C', '7D']

def hexaToDec(hexval):
    length = len(hexval)
    base = 1
    dec_val = 0
    for i in range(length - 1, -1, -1):
        if hexval[i] >= '0' and hexval[i] <= '9':
            dec_val += (ord(hexval[i]) - 48) * base
            base = base * 16
        elif hexval[i] >= 'A' and hexval[i] <= 'F':
            dec_val += (ord(hexval[i]) - 55) * base
            base = base * 16
    return dec_val

def decToHexa(n):
    hexaDeciNum = ['0'] * 100
    i = 0
    s=""
    while(n != 0):
        temp = 0
        temp = n % 16
        if(temp < 10):
            hexaDeciNum[i] = chr(temp + 48)
            i = i + 1
        else:
            hexaDeciNum[i] = chr(temp + 55)
            i = i + 1
        n = int(n / 16)
    j = i - 1
    while(j >= 0):
        s = s+(hexaDeciNum[j])
        j = j - 1
    return s

def dec2bin(x):
    if x == 0: return [0]
    bit = []
    while x:
        bit.append(x % 2)
        x >>= 1
    return bit[::-1]

def bin2dec(binary):   
    decimal, i = 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    return decimal

def xor(ary1,ary2):
    ary = []
    for i in range(0,len(ary1)):
        if ary1[i]==ary2[i]:
            ary.append(0)
        else:
            ary.append(1)
    return ary

def string_To_ary(string):
    ary= []
    for i in range(0,len(string),2):
        ary.append(string[i]+string[i+1])
    return ary

def ary_To_string(ary):
    a=""
    for i in ary:
        i = str(i)
        a=a+i
    return a

def comp_len_32(ary):
    temp=[]
    for i in range(0,32-len(ary)):
        temp.append(0)
    for i in ary:
        temp.append(i)
    return temp

def key_set():
    temp= string_To_ary(key)
    for i in range(0,len(temp),4):
        w.append(temp[i:i+4])

def comp_word(hexa):
    s=""
    if len(hexa)==0:
        s="00"
    if len(hexa)==1:
        s="0"
    return s+hexa

def shift(num,ary):
    if num > 1:
        ary = shift(num-1,ary)
    a = ary[0]
    shifted = []
    for i in range(1,len(ary)):
        shifted.append(ary[i])
    shifted.append(a)
    return shifted

def shift_Right(num,ary):
    if num > 1:
        ary = shift_Right(num-1,ary)
    shifted = [ary[len(ary)-1]]
    for i in range(0,len(ary)-1):
        shifted.append(ary[i])
    return shifted

def permutation(ary):
    temp = []
    for i in ary:
        temp.append((sbox[hexaToDec(i[0])*16+hexaToDec(i[1])]))
    return temp

def inv_sbox(ary):
    temp = []
    for i in ary:
        i = comp_word(i)
        temp.append((rsbox[hexaToDec(i[0])*16+hexaToDec(i[1])]))
    return temp

def adding_inc(ary):
    replace = ['00','01','02','04','08','10','20','40','80','1B','36']
    for i in range(0,len(replace)):
        if ary[0]==replace[i]:
            ary[0]=replace[i+1]
            return ary

def xor_hexas(ary1,ary2):
    binOfHex = ary_To_string(xor(comp_len_32(dec2bin(hexaToDec(ary_To_string(ary1)))),comp_len_32(dec2bin(hexaToDec(ary_To_string(ary2))))))
    ary=[]
    n= 0
    for i in range(8,len(binOfHex),8):
        ary.append(str(decToHexa(bin2dec(int(binOfHex[n:i])))))
        n=i
    ary.append(str(decToHexa(bin2dec(int(binOfHex[n:])))))
    s=""
    for i in range(0,4):
        for j in range(0,2-len(ary[i])):
            s=s+"0"
        ary[i] = s+ary[i]
        s=""
    return ary

def xor_arys(a,b,c,d,w,x,y,z):
    a=xor_hexas(a, w)
    b=xor_hexas(b, x)
    c=xor_hexas(c, y)
    d=xor_hexas(d, z)
    return a,b,c,d

def transpos(a,b,c,d):
    ary = []
    for i in range(0,4):
        ary.append(a[i])
        ary.append(b[i])
        ary.append(c[i])
        ary.append(d[i])
    return ary[:4],ary[4:8],ary[8:12],ary[12:16]

def generating_key_word():
    key_set()
    adding= ["00","00","00","00"]
    for n in range(4,41,4):
        rotated = shift(1,w[n-1])
        sub = permutation(rotated)
        adding = adding_inc(adding)
        w.append(xor_hexas(w[n-4], xor_hexas(sub, adding)))
        w.append(xor_hexas(w[n], w[n-3]))
        w.append(xor_hexas(w[n+1], w[n-2]))
        w.append(xor_hexas(w[n+2], w[n-1]))
        print("Round {0}: ".format(int(n/4)),end="")
        for i in range(n,n+4):
            for j in w[i]:
                print(j,end="")
            print("    ",end="")
        print("")

def galois_multiplication(a, b):
        """Galois multiplication of 8 bit characters a and b."""
        p = 0
        for counter in range(8):
            if b & 1: p ^= a
            hi_bit_set = a & 0x80
            a <<= 1
            # keep a 8 bit
            a &= 0xFF
            if hi_bit_set:
                a ^= 0x1b
            b >>= 1
        return p

# galois multiplication of 1 column of the 4x4 matrix
def mixColumn(column, isInv):
    if isInv: mult = [14, 9, 13, 11]
    else: mult = [2, 1, 1, 3]
    cpy = list(column)
    g = galois_multiplication

    column[0] = g(cpy[0], mult[0]) ^ g(cpy[3], mult[1]) ^ \
                g(cpy[2], mult[2]) ^ g(cpy[1], mult[3])
    column[1] = g(cpy[1], mult[0]) ^ g(cpy[0], mult[1]) ^ \
                g(cpy[3], mult[2]) ^ g(cpy[2], mult[3])
    column[2] = g(cpy[2], mult[0]) ^ g(cpy[1], mult[1]) ^ \
                g(cpy[0], mult[2]) ^ g(cpy[3], mult[3])
    column[3] = g(cpy[3], mult[0]) ^ g(cpy[2], mult[1]) ^ \
                g(cpy[1], mult[2]) ^ g(cpy[0], mult[3])
    return column

def mix_col(ary):
    
    ary = transpos(ary[0], ary[1], ary[2], ary[3])
    temp=[]
    for i in range(0,4):
        a = mixColumn([hexaToDec(ary[i][0]),hexaToDec(ary[i][1]),hexaToDec(ary[i][2]),hexaToDec(ary[i][3])],1)
        for i in a:
            temp.append(decToHexa(i))
    return transpos(temp[:4],temp[4:8],temp[8:12],temp[12:16])


w = []    
generating_key_word()


cipher_text = string_To_ary(cipher_text)
a,b,c,d = transpos(cipher_text[:4],cipher_text[4:8],cipher_text[8:12],cipher_text[12:16])
w[40],w[41],w[42],w[43] = transpos(w[40],w[41],w[42],w[43])
a,b,c,d = xor_arys(a,b,c,d,w[40],w[41],w[42],w[43])
cipher_text = [a,b,c,d]
print("")

for i in range(37,0,-4):
    i = i-1
    a = inv_sbox(a)
    b = inv_sbox(shift_Right(1,b))
    c = inv_sbox(shift_Right(2,c))
    d = inv_sbox(shift_Right(3,d))
    w[i],w[i+1],w[i+2],w[i+3] = transpos(w[i],w[i+1],w[i+2],w[i+3])
    a,b,c,d = xor_arys(a,b,c,d,w[i],w[i+1],w[i+2],w[i+3])
    if i!=0:
        a,b,c,d = mix_col([a, b, c, d])
    cipher_text.append(a)
    cipher_text.append(b)
    cipher_text.append(c)
    cipher_text.append(d)

#print(len(cipher_text))

for i in range(0,41,4):
    print("Ciphertext {0} : ".format(int(i/4)),end="")
    print_ency = transpos(cipher_text[i],cipher_text[i+1],cipher_text[i+2],cipher_text[i+3])
    for k in range(0,4):
        for j in print_ency[k]:
            print(j,end="")
        print(" ",end="")
    print("")





