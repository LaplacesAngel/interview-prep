create table customer(
customer_id integer primary key,
firstname varchar,
lastname varchar,
ccnumber integer,
)

create table orders(
order_id integer primary key,
order_price integer,
number_bottles integer,
customer_id integer foreign key
)

create table orders_wines(
order_id integer,
wine_id integer)

create table wines(
wine_id integer primary KEY,
wine_name varchar
brand varchar,
type varchar,
)

-- given a customer id, list of wines purchased

select distinct wine_name 
from wines 
inner join orders_wines
where wines.wine_id = orders_wines.wines_id
inner join orders
where orders_wines.order_id = orders.orders_id
inner join Customer
where orders.CustomerID = Customer.CustomerID

wineries
  |
  |
packages
  |
  |
batches
  |
  |
customers
  |
  |
wines
