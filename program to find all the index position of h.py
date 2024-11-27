#w.a.p.t.p all the index positions where r is present in a given string

s='sreerag'
for ip in range(len(s)):
    if s[ip]=='r':
        print(ip)

'''
iteration
1.controller will take 0 and check whether s[0] is equals to 'r' or not.it is not
  equal so condition does not satisfies
2.it will take 1 and check whether s[1] is equals to 'r' or not.it is equal so
  condition satisfies and 1 will print
3.it will take 2 and check whether s[2] is equals to r' or not.it is not equal so
  condition does not satisfies
4.it will take 3 and check whether s[3] is equals to r' or not.it is not equal so
  condition does not satisfies
5.it will take 4 and check whether s[4] is equals to 'r' or not.it is equal so
  condition satisfies and 4 will print
6.it will take 5 and check whether s[5] is equals to r' or not.it is not equal so
  condition does not satisfies
7.it will take 6 and check whether s[6] is equals to r' or not.it is not equal so
  condition does not satisfies
8.after iteration controller will come out of the loop

'''



