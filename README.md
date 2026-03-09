# retail-sales-analysis-project
Proyecto ETL de retail: Limpieza en Python, modelado en SQL y visualización en Power BI

# 📊 Retail Sales Analysis: De la Data Cruda al Dashboard Estratégico

## 👤 Perfil del Autor
**Tomás Nahuel Encina**  
**Contador Público (UBA) & Data Analyst**   
📍 Pilar, Buenos Aires

---

## 🚀 Presentación del Problema
En este proyecto, abordo el análisis de un dataset de retail cuyo volumen de registros supera las capacidades operativas de **Microsoft Excel**, generando lentitud y pérdida potencial de integridad en la información. 

Mi objetivo fue diseñar un flujo de trabajo profesional utilizando herramientas de programación y bases de datos para garantizar un análisis escalable y preciso.

## 🛠️ Stack Tecnológico
Para la resolución, utilicé un ecosistema de herramientas integradas:
* **Python (Pandas):** Limpieza, normalización y transformación de datos.
* **MySQL (PopSQL):** Almacenamiento estructurado bajo un modelo de estrellas.
* **Power BI:** Visualización avanzada y creación de métricas de rentabilidad.

---

## 🏗️ Arquitectura de Datos (Star Schema)
Para optimizar el rendimiento de las consultas y la visualización, estructuré la información en un **Modelo de Estrellas**:
1. **Tabla de Hechos (`fact_sales`):** Contiene las métricas transaccionales y claves foráneas.
2. **Tablas de Dimensión (`dim_customer`, `dim_product`):** Almacenan los atributos descriptivos de clientes y productos para evitar la redundancia.

---

## 🔄 Proceso de Desarrollo

### 1. Preparación con Python
Utilicé **VS Code** para ejecutar scripts de limpieza que incluyeron:
* Imputación de valores nulos en `Customer ID` y `Description`.
* **Lógica Contable:** Creación de una columna de categoría para diferenciar entre "Venta", "Cancelación" y "Ajuste Contable".
* Cálculo de ingresos por línea: $$LineTotal = Price \times Quantity$$.

### 2. Manipulación en SQL
Mediante **PopSQL**, realicé la carga masiva de datos y el análisis exploratorio
* Creación de tablas con restricciones de integridad referencial.
* Consultas para identificar el Top 5 de clientes con mayor volumen de compra.
* Filtrado de ventas netas excluyendo transacciones sin identificación de cliente.

### 3. Visualización en Power BI
El tablero final permite monitorear la salud financiera del negocio a través de:
* **Métricas DAX:** Ventas Netas, Margen Bruto (%), Ticket Promedio y Costo Operativo (Picking).
* **Análisis de Rentabilidad:** Identificación de productos líderes como 'Regency Cakes'.



## 📫 Contacto
* **LinkedIn:** (www.linkedin.com/in/tomas-encina-217395202) 
* **Email:** tomyencina23@gmail.com
