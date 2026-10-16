def durian_calculator():
    total_count = 0     
    total_weight = 0.0  

    weight = -1
    while weight != 0:
        weight = float(input("Please input Durian weight: "))

        if weight > 0:
            total_count = total_count + 1      
            total_weight = total_weight + weight 

   
    if total_count > 0:
        avg_weight = total_weight / total_count
        print(f"Total of {total_count} Durians")
        print(f"Average weight is {avg_weight:.2f}")
    else:
        print("No durians recorded.")

durian_calculator()