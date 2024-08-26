NAMES = ["John", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23]

# enumerate
# for i, name in enumerate(NAMES):
#     print(f"{i} {name}")

# enumarate ages
for i, age in enumerate(AGES):
    print(f"{i} {age}")


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



# enumerat2
for i, musician in enumerate(JOHN_PAUL):
    print(f"{i} {musician}")