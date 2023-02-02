size=int(input('enter the size of the list :'))
list1=[]
while len(list1)<size:
    elem=input('enter the string :')
    if len(elem)<2:
        print('length of string is less than two')
    else:
        list1.append(elem)
list1.sort(key=lambda x:x[-2])
print(list1)