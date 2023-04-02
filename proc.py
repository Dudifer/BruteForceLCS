import time
def LCS(s, t):
    ti=time.time()
    ss,st=set(),set()
    for c in s:
        for e in ss:
            e+=c
        ss=ss.union({c})
    for c in st:
        for e in ss:
            e+=c
        st=st.union({c})
    cs=ss.intersection(st)
    maxLen=0
    lcs=""
    for s in cs:
        if len(s)>maxLen:
            lcs=s
    tf=time.time()
    return lcs, tf-ti


str1=input("String 1: ")
str2=input("String 2: ")
lcs, rt=LCS(str1, str2)
print("LCS: "+lcs+"\nRuntime:",rt)

