#l=[11,22,33,44,55,66] o/p-[22,11,44,33,66,55]

l=[11,22,33,44,55,66]
for ip in range(0,len(l),2):
    l[ip],l[ip+1]=l[ip+1],l[ip]
print(l)


'''
iteration
1.controller will take 0 and l[0] will be assigned to l[1] and l[1] will assigned
  to l[0]
2.it will take 2 and l[2] will be assignes to 1[3] and l[3] will assigned to 1[2]
3.it will take 4 and l[4] will be assignes to 1[5] and l[5] will assigned to 1[4]
4.after iteration controller will come out of the loop and printing l

'''


