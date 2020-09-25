from collections import Counter

li=[2,3,4,5]
li2=[2,3,4,5]
print(li+li2)
print(type(li))
str1=" heel oo "
print(str1.strip())
print(li[-3:-1])
for i in range(1,10,2):
	print(i)

#Palindrom
# R A D A R ------> R A D A R
def pali(n1):
	n2=n1[::-1]
	if n1==n2:
		return True

	else :
		return False

n1="radar"
if (pali(n1)):
	print("it is Palindrom")
else :
	print("it isn't Palindrom")

#fabonicci
#0 1 1 2 3 5 8 13 ......
pre,npre=0,1
i=0
n=10
if n<0:
	print("Incorrect Input")
elif n==0:
	print(n)
elif n==1:
	print(n)      
else:
	while i<n:
		print(pre)
		sum=pre+npre
		pre=npre
		npre=sum
		i+=1

def fabb():
    i=0
    j=1
    print(i)
    print(j)
    for x in range(7):
        sum=i+j
        print(sum)
        i=j
        j=sum
        
fabb()


#factorial using recursion 
# 4!=4*3*2*1
def fact(n):
	if n==1:
		return n
	else :
		return n*fact(n-1)

n=5
print(fact(n))

#factorial without recursion 
# 4!=4*3*2*1
n=5
i=1
fact=1
if n==1:
	print(n)
else :
	while i<=n :
		fact=i*fact
		i+=1
	print(fact)
		

#Anagram
#"listen" ------>"silent"
def ana(str1, str2):
	if sorted(str1)==sorted(str2):
		print("Anagram")
	else :
		print("Not Anagram")

str1="listen"
str2="silent"
ana(str1,str2)


def anagram(str1,str2):
    if len(str1)==len(str2):
        for i in range(len(str2)):
            for j in range(len(str2)):
                if str1[i]==str2[j]:
                    break
        print("Anagram")
    else:
        print("Not Anagram")
    
anagram("LISTEN","SILENT")

#Anagram Using Count Variable
from collections import Counter
def anagram(s1, s2):
    return Counter(s1) == Counter(s2)

s1="listen"
s2="silent"
if anagram(s1, s2):
	print("Anagram")
else :
	print("Not Anagram")

#Armstrong number
#1534=1*1*1*1+5*5*5*5+3*3*3*3+4*4*4*4
numb=1534
n=len(str(numb))
temp=numb
digit=0
sum=0

while temp>0:
	digit=temp%10
	sum +=digit**n
	temp//=10

if numb==sum:
	print("Armstrong")
else :
	print("Not Armstrong")








