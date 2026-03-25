stock_count = int(input("How many items are in stock?"))
                 
if stock_count == 0:
    print("Out of stock")
elif stock_count < 5:
    print("Low stock")
else:
    print("In stock")

total = 0
for num in range(2, 51, 2):
    total += num
print(total)