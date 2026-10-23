class vehicle:
    def __init__(self,license_plate,brand,model,year,daily_rate,days):
        self.license_plate = license_plate
        self.brand = brand
        self.model = model
        self.year = int(year)
        self.daily_rate = float(daily_rate)
        self.days = int(days)

    def show(self):
        return f"ป้ายทะเบียน {self.license_plate} แบรนด์ {self.brand} รุ่น {self.model} ปีที่ผลิต {self.year} ค่าเช่ารายวัน {self.daily_rate}"
    
    def cal_rent_cost(self):
        rent_price = self.daily_rate*self.days
        return f"เช่าได้ {self.days} วัน ราคา {rent_price} บาท"


class car(vehicle):
    def __init__(self,license_plate,brand,model,year,daily_rate,days,seats):
            super().__init__(license_plate,brand,model,year,daily_rate,days)
            self.seats = int(seats)
            
    def show(self):
            show_info_car = super().show()
            return f"{show_info_car} จำนวนที่นั่ง {self.seats}"
    
    def cal_rent_cost(self):
            
            rent_price = self.daily_rate*self.days
            if self.days >= 5:
                   self.days += 2
            return f"เช่าได้ {self.days} วัน ราคา {rent_price} บาท"
    
class truck(vehicle):
    def __init__(self,license_plate,brand,model,year,daily_rate,days,payload):
                super().__init__(license_plate,brand,model,year,daily_rate,days)
                self.payload = int(payload)
                
    def show(self):
                show_info_truck = super().show()
                return f"{show_info_truck} น้ำหนัก {self.payload}"
    

vehicle1 = vehicle("จปร6648","susuki","swift","2550","2000","8")
car1 = car("จปร6648","susuki","swift","2550","2000","8","4")
truck1  = truck("จปร6648","susuki","swift","2550","2000","8","9500")

print(vehicle1.show())
print(car1.show())
print(car1.cal_rent_cost())
print(truck1.show())
print(truck1.cal_rent_cost())
