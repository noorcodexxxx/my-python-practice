subject="History"  #global variable
def calculate_marks():
    obtained_marks=94  #local variable
    print("Inside function-subject:",subject)
    print("Inside function -marks:",obtained_marks)
calculate_marks()
print("Outside function -subject:", subject)