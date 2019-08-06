def convert(s):
    new = ""
    for x in s:
        new = new + x

    return new
s = ['t', 'a', 'm', 'a', 'g', 'h', 'n', 'o']
print(convert(s))


def sublists(list1):
    sublist = []

    for i in range(len(list1) + 1):

        for j in range(i + 1, len(list1) + 1):

            sub = list1[i:j]
            print(sub)
            sublist.append(sub)

    return sublist

l1 = [1, 2, 3, 4, 5]
print(sublists(l1))


my_list=['p','q']
n = 4
new_list = ['{}{}'.format(x, y) for x in my_list for y in range(1, n+1)]
print(new_list)
print()

#DICTIONARY IN PYTHON DENOTED WITH {}
#d={'key1':[value1,value2],'key2':[value3,value4]}
d={1:[11,12],2:[22,21]}
print(len(d))
print(d.keys())#all the keys i the dictionary
print(d.values())#all value in the dictionary
print(d.items())#array of tuples
print([item for item in d])#all keys or print(x for x in d) ....similar to d.keys()
print(d)#prints the exact dictionary
print(d[1] + d[2])#key hoche 1 ..........like d[key] ........key of dictionary cant be represented as an index no.
print(type(d[1]))
print(d[1][0],d[1][1])#..........d[key][value_index]......thats the format
d[1][0]=20#modify a key value in the dictionary
print(d)

d[3]=20
print(d)#ading a new key 3 with value 20
d[3]=40#modifying the newly added value of key=3 with 40
print(d)

d[1]=[d[1],30]
print(d)
d[1].append(30)
print(d)


l1=[1,2,3,4,5]
l2=[4,5,6]
l3=[x*y for (x,y) in zip(l2,l1)]#looks for the minimum number of list elements
print(l3)
print()


d={'k1':{'k11':[20,{'k12':30}]}}
print(d)
print(d['k1']['k11'][1]['k12'])#accessing 30
print()


#print color name with corresponding color code with dictionary
cname=['black','white','blue']
ccode=['#100','#200','#300']
print(cname[0])
#e={'key1':[value1,value2],'key2':[value3,value4]}
e=[{'color name':[x for x in cname],'color code':[x for x in ccode]}]
print(e)
e=[{'color name':x,'color code':y} for x,y in zip(cname,ccode)]
print(e)
print()
