SELECT 
    Categoria, 
    COUNT(Invoice) AS Total_Operaciones, 
    SUM(Quantity) AS Total_Unidades_Movidas,
    ROUND(SUM(LineTotal), 2) AS Monto_Total
FROM fact_sales
GROUP BY Categoria
ORDER BY Monto_Total DESC;


SELECT 
    c.CustomerID, 
    c.Country, 
    COUNT(DISTINCT f.Invoice) AS Cantidad_Pedidos,
    ROUND(SUM(f.LineTotal), 2) AS Total_Comprado
FROM fact_sales f
JOIN dim_customer c ON f.CustomerID = c.CustomerID
WHERE f.Categoria = 'Venta' 
  AND f.CustomerID != 0 
GROUP BY c.CustomerID, c.Country
ORDER BY Total_Comprado DESC
LIMIT 10;
