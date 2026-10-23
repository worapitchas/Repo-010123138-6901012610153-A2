import datetime


class Device:
    def __init__(self, device_id):
        self.device_id = device_id
        self.status = 'Available'  


class BorrowSystem:
    def __init__(self):
        
        self.devices = {
            'DEV001': Device('DEV001'),
            'DEV002': Device('DEV002'),
            'DEV003': Device('DEV003')
        }
        self.users = {
            'U001': True,
            'U002': True,
            'U003': True
        }
        self.records = []   

    
    def borrow_device(self, user_id, device_id):
        u_id = user_id.strip().upper()
        d_id = device_id.strip().upper()

        
        if u_id not in self.users or d_id not in self.devices:
            return "ไม่พบข้อมูล"
        
        device = self.devices[d_id]
        
        
        if device.status != 'Available':
            return "อุปกรณ์ไม่พร้อมใช้งาน"
        
        
        device.status = 'Borrowed'
        
        
        record = {
            'user_id': u_id,
            'device_id': d_id,
            'borrow_date': datetime.date.today().strftime('%Y-%m-%d'),
            'return_date': None
        }
        self.records.append(record)
        return "ยืมสำเร็จ"

    
    def return_device(self, device_id):
        d_id = device_id.strip().upper()

        
        if d_id not in self.devices:
            return "ไม่พบรหัสอุปกรณ์นี้"
        
        device = self.devices[d_id]
        
        
        if device.status != 'Borrowed':
            return "อุปกรณ์ไม่ได้ถูกยืมอยู่"
        
        
        device.status = 'Available'
        
        
        for record in reversed(self.records):
            if record['device_id'] == d_id and record['return_date'] is None:
                record['return_date'] = datetime.date.today().strftime('%Y-%m-%d')
                break
                
        return "คืนสำเร็จ"



if __name__ == "__main__":
    sys = BorrowSystem()

    while True:
        print("\n=========================================")
        print(" รายชื่ออุปกรณ์ในระบบ และ [สถานะปัจจุบัน] ")
        print("=========================================")
        
        for d_id, d_obj in sys.devices.items():
            print(f"- รหัสอุปกรณ์: {d_id} | สถานะปัจจุบัน: [{d_obj.status}]")
        print("=========================================")

        print("\n----- เมนูระบบยืม-คืนอุปกรณ์ -----")
        print("1. ยืมอุปกรณ์")
        print("2. คืนอุปกรณ์")
        print("0. ออกจากโปรแกรม")
        
        choice = input("เลือกทำรายการไหน? (พิมพ์ 1, 2 หรือ 0): ").strip()

        if choice == "0":
            print("\nปิดระบบเรียบร้อย ขอบคุณครับ")
            break

        
        elif choice == "1":
            print("\n--- [ทำรายการยืมอุปกรณ์] ---")
            user_id = input("กรอกรหัสผู้ใช้ (User ID): ").strip()
            device_id = input("กรอกรหัสอุปกรณ์ (Device ID): ").strip()
            
            result = sys.borrow_device(user_id, device_id)
            print(f"\nผลลัพธ์: {result}")
            
            if result in ["ไม่พบข้อมูล", "อุปกรณ์ไม่พร้อมใช้งาน"]:
                print(">> เกิดข้อผิดพลาด! กำลังกลับไปเริ่มต้นโปรแกรมใหม่...\n")
                continue

        
        elif choice == "2":
            print("\n--- [ทำรายการคืนอุปกรณ์] ---")
            device_id = input("กรอกรหัสอุปกรณ์ (Device ID): ").strip()
            
            result = sys.return_device(device_id)
            print(f"\nผลลัพธ์: {result}")
            
            if result in ["ไม่พบรหัสอุปกรณ์นี้", "อุปกรณ์ไม่ได้ถูกยืมอยู่"]:
                print(">> เกิดข้อผิดพลาด! กำลังกลับไปเริ่มต้นโปรแกรมใหม่...\n")
                continue

        else:
            print("\n>> เลือกเมนูไม่ถูกต้อง! โปรดระบุ 1 หรือ 2 เท่านั้น")
            continue

        
        again = input("\nต้องการทำรายการอื่นต่อหรือไม่? (y/n): ").strip().lower()
        if again != 'y':
            print("\nสิ้นสุดการทำงานของโปรแกรม")
            break
