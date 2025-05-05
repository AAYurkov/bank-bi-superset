import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
from pathlib import Path

N_ROWS = 10_000
START = datetime(2025, 1, 1)
END   = datetime(2025, 5, 5)

def rand_date(start, end):
    delta = end - start
    return start + timedelta(seconds=random.randint(0, int(delta.total_seconds())))

rng = np.random.default_rng(42)
categories = ['Payments', 'Transfers', 'Deposits', 'ATM', 'Fees', 'Refunds']
currencies  = ['RUB', 'USD', 'EUR']

df = pd.DataFrame({
    "txn_id":    np.arange(1, N_ROWS + 1, dtype=np.uint32),
    "client_id": rng.integers(100, 500, size=N_ROWS, dtype=np.uint32),
    "amount":    np.round(rng.uniform(10, 10_000, size=N_ROWS), 2),
    "currency":  rng.choice(currencies, size=N_ROWS),
    "txn_ts":    [rand_date(START, END).strftime("%Y-%m-%d %H:%M:%S") for _ in range(N_ROWS)],
    "category":  rng.choice(categories, size=N_ROWS),
})

Path("data").mkdir(exist_ok=True)
out = Path("data/bank_txn.csv")
df.to_csv(out, index=False)
print(f"✅  Saved {len(df):,} rows to {out}")