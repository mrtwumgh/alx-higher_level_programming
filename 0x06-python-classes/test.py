a = 5
b = (3,2)

for i in range(b[1]):
    print("-")
for i in range(a):
    for j in range(b[0]):
        print('-', end='')
    for j in range(a):
        print('#',end='')
    print()
