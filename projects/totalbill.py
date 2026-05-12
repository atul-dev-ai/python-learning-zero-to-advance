price = float(input("Enter product price: "))
quantity = float(input("Enter product quantity: "))

total_price = price * quantity
gst = total_price * 18/100
final_amount = total_price + gst

print("Total Price: ", total_price)
print("GST: ", gst)
print("Final Amount", final_amount)