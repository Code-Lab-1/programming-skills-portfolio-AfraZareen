# Pizza Toppings
prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "

while True:
    topping = input(prompt)
    if topping != 'quit':
        print(f"  I'll add {topping} to your pizza.")
    else:
        break

#Method 2
while True:
    pizza = input("What kind pizza topping would you like: ")
    if pizza == "quit":
        break
    print(f"I will add the {pizza} topping to your pizza")
        
