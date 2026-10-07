# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

limit = 20
value = int(input("Value: "))

if value > limit:
    print("OVER")
elif value==limit:
    print("WARNING")
else:
    print("OK") 
