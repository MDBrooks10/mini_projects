#calculate how much compound interest you might earn over a set amount of time

def calc():
    interest_rate = input("What is you interest rate? - %")
    investment = input("How much do you invest? - £")
    time_scale = input("When do you want to withdraw? - ")
    info_check = input(f"So you want to invest £{investment} over {time_scale} years with an interest rate of {interest_rate}%? Y/N - ")
    if info_check == "N":
        calc()
    elif info_check == "Y":
        interest = float(investment) / 100 * float(interest_rate)

    else:
        print("Please answer Y or N...")
        calc()

calc()