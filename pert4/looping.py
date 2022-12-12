# looping python with range
for i in range(5):
    print(i)

#looping python with break
for i in range(1,11):
    print(i,' x ',i ,' = ',i*i)
    if i == 5:
        break

# looping python with continue
for i in range(1,11):
    if i == 5:
        continue
    print(i,' x ',i ,' = ',i*i)

# nested loop
listCity = ['Kalimantan', 'Sumatra', 'Sulawesi']
listPlace = ['West', 'North', 'South']
for city in listCity:
    for place in listPlace:
        print(city, place)



# contoh penambahan terkait break/continue
for val in "bahasa":
    if val == "h":
        continue
        #break
    print (val)
print ("selesai")