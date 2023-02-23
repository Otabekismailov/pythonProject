<pre>
task-1,Categories jadval barcha ustun ma’lumotlarini bilan qaytaring.

javob:
'''sql
SELECT * FROM categories
'''
</pre>
![img.png](img.png)
<pre>
task-2,Categories jadval category_name va description ustun ma’lumotlarini qaytaring.
javob:
'''sql
SELECT category_name, description from categories
'''
</pre>
![img_1.png](img_1.png)
<pre>
task-3,Categories jadval barcha ustun ma’lumotlari olishda ustun nomlarini o’zbekcha tarjimada
qaytaring. M-n: category_name=Nomi
javob:
'''sql
SELECT category_id AS kategoriya_id, category_name AS kategoriya_nomi, description AS Tavsifi, picture AS Rasm
FROM categories
'''
</pre>
![img_2.png](img_2.png)
<pre>
task-4 Categories jadvaldan kategoriya nomi ’Confections’ ga teng bo’lgan ma’lumotlarni
qaytaring.
javob:
'''sql
SELECT * FROM categories WHERE category_name= 'Confections'
'''
</pre>
![img_3.png](img_3.png)
<pre>
task-5 Categories jadvaldan kategoriya nomi ‘Produce’ yoki ‘Seafood’ bo’lgan ma’lumotlarni
qaytaring.
javob:
'''sql
SELECT * FROM categories WHERE category_name = 'Produce' OR category_name = 'Seafood'
'''
</pre>
![img_4.png](img_4.png)
<pre>
TASK-6
</pre>
![img_5.png](img_5.png)
<pre>
javob:
'''sql
SELECT * FROM categories WHERE category_id BETWEEN 6 AND 8
'''
</pre>
![img_6.png](img_6.png)
<pre>
TASK-7,Categories jadvaldan ma’lumotlarni description alifbo bo’yicha Z-A tartibida chiqaring.
javob:
'''sql
SELECT *
from categories
order by description desc
'''
</pre>
![img_7.png](img_7.png)
<pre>
TASK-8, Customers jadvalidan barcha ma’lumotlarni oling
javob:
'''sql
SELECT * from customers
'''
</pre>
![img_8.png](img_8.png)
<pre>
TASK-9,Customers jadvalida ustun nomlarini o’zbekcha holatda oling
javob:
'''sql
SELECT customer_id AS mijoz_id,
company_name AS kompanina_nomi,
contact_name AS mijoz_nomi,
contact_title as mijoz_unvon,
address as manzil,
city as shahar,
region as viloyat,
postal_code as poshta_kodi,
country as mamlakat_nomi,
phone as telefon_raqami,
fax as faks
from customers
'''
</pre>
![img_9.png](img_9.png)
<pre>
#TASK-10, Customers jadvalidan contact_title ‘Owner’ bo’lgan ma’lumotlarni qaytaring.
javob:
'''sql
SELECT *
FROM customers
WHERE contact_title = 'Owner'
'''
</pre>
![img_10.png](img_10.png)
<pre>
#TASK-11,Customers jadvalidan city ‘London’ bo’lgan ma’lumotlarni qaytaring.
javob:
'''sql

SELECT *
FROM customers
WHERE city = 'London'
'''
</pre>
![img_11.png](img_11.png)
<pre>
#TASK-12,Customers jadvalidan region ustun NULL bo’lgan ma’lumotlarni qaytaring
javob:
'''sql
SELECT *
FROM customers
WHERE region is null
'''
</pre>
![img_12.png](img_12.png)
<pre>
#TASK-13,Customers jadvalidan region ustun NULL bo’lmagan ma’lumotlarni qaytaring.
javob:
'''sql
SELECT *
FROM customers
WHERE region is not null
'''
</pre>
![img_13.png](img_13.png)
<pre>
#TASK-14,Customers jadvalidan country ustun Germany bo’lgan ma’lumotlarni qaytaring.
javob:
'''sql
SELECT *
FROM customers
WHERE country ='Germany'
'''
</pre>
![img_14.png](img_14.png)
<pre>
#TASK-15,Customers jadvalidan country ustun Germany bo’lgan qatorlar sonini qaytaring.
javob:
'''sql
SELECT count(*)
FROM customers
WHERE country = 'Germany'
'''
</pre>
![img_15.png](img_15.png)
<pre>
#Task-16, Customers jadvalidan fax ustun NULL bo’lmalgan ma’lumotlarni contact_name ustun
alifbo tartiba tartiblab qaytaring.
javob:
'''sql
SELECT *
FROM customers
WHERE (fax is not null)
order by contact_name
'''
</pre>
![img_16.png](img_16.png)
<pre>
#Task-17,Employees jadvaldan barcha ma’lumotlarni qaytaring.
javob:
'''sql
SELECT * FROM employees
'''
</pre>
![img_17.png](img_17.png)
<pre>
#Task-18,Employees jadval ustun nomlarini o’zbekcha qaytaring.
javob:
'''sql
SELECT employee_id as xodim_id,
last_name as familya,
first_name as ism,
title as unvon,
title_of_courtesy as unvon_boyicha_hurmati,
birth_date as tugilgan_malumotlar,
hire_date as ish_boshlagan_kun,
address as manzil,
city as shahar,
region as viloyat,
postal_code as pochta_kodi,
country as mamlakati,
home_phone as uy_telefon_raqami,
extension as kengaytma,
photo as rasm,
notes as malumot
FROM employees
'''
</pre>
![img_18.png](img_18.png)
<pre>
#TAsk-19,Employess jadvaldan title_of_courtest ‘Mr’ bo’lgan xodimlarni firts_name alifbo tartibida
qaytaring.
javob:
'''sql
SELECT *
FROM employees
WHERE title_of_courtesy = 'Mr.'
order by first_name
'''
</pre>
![img_19.png](img_19.png)
<pre>
#Task-20,Employes jadvalda title ‘Sales Representative’ bo’lgan xodimlar sonini qaytaring
javob:
'''sql
SELECT * FROM employees where title='Sales Representative'
'''
</pre>
![img_20.png](img_20.png)
<pre>
#Task-21,Employees jadvalda hire_date 1994-yilda bo’lgan ma’lumotlarni qaytaring.
javob:
'''sql
SELECT *
FROM employees
where hire_date between '1994-01-01' and '1994-12-31'
'''
</pre>
![img_21.png](img_21.png)
<pre>
#Task-22,Employees jadvaldan region NULL bo’lmagan xodimlarni first_name, last_name, title, city,
home_phone ma’lumotlarini first_name Z-A alifbo tartibida qaytaring.
javob:
'''sql
SELECT first_name, last_name, title, city, home_phone
FROM employees
WHERE region IS not NULL
order by first_name
'''
</pre>
![img_22.png](img_22.png)
<pre>
#Task-23,Orders jadvaldan customer_id ‘VINET’ bo’lgan buyurtmalarni qaytaring
javob:
'''sql
SELECT *
FROM orders
WHERE customer_id = 'VINET'
'''
</pre>
![img_23.png](img_23.png)
<pre>
#Task-24,Orders jadvaldan order_date ustuni orqali 1996-yildagi ma’lumotlarni qaytaring
javob:
'''sql
SELECT *
FROM orders
WHERE order_date between '1996-01-01'and '1996-12-31'
'''
</pre>
![img_24.png](img_24.png)
<pre>
#Task-25,Orders jadvaldan ship_region ustun NULL bo’lmagan ma’lumotlarni qaytaring.
javob:
'''sql
SELECT *
FROM orders
WHERE ship_region is not null
'''
</pre>
![img_25.png](img_25.png)
<pre>
#Task-26,Orders jadvaldan order_id 10300 va 10400 orasida bo’lgan ma’lumotlarni qaytaring
javob:
'''sql
SELECT *
FROM orders
WHERE order_id between '10300' and '10400'
'''
</pre>
![img_26.png](img_26.png)
![img_27.png](img_27.png)
<pre>
#Task-27, Order Details jadvaldan unit_price ustun umumiy qiymatini qaytaring.
javob:
'''sql
SELECT count(unit_price)
FROM order_details
'''
</pre>
![img_28.png](img_28.png)


