from dataclasses import dataclass
import math

@dataclass
class Machine():
    day_on_sale: int
    price: int
    resale: int
    daily_earning: int
    efficency: float
    break_even_day: int
    index: int

    def __lt__(self, machine2):
        if self.day_on_sale == machine2.day_on_sale:
            if self.efficency == machine2.efficency:
                return self.break_even_day < machine2.break_even_day
            else:
                return self.efficency > machine2.efficency
        return self.day_on_sale < machine2.day_on_sale

    def __repr__(self):
        string = '(' \
            +str(self.day_on_sale)+' '\
            +str(self.price)+' '\
            +str(self.resale)+' '\
            +str(self.daily_earning)+' '\
            +str(round(self.efficency,3))+' '\
            +str(self.break_even_day)+' '\
            +str(self.index)+' '\
            +')'
        return string

@dataclass
class Money():
    cash: int
    resale_value: int
    daily_earning: int
    day_calculated: int
    current_efficiency: float



def find_max_profit(machines, starting_money, num_days):
    current_money = Money(starting_money, 0, 0, 0, 0)
    memo = [[] for i in range(len(machines))]

    stack = []
    stack.append((machines, current_money))
    max_profit = 0

    while stack:
        machines, current_money = stack.pop(-1)

        if len(machines) == 0:
            total_capital = current_money.cash + current_money.resale_value + (current_money.daily_earning * (num_days - current_money.day_calculated))
            if total_capital > max_profit:
                max_profit = total_capital
            continue


        machines = machines.copy()
        machine = machines.pop(0)
        total_capital = current_money.cash + current_money.resale_value + (current_money.daily_earning * (machine.day_on_sale - current_money.day_calculated -1))

        # searching our memo to see if we have been at this given level of the tree with strictly better circumstances
        if any(m[0] >= total_capital and m[1] >= current_money.current_efficiency
               for m in memo[machine.index]):
            continue

        '''
        appending not buys first means we process buys first
        this allows us to skip not buy scenarios where buying the machine is strictly better in terms of money and efficency
        '''
        if total_capital > machine.price:
            # removing machines that can not possibly make us more money than our current machine
            pruned_machines= [x for x in machines if (x.efficency > machine.efficency or x.break_even_day < machine.break_even_day)]
            stack.append((pruned_machines, current_money))
            current_money_buy = Money(total_capital-machine.price, machine.resale, machine.daily_earning, machine.day_on_sale, machine.efficency)
            stack.append((pruned_machines, current_money_buy))
        else:
            stack.append((machines, current_money))

        memo[machine.index].append((total_capital, current_money.current_efficiency))

    return max_profit



f = open('test.txt', 'r')

test_case = f.readline().rstrip().split(' ')
case_num = 1
while test_case != ['0','0','0']:
    num_machines = int(test_case[0])
    current_money = int(test_case[1])
    num_days = int(test_case[2])

    machines = []
    for i in range(num_machines):
        read_machine =  list(map(int, f.readline().rstrip().split(' ')))
        machine = Machine(read_machine[0], read_machine[1], read_machine[2], read_machine[3], 0, num_days+1, i)

        if machine.day_on_sale != num_days:
            machine.efficency =  (((num_days - machine.day_on_sale) * machine.daily_earning) + (machine.resale - machine.price)) / (num_days - machine.day_on_sale)
            machine.break_even_day = machine.day_on_sale + math.ceil((machine.price - machine.resale) / machine.daily_earning)
            if machine.efficency > 0:
                machines.append(machine)
    machines = sorted(machines)

    money = find_max_profit(machines, current_money, num_days)
    print('Case '+str(case_num)+': '+str(money))

    test_case = f.readline().rstrip().split(' ')
    case_num += 1
