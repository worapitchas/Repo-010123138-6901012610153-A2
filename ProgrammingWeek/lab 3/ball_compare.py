def compare_ball(football,basketball,volleyball):

    if football > basketball and football > volleyball:
        print(f"ลูกฟุตบอลมีจำนวนมากที่สุด ({football} ลูก)")
        
    elif basketball > football and basketball > volleyball:
        print(f"ลูกบาสเกตบอลมีจำนวนมากที่สุด ({basketball} ลูก)")
        
    elif volleyball > football and volleyball > basketball:
        print(f"ลูกวอลเลย์บอลมีจำนวนมากที่สุด ({volleyball} ลูก)")
        
    else:
        print(f"ไม่มีลูกบอลใดมากที่สุด")

fb = int(input("กรอกจำนวนลูกฟุตบอล: "))
bb = int(input("กรอกจำนวนลูกบาสเกตบอล: "))
vb = int(input("กรอกจำนวนลูกวอลเลย์บอล: "))

compare_ball(fb,bb,vb)