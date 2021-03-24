import random

max_num = int(1e9)
max_machines = int(1e5)
starting_amount = 1000
max_price = starting_amount * 10
num_tests = 3


f = open('test.txt', 'w')

for i in range(num_tests):
    f.write(str(max_machines)+' 1000 ' + str(max_num)+'\n')
    for i in range(max_machines):

        day = random.randint(1, max_num)
        price = random.randint(2, max_price)
        resale = random.randint(1, price-1)
        daily_money = random.randint(1, max_price/2)

        f.write(str(day)+' '+
                str(price)+' '+
                str(resale)+' '+
                str(daily_money)+'\n')

f.write('0 0 0')
f.close()
