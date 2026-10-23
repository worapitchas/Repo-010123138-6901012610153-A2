def best_salesperson(sales_data):
    max_total = -1
    best_person_index = -1

    for i in range(len(sales_data)):

        current_total = sum(sales_data[i])
        if current_total > max_total:
            max_total = current_total
            best_person_index = i
    return best_person_index, max_total



sales_data = [
    [1200, 1500, 1100, 1800, 2000],  
    [2500, 2100, 1900, 2200, 2400],  
    [900, 1300, 1400, 1000, 1200], 
]

person, total = best_salesperson(sales_data)
print(f"พนักงานที่ทำยอดขายสูงสุดคือคนที่ (Index): {person}")
print(f"ยอดขายรวมทั้งหมด: {total} บาท")