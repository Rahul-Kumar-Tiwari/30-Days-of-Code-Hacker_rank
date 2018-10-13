n=int(input())
for i in range(0,n):
    s=input()
    for j in range(len(s)):
        if j%2==0:
            print(s[j],end='')
    print(' ',end='')
    for j in range(len(s)):
        if j%2!=0:
            print(s[j],end='')
    print('')