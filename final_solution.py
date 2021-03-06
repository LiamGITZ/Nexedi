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
        string = string = (f'({self.day_on_sale} {self.price} {self.resale} {self.daily_earning}'
                         + f' {round(self.efficiency, 3)} {self.break_even_day} {self.index})')
        return string

@dataclass
class Money():
    cash: int
    resale_value: int = 0
    daily_earning: int = 0
    day_calculated: int = 0
    current_efficiency: float = 0



def find_max_profit(machines, starting_money, num_days):
    current_money = Money(starting_money)
    memo = [[] for i in range(len(machines))]

    # the stack contains a list of tuples which contain the information needed to finish any given branch of the tree
    # contain the remaining machines in the current branch of the tree and our current Money values
    stack = []
    stack.append((machines, current_money))
    max_profit = 0

    while stack:
        machines, current_money = stack.pop(-1)

        # reached leaf node in tree
        if len(machines) == 0:
            total_capital = current_money.cash + current_money.resale_value + \
                            (current_money.daily_earning * (num_days - current_money.day_calculated))
            if total_capital > max_profit:
                max_profit = total_capital
            continue

        #create a copy of machines so that we have our own list to edit in each instance
        machines = machines.copy()
        machine = machines.pop(0)
        total_capital = current_money.cash + current_money.resale_value + \
                        (current_money.daily_earning * (machine.day_on_sale - current_money.day_calculated -1))

        # searching our memo to see if we have been at this given level of the tree with strictly better circumstances
        if any(m[0] >= total_capital and m[1] >= current_money.current_efficiency
               for m in memo[machine.index]):
            continue

        '''
        appending not-buys first means we process buys first
        this allows us to skip not buy scenarios where buying the machine is strictly better in terms of money and efficency
        '''
        if total_capital >= machine.price:
            # removing machines that can not possibly make us more money than our current machine
            pruned_machines= [x for x in machines if (x.efficency > machine.efficency or x.break_even_day < machine.break_even_day)]
            stack.append((pruned_machines, current_money))
            current_money_buy = Money(total_capital-machine.price, machine.resale, machine.daily_earning, machine.day_on_sale, machine.efficency)
            stack.append((pruned_machines, current_money_buy))
        else:
            stack.append((machines, current_money))

        memo[machine.index].append((total_capital, current_money.current_efficiency))

    return max_profit



f = open('input.txt', 'r')

test_case = f.readline().rstrip().split(' ')
case_num = 1
while test_case != ['0','0','0']:
    num_machines = int(test_case[0])
    current_money = int(test_case[1])
    num_days = int(test_case[2])

    machines = []
    memo_index = 0
    for i in range(num_machines):
        read_machine =  list(map(int, f.readline().rstrip().split(' ')))
        machine = Machine(read_machine[0], read_machine[1], read_machine[2], read_machine[3], 0, num_days+1, memo_index)

        if machine.day_on_sale != num_days:
            machine.efficency =  (((num_days - machine.day_on_sale) * machine.daily_earning) + 
                                 (machine.resale - machine.price)) / (num_days - machine.day_on_sale)

            machine.break_even_day = machine.day_on_sale + math.ceil((machine.price - machine.resale) / machine.daily_earning)

            if machine.efficency > 0:
                machines.append(machine)
                memo_index += 1
    # sorted first by day_on_sale, second by efficency, and finally by break_even_day
    machines = sorted(machines)

    money = find_max_profit(machines, current_money, num_days)
    print('Case '+str(case_num)+': '+str(money))

    test_case = f.readline().rstrip().split(' ')
    case_num += 1
