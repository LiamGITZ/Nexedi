# Nexedi

## Running the Project :
#### Dependencies:
python3.9.1 \
pip install dataclasses

Run:   
python3 final_solution.py


## Terms :
#### Efficiency :
The money a given machine will make if it is the only purchased machine (regardless of if it can be purchased) divided by the number of days its operates. \
= ((total_days - day_purchased) * daily_profit_generated) + (price - resale)) / (total_days - day_purchased)

#### Break Even Day :
The day on which the purchase of the machine will be payed off.\
= day_purchased + ceil((price-resale) / daily_profit_generated)

## Greedy Algorithm ~(1.5 hrs) :
Created an algorithm that first calculated the efficiency of each machine. The program then walked through the list of machines calculating if purchasing any given machine would be a net positive income before the next even more efficient machine and if it was net positive would purchase the machine. This approach does a decently good job of predicting the most optimal machines, however it does have a flaw if we do not purchase the next most efficient machine.
 
#### Failure point :
 
    Day1:----------------------------------->Day6-->Day8
    Current_machine(lowest efficiency)------>next_machine(slightly more efficient)-->last_machine(most efficient)
 
 For example, in the diagram above if the Current_machine's break even day was on the seventh day our current algorithm would not purchase it as it would not make us money before the next most efficient machine, however in this case we do want to purchase the Current_machine because we will not be purchasing the next_machine and will instead be purchasing the last_machine giving us more than enough time to break_even.
 
### ~(2 hrs of thought)
## Recursive Solution ~(2hrs) :
Created an algorithm that first calculated the efficiency and break_even_day of each machine. The algorithms then recursively found the best possible combination of machines using Dynamic Programming.
    
The program used 2 optimizations that improved it over brute force:
#### Optimization 1 (Pruning) :
Similar to the strategy of the greedy algorithm, the recursive solution does a pruning step in which any machine that is both less efficient and has a later Break_even_Day is removed. This solves the failure point of our greedy algorithm, as it now takes in to account that we may want a less efficient machine if       it has an earlier break_even_day.
      
 #### Optimization 2 (Memoization) :
Memoization was done saving results at every given level in the recursive tree (see tree below). If our previous results at the same level in the tree had both more total_capital and more efficiency at the same place, then we know our resulting cash will be lower than when we had more money and efficiency. If the efficiency and total_capital are the same, then we know we have already computed the results.\
***(For this step it is important to note that we should try the Buy branches of the tree first before the not_Buy, branches as buying a given machine will give us the possibility of having more money and efficiency.)***
      
Tree:

          /M3
       /M2\M3
     M1
       \M2/M3
          \M3
 
#### Failure point
RecursionError: maximum recursion depth exceeded while calling a Python object

## Final Solution ~(2hrs) :
   The same methodology as the recursive solution with the difference of being allocated on the heap instead of the call stack.
