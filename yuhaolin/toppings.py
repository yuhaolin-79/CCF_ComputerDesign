requested_toppings = ['mushrooms','onions','pineapple','green peppers']
for topping in requested_toppings:
    if topping == 'green peppers':
        print("Sorry, we are out of green peppers.")
    else:
        print(f"Adding {topping}")
print("\nFinished making your pizza!")

