quarter = 25
dime = 10
nickel = 5
pennies = 1

"""
    primeiro tentei fazer funcionar da maneira mais simples, utilizando o menor numero de moedas possível
"""

"""def makeChange(value):
    
    def current_change(value):
        quarter_q = value // quarter
        try:
            value = value - (quarter_q * quarter)
        except:
            pass
        dime_q = value // dime
        try:
            value = value - (dime_q * dime)
        except:
            pass
        nickel_q = value // nickel
        try:
            value = value - (nickel_q * nickel)
        except:
            pass
        pennies_q = value // pennies

        way = [quarter_q, dime_q, nickel_q, pennies_q]

    if way[0] > 0:
        current_change(value)

    way_list = []
    way_list.append(way)
    way_list = [ele for ind, ele in enumerate(way_list) if ele not in way_list[:ind]]
    return way_list"""

"""
  depois comecei pela maneira que devia ter começado, com nested loops, diminuindo a quantidade das moedas maiores a cada loop
  mas não deu tempo :/ 
"""


def makeChange(value):
    quarter_q = value // quarter
    for q_q in range(quarter_q):
        try:
            value = value - ((q_q + 1) * quarter)
            print(value)
        except:
            value = value
        """for d_q + 1 in range(dime_q):
        for n_q + 1 in range(nickel_q):
          for p_q + 1 in range(pennies_q):
            
            if value == 0:"""


n = 125
print(f"O valor e {n}")
print(makeChange(n))
