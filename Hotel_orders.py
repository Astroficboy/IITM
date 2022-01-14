def DishPrepareOrder(orders):
    sorted_orders = sorted(orders)
    order_dic = {}
    for i in range(0, len(sorted_orders)):
            order_dic[sorted_orders[i]] = 1
            
    for i in range(0, len(sorted_orders)-1):
        if sorted_orders[i] == sorted_orders[i+1]:
            order_dic[sorted_orders[i]] += 1
            
    number_of_times = 0
    for order in sorted_orders:
        value = order_dic.get(order)
        if value > number_of_times:
            number_of_times = value
            continue

        else:
            break
            
    orders_sorted_keys = sorted(order_dic, key=order_dic.get, reverse=True)

    return orders_sorted_keys
