#implement the logic of count method

s='hai sreerag'
sub='r'
c=0
for ip in range(len(s)):
    if s[ip:ip+len(sub)]==sub:
        c+=1
print(c)

'''
iteration
1.controller will take 0 and it will check s[0:1]=='r'.it is not equal so condition
  does not satisfies and c will remains on 0
2.it will take 1 and it will check s[1:2]=='r'.it is not equal so condition does
  not satisfies and c will remains on 0
3.it will take 2 and it will check s[2:3]=='r'.it is not equal so condition does
  not satisfies and c will remains on 0
4.it will take 3 and it will check s[3:4]=='r'.it is not equal so condition does
  not satisfies and c will remains on 0
5.it will take 4 and it will check s[4:5]=='r'.it is not equal so condition does
  not satisfies and c will remains on 0
6.it will take 5 and it will check s[5:6]=='r'.it is eqaul so condition satisfies
  and increment will happen and c will goes from 0 to 1
7.it will take 6 and it will check s[6:7]=='r'.it is not equal so condition does
  not satisfies and c will remains on 1
8.it will take 7 and it will check s[7:8]=='r'.it is not equal so condition does
  not satisfies and c will remains on 1
9.it will take 8 and it will check s[8:9]=='r'.it is eqaul so condition satisfies
  and increment will happen and c will goes from 1 to 2
10.it will take 9 and it will check s[9:10]=='r'.it is not equal so condition does
  not satisfies and c will remains on 2
11.it will take 10 and it will check s[10:11]=='r'.it is not equal so condition does
  not satisfies and c will remains on 2
12.after iteration controller will come out of the loop and printing c

'''





