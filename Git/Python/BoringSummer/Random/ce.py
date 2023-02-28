from unicodedata import name


def main():
    i = input()
    count = 0
    l = []
    while i != "stop":
        l.append(i)
        i = input()
    temp= 0
    for i in range(len(l)-1):
        if len(l)>=5:

            if float(l[i]) >=25 and float(l[i+1]) >=25 and float(l[i+2]) >=25 and float(l[i+3]) >=25 and float(l[i+4]) >=25:
                if float(l[i]) >=30 :
                    count+=1
                if float(l[i+1]) >=30 :
                    count+=1
                if float(l[i+2]) >=30 :
                    count+=1
                if float(l[i+3]) >=30 :
                    count+=1
                if float(l[i+4]) >=30 :
                    count+=1
                if count >= 3:
                    temp+=1
    if temp>= 1:
        print("hittegolf")
    else:
        print("geen hittegolf")

if __name__ == '__main__':
    main()