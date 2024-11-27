#w.a.p.t find the sum of even digits present in odd index position

s='sreerag624'
sed=0
for ip in range(len(s)):
    if s[ip].isdigit():
        if ip%2==1 and int(s[ip])%2==0:
            sed+=int(s[ip])
print(sed)

'''
iteration
1.controller will take 0 and check whether s[0] is digit or not.s[0] is not a digit
  so condition does not satisfies
2.it will take 1 and check whether s[1] is digit or not.s[1] is not a digit so condition
  does not satisfies
3.it will take 2 and check whether s[2] is digit or not.s[2] is not a digit so condition
  does not satisfies
4.it will take 3 and check whether s[3] is digit or not.s[3] is not a digit so condition
  does not satisfies
5.it will take 4 and check whether s[4] is digit or not.s[4] is not a digit so condition
  does not satisfies
6.it will take 5 and check whether s[5] is digit or not.s[5] is not a digit so condition
  does not satisfies
7.it will take 6 and check whether s[6] is digit or not.s[6] is not a digit so condition
  does not satisfies
8.it will take 7 and check whether s[7] is digit or not.s[7] is digit so condition
  satisfies.it will check 7 is odd or not and int(s[7]) is even or not.7 is odd and int(s[7])
  is even so condition satisfies.sed will be added with int(s[7])
9.it will take 8 and check whether s[8] is digit or not.s[8] is digit so condition
  satisfies.it will check 8 is odd or not and int(s[8]) is even or not.8 is not
  odd so condition does not satisfies
10.it will take 9 and check whether s[9] is digit or not.s[9] is digit so condition
  satisfies.it will check 9 is odd or not and int(s[9]) is even or not.9 is odd and int(s[9])
  is even so condition satisfies.sed will be added with int(s[9])
11.after iteration controller will come out of the loop and printing sed

'''




