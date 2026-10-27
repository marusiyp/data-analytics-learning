# Data Analytics Learning

Practice projects from my path into data analytics: SQL, Python (pandas, NumPy) and Power BI.

## Projects

| Notebook | What it covers | Tools |
|---|---|---|
| [Sakila DVD rental: exploratory analysis](notebooks/01_pandas_sakila.ipynb) | 21 business questions on revenue, customers, the film catalogue and rentals, with observations and a summary. Results are cross-checked against SQL. | Python, pandas, SQLAlchemy, MySQL |

## Key findings (Sakila)

- Total revenue was 67,406.56 from 16,044 payments; July 2005 alone brought about 42% of it.
- A typical payment is 3.99 (median), below the mean of 4.20, so payment amounts are right-skewed.
- All 182 rentals from February 2006 are unreturned, which shows the dataset ends partway through that month.

## How to run

1. Install MySQL 8 with the [sakila sample database](https://dev.mysql.com/doc/sakila/en/).
2. Create the environment:
   ```bash
   conda create -n da python=3.12 pandas numpy matplotlib jupyter sqlalchemy pymysql
   conda activate da
   ```
3. Open the notebook and run all cells. The MySQL password is requested at runtime and never stored.

## Skills

SQL (joins, CTEs, window functions) · pandas · data cleaning · exploratory analysis · Git
