def coin_exchange():
    amount = -1

    while amount != 0:
        amount = int(input("กรุณาใส่จำนวนเงินที่ต้องการแลก (ใส่ 0 เพื่อเลิกทำ): "))

        if amount > 0:
            temp_amount = amount

            coin10 = temp_amount // 10
            temp_amount %= 10

           
            coin5 = temp_amount // 5
            temp_amount %= 5

        
            coin1 = temp_amount

            print(f"เหรียญ 10 จำนวน {coin10} เหรียญ")
            print(f"เหรียญ 5 จำนวน {coin5} เหรียญ")
            print(f"เหรียญ 1 จำนวน {coin1} เหรียญ")
            print("-" * 30)

    print("จบการทำงานของโปรแกรม")


coin_exchange()