# Data Analytics Learning

Practice projects from my path into data analytics: SQL, Python (pandas, NumPy) and Power BI.
All analyses use the MySQL sample database *sakila*, a fictional DVD rental store.

## Projects

| # | Notebook | What it covers | Key skills |
|---|---|---|---|
| 1 | [Exploratory analysis](notebooks/01_pandas_sakila.ipynb) | 21 business questions on revenue, customers, the film catalogue and rentals | filtering, grouping, dates, binning, pivot tables |
| 2 | [Combining tables](notebooks/02_pandas_merge_sakila.ipynb) | 6 questions that need data from up to 5 related tables | merges, merge validation, cross-tabs, anti-joins |

Every notebook ends with a summary of findings, and results are cross-checked against SQL queries.

## Key findings

- **Revenue:** 67,406.56 from 16,044 payments; July 2005 alone brought about 42% of it.
- **Payments:** a typical payment is 3.99 (median), below the mean of 4.20, so amounts are right-skewed.
- **Stores:** both stores' stock earns the same, and customers rent about half their DVDs from the store they are not registered at.
- **Catalogue:** all 42 never-rented films are titles the store has no copy of, so unrented titles are a stock issue, not a demand issue.
- **Data quality:** all 182 rentals from February 2006 are unreturned, which shows the dataset ends partway through that month.

## How to run

1. Install MySQL 8 with the [sakila sample database](https://dev.mysql.com/doc/sakila/en/).
2. Create the environment:
   ```bash
   conda create -n da python=3.12 pandas numpy matplotlib jupyter sqlalchemy pymysql
   conda activate da
   ```
3. Open a notebook and run all cells. The MySQL password is requested at runtime and never stored.

## Skills

SQL (joins, CTEs, window functions) · pandas · data cleaning · exploratory analysis · Git
