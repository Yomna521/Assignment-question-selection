#Q3: Assignment selection questions


def sort_q(question, N):
    sorted_q=question
    for i in range(N-1):
        for j in range(i+1, N):
            if sorted_q[i][2]<sorted_q[j][2]:
                t=sorted_q[i]
                sorted_q[i]=sorted_q[j]
                sorted_q[j]=t
            elif sorted_q[i][2]==sorted_q[j][2]:
                #check ratio
                ri = sorted_q[i][1]/sorted_q[i][2]
                rj = sorted_q[j][1]/sorted_q[j][2]
                if ri>rj:
                    t=sorted_q[i]
                    sorted_q[i]=sorted_q[j]
                    sorted_q[j]=t
    return sorted_q

def calc_min(minmark, student, question):
    needed_marks= minmark - student
    i=0
    n = []
    while needed_marks>0:
        needed_marks -= question[i][1]
        n.append(question[i][0])
        i+=1
    return n
    
if __name__ == "__main__":
   line1= input().split(' ')
   minmark = int(line1[0])
   S = int(line1[1])
   N = int(line1[2])

   line2 = input().split(' ')
   student_mark = [int(i) for i in line2]

   question=[]
   for i in range(1,N+1):
       l = input().split(' ')
       
       b = []
       b.append(i)
       b.append(int(l[0]))
       b.append(int(l[1]))

       question.append(b)

   sorted_q = sort_q(question, N)
   
   for i in range(S):
       b = calc_min(minmark,student_mark[i],sorted_q)
       print(len(b),end=' ')
       b.sort()
       for x in range(len(b)):
           print(b[x], end=' ')
       print('')

