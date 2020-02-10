import numpy as np
import matplotlib.pyplot as plt
import sys

def encode_file(filename,plot=False,save=False):
    # load to array
    f = np.fromfile(filename, dtype=np.uint8)
    if plot == True:
        side = int(np.ceil(np.sqrt(len(f))))
        im = np.concatenate((f,np.zeros(side**2 - len(f),dtype = np.uint8))).reshape((side,side))
        plt.figure(figsize = (5,5))
        plt.imshow(im,cmap = 'hsv')
        plt.axis('off')
    
    #build binary representation
    s = "0b"
    for a in f:
        temp = bin(a)[2:]
        new = (8 - len(temp))*'0' + temp
        s += new
      
    a = eval(s) # to decimal
    if save == True:
        with open("code_to_number.txt","w") as f:
            f.write(str(a))
    return a

def print_number(a,linelength=80):
    s = str(a)
    N = len(s)//linelength
    for i in range(N):
        print(s[i*linelength:(i+1)*linelength])
    print(s[N*linelength:])

def decode_number(a,filename_new = "program"):
    # erase the first "0b" characters and add zeros until 
    # it has len that is multiple of 8
    padding = 8 - (len(bin(a))-2) % 8 
    s2 = padding*"0" + bin(a)[2:]
    
    #load to array and build file
    f2 = np.array([eval("0b"+s2[8*i:8*(i+1)]) for i in range(len(s2)//8)],dtype =np.uint8)
    f2.tofile(filename_new)
    
    
if __name__ == "__main__" and len(sys.argv) >= 2:
    N = int(sys.argv[1])
    print("Turning the following number into file:\n")
    print_number(N)
    print("\nDone.\n")
