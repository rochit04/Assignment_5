dictionary={'Arun':56,'Rajdip':88,'Alice':85,'Vim':75}
a=input("Enter the student's name:")
if a in dictionary:
    print(a,"'s marks is:",dictionary[a])
else:
    print('Student not found.')
