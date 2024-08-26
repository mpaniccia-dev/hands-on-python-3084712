NAMES = ["John", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23]

# JOHN = NAMES[0]
# PAUL = NAMES[1]

JOHN_PAUL = NAMES[:3]  #TO THE LEFT OF 2
# GEORGE_RINGO = NAMES[2:] #TO THE RIGHT OF 2
# REVERSE = NAMES[::-1] #START:STOP:STEP  = NO START, NO STOP, REVERSE STEP
# EVERY_OTHER = NAMES[::-2]

# print(sum(AGES))
# print(min(AGES))
# print(max(AGES))

print(JOHN_PAUL)
# print(GEORGE_RINGO)
# print(REVERSE)


# i = 0
# while i < len(NAMES):
#     print(NAMES[i], AGES[i])
#     i += 1

# for name in NAMES:
#     print(name)

# for name, age in zip(NAMES, AGES):  #zip is like building a new list but does not take up space in memory
#     print(f"{name} {age}")

# for name in reversed(NAMES):
#     print(name)

# for i in range(5):
#     print(i)    

# enumerate
# for i, name in enumerate(NAMES):
#     print(f"{i} {name}")

# enumerat2
for i, musician in enumerate(JOHN_PAUL):
    print(f"{i} {musician}")
    
