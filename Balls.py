def gntr(level, n=1):
    if level <= 1 or n < 1:
        return 0
    return 1+gntr(level-n, n+1)
 
level = int(input())
print(gntr(level))

