price = int(input())
quantity = int(input())
result = 0

for i in range(quantity):
    a, b = map(int, input().split())
    result += a*b

if price == result:
    print("Yes")
else:
    print("No")
