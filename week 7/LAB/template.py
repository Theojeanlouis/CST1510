"""
RECORD CHECK  -  my version
===========================

Name  :Theo
Lane  : AI       
Date  : 06/11/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write parse_line(raw_line) that cleans and parses one raw, messy line
#    into a dict. Handle inconsistent spacing and case - that is the whole
#    point of this week.
#
#    Typical and above: also write status_of(...), shaped for your lane
#    (e.g. OVER LIMIT / WARNING / OK, or FLAGGED / OK). Give both a
#    one-line docstring.

# your function(s) go here
def parse_line(raw_line):
    """Turn one messy raw status line into a clean dict."""
    line = raw_line.strip()
    hostname_part, rest = line.split(",", 1)
    hostname = hostname_part.strip().lower()

    fields = {}
    for piece in rest.split(","):
        key, value = piece.split("=")
        fields[key.strip().lower()] = float(value.strip())

    return {"hostname": hostname, "used": fields["used"], "total": fields["total"]}

def status_of(used, total):
    """Return FLAGGED or OK for a used/total pair."""
    percent = (used / total) * 100
    if percent >=90:
        return "FLAGGED"
    else:
        return "OK"


# ====================================================================== INPUT
# 2. Your raw, messy records - at least 5, deliberately varied in spacing
#    and case. Match the shape to your lane:
#
#    AI / Data Science : "  Survey_2026 , rating=4 , age=23  "
#    Cyber Security     : "SRC=10.0.0.5,ATTEMPTS=12,RESULT=FAILED"
#    IT                  : "  Srv-01 , used=87 , total=100  "
#
#    Excellent: save these lines to a file and load them with open() /
#    a for loop over the file, instead of writing them directly here.

with open("messy_lines.txt") as f:
    flagged_count=0
    total_records=0
    for raw_line in f: #looping through the lines in the  file
# =============================================================== PROCESS + OUTPUT
# 3. Parse and report on every record.
#
#    Threshold : parse each record, print the cleaned dict.
#    Typical   : also call status_of(...) for each, print it alongside.
#    Excellent : print a one-line summary at the end - how many records,
#                how many flagged.
        
        record =parse_line(raw_line)
        total_records+=1
        print(record)
        print(record["hostname"], status_of(record["used"],record["total"]))
        print()
        if status_of(record["used"],record["total"]) == "FLAGGED":
            flagged_count+=1

    print(f"There are {flagged_count} records that are flagged out of {total_records}")
# ValueError : could not convert string to float: "unknown"

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it against at least 5 genuinely messy raw records
#    [ ] Run it with a value that will not convert to a number - write the
#        error down
#    [ ] Check every function does one job, with a docstring
 