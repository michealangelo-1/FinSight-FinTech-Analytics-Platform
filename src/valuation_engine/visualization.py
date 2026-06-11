import pandas as pd
import matplotlib.pyplot as plt


def create_heatmap(csv_path):

    df = pd.read_csv(csv_path)

    pivot = df.pivot(
        index="growth_rate",
        columns="discount_rate",
        values="enterprise_value"
    )

    plt.figure(figsize=(8, 6))

    image = plt.imshow(pivot)

    plt.colorbar(image, label="Enterprise Value ($)")

    plt.xticks(
        range(len(pivot.columns)),
        [f"{x:.0%}" for x in pivot.columns]
    )

    plt.yticks(
        range(len(pivot.index)),
        [f"{x:.0%}" for x in pivot.index]
    )

    plt.xlabel("Discount Rate")
    plt.ylabel("Growth Rate")
    plt.title("DCF Sensitivity Analysis")

    plt.tight_layout()

    plt.savefig(
        "outputs/valuation_sensitivity_heatmap.png"
    )

    plt.close()