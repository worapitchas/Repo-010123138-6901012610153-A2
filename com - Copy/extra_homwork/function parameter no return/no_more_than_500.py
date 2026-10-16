    
def check_val(index):  
    number = [300,800,600,400,300,900,550,650,420,601]
    

    
    val = number[index]

    if val > 500:
        print(f"{val} more than 500")
    else:
        print(f"{val} is not more than 500")
       

index = int(input("choose number order"))

check_val(index)