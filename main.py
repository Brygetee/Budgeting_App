#Build a simple personal budgeting CLI app where users input income and expenses, and it calculates savings.
#Goal: Store and manipulate data using types like strings, integers, floats, and use arithmetic or logical operators.

def get_float_input(prompt):
    """Ask for a numerical input value and validate it."""
    while True:
        try:
            value = float(input(prompt))
            if value <0:
                print("Please enter a positive number.")
                # Continue back to the start of the while loop to ask again
                continue
            return value
        # if user enters a letter or invalid character
        except ValueError:
            print("Please enter a valid number.")

def budgeting_app(weekly_income, weekly_expenses, expected_savings, weekly_savings):
    weeks_in_a_year = 52

    weekly_net_income = weekly_income - weekly_expenses
    annual_net_income = weekly_net_income * weeks_in_a_year
    annual_savings = weekly_savings * weeks_in_a_year
    additional_potential_savings = annual_net_income - annual_savings
    weekly_savings_to_meet_goal = expected_savings / weeks_in_a_year

    print("\n📈 Budget Summary 📈")

    if annual_net_income > expected_savings:
        print(f"It looks like achieving your savings goal of ${expected_savings:,.2f} will be possible this year! If you only choose to put away ${weekly_savings:,.2f} per week, at the end of the year you would have ${annual_savings:,.2f} in savings. If you choose to save all of your weekly income after expenses, (${weekly_net_income:,.2f}) for the entire year you would have saved a grand total of ${annual_net_income:,.2f}.")
    elif annual_net_income == expected_savings:
        print(f"Congratulations, looks like you'll be meeting your exact savings goal of ${expected_savings:,.2f}.")
    else:
        print(f"Unfortunately with your income, you do not meet your expected savings goals of ${expected_savings:,.2f} and would need to put away ${weekly_savings_to_meet_goal:,.2f} a week to reach your goal.")
if __name__ == "__main__":
    weekly_income = get_float_input("Please enter your weekly income:\n$")
    weekly_expenses = get_float_input("Please enter your weekly expenses\n$")
    expected_savings = get_float_input("How much money would you like to have saved up by the end of the year?\n$")
    weekly_savings = get_float_input("How much money are you able to set aside per week to reach this goal?\n$")

    budgeting_app(weekly_income, weekly_expenses, expected_savings, weekly_savings)
