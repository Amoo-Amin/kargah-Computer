n1 = int(input())
n2 = int(input())
if n1 < n2 :
    n1 , n2 = n2 , n1
for i in range(n2,0,-1):
    if n2 % i == 0 and n1 % i == 0 :
        print(i)
        break