import pandas as pd

def approval_by(df, column):
    """Number of applications and approval rate for each value of a column."""
    return (
        df.groupby(column, dropna=False, observed=False)
          .agg(applications=("Loan_ID", "count"),
               approval_rate=("approved", "mean"))
    )
