"""
RECORD CHECK  -  my version
===========================

Name  :Theo
Lane  :AI      
Date  :10/10/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
count=0 
def status_of(percent):
    """returns the status of different percentage"""
    if percent >= 100:
        count+=1
        return "OVER LIMIT"
        
    elif percent >=90:
        return"WARNING"
    else:
        return "OK"
"""defining a function that calculate  anr return a difference and a percentage out of its parameters"""
def check(value, limit):
     difference=limit-value
     percent=(value/limit)*100
     return difference, percent

def print_report(label, value, limit, difference,percent, status):
    print(f"  Value       : {value:>10.2f}")
    print(f"  Limit       : {limit:>10.2f}")
    print(f"  Difference  : {difference:>+10.2f}")
    print(f"  Of limit    : {percent:>9.1f} %")
    print(f"  Status      : {status_of(percent):>10}")   



# ==================================================================== INPUT
# 2. Ask for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())
while True:
    label = input("Enter a label or \"quit\" if you want to quit:")
    if label == "quit" :
            break 
        
        
    value = float(input("Enter a value:"))    # replace with an input() call, converted
    limit = float(input("Enter a limit:"))    # replace with an input() call, converted


# ================================================================== PROCESS
# 3. Work out the difference, the percentage, and the status.
#
#    Threshold : call status_of() to get the status. Work out the
#                difference and percentage inline, not in a function.
#    Typical   : call check() to get the difference and percentage instead.
    difference, percent =check(value,limit)  # replace with your code
    difference=difference
    percent=percent
    status = status_of(percent)          # replace with your code


# =================================================================== OUTPUT
# 4. Print the report.
#
#    Threshold : the three values you were given, plus status, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : call print_report() instead of printing directly here, and
#                wrap sections 2-4 in a loop so you can check as many records
#                as you like in one run - type "quit" as the label to stop.
#                Keep count of how many came back OVER LIMIT and print that
#                once, after the loop ends.

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    

    
    print(print_report(label, value, limit, difference,percent, status))


    print("=" * 34)

print(f"{count} record(s) came back with a status of 'over limit'")
# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every function does one job - if a function both calculates
#        and prints, split it
