# Name: ERICKA JOY C. PALMA
# Section: IV-BSIT-B
# Activity: P2: Custom Module: student_utils 
# Date: November 25, 2026

# calculate average
def get_average(grades):
    return sum(grades) / len(grades)

# finds highest
def get_highest(grades):
    return max(grades)

# find lowest
def get_lowest(grades):
    return min(grades)

# determines pass or fail
def get_status(average):
    if average >= 75:
        return "PASSED"
    else:
        return "FAILED"
