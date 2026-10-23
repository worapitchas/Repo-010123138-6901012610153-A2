class integer:
    def __init__(self,number,add_number,remove_number):
        self.number = number
        self.add_number = int(add_number)
        self.remove_number = int(remove_number)

    def show(self):
        return f"ตัวเลข {self.number}"

    def add(self):
        self.number.append(self.add_number)
        return f"ตัวเลขหลังเพิ่ม {self.number}"

    def remove(self):
            self.number.remove(self.remove_number)
            return f"ตัวเลขหลังลบ {self.number}"


class set(integer):
    def __init__(self,number,add_number,remove_number):
        super().__init__(number,add_number,remove_number)
    def show(self):
        show_set = super().show()
        return show_set

    def add(self):
        for v in self.number:
             
            if v != self.add_number:
                self.number.append(self.add_number)
                return f"ตัวเลขหลังเพิ่ม {self.number}"
            else:
                return "เลขซ้ำ"
            
    def remove(self):
        remove_set = super().remove()
        return remove_set

class bag(integer):
    def __init__(self,thing,add_thing,remove_thing):
        self.thing = thing
        self.add_thing = add_thing
        self.remove_thing = remove_thing

    def show(self):
        return self.thing

    def add(self):
        self.thing.append(self.add_thing)
        return f"กระเป๋าหลังเพิ่ม {self.thing}"
            
    def remove(self):
        self.thing.remove(self.remove_thing)
        return f"กระเป๋าหลังลบ {self.thing}"




list_number = [1,2,3,4,5,6,7,8,9]
list_set1 = [1,2,3,4,5,6,7,8,9]
list_set2 = [1,2,3,4,5,6,7,8,9]
list_bag = ["lipstick","mirror","pen"]

integer1 = integer(list_number,"10","1")
set1 = set(list_set1,"10","1")
set2 = set(list_set2,"1","1")
bag1 = bag(list_bag,"pencil","mirror")

print(integer1.show())
print(integer1.add())
print(integer1.remove())
print(set1.show())
print(set1.add())
print(set1.remove())
print(set2.show())
print(set2.add())
print(set2.remove())
print(bag1.show())
print(bag1.add())
print(bag1.remove())
