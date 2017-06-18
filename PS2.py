#------------------
# User Instructions
#
# Hopper, Kay, Liskov, Perlis, and Ritchie live on
# different floors of a five-floor apartment building.
#
# Hopper does not live on the top floor.
# Kay does not live on the bottom floor.
# Liskov does not live on either the top or the bottom floor.
# Perlis lives on a higher floor than does Kay.
# Ritchie does not live on a floor adjacent to Liskov's.
# Liskov does not live on a floor adjacent to Kay's.
#
# Where does everyone live?
#
# Write a function floor_puzzle() that returns a list of
# five floor numbers denoting the floor of Hopper, Kay,
# Liskov, Perlis, and Ritchie.

import itertools

def higher(a,b):
    return a > b;

def adjacent(a,b):
    return abs(a-b) == 1;

def floor_puzzle():
    floors = bottom, _, _, _,top = [1,2,3,4,5]
    orderings = list(itertools.permutations(floors))  #1
    return next([Hopper, Kay, Liskov, Perlis, Ritchie]
            for (Hopper, Kay, Liskov, Perlis, Ritchie) in orderings
            if Hopper is not top
            if Kay is not bottom
            if Liskov not in [bottom,top]
            if higher(Perlis,Kay)
            if not adjacent(Ritchie,Liskov)
            if not adjacent(Liskov,Kay))

print(floor_puzzle())

# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes
# a string as input and returns the i and j indices that
# correspond to the beginning and end indices of the longest
# palindrome in the string.
#
# Grading Notes:
#
# You will only be marked correct if your function runs
# efficiently enough. We will be measuring efficency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!

def find_pal(text,a,b):
    if a<0:
        return (0,0)
    if b> len(text)-1:
        return (a,a)

    while a>=0 and b<len(text) and text[a] == text[b]:
        a-=1
        b+=1

    if a < 0 or b>=len(text) or text[a] != text[b]:
        return (a+1,b)
    return (a,b+1)

def gen_pal(text,i):
    # scan string from left to right to try to find middle of palindroms
    # in the form aa or aba
    return max( (find_pal(text,i,i+1),find_pal(text,i-1,i+1)),key=lambda x: x[1]-x[0])

def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    if text == '':
        return (0,0)
    text= text.lower()
    val = max( (gen_pal(text,i) for i in range(len(text))),key=lambda x: x[1]-x[0])
    print("MAX " + str(val))
    return val

def test():
    L = longest_subpalindrome_slice
#    assert L('racecar') == (0, 7)
#    assert L('Racecar') == (0, 7)
#    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8,21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'

print(test())
