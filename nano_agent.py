# WHAT WILL BE MY FINAL PROJECT FOR UDACITY

# An agent needs data input

# Input specifies it's state, for an MDP this state specifies everything the agent need know to predict the future
# for a POMDP this is not the case

# Our agent needs to select actions that maximize future rewards, not just imediate rewards. This is accomplished by value 
# functions; value functions are recursive functions that equal the value function of the next state plus the reward from the 
# action taken to get there. Future value functions are often decreased geometrically with the time to realization. 

# We take an action based on our policy, land in the next state, and get a reward. 
