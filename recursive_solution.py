import time
from line_profiler import LineProfiler
import math
'''
machines is a list of currently available machines to purchase (now or future)

current_money = [cash, resale, daily_earnings, day_calculated, cur_efficency]

num days is total number of days

memo = machines[
               for each Machine "[(money_found, efficiency_found), (money_found, efficiency_found)]"
               ]

'''
def find_max_profit(machines, current_money, num_days, memo):
    machines = machines.copy()
    if len(machines) == 0:
        total_money = current_money[0] + current_money[1] + (current_money[2] * (num_days - current_money[3]))
        return total_money, []

    machine = machines.pop(0)
    total_money = current_money[0] + current_money[1] + (current_money[2] * (machine[0] - current_money[3] -1))

    for memoed in memo[machine[6]]:
        if memoed[0] >= total_money and memoed[1] >= current_money[4]:
            return 0, []

    buy = 0
    if total_money >= machine[1]:
        machines = [x for x in machines if (x[4] > machine[4] or x[5] < machine[5])]
        current_money_buy = [total_money-machine[1], machine[2], machine[3], machine[0], machine[4]]
        buy, buy_machines = find_max_profit(machines, current_money_buy, num_days, memo)

    not_buy, not_buy_machines = find_max_profit(machines, current_money, num_days, memo)

    memo[machine[6]].append((total_money, current_money[4]))
    if buy > not_buy:
        buy_machines.append(machine)
        return buy, buy_machines
    return not_buy, not_buy_machines



f = open('input.txt', 'r')

startTime = time.time()
test_case = f.readline().rstrip().split(' ')
case_num = 1
while test_case != ['0','0','0']:
    num_machines = int(test_case[0])
    current_money = int(test_case[1])
    num_days = int(test_case[2])

    machines = []
    memo_id = 0
    for i in range(num_machines):
        machine =  list(map(int, f.readline().rstrip().split(' ')))

        efficency = 0
        break_even = num_days+1
        if machine[0] == num_days:
            efficency = machine[2] - machine[1]
        else:
            efficency =  (((num_days - machine[0]) * machine[3]) + (machine[2] - machine[1])) / (num_days - machine[0])
            break_even_day = machine[0] + math.ceil((machine[1] - machine[2]) / machine[3])

        if efficency > 0:
            machine.append(efficency)
            machine.append(break_even_day)
            machine.append(memo_id)
            memo_id += 1
            machines.append(machine)
    machines.sort()

    print(machines)
    current_money_list = [current_money, 0, 0, 0, 0]
    memo = [[] for i in range(len(machines))]
    #lp = LineProfiler()
    #lp_wrapper = lp(find_max_profit)
    #money, used_machines = lp_wrapper(machines, current_money_list, num_days, memo)
    #lp.print_stats()
    money, used_machines = find_max_profit(machines, current_money_list, num_days, memo)
    print('Case '+str(case_num)+': '+str(money))
    #print(used_machines)

    test_case = f.readline().rstrip().split(' ')
    case_num += 1
executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))
