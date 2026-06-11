def calculate_dcf(
    free_cash_flow,
    growth_rate,
    discount_rate,
    terminal_growth_rate,
    years=5
):
    projected_fcfs = []

    current_fcf = free_cash_flow

    for _ in range(years):
        current_fcf *= (1 + growth_rate)
        projected_fcfs.append(current_fcf)

    present_value = 0

    for i, fcf in enumerate(projected_fcfs, start=1):
        present_value += fcf / ((1 + discount_rate) ** i)

    terminal_value = (
        projected_fcfs[-1]
        * (1 + terminal_growth_rate)
        / (discount_rate - terminal_growth_rate)
    )

    discounted_terminal_value = (
        terminal_value
        / ((1 + discount_rate) ** years)
    )

    enterprise_value = (
        present_value +
        discounted_terminal_value
    )

    return enterprise_value