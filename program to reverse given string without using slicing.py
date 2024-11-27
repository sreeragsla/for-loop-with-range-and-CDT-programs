#w.a.p.t reverse a given string without using slicing

s='sreerag'
rev=''
for ip in range(-1,-(len(s)+1),-1):
    rev=rev+s[ip]
print(rev)

'''
#method 2

s=input()
rev=''
for i in s:
    rev=i+rev    (here it will add from the back)
print(rev)

'''

'''
iteration
1.controller will take -1 and rev will be added with s[-1] and added value will be
  stored in rev
2.it will take -2 and rev will be added with s[-2] and added value will be stored
  in rev
3.it will take -3 and rev will be added with s[-3] and added value will be stored
  in rev
4.it will take -4 and rev will be added with s[-4] and added value will be stored
  in rev
5.it will take -5 and rev will be added with s[-5] and added value will be stored
  in rev
6.it will take -6 and rev will be added with s[-6] and added value will be stored
  in rev
7.it will take -7 and rev will be added with s[-7] and added value will be stored
  in rev
8.after iteration controller will come out of the loop and printing rev

'''


