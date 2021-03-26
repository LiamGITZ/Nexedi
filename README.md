# Nexedi
#Terms :
**Efficiency :**
  The money a given machine will make if it is the only purchased machine (regardless of if it can be purchased) divided by the number of days its operates. 
  = ((total_days - day_purchased) * daily_profit_generated) + (price - resale)) / (total_days - day_purchased)

**Break Even Day :**
  The day on which the purchase of the machine will be payed off.
  = Purchased_day + ceil((price-resale) / daily_profit_generated)

#Greedy Algorithim ~(1.5 hrs) : 
  Created an algorithim that first calculated the efficiency of each machine. The program then walked through the list of machines calculating if purchasing any
  given machine would be a net positive income before the next even more efficient machine and if it was net positive would purchase the machine.
  This approach does a decently good job of predicting the most optimal machines however it does have a flaw if the next purchaseable machine is not the next more 
  efficient machine. 
  
  **Failure point**
  Day1:----------------------------------->Day6-->Day8 
  Current_machine(lowest efficiency)------>next_machine(slightly more efficienct)-->last_machine(most efficient) 
  
  For example in the diagram above if the Current_machine's break even day was on the seventh day our current algorithim would not purchase it as it would not make 
  us money before the next most effiecent machine however in this case we do want to purchase the Current_machine because we will not be purchasing the next_machine 
  and will instead be purchasing the last_machine giving us more than enough time to break_even.
  
  ~(2 hrs of thought)
  #Recursive Solution ~(2hrs) :
    Created an algorithim that first calculated the efficiency and break_even_day of each machine. The algori
 p.
  
  **Failure point**
  RecursionError: maximum recursion depth exceeded while calling a Python object

#Final Solution ~(2hrs) :
   The same methedology as the recursive solution with the difference of being alcoated on the heap instead of the call stack.
