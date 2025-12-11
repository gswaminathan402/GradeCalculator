numTypes=input('Enter number of categories: ')

final=0
i=1
while i <= float(numTypes):
    print('Category ' + str(i))
    grade=input('Enter grade: ')
    weight=input('Enter grade weight: ')
    final+=float(grade)*float(weight)
    i+=1

print('Final Grade: ',final)
