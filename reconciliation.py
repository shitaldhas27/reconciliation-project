# reconciliation.py

import pandas as pd

# Load CSV files
platform_df = pd.read_csv("platform_transactions.csv")
bank_df = pd.read_csv("bank_settlements.csv")

# -----------------------------
# Detect duplicate transactions
# -----------------------------
platform_df["duplicate_flag"] = platform_df.duplicated(
    subset=["transaction_id"],
    keep=False
)

# -----------------------------
# Merge datasets
# -----------------------------
merged_df = pd.merge(
    platform_df,
    bank_df,
    on="transaction_id",
    how="left",
    suffixes=("_platform", "_bank")
)

# -----------------------------
# Reconciliation logic
# -----------------------------
status_list = []

for index, row in merged_df.iterrows():

    # Missing settlement
    if pd.isna(row["settled_amount"]):
        status = "Missing Settlement"

    # Duplicate transaction
    elif row["duplicate_flag"] == True:
        status = "Duplicate"

    # Amount mismatch
    elif abs(row["amount"] - row["settled_amount"]) > 1:
        status = "Amount Mismatch"

    # Matched
    else:
        status = "Matched"

    status_list.append(status)

merged_df["status"] = status_list

# -----------------------------
# Save final output
# -----------------------------
merged_df.to_csv("final_output.csv", index=False)

# -----------------------------
# Print summary
# -----------------------------
print("\nReconciliation Summary:\n")
print(merged_df["status"].value_counts())

print("\nFinal report saved as final_output.csv")