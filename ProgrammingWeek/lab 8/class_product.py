class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)

    def show(self):
        print(f"ชื่อ {self.name} ราคา {self.price} ปริมาณ {self.quantity}")


def show_most_product(products):
    if not products:
        print("ไม่พบข้อมูลสินค้า")
        return

    max_product = products[0]

    for p in products:
        current_value = p.price * p.quantity
        max_value = max_product.price * max_product.quantity

        if current_value > max_value:
            max_product = p

    print("สินค้าที่มีมูลค่ามากที่สุดคือ:")
    max_product.show()


product_list = []

with open("class_product.txt", "r", encoding="utf-8") as file:
    for line in file:
        
        data = line.strip().replace(",", " ").split()
        if len(data) == 3:
            s = Product(data[0], data[1], data[2])
            product_list.append(s)

show_most_product(product_list)