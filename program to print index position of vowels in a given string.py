#w.a.p.t.p the index position of vowels in a given string

s='sreerag'
v='aeiouAEIOU'
for ip in range(len(s)):
    if s[ip] in v:
        print(ip)

'''
iteration
1.controller will take 0 and check whether s[0] is present in v or not.s[0] is not
  present so condition does not satisfies
2.it will take 1 and check whether s[1] is present in v or not.s[1] is not present
  so condition does not satisfies
3.it will take 2 and check whether s[2] is present in v or not.s[2] is present in
  v so condition satisfies and printing 2
4.it will take 3 and check whether s[3] is present in v or not.s[3] is present in
  v so condition satisfies and printing 3
5.it will take 4 and check whether s[4] is present in v or not.s[4] is not present
  so condition does not satisfies
6.it will take 5 and check whether s[5] is present in v or not.s[5] is present in
  v so condition satisfies and printing 5
7.it will take 6 and check whether s[6] is present in v or not.s[6] is not present
  so condition does not satisfies
8.after iteration controller will come out of the loop

'''




    
