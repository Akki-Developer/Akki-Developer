#count the substring in string

def count_substring(string, sub_string):
	sum=0
	for i in range(0, len(string) - len(sub_string) + 1):
		if (string[i:(len(sub_string)+i)] == sub_string):
			sum=sum+1
			print(string[i:(len(sub_string)+i)])
			#print(sub_string)
		print(string[i:(len(sub_string)+i)])
	print(sum)

string="ABCDCDCDCDC"
sub_string="CDC"
count_substring(string, sub_string)


#[7,5,2]

num=157
res=[x for x in str(num)][::-1]
print("".join(res))


num=157
sum=0
while(num>0):
    digit=num%10
    sum=sum*10+digit
    num=num//10
    
print(sum)

#second highest number in a program

li=[12,10,50,70,60]
li.sort()
print(li[-2])
