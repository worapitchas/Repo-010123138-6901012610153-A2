full_price = float(input("ราคาเต็มสินค้า : "))
discount = int(input("ลดราคากี่เปอร์เซ็น : "))

final_price = full_price - (full_price*(discount*0.01))

print(final_price)