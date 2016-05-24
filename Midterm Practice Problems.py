# If you want to run the code, you should comment out the problems you haven't
#  done yet so you can't see the answers for them.
# Hints for each problem are at the bottom of this file


# === From Memory ===
# Problem 1: Recursion Code
# Problem 2: Multiple Choice about Function Failure
# Problem 3: Try/Except/Finally Output
# Problem 4: Matching about Host/Port
# Problem 5: Defining Class (initializing)
# Problem 6: Know the difference between Private/Public functions/attributes
# Problem 7: Meaning of if name == main
# ====================

# ===== PRACTICE MIDTERM =====
# 1. What's the output of the following code? 
try:
    try:
        a = 5
        b = 7
        c = "five"
        d = "seven"
        print(a*c)
        print(c+d)
    except:
        print(b*c)
    else:
        print(c*d)
    finally:
        print("first finally")
except:
    print("second except")
else:
    print("second else")
finally:
    print("second finally")


# 2. Imagine you have 3 modules as seen below
"first.py"
import second
print("1")
if __name__ == '__main__':
    print("first main")

"second.py"
import third
print("2")
if __name__ == '__main__':
    import first
    print("second main")

"third.py"
print("3")
if __name__ == '__main__':
    import second
    print("third main")

# What is the output if
#  a) first.py is run,
#  b) second.py is run, and
#  c) third.py is run?


# 3. What's wrong with the following class? Just try to fix the class,
#  don't fix anything in the if name = main block
class Person:
    def __init__(name):
        self.name = name
    def grow_up():
        self.age += self.age + 1

if __name__ == '__main__':
    a = Person("Alex")
    a.grow_up()


# 4. Write a function that takes a nested list of integers and returns the
#  sum
def find_sum(l: list) -> int:
    pass


# 5. What does the underscore before a function mean?




# 6. What does the if __name__ == '__main__' statement mean?





## Read all his code examples for review. If you understand everything he
##  wrote in his code examples, as well as what you did in projects,
##  you should be fine.
## Things to look over that I didn't go in depth about:
##  the sockets, protocol, and classes code examples.
## Make sure you're able to write your own classes!
## On Wednesday I'll be going over any questions you might have, so make sure
##  to bring them!








## Hints 
## 1. Remember what each word means. When do you do the except and else
##  blocks? When in doubt, always do finally!
##
## 2. If a module is loaded once through import, it doesn't load again, even if
##  the same import is called again. Python is smart enough to remember what
##  modules have been loaded already
##
## 3. Remember what we went over in class about classes. What always has to be
##  inside a class? There's 2 problems only, but they might be found in multiple
##  places
##
## 4. With recursion, always start small. How do you find the minimum of a simple
##  list of integers? After you get that, seperate it into the differnt possible
##  cases and deal with each seperately.













        

