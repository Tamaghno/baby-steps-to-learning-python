s='this is python'
print(s[-1:-15:-1])
print(s.find('i'))

#print(s.index('j'))
print(s.find('j'))
print(s.partition('i'))
print(s.split('i'))
print(s.split())
print(s.partition(' '))
for i in range(len(s)):
    print(s[i])
for i in range(len(s)):
    print(s[i],end='.')
print()

l=[1,2,3]
r=[4,5,6]
print()
l.append(r)
print(l)
l.extend(r)
print(l)
l.append('i')
print(l)

#removing every third element
a = [1,2,3,4,5,6,7,8,9,10]
k=2
del a[k-1::k]
print(a)

k=3
del a[k-1::k]
print(a)

k=4
del a[k-1::k]
print(a)

k=5
del a[k-1::k]
print(a)

print()
a=[2,4,6,8,9,10,12,14,16]
a.pop(0)
a.pop(4)
a.pop(6)
print(a)

k=1
#2d array
row=[]
for i in range(4):
    col=[]
    for j in range(3):
        n=k+1
        col.append(n)
    row.append(col)

print()
print(row)
print()

#row=[]
#for i in range(4):
 #   col=[]
    #for j in range(5):
        #col2=[]
       # for k in range(6):
           # col3=[]
            #for l in range(7):
               # col4=[]
print()
l=[x for x in range (10)]
print(l)
l=[x for (i,x) in enumerate(l) if i not in (1,5,7)] #where i is the index of enumerated l
print(l)

print()
s="abcdef"
t="defghh"
l=[x for x in s]
print(l)
y=[x for x in t]
print(y)
m=[x for (i,x) in enumerate(l) if x in y and x not in l[i+1:]]#intersection between two sets
print(m)
print()
l=[x for x in l for x in l]#printing abcdef the same no of times as abcdef is present
print(l)
print()

#printing  aa,bbb,cccc,ddddd,eeeeee..........
s="abcdefghijklmnopqrstuvwxyz"
l=[x*(i+1) for (i,x) in enumerate(s)]
print(l)
l=[chr(i)*(i-96) for i in range(97,122)]
print(l)
print()

#create 3*4*5 matrix with * sign
l=[[['*' for x in range(5)]for x in range(4)]for x in range(3)]
print(l)