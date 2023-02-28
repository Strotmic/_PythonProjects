l = [None, '1-abc-353', 'None', None, '1-fds-334']
count=0
print('Dit is de status van de parkeergarage:')
for i in range(len(l)):
    if l[i] == None:
        count +=1
        print(f"Plaats {i} - vrij")
    else:
        print(f"Plaats {i} - bezet")

print(f'Aantal vrije plaatsen \n {count}')
