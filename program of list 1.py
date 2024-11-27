#L=[11,2,44,66,77] o/p- ['odd','even','even','even','odd']

L=[11,2,44,66,77]
for ip in range(len(L)):
    if L[ip]%2==0:
        L[ip]='even'
    else:
        L[ip]='odd'
print(L)

'''
#method 2

L=[11,2,44,66,77]
l=''
for i in L:
    if i%2==0:
        l.append('even')
    else:
        l.append('odd')
print(l)

'''
'''
iteration
1.controller will take 0 and check whether L[0]%2==0 or not.it is not equal so it
  will comes to the else part L[0] will assigned to 'odd'
2.it will take 1 and check whether L[1]%2==0 or not.it is equal so condition satisfies
  and L[1] will assignes to 'even'
3.it will take 2 and check whether L[2]%2==0 or not.it is equal so condition satisfies
  and L[2] will assignes to 'even'
4.it will take 3 and check whether L[3]%2==0 or not.it is equal so condition satisfies
  and L[3] will assignes to 'even'
5.it will take 4 and check whether L[4]%2==0 or not.it is not equal so itwill comes
  to the else part L[0] will assigned to 'odd'
6.after iteration controller will come out of the loop and printing L

'''



