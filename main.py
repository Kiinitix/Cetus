t_input = 'HELLO'
alpha1= 'v'

alpha = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}

alpha_key = list(alpha.keys())
alpha_value = list(alpha.values())
alpha_newv = []
alpha_newk = []

if (alpha1 in alpha.keys()):
          key = alpha_key.index(alpha1)         #index of the key
          first = 27 - key
          for i in range(key, 26):                #key to end
                    alpha_newv.append(alpha_value[i])
          for j in range(0, key):
                    alpha_newv.append(alpha_value[j])
          for k in alpha_newv:
                    alpha_newk.append(alpha_key[k-1])
              
def FibRecursion(n):  
   if (n <= 1):  
       return n  
   else:  
       return(FibRecursion(n-1) + FibRecursion(n-2))  

fibo = []  
for i in range(2, 28):  
          fibo.append(FibRecursion(i))

enc1 = ''
for i in fibo:
          enc1 += alpha_newk[(i%26)-1]
          if (len(enc1) >= len(t_input)):
                    break

ASCII = []
for i in range(0, len(enc1)):
          ASCII.append(ord(alpha_newk[i-1]) + ord(alpha_newk[i]) + ord(alpha_newk[i+1]) + ord(t_input[i]))
          print ()
          print ((alpha_newk[i-1]))
          print ((alpha_newk[i]))
          print ((alpha_newk[i+1]))
          print ((t_input[i]))

def tohex(dec):
    x = (dec%16)
    igits = "0123456789ABCDEF"
    digits = list(igits)
    rest = int(dec/16)
    if (rest == 0):
        return digits[x]
    return tohex(rest) + digits[x]

hex_ = [hex(i) for i in ASCII]
