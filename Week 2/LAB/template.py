"""
RECORD CHECK  -  my version
===========================

Name  :Theo
Lane  :AI      (delete two)
Date  :03-10-26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())While True:

while True:

    label =input("Enter a hostname or type 'quit' if you wish to leave: ")
    if label == "quit":
        break
    else:


     value =float(input("Enter value: "))     
     limit = float(input("Enter limit: "))     


# ================================================================== PROCESS
# 2. Work out the difference and the percentage.       [Typical and above]

    difference =limit-value  # replace with your calculation
    percent = (value/limit)*100 # replace with your calculation
# 3. Decide a status and store it in a variable called status.
#
#    Threshold : if / else        -> "OVER LIMIT" or "OK"
#    Typical   : if / elif / else -> "OVER LIMIT" (100% or more),
    count=0                                  
    if percent>=100:
        status = "OVER LIMIT"
        count+=1
    elif percent>=90:
        status="WARNING"
    else:
        status= "OK"
         


# =================================================================== OUTPUT
# 4. Print the report.
#
#    Threshold : the three values you were given, plus status, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : wrap sections 1-4 in a loop so you can check as many records
#                as you like in one run - type "quit" as the label to stop.
#                Keep count of how many came back OVER LIMIT and print that
#                once, after the loop ends.

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"  Value       : {value:>10.2f}")
    print(f"  Limit       : {limit:>10.2f}")
    print(f"  Difference  : {difference:>+10.2f}")
    print(f"  Of limit    : {percent:>9.1f} %")
    print(f"  Status      : {status:>10}")



    print("=" * 34)

print(f"{count} record(s) came back with a status of 'over limit'")
# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds
