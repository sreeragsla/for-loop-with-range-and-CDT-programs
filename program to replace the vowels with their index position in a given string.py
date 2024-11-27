#w.a.p.t replace all the vowels with their index positions in a given string

s='sreerag'
v='aeiouAEIOU'
new=''
for ip in range(len(s)):
    if s[ip] in v:
        new+=str(ip)
    else:
        new+=s[ip]
print(new)

'''
iteration
1.controller will take 0 and check whether s[0] is present in v or not.s[0] is not
  present so condition does not satisfies.so controller will come to the else part
  and new will be added with s[0] and added value will be stored in new
2.it will take 1 and check whether s[1] is present in v or not.s[1] is not present
  so condition does not satisfies.so controller will come to the else part and
  new will be added with s[1] and added value will be stored in new
3.it will take 2 and check whether s[2] is present in v or not.s[2] is present in
  v so condition satisfies.new will be added with str(2) and added value will be
  stored in new
4.it will take 3 and check whether s[3] is present in v or not.s[3] is present in
  v so condition satisfies.new will be added with str(3) and added value will be
  stored in new
5.it will take 4 and check whether s[4] is present in v or not.s[4] is not present
  so condition does not satisfies.so controller will come to the else part and
  new will be added with s[4] and added value will be stored in new
6.it will take 5 and check whether s[5] is present in v or not.s[5] is present in
  v so condition satisfies.new will be added with str(5) and added value will be
  stored in new
7.it will take 6 and check whether s[6] is present in v or not.s[6] is not present
  so condition does not satisfies.so controller will come to the else part and
  new will be added with s[6] and added value will be stored in new
8.after iteration controller will come out of the loop and printing new

'''


