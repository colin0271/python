earning = int(input("выручка"))
costs = int(input("издежки"))

if costs > earning:
    print("убыток.")
elif earning > costs:
    print("прибыль.")
    profitability =round((earning - costs) / earning, 2)
    print(f"рентабельность: {profitability}")
    empl_count = int(input("количество штатных сотрудников:"))
    profit_per_empl =((earning - costs) / empl_count, 2)
    print(f"прибыль фирмы в расчёте на одного сотруднка: {profit_per_empl}")
elif earning == costs:
    print("финансовый рузультат = 0")