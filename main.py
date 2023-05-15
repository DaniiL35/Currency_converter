conversion_rates = {
    'USD' : 1.0,
    'EUR' : 0.91,
    'GBP' : 0.76,
    'INR' : 72.97,
    'NIS' : 3.66
}
def converter():
    # Prompt the user for input
    amount = float(input("enter the amount: "))
    from_currency = input('enter the source currency:').upper()
    to_currency = input('enter the Target currency:').upper()

    #convert the amount from one currency to another
    initial_amount = amount * conversion_rates[to_currency]
    converted_amount = initial_amount / conversion_rates[from_currency]
    converted_amount = round(converted_amount, 2)

    #print the result
    print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")

    # Ask the user if they want to convert again
    again = input('Do you want to convert again? (y/n): ').lower()
    if again != 'y':
        exit()
    else:
        converter()

converter()