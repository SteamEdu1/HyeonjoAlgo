"""
While loops are similar to for loops except they are much more customisable

definition: while loops repeat code as long as a condition is true
"""

# example 1 - infinite loop:
while 1 == 1:
    print("hello")

# example 2 - invalid loop:
while 1 == 2:
    print("hello")

# example 3 - counter while loop
# i represents the counter
# repeat code as long as i is less than 10
# the below code will print:
# 0 1 2 3 4 5 6 7 8 9
i = 0
while i < 10:
    print(i)
    i += 1

# example 4 - inputs with while loop
print("What is 1 + 1?")
answer = input()
while answer != "2":
    print("You got the wrong answer")
    answer = input()
print("You got the right answer")

# example 5 - inputs + break in while loop
print("What is 1 + 1?")
answer = input()
while True:
    if answer != "2":
        print("You got the wrong answer")
        answer = input()
    else:
        print("You got the right answer")
        break
