#shrinking guest list
names = ["Luna" , "jack" , "Chris"]
print("Sorry, we can only invite two people to dinner. ")
print("Sorry" , names.pop() , "there's no room at the table.")
for i in names:
    print(i , "I invite you to dinner")
for i in names:
    del names[0]
    del names[0]
print(names)
print("No of guests coming for dinner:",len(names))
