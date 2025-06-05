def gcd(p,q):
    #علیرضا شیخ ممو 4031531023
    if q==0: return p
    return gcd(q,p%q)
print('done')
def fact(n):
    #هانیه عباسی
    s=1
    for i in range(n):
        s=s*i
    return(s)