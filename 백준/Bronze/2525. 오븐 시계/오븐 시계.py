hour, minute = map(int, input().split())
timer = int(input())

hour = (hour + ((minute + timer)//60) )%24
minute = (minute + timer)%60

print(hour,minute)