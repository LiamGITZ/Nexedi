import math
import time
'''
current_money = [cash, resale, daily_earnings, day_calculated, cur_efficency]

memo = machines[
               for each Machine "[(money_found, efficiency_found), (money_found, efficiency_found)]"
               ]

machine = d,p,r,g, efficiency_metric, break_even_day, memo_index
'''
def find_max_profit(machines, starting_money, num_days):
    current_money_list = [starting_money, 0, 0, 0, 0]
    memo = [[] for i in range(len(machines))]

    stack = []
    stack.append((machines, current_money_list))
    max_profit = 0

    while stack:
        machines, current_money = stack.pop(-1)

        if len(machines) == 0:
            total_money = current_money[0] + current_money[1] + (current_money[2] * (num_days - current_money[3]))
            if total_money > max_profit:
                max_profit = total_money
            continue


        machines = machines.copy()
        machine = machines.pop(0)
        total_money = current_money[0] + current_money[1] + (current_money[2] * (machine[0] - current_money[3] -1))

        if any(m[0] >= total_money and m[1] >= current_money[4]
               for m in memo[machine[6]]):
            continue

        '''
        appending not buys first results in a more likely t
        '''
        if total_money > machine[1]:
            machines = [x for x in machines if (x[4] > machine[4] or x[5] < machine[5])]
            stack.append((machines, current_money))
            current_money_buy = [total_money-machine[1], machine[2], machine[3], machine[0], machine[4]]
            stack.append((machines, current_money_buy))
        else:
            stack.append((machines, current_money))

        memo[machine[6]].append((total_money, current_money[4]))

    return max_profit


f = open('test.txt', 'r')

startTime = time.time()
case_num = 1
test_case = f.readline().rstrip().split(' ')
while test_case != ['0','0','0']:
    num_machines = int(test_case[0])
    current_money = int(test_case[1])
    num_days = int(test_case[2])

    machines = []
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
            machine.append(i)
            machines.append(machine)
    machines.sort()

    money = find_max_profit(machines, current_money, num_days)
    print('Case '+str(case_num)+':'+str(money))

    test_case = f.readline().rstrip().split(' ')
    case_num += 1
executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))
