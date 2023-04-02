import time
import random
import matplotlib.pyplot as plt
import string
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
def runtimeAnalysis():
    def stringGenerator(n):
        sl1,sl2=[],[]
        for i in range(1,n+1):
            s1,s2="",""
            for j in range(1,i+1):
                s1+=random.choice(string.ascii_letters)
                s2+=random.choice(string.ascii_letters)
            sl1.append(s1)
            sl2.append(s2)
        return sl1,sl2

    n=int(input("Input length limit: "))
    x=list(range(1,n+1))
    strings1,strings2=stringGenerator(n)
    y=[]
    for i in range(n):
        lcs, rt=LCS(strings1[i],strings2[i])
        y.append(rt)
    plt.plot(x,y)
    plt.xlabel("String Lengths")
    plt.ylabel("Runtimes")
    plt.show()

def main():
    inp=int(input("1=single lcs. 2=lcs runtime analysis.\n"))
    if inp==1:
        str1=input("String 1: ")
        str2=input("String 2: ")
        lcs, rt=LCS(str1, str2)
        print("LCS: "+lcs+"\nRuntime:",rt)
    if inp==2:
        runtimeAnalysis()
main()
