#Question 1
list = ["Apple" , "Banana" , "Car" , "Dolphin"]
for i in list:
  print("This following lines wil print each letters of " , i)
  for letter in i:
    print(letter)
#Question 2
#Program to find the sum of all numbers stored in a list
numbers = [6,5,3,8,4,2,5,4,11]
sum = 0
for val in numbers:
    sum = sum + val
    print("The sum is" , sum)
