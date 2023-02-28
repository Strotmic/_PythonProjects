speed = float(input('What is the download speed in MB/s '))
size = float(input('What is the size in GB '))

total = size * 1000

time = total / speed
time = int(round(time))
hour=0
minuts = 0
seconds=0
days=0
for i in range(time):
    if i % 60 == 0:
        seconds=0
        minuts+=1
        if minuts %60 == 0:
            minuts = 0
            hour +=1
            if hour %24 ==0:
                hour =0
                days+=1

print(f'time till completion is {days} days {hour} hours {minuts} minutes and {seconds} seconds')
