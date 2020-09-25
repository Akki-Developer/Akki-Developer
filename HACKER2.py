if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    sum=0

for x in student_marks:
    if x == query_name:
        rlist=student_marks[x]
        for i in range(len(rlist)):
        	sum=sum+rlist[i]
        formatted_float = "{:.2f}".format(sum/len(rlist))
        print(formatted_float)

