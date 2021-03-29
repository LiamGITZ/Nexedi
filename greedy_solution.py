import time
f = open('input.txt', 'r')

startTime = time.time()
test_case = f.readline().rstrip().split(' ')
test_num = 1
while test_case != ['0','0','0']:
    num_machines = int(test_case[0])
    current_money = int(test_case[1])
    num_days = int(test_case[2])

    machines = []
    for i in range(num_machines):
        machine =  list(map(int, f.readline().rstrip().split(' ')))

        efficency = 0
        if machine[0] == num_days:
            efficency = machine[2] - machine[1]
        else:
            efficency =  (((num_days - machine[0]) * machine[3]) + (machine[2] - machine[1])) / (num_days - machine[0])

        if efficency > 0:
            machine.append(efficency)
            machines.append(machine)
    machines.sort()

    current_daily = 0
    while len(machines) > 0:
        machine = machines.pop(0)
        if current_money >= machine[1]:
            machines = [x for x in machines if x[4] > machine[4]]

            found_next_purchase = False
            profit = (((num_days - machine[0]) * machine[3]) + (machine[2] - machine[1]))
            while not found_next_purchase and len(machines) > 0:
                next_machine = machines[0]
                profit =  (((next_machine[0] - machine[0] - 1) * machine[3]) + (machine[2] - machine[1]))
                if profit + current_money >= next_machine[1] or current_money >= next_machine[1]:
                    if profit < (current_daily * (next_machine[0] - machine[0] - 1)):
                        profit = current_daily * (next_machine[0] - machine[0] - 1)
                    else:
                        current_daily = machine[3]
                    found_next_purchase = True
                else:
                    machines.pop(0)
                    if len(machines) == 0:
                        profit = (((num_days - machine[0]) * machine[3]) + (machine[2] - machine[1]))
            if profit > 0:
                current_money += profit
        else:
            machine.pop(0)

    print('Case '+str(test_num)+': ' + str(current_money))
    test_case = f.readline().rstrip().split(' ')
    test_num+=1
print('it took: ', (time.time() - startTime))
