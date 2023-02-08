#collect input; loan and interest and years 
# calculate the monthly payment
# show to user



def main():
    print("Monthly payment calculator")
    loan = float(input("Enter your loan: "))
    interest = float(input("Interest: "))
    years = int(input("Years to pay off: "))

    monhtly_interest = interest / 1200
    amount_monthly = years * 12
    payment = loan * monhtly_interest / (1 - (1 + monhtly_interest) ** (-amount_monthly))

    print("Monthly payment " + str(payment))

main()