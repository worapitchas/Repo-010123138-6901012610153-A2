def cal_ticket_price(tickets):
    total = tickets * 100  
    return total           

amount = int(input("กรอกจำนวนตั๋วที่ต้องการซื้อ (ใบ): "))

price = cal_ticket_price(amount)

print(f"ราคารวมทั้งหมดคือ: {price} บาท")

