if __name__ == '__main__':
    matrix=[]
    score_list=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        matrix.append([name,score])
        score_list.append(score)
    cal=sorted(list(set(score_list)))[1]

    for name,score in sorted(matrix):
        if score==cal:
            print(name)


#-------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    x,y,z,n=(int(input())for _ in range(4))
    print([[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1)
    if a+b+c !=n])

#-------------------------------------------------------------------------------------------------

def solve(s):
    return ' '.join(i.capitalize() for i in s.split(' '))  	

s="akki gupta lol"
solve(s)

#--------------------------------------------------------------------------------------------------


import textwrap

def wrap(string, max_width):
    wrapp=textwrap.TextWrapper(width=max_width)
    res=wrapp.fill(text=string)
    return res

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

#--------------------------------------------------------------------------------------------------

def print_formatted(number):
    n1=len("{0:b}".format(n))
    for i in range(1,number+1):
        strin="{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}"
        print(strin.format(i,width=n1))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

#---------------------------------------------------------------------------------------------------

a,b = [set(input().split()) for _ in range(4)][1::2]
print(*sorted(a^b, key=int), sep='\n')

#--------------------------------------------------------------------------------------------------

import math

c='♥'
width = 40

print ((c*2).center(width//2)*2)

for i in range(1,width//10+1):
    print (((c*int(math.sin(math.radians(i*width//2))*width//4)).rjust(width//4)+
           (c*int(math.sin(math.radians(i*width//2))*width//4)).ljust(width//4))*2)

for i in range(width//4,0,-1):
    print ((c*i*4).center(width))
print ((c*2).center(width))

#--------------------------------------------------------------------------------------------------


n,m=map(int,input().split())
pattern=[('.|.'*(2*i+1)).center(m,'-')for i in range(n//2)]
print('\n'.join(pattern+['WELCOME'.center(m,'-')]+pattern[::-1]))