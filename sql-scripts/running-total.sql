SELECT employeeID, SUM(amount)
FROM sales
GROUP BY employeeID;
