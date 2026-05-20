# data_generator.py

import pandas as pd
import random
from faker import Faker
from datetime import timedelta

fake = Faker()

platform_data = []
bank_data = []

# -----------------------------
# Generate normal transactions
# -----------------------------
for i in range(1, 101):

    txn_id = f"TXN{i}"

    amount = round(random.uniform(100, 5000), 2)

    txn_date = fake.date_time_this_year()

    settlement_date = txn_date + timedelta(days=random.randint(1, 2))

    platform_data.append({
        "transaction_id": txn_id,
        "amount": amount,
        "txn_date": txn_date
    })

    bank_data.append({
        "transaction_id": txn_id,
        "settled_amount": amount,
        "settlement_date": settlement_date
    })

# -----------------------------
# Add duplicate transaction
# -----------------------------
platform_data.append(platform_data[5])

# -----------------------------
# Add amount mismatch
# -----------------------------
bank_data.append({
    "transaction_id": "TXN200",
    "settled_amount": 9999,
    "settlement_date": fake.date_time_this_year()
})

platform_data.append({
    "transaction_id": "TXN200",
    "amount": 5000,
    "txn_date": fake.date_time_this_year()
})

# -----------------------------
# Add missing settlement
# -----------------------------
platform_data.append({
    "transaction_id": "TXN300",
    "amount": 2500,
    "txn_date": fake.date_time_this_year()
})

# -----------------------------
# Add unmatched refund
# -----------------------------
bank_data.append({
    "transaction_id": "REFUND999",
    "settled_amount": -500,
    "settlement_date": fake.date_time_this_year()
})

# -----------------------------
# Save CSV files
# -----------------------------
platform_df = pd.DataFrame(platform_data)
bank_df = pd.DataFrame(bank_data)

platform_df.to_csv("platform_transactions.csv", index=False)
bank_df.to_csv("bank_settlements.csv", index=False)

print("CSV files generated successfully!")