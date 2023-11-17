age = int(input("Enter your age"))
if age < 18:
    if age < 13:
        print("kid")
    else:
        print("teen")
else:
    print("adult")