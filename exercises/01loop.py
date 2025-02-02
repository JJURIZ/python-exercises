# Write a method called `p_times` that takes a `statement` and
# a `num` as inputs, and outputs the `statement` some `num` of times
# to the console.
#
# Example method call:
#
# p_times('Hello there', 1)
#
# > Hello there
#
# p_times('Hello there', 3)
#
# > Hello there
# > Hello there
# > Hello there

# My Solution
def p_times(str, loops):
    for i in range(loops):
        print(str)

p_times("Hello there!", 4)

# CLASS EXAMPLES
"""
def p_times(statement, num):
    statement = statement + '\n'
    print(statement * num)

p_times('Today is Friday', 1)
p_times('Tomorrow is Saturday', 2)
"""

# USING A WHILE LOOP
"""
def p_times(statement, num):
    i = 0
    while i < num:
        print(statement)
        i += 1

p_times('Today is Friday', 1)
p_times('Tomorrow is Saturday', 2)
"""