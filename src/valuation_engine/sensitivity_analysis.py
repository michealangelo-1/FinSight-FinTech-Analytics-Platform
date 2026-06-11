import pandas as pd

from dcf_model import calculate_dcf


def run_sensitivity_analysis():

    results = []

    growth_rates = [0.06, 0.08, 0.10]
    discount_rates = [0.08, 0.10, 0.12]

    for growth in growth_rates:
        for discount in discount_rates:

            value = calculate_dcf(
                free_cash_flow=100000000000,
                growth_rate=growth,
                discount_rate=discount,
                terminal_growth_rate=0.03
            )

            results.append({
                "growth_rate": growth,
                "discount_rate": discount,
                "enterprise_value": value
            })

    return pd.DataFrame(results)