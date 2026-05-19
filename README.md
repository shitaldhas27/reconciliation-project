## Assumptions

1. One transaction has one settlement
2. Difference <= 1 rupee is acceptable
3. Duplicate transactions are invalid
4. Missing settlement = failure
5. Refunds may not have original transaction

## Test Cases

1. Exact Match → Matched
2. Missing → Missing Settlement
3. Difference > 1 → Amount Mismatch
4. Duplicate → flagged


## Brainstorming Thread

- Generate reconciliation system design
- Add duplicate detection logic
- Improve dataset generation
- Explain mismatch types
- Create Streamlit dashboard design


Build a Python-based reconciliation system using pandas.

Requirements:
- Generate synthetic platform and bank datasets
- Include anomalies: duplicates, rounding issues, missing settlements, unmatched transactions
- Compare datasets using transaction_id
- Classify: Matched, Missing, Mismatch
- Export final CSV
- Build Streamlit dashboard with summary + download

Include test cases and assumptions.