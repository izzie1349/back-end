
# Complete the tasks below by writing functions! Keep in mind, these can be
# tough, its all about breaking the problem down into smaller, logical
# steps.

#####################
## -- PROBLEM 1 -- ##
#####################

# Given a list of integers, return True if the sequence of numbers 1, 2, 3
# appears in the list somewhere.

def arrayCheck(nums):
    return set(nums).issubset([1,2,3])


print(arrayCheck([1,1,2,3,1]))
print(arrayCheck([1,1,2,4,1]))
print(arrayCheck([1,1,2,1,2,3]))


#####################
## -- PROBLEM 2 -- ##
#####################

# Given a string, return a new string made of every other character starting
# with the first, so "Hello" yields "Hlo".


def stringBits(str):
    new_str = str[::2]
    return new_str

print(stringBits('Hello'))
print(stringBits('Hi'))
print(stringBits('Heeololeo'))


#####################
## -- PROBLEM 3 -- ##
#####################

# Given two strings, return True if either of the strings appears at the very end
# of the other string, ignoring upper/lower case differences (in other words, the
# computation should not be "case sensitive").

def end_other(a, b):
    a = a.lower()
    b = b.lower()

    if a[-3:] == b[-3:]:
        return True

print(end_other('Hiabc', 'abc'))
print(end_other('AbC', 'HiaBc'))
print(end_other('abc', 'abXabc'))

#####################
## -- PROBLEM 4 -- ##
#####################

# Given a string, return a string where for every char in the original,
# there are two chars.

def doubleChar(str):
    s = []
    for char in str:
        s.append(char*2)
    s = ''.join(s)

    return s

print(doubleChar('The'))
print(doubleChar('AAbb'))
print(doubleChar('Hi-There'))





#####################
## -- PROBLEM 5 -- ##
#####################

# Read this problem statement carefully!

# Given 3 int values, a b c, return their sum. However, if any of the values is a
# teen -- in the range 13-19 inclusive -- then that value counts as 0, except 15
# and 16 do not count as a teens.

def no_teen_sum(a, b, c):
  a = fix_teen(a)
  b = fix_teen(b)
  c = fix_teen(c)

  return a+b+c


def fix_teen(n):
    if n >= 13 and n <=19 and n != 15 and n != 16:
        n = 0
    return n


print(no_teen_sum(1, 2, 3))
print(no_teen_sum(2, 13, 1))
print(no_teen_sum(2, 1, 14))


#####################
## -- PROBLEM 6 -- ##
#####################

# Return the number of even integers in the given array.

def count_evens(nums):
  even = []
  for x in nums:
      if x%2 == 0:
          even.append(x)
  count = len(even)
  return count

print(count_evens([2, 1, 2, 3, 4]))
print(count_evens([2, 2, 0]))
print(count_evens([1, 3, 5]))
