if __name__ == '__main__':
    N = int(input())
    result=[]
    option=input()
while N>0: 
    res=option.split()
    lst=res[0]
    N-=1
    # print(lst)
    args=res[1:]
    if lst != "print":
    	lst=lst+"("+",".join(args)+")"
    	eval("result."+lst)
    else :
    	print(result)

#--------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    res=tuple(integer_list)
print(hash(res))

#--------------------------------------------------------------------------------------------------

S = input()
for s in S:
    if s.islower():
        print(s.upper(), end="")
    else:
        print(s.lower(), end="")
print()
