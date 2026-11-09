# Data Analytics Learning

Data analysis projects using SQL and Python (pandas, NumPy, Matplotlib, seaborn). Each notebook answers business questions and ends with a summary of findings.

## Projects

| # | Notebook | Data | What it covers | Key skills |
|---|---|---|---|---|
| 1 | [Exploratory analysis](notebooks/01_pandas_sakila.ipynb) | sakila (MySQL) | 21 business questions on revenue, customers, the film catalogue and rentals | filtering, grouping, dates, binning, pivot tables |
| 2 | [Combining tables](notebooks/02_pandas_merge_sakila.ipynb) | sakila (MySQL) | 6 questions that need data from up to 5 related tables | merges, merge validation, cross-tabs, anti-joins |
| 3 | [Loan applications: cleaning and EDA](notebooks/03_loan_cleaning_eda.ipynb) | [Kaggle loan data](https://www.kaggle.com/datasets/burak3ergun/loan-data-set) | cleaning 614 loan applications, building affordability features and finding what drives approval | missing-value strategy, outliers (IQR), feature engineering, functions |
| 4 | [Loan applications: visualisation](notebooks/04_loan_visualisation.ipynb) | output of notebook 3 | 6 charts on income, credit history and affordability, ending with one headline chart | Matplotlib, seaborn, log scales, annotated heatmaps, chart storytelling |

Every notebook ends with a summary of findings. The sakila results are cross-checked against SQL queries.

## Key findings

**Sakila DVD rental (notebooks 1–2)**
- **Revenue:** 67,406.56 from 16,044 payments; July 2005 alone brought about 42% of it.
- **Stores:** both stores' stock earns the same, and customers rent about half their DVDs from the store they are not registered at.
- **Catalogue:** all 42 never-rented films are titles the store has no copy of, so unrented titles are a stock issue, not a demand issue.
- **Data quality:** all 182 rentals from February 2006 are unreturned, which shows the dataset ends partway through that month.

**Loan applications (notebooks 3–4)**
- **Credit history** drives approval: 79.6% approved with a good history vs 7.9% with a bad one. A missing history (74.0%) behaves like a good one, so it was kept as its own category instead of being guessed.
- **Affordability** matters only at the extreme: approval stays at about 70% while repayments take up to 25% of income, but drops to 38.5% above 40%. Even with a good credit history, it falls from about 80% to 30%.
- **Income** on its own barely matters: the median income of approved and rejected applicants differs by less than 3%.
- `Loan_Status` records **approval, not repayment**, and the 9% interest rate used for repayments is an assumption.

## How to run

1. Create the environment:
   ```bash
   conda create -n da python=3.12 pandas numpy matplotlib seaborn jupyter sqlalchemy pymysql pyarrow
   conda activate da
   ```
2. **Notebooks 1–2:** install MySQL 8 with the [sakila sample database](https://dev.mysql.com/doc/sakila/en/). The MySQL password is requested at runtime and never stored.
3. **Notebook 3:** download the [loan dataset](https://www.kaggle.com/datasets/burak3ergun/loan-data-set) and save it as `data/loan_data_set.csv`. Data files are not stored in this repository.
4. **Notebook 4:** run notebook 3 first; it saves the cleaned data as `data/loans_clean.parquet`.
5. Open a notebook and run all cells.

## Skills

SQL (joins, CTEs, window functions) · pandas · data cleaning · feature engineering · exploratory analysis · data visualisation (Matplotlib, seaborn) · Git
