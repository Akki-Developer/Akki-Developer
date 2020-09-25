# (() --> False
# ())) --> False
# (()()) --> True
# )( --> False
# () --> True

# [({})] 

stack=[]
val="({}[])"

# print(val)
def fun():
	for i in val :
		if i=="(" or i=="{" or i =="[" :
			stack.append(i)

		elif i==")" or i=="]" or i=="}":
			if len(stack)==0:
				return False
			top=stack.pop()
			if not comparestr(top,i):
				return False
	if len(stack) != 0:
		return False
	return True


def comparestr(char1,char2):
	if char1 =="(" and char2==")":
		return True
	elif char1=="{" and char2=="}":
		return True
	elif char1=="[" and char2=="]":
		return True
	else :
		return False
			
print(fun())

#--------------------------------------------------------------------------------------------------
#input==12
#output==12 8 4 0 4 8 12 without using Loop
def series(i,flag):
	print(i)
	if (i <= 0):#this loop excutes only i==0 or i<0 than change flag value to excute i+4 block
		if flag==False:#(Switch the flag value)
			flag = True
		else:
			flag = False
	if i == n and flag==False:#when i==12 and flag==False(at the end of series)this exit the function 
		return
	#if flag==Ture then i-4 block excute and return flag==true 
	if flag==True:
		return series(i-4,flag)
	#when flag==false then i+4 block excute and retuen flag==True
	if flag==False:	
		return series(i+4, flag)


n=12
i=n
flag=True
series(n,flag)

#--------------------------------------------------------------------------------------------------
#hello remove duplicates and sort 
#output = helo
strg="hello"
rdup=set(strg)
sortr=sorted(rdup)
print(sortr)
res=" ".join(sortr)
print(res)