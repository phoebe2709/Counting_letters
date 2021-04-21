
a = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
c=['A']
d = ['G']
e = ['C']
f = ['T']
count=0
for i in a:
    if str(i) in c:
        count+=1

print("A =",count)

count=0
for i in a:
    if str(i) in d:
        count+=1
        
print("G =",count)

count=0
for i in a:
    if str(i) in e:
        count+=1

print("C =",count)


count=0
for i in a:
    if str(i) in f:
        count+=1
        
print("T =",count)