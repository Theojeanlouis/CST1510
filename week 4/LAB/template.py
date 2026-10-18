"""
RECORD CHECK  -  my version
===========================

Name  : Theo
Lane  :  AI      
Date  :17/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

# your function(s) go here
def check_record(value, limit):
    """calculate difference and percent and returning them and status also"""
    difference=limit-value
    percent=(value/limit)*100
    if percent >= 100:
        count+=1
        status="OVER LIMIT"
        
    elif percent >=90:
        status= "WARNING"
    else:
        status =  "OK"
    return difference, percent, status
    



def print_report(label, value, limit, difference,percent, status):
    """print all the information when called""" 
    print(f"  Value       : {value:>10.2f}")
    print(f"  Limit       : {limit:>10.2f}")
    print(f"  Difference  : {difference:>+10.2f}")
    print(f"  Of limit    : {percent:>9.1f} %")
    print(f"  Status      : {status:>10}")   











# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#    Threshold : write the list directly in the code - at least 3 records.
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
#    Excellent : also write the results out to a new file (one line per
#                record: label, status), as well as printing them.
#                record: label, status), as well as printing them.
record = [ ]
def load_records(path):
    """Reads label,value, limit lines from a file and returns the list"""
    with open(path) as f:
        for line in f:
            label, value , limit=line.strip().split(",")
            record.append({
                "label": label,
                "value": value,
                "limit": limit
            })
    return record

with open("results2.txt", "w") as f:
    for rec in record:
        if rec["value"] > rec["limit"]:
            f.write(f"{rec["label"]} , OVER LIMIT\n")
        else:
            f.write(f"{rec["label"]} , OK\n")

with open("results2.txt"):
    read=f.read()
    print(read)
# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

# your loop goes here
print(load_records("template.txt"))
for rec in record:
    print(check_record())
    print(print_report())










# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
