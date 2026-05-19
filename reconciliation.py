import pandas as pd

platform_df = pd.read_csv("platform_transactions.csv")
bank_df = pd.read_csv("bank_settlements.csv")

merged = pd.merge(platform_df, bank_df, on="transaction_id", how="left")

def check(row):

    if pd.isna(row["settled_amount"]):
        return "Missing Settlement"

    if abs(row["amount"] - row["settled_amount"]) > 1:
        return "Amount Mismatch"

    return "Matched"

merged["status"] = merged.apply(check, axis=1)

duplicates = bank_df[bank_df.duplicated("transaction_id", keep=False)]

print(duplicates)

merged.to_csv("final_output.csv", index=False)

print("DONE")