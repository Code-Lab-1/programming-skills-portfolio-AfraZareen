sandwich_orders = ["pastrami" , "grilled chicken" , "zinger" , "pastrami" , "cheese" , "veggie" , "pastrami"]
finished_sandwich = []
print("I am sorry for the inconvenience, we are out of pastrami.")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I am making your {current_sandwich} sandwich.")
    finished_sandwich.append(current_sandwich)
print("\n")
for sandwich in finished_sandwich:
    print(f"I made a {sandwich} sandwich.")    