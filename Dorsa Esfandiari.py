a=int(input())
b=int(input())
for m in range(max(a,b),(a*b)+1):
    if m%a==0 and m%b==0:
        print(float(m))
        break
