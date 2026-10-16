from datetime import datetime

class Device:
    def __init__(self, device_id, name, status="Available"):
        self.id = device_id
        self.name = name
        self.status = status 