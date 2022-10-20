sandwich_orders = ["Zinger" , "Grilled Chicken" , "Veggie" , "Cheese"]
finished_sandwich = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I am making your {current_sandwich} sandwich.")
    finished_sandwich.append(current_sandwich)
print("\n")
for sandwich in finished_sandwich:
    print(f"I made a {sandwich} sandwich.")