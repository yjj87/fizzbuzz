j = 1
if j==1:
    print("This is {} from conflict1 branch".format(j))

for j in range(10):
    if j%2==0:
    print("This is {} from conflict1 and main branch".format(j))

for j in range(10):
    if j%2==0:
        print("This is {} from conflict1 and main branch".format(j))

for j in range(10):
    if j%2==0:
        print("This is {} from conflict1 and main branch".format(j))
    else:
        print(j)
