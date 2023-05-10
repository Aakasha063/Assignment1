-- Count the number of Salesperson whose name begin with ‘a’/’A’.
SELECT Count(*) AS num_salesperson FROM salespeople
WHERE sname LIKE "%A" OR sname LIKE "%a"; 


-- Display all the Salesperson whose all orders worth is more than Rs. 2000
SELECT Sname FROM salespeople S
JOIN orders O
ON S.snum = O.snum
GROUP BY S.Snum, S.Sname
HAVING max(O.amt) > 2000;

-- Count the number of Salesperson belonging to Newyork.
SELECT COUNT(*) AS num_of_salesperson FROM salespeople
WHERE city = 'NewYork';


-- Display the number of Salespeople belonging to London and belonging to Paris.
SELECT COUNT(*) AS num_of_salesperson from salespeople
WHERE City IN ('London', 'Paris')
GROUP BY City;


-- Display the number of orders taken by each Salesperson and their date of orders.
SELECT Sname, COUNT(*) AS num_of_orders, Odate FROM Salespeople S
LEFT JOIN orders O ON S.Snum = O.Snum
GROUP BY S.Sname, O.odate
ORDER BY O.Odate, S.Sname;