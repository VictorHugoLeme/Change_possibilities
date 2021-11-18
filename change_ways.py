QUARTER = 25
DIME = 10
NICKEL = 5
PENNIE = 1


def makeChange(value):
    # i just iterate the value trough the list of coins
    # growing the number of the coin until the value is 0
    # then i go for the next coin
    way_list = []
    way = [0, 0, 0, 0]
    for q_quant in range((value // QUARTER) + 1):
        # set the quarter quantity to the way:
        way[0] = q_quant
        value_after_Q = value - (q_quant * QUARTER)

        for d_quant in range((value_after_Q // DIME) + 1):
            # set the dime quantity to the way:
            way[1] = d_quant
            value_after_D = value_after_Q - (d_quant * DIME)

            for n_quant in range((value_after_D // NICKEL) + 1):
                # set the nickel quantity to the way:
                way[2] = n_quant
                value_after_N = value_after_D - (n_quant * NICKEL)
                p_quant = value_after_N // PENNIE

                # set the pennie quantity to the way:
                way[3] = p_quant

                # append to the way list making a copy of the way:
                way_list.append(way.copy())

                # revomes any dup if existent:
                way_list = [
                    _way
                    for ind, _way in enumerate(way_list)
                    if _way not in way_list[:ind]
                ]
    return way_list


n = 25
print(makeChange(n))
