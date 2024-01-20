f = open('Perepis.txt', 'r')
L = []
for i in f:
    i = i.strip('\n')
    L.append(i)
print(L)

k = 0
for i in L:
    L1 = i.split('  ')
    print(L1[0])
    L2 = L1[3].split('.')

    if int(L2[2]) < 1978:
        L2.append(i)
        k += 1
print(k)

a = int(input())
b = int(input())

for i in L:
    L3 = i.split('  ')
    L4 = L3[3].split('.')
    if  a < int(L2[2]) < b:
        print(L2)



f.close()





