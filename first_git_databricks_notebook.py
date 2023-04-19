# Databricks notebook source
print("hello world")

# COMMAND ----------

# MAGIC %fs ls dbfs:/public/retail_db/orders

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TEMPORARY VIEW vw_orders (
# MAGIC   order_id INT,
# MAGIC   order_date STRING,
# MAGIC   order_customer_id INT,
# MAGIC   order_status STRING
# MAGIC ) USING CSV
# MAGIC OPTIONS (
# MAGIC   path='dbfs:/public/retail_db/orders'
# MAGIC )

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC SELECT order_status, count(*) as no_of_orders FROM vw_orders GROUP BY 1 ORDER BY 2 DESC

# COMMAND ----------


