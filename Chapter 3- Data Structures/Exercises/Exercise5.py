names = ["Luna" , "Jasper" , "Chris"]
for i in names:
    print(i , "We are gladly inviting you to join us on a delicious dinner party")
print("Sorry" ,names[1] , "can't make it to dinner")
names.remove("Jasper")
print(names)
names.insert(1,"jack")
print(names)
for i in names:
    print(i , "We are gladly inviting you to join us on a delicious dinner party")