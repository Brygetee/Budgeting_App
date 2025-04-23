def calculate_budget(weekly_income, weekly_expenses, expected_savings, weekly_savings):
    """ Calculate and return a summary message of the user's budgeting plan.
    Parameters:
    - weekly_income (float): User's weekly income.
    - weekly_expenses (float): User's weekly expenses.
    - expected_savings (float): User's annual savings goal.
    - weekly_savings (float): User's planned weekly savings.

    Returns:
    - A message summarizing the budgeting outcome. (string)
    """

    weeks_in_a_year = 52
    weekly_net_income = weekly_income - weekly_expenses
    annual_net_income = weekly_net_income * weeks_in_a_year
    annual_savings = weekly_savings * weeks_in_a_year
    weekly_savings_to_meet_goal = expected_savings / weeks_in_a_year

    # Evaluate if the annual net income meets or exceeds the expected savings goal
    if annual_net_income > expected_savings:
        message = (
            f"It looks like achieving your savings goal of ${expected_savings:,.2f} "
            f"will be possible this year! If you save ${weekly_savings:,.2f} per week, "
            f"you'll have ${annual_savings:,.2f}. If you save all your net income "
            f"(${weekly_net_income:,.2f}/week), you’d have ${annual_net_income:,.2f} by the end of the year."
        )
    elif annual_net_income == expected_savings:
        message = f"Congratulations, you'll be meeting your exact savings goal of ${expected_savings:,.2f}!"
    else:
        message = (
            f"Unfortunately, you don't meet your savings goal of ${expected_savings:,.2f}. "
            f"You’d need to save ${weekly_savings_to_meet_goal:,.2f} a week to reach your goal."
        )

    return message
