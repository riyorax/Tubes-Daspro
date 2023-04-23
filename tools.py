import os
import sys

# FIKSS

def seplit(string, x):
    output = ['' for i in range(x)]
    output_ix = 0
    for i in range(len(string)):
        if string[i] == "\n":
            break
        elif string[i] != ";":
            output[output_ix] += string[i]
        else:
            output_ix += 1
    return output
        
def csv_array_user(file,array):
    f = open(file, 'r')
    cc = f.readline()
    if cc == '':
        print("Selesai")
    else:
        i = 0
        while True:
            array[i] = seplit(cc, 3)
            cc = f.readline()
            if cc == "":
                break
            i+=1
    f.close()
    return array

def csv_array_bahan_bangunan(file,array):
    f = open(file, 'r')
    cc = f.readline()
    if cc == '':
        print("Selesai")
    else:
        i = 0
        while True:
            array[i] = seplit(cc, 3)
            cc = f.readline()
            if cc == "":
                break
            i+=1
    f.close()
    return array

def array_to_line_1(a,b,c):
    output = ""
    output += str(a)
    output += ";"
    output += str(b)
    output += ";"
    output += str(c)
    output += "\n"
    return output

def array_to_line_2(a,b,c,d,f):
    output = ""
    output += str(a)
    output += ";"
    output += str(b)
    output += ";"
    output += str(c)
    output += ";"
    output += str(d)
    output += ";"
    output += str(f)
    output += "\n"
    return output

def write_csv_bahan_bangunan(file,array):
    f = open(file, 'w')
    for i in range(3):
        f.write(array_to_line_1(array[i][0],array[i][1],array[i][2]))
    f.close()

def csv_array_candi(file,array):
    f = open(file, 'r')
    cc = f.readline()
    if cc == '':
        print("Selesai")
    else:
        i = 0
        while True:
            array[i] = seplit(cc, 5)
            cc = f.readline()
            if cc == "":
                break
            i+=1
    f.close()
    return array

def write_csv_candi(file,array,id,pembuat,pasir,batu,air):
    array = csv_array_candi(file,array)
    count = 0
    for i in range(101):
        if array[i] != "*":
            count+=1
    array[count] = [str(id),str(pembuat),str(pasir),str(batu),str(air)]
    f = open(file, 'w')
    for i in range(count+1):
        f.write(array_to_line_2(array[i][0],array[i][1],array[i][2],array[i][3],array[i][4]))
    f.close()