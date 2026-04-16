# function to determine pay rate
def get_rate(job_code):
    if job_code == "L":
        return 25
    elif job_code == "A":
        return 30
    elif job_code == "J":
        return 50
    else:
        return 0


total_gross = 0

choice = "yes"

while choice.lower() == "yes":

    # input phase
    last_name = input("Enter employee last name: ")
    job_code = input("Enter job code (L, A, J): ").upper()
    hours = float(input("Enter hours worked: "))

    # process phase
    rate = get_rate(job_code)

    if hours > 40:
        regular_pay = 40 * rate
        overtime_pay = (hours - 40) * rate * 1.5
        gross_pay = regular_pay + overtime_pay
    else:
        gross_pay = hours * rate

    total_gross += gross_pay

    # output phase
    print("Employee:", last_name)
    print("Gross Pay: $", round(gross_pay,2))

    choice = input("Do you want to enter another employee? (Yes/No): ")

print("Total Gross Pay for all employees: $", round(total_gross,2))