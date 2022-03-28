def solution(ings, menu, sell):
    
    ings_dict = {} # 재료에 대한 딕셔너리
    
    for ings_item in ings: # 재료에 대한 딕셔너리를 만듭니다.
        name, data = ings_item.split()
        ings_dict[name] = int(data)
    
    menu_dict = {} # 각 제품에 대한 수익을 구하기 위해 딕셔너리를 만듭니다.
    
    for menu_item in menu:
        name, ings_list, price = menu_item.split()
        cost = 0 # 재료에 대한 비용
        for key in ings_dict:
            cost += ings_list.count(key) * ings_dict[key]
        
        revenue_data = int(price) - cost # 순이윤
        menu_dict[name] = revenue_data
        
    total_revenue = 0
    
    for sell_item in sell: # 순이윤을 구하기 위한 반복문
        name, data = sell_item.split()
        total_revenue += int(data) * menu_dict[name]
        
    return total_revenue

########################## case 1 ################################
# ings = ["b 30", "e 20", "c 120", "f 10"]
# menu = ["BAGUETTE ffbf 50", "WHITEBREAD efbb 130", "CHOCOBREAD cbefc 450", "EGGBREAD eefbf 150", "SWISSROLL efcb 180", "POUNDCAKE fbbe 170", "MADELEINE feef 120"]
# sell = ["BAGUETTE 30", "WHITEBREAD 43", "CHOCOBREAD 12", "SWISSROLL 10", "POUNDCAKE 7"]

########################## case 2 ################################
ings = ["x 25", "y 20", "z 1000"]
menu = ["AAAA xyxy 15", "TTT yy 30", "BBBB xx 30"]
sell = ["BBBB 3", "TTT 2"]

print(solution(ings, menu, sell))
