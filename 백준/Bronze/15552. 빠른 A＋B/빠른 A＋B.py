import sys

times = int(input())

for i in range(times):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)