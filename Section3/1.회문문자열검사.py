n = int(input())

#1
for i in range(n):
    a = input()
    a = a.upper()
    size = len(a)
    for j in range(size//2):
        if a[j] != a[-1-j]:
            print('#%d NO'%(i+1))
            break
    else:
        print('#%d YES'%(i+1))

#2
for i in range(n):
    a = input()
    a = a.upper()
    if a == a[::-1]:
        print('#%d YES' % (i + 1))
    else:
        print('#%d NO' % (i + 1))