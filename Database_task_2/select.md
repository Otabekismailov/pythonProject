## task 1

```sql
SELECT *
FROM salesman
```

![Снимки экрана](./pictures/Снимок экрана от 2023-02-25 20-55-08.png)

# task 2

```sql
SELECT 'This is SQL Exercise, Practice and Solution'
```

![Снимки экрана](./pictures/Снимок экрана от 2023-02-25 20-44-09.png)

# TASK 3

```sql
SELECT 5, 10, 15
```

![Снимки экрана](./pictures/Снимок экрана от 2023-02-25 20-53-07.png)

# task 4

```sql
SELECT 15 + 10;
```

![Снимки экрана](./pictures/Снимок экрана от 2023-02-26 12-32-05.png)

# task 5

```sql
SELECT 10 + 15 / 3;
```

![Снимки экрана](./pictures/Снимок экрана от 2023-02-26 12-49-42.png)

# task 6

```sql
SELECT name, commission
from salesman;
```

![Снимки экрана](./pictures/Снимок экрана от 2023-02-26 12-54-15.png)

# TASK 7

```sql
SELECT ord_date, salesman_id, ord_no, purch_amt, customer_id
from orders

```

![Снимки экрана](./pictures/Снимок экрана от 2023-02-26 13-05-39.png)

# TASK 8

```sql
SELECT DISTINCT salesman_id
FROM orders
ORDER BY salesman_id;
```

![Снимки экрана](./pictures/Снимок экрана от 2023-02-26 13-27-16.png)

# TASK 9

```sql
SELECT name, city
FROM salesman
where city = 'Paris';
```

![Снимки экрана](./pictures/Снимок экрана от 2023-02-26 13-36-51.png)

# TASK 10

```sql
SELECT customer_id, cust_name, city, grade, salesman_id
FROM customer
where grade = 200;
```

![Снимки экрана](./pictures/Снимок экрана от 2023-02-26 13-42-09.png)

# TASK 11

```sql
SELECT ord_no, ord_date, purch_amt
from orders
where salesman_id = 5001;
```

![Снимки экрана](./pictures/Снимок экрана от 2023-02-26 13-46-02.png)

# TASK 12

```sql
SELECT year, subject, winner
from nobel_win
where year = 1970;
```

![Снимки экрана](./pictures/Снимок экрана от 2023-02-26 13-50-32.png)

# TASK 13

```sql
SELECT year, subject, winner
from nobel_win
where year = 1970 and subject = 'Literature';
```

![Снимки экрана](./pictures/Снимок экрана от 2023-02-26 13-53-30.png)

# TASK 14

```sql
SELECT year, subject
from nobel_win
where winner = 'Dennis Gabor';
```

![Снимки экрана](./pictures/Снимок экрана от 2023-02-26 13-56-23.png)

# TASK 15

```sql
SELECT winner
from nobel_win
where year >= 1950 and subject = 'Physics';
```

![Снимки экрана](./pictures/Снимок экрана от 2023-02-26 14-01-31.png)

# TASK 16

```sql
SELECT year, subject, winner, country
from nobel_win
where year between 1965 and 1975 and subject = 'Chemistry'
```

![Снимки экрана](./pictures/Снимок экрана от 2023-02-26 14-07-32.png)

# TASK 17

```sql
SELECT *
from nobel_win
where year > 1972 and winner = 'Menachem Begin' or winner = 'Yitzhak Rabin';
```

![Снимки экрана](./pictures/Снимок экрана от 2023-02-26 14-22-50.png)

# TASK 18

```sql
select year, subject, winner, country, category
from nobel_win
where winner like 'Louis%'
```

![Снимки экрана](./pictures/Снимок экрана от 2023-02-26 14-32-29.png)

# TASK 20

```sql
select year, subject, winner, country, category
from nobel_win
where subject <> 'Physiology' and subject <> 'Economics' 
```

![Снимки экрана](./pictures/Снимок экрана от 2023-02-26 14-41-15.png)

# TASK 21

```sql
select year, subject, winner, country, category
from nobel_win
where (year <= 1971 and subject= 'Physiology')
UNION
(
select *
from nobel_win
where year >= 1974 and subject = 'Peace')
```

![Снимки экрана](./pictures/Снимок экрана от 2023-02-26 14-50-26.png)

# TASK 22

```sql
select year, subject, winner, country, category
from nobel_win
where winner = 'Johannes Georg Bednorz'
```

![Снимки экрана](./pictures/Снимок экрана от 2023-02-26 14-55-11.png)

# TASK 23

```sql
select *
from nobel_win
where subject not ilike 'p%'
order by year desc, winner
```

![Снимки экрана](./pictures/Снимок экрана от 2023-02-26 15-00-13.png)

# TASK 24

```sql
SELECT *
FROM nobel_win
WHERE year =1970
ORDER BY
    CASE
    WHEN subject IN ('Economics', 'Chemistry') THEN 1
    ELSE 0
END
ASC,
 subject,
 winner;
```

![Снимки экрана](./pictures/Снимок экрана от 2023-02-26 15-32-44.png)

# TASK 25

```sql
SELECT *
FROM item_mast
where pro_price between 200 and 600
```

![Снимки экрана](./pictures/Снимок экрана от 2023-02-26 15-38-29.png)

# TASK 26

```sql
SELECT avg(pro_price)
FROM item_mast
where pro_com = 16;
```

![Снимки экрана](./pictures/Снимок экрана от 2023-02-26 15-47-51.png)

# TASK 27

```sql
 SELECT pro_name as "Item Name", pro_price AS "Price in Rs."
 FROM item_mast;
```

![Снимки экрана](./pictures/Снимок экрана от 2023-02-26 15-51-45.png)

# TASK 28

```sql
 SELECT pro_name, pro_price
 FROM item_mast
 where pro_price >= 250
 order by pro_price desc, pro_name;
```

![Снимки экрана](./pictures/Снимок экрана от 2023-02-26 15-59-11.png)

# TASK 29

```sql
SELECT avg(pro_price), pro_com
FROM item_mast
group by pro_com 
```

![Снимки экрана](./pictures/Снимок экрана от 2023-02-26 16-07-23.png)

# TASK 30

```sql
SELECT pro_name, pro_price
FROM item_mast
where pro_price = (select min(pro_price) from item_mast)
```

![Снимки экрана](./pictures/Снимок экрана от 2023-02-26 16-15-21.png)

# TASK 31

```sql
SELECT DISTINCT emp_lname
FROM emp_details;

```

![Снимки экрана](./pictures/Снимок экрана от 2023-02-26 16-20-18.png)

# TASK 32

```sql
SELECT *
FROM emp_details
where emp_lname = 'Snares';
```

![Снимки экрана](./pictures/Снимок экрана от 2023-02-26 16-24-30.png)

# TASK 33

```sql
SELECT *
FROM emp_details
where emp_dept = 57;
```

![Снимки экрана](./pictures/Снимок экрана от 2023-02-26 16-27-51.png)