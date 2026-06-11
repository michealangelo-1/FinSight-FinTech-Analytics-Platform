import pandas as pd

from data_loader import get_stock_info
from dcf_model import calculate_dcf
from multiples_model import estimate_value_from_pe
from sensitivity_analysis import run_sensitivity_analysis
from peer_comparison import compare_peers
from visualization import create_heatmap


def main():

    # Load stock information
    stock = get_stock_info("AAPL")

    # DCF Valuation
    dcf_value = calculate_dcf(
        free_cash_flow=100000000000,
        growth_rate=0.08,
        discount_rate=0.10,
        terminal_growth_rate=0.03
    )

    # P/E Valuation
    pe_value = estimate_value_from_pe(
        earnings=100000000000,
        pe_ratio=25
    )

    # Display stock information
    print(stock)

    print(f"\nDCF Enterprise Value: ${dcf_value:,.2f}")

    print(f"\nP/E Valuation: ${pe_value:,.2f}")

    # Sensitivity Analysis
    sensitivity_df = run_sensitivity_analysis()

    print("\nSensitivity Analysis")
    print(sensitivity_df)

    sensitivity_df.to_csv(
        "outputs/sensitivity_analysis.csv",
        index=False
    )

    # Create Heatmap
    create_heatmap(
        "outputs/sensitivity_analysis.csv"
    )

    # Valuation Summary
    valuation_summary = pd.DataFrame([
        {
            "ticker": stock["ticker"],
            "company_name": stock["company_name"],
            "current_price": stock["current_price"],
            "market_cap": stock["market_cap"],
            "dcf_value": dcf_value,
            "pe_value": pe_value
        }
    ])

    valuation_summary.to_csv(
        "outputs/valuation_summary.csv",
        index=False
    )

    print("\nValuation Summary")
    print(valuation_summary)

    # Peer Comparison
    peer_df = compare_peers()

    peer_df.to_csv(
        "outputs/peer_comparison.csv",
        index=False
    )

    print("\nPeer Comparison")
    print(peer_df)


if __name__ == "__main__":
    main()