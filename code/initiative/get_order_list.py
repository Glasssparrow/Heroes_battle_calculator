

def get_order_list(unit1, unit2):
    fast_unit, slow_unit = unit1, unit2
    if fast_unit.initiative < slow_unit.initiative:
        fast_unit, slow_unit = slow_unit, fast_unit
    time_fast = (1-fast_unit.initiative_position)/fast_unit.initiative
    time_slow = (1-slow_unit.initiative_position)/slow_unit.initiative
    step_fast = 1 / fast_unit.initiative
    step_slow = 1 / slow_unit.initiative
    order = {
        time_fast: fast_unit.color,
        time_slow: slow_unit.color
    }
    for x in range(5):
        order[time_fast+x*step_fast] = fast_unit.color
        order[time_slow+x*step_slow] = slow_unit.color
    sorted_items = sorted(order.items(), reverse=True)
    while (len(sorted_items) > 4 and
           sorted_items[0][1] == sorted_items[1][1] == slow_unit.color):
        del order[sorted_items[0][0]]
        del sorted_items[0]

    return sorted(order.values())
