import pandas as pd
import random
from faker import Faker

fake = Faker()

platform_data = []
bank_data = []

for i in range(120):

    txn_id = f"TXN{i+1}"
    amount = round(random.uniform(100, 5000), 2)

    txn_date = fake.date_time_this_year()

    platform_data.append({
        "transaction_id": txn_id,
        "amount": amount,
        "txn_date": txn_date
    })

    settle_delay = random.randint(1, 3)
    settle_date = txn_date + pd.Timedelta(days=settle_delay)

    settled_amount = amount

    if i % 10 == 0:
        settled_amount = amount + 1

    bank_data.append({
        "transaction_id": txn_id,
        "settled_amount": settled_amount,
        "settlement_date": settle_date
    })

# duplicate
bank_data.append(bank_data[5])

platform_df = pd.DataFrame(platform_data)
bank_df = pd.DataFrame(bank_data)

platform_df.to_csv("platform_transactions.csv", index=False)
bank_df.to_csv("bank_settlements.csv", index=False)

print("DATA CREATED")