def ft_check_card(ord_type, price,deposit):

    
    print('*****카드잔액*****')
    if ord_type == '입금':
        deposit += price
        print(f'{price}원 입금되었습니다.')
        print(f'현재 잔액: {deposit} 원\n')
    elif ord_type == '출금':
        deposit -=price
        print(f'{price}원 출금되었습니다.')
        print(f'현재 잔액: {deposit} 원\n')
    else:
        print('잘못 누르셨습니다.')
    
    
product_list = {1: 1000, 2: 1200, 3: 500}

def ft_card_vending_machine(prod_n,price):
    
    if prod_n not in product_list.keys():
            print(f'물건이 없습니다.')
       
    else:
        deposit = 1000000
        ft_check_card('출금',price,deposit)
        print(f'-----자판기-----')
        product_price = product_list[prod_n]
        
        if product_price > price:
            money = product_price - price
            
            print(f'남은 금액: {money}원\n')
            ft_check_card('출금',money,deposit-price)
            print(f'-----자판기-----\n상품 ({prod_n})가 나왔습니다.\n')
            
        elif product_price < price:
            money = price - product_price
            print(f'거스름돈: {money}원\n상품 ({prod_n})이 나왔습니다.\n')                
            ft_check_card('입금',money,deposit-price)
        else:
            print(f'상품 ({prod_n})이 나왔습니다.\n')
