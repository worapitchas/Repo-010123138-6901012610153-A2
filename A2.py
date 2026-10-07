from datetime import datetime

class Device:
    def __init__(self, device_id, name, status="Available"):
        self.id = device_id
        self.name = name
        self.status = status 

class BorrowSystem:
    def __init__(self):
       
        self.devices = {}    
        self.users = set()     
        self.records = []    

    
    def add_device(self, device_id, name, status="Available"):
        self.devices[device_id] = Device(device_id, name, status)

    def add_user(self, user_id):
        self.users.add(user_id)

    
    def show_status(self):
        print("\n=== ข้อมูลและสถานะอุปกรณ์ในระบบ ===")
        for d_id, device in self.devices.items():
            print(f"รหัส: {device.id} | ชื่อ: {device.name} | สถานะ: {device.status}")

