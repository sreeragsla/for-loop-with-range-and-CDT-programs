#L=[11,22,33,44,-1,66,50] o/p-['odd','even','odd','even',-1,'even','even]

L=[11,22,33,44,-1,66,50]
for ip in range(len(L)):
    if L[ip]>0:
        if L[ip]%2==0:
            L[ip]='even'
        else:
            L[ip]='odd'
print(L)

'''
iteration
1.controller will take 0 and check whether L[0] is greater than 0 or not.L[0] is
  greater than 0 so condition satisfies and it will check L[0]%2==0 or not.L[0]
  is not equal so it will come to the else part and L[0] will assign 'odd'
2.it will take 1 and check whether L[1] is greater than 0 or not.L[1] is greater
  than 0 so condition satisfies and it will check L[1]%2==0 or not.L[1] is equal
  so condition satisfies and L[1] will assign 'even'
3.it will take 2 and check whether L[2] is greater than 0 or not.L[2] is greater
  than 0 so condition satisfies and it will check L[2]%2==0 or not.L[2] is not
  equal so it will come to the else part and L[2] will assign 'odd'
4.it will take 3 and check whether L[3] is greater than 0 or not.L[3] is greater
  than 0 so condition satisfies and it will check L[3]%2==0 or not.L[3] is equal
  so condition satisfies and L[3] will assign 'even'
5.it will take 4 and check whether L[4] is greater than 0 or not.L[4] is not greater
  than 0 so condition does not satisfies
6.it will take 5 and check whether L[5] is greater than 0 or not.L[5] is greater
  than 0 so condition satisfies and it will check L[5]%2==0 or not.L[5] is equal
  so condition satisfies and L[5] will assign 'even'
7.it will take 6 and check whether L[6] is greater than 0 or not.L[6] is greater
  than 0 so condition satisfies and it will check L[6]%2==0 or not.L[6] is equal
  so condition satisfies and L[3] will assign 'even'
8.after iteration controller will come out of the loop and printing L

'''


                
