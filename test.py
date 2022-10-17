from checker import Checker


thing = input("Enter a file (full root url) to check: ")
check = Checker()
print(open(thing).read())
check.check(thing)
