#calculate how much compound interest you might earn over a set amount of time

def calc():
    year = 0
    interest_rate = input("What is you interest rate? - %")
    investment = input("How much do you invest? - £")
    time_scale = input("Over how many years? - ")
    info_check = input(f"So you want to invest £{investment} over {time_scale} years with an interest rate of {interest_rate}%? Y/N - ")
    print(info_check)
    if info_check.upper() == "N":
        calc()
    elif info_check.upper() == "Y":
        
        while year < int(time_scale):
            interest = float(investment) / 100 * float(interest_rate) + float(investment)
            investment = interest
            year += 1
            continue

        print(f"£{investment}")

    else:
        print("Please answer Y or N...")
        calc()

calc()