from  functions import cal_counter, price_counter 

order = []
while True:
    choice = input("Please enter each choice then press enter, if you are finished enter 'end': ")
    if choice == "end":
        break
    else:
        order = order + [choice]

print(f"Your total calories = {cal_counter(order)}")
print(f"The total price = {price_counter(order)}")




