states = ["washington", "Oregon", "California"]

'''
print(states[-0])
print(states[-1])
print(states[-2])
'''

states[2] = "Arizona" 
print(states)

#print(len(states))#

states.append("New York")
print(states)

states.pop(1)
print(states)