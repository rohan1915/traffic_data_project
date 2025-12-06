# Databricks notebook source
# MAGIC %md
# MAGIC ####Saving the external locations in variables

# COMMAND ----------


bronze_path = spark.sql('describe external location `bronze`').select('url').collect()[0][0]
silver_path = spark.sql('describe external location `silver`').select('url').collect()[0][0]
gold_path = spark.sql('describe external location `gold`').select('url').collect()[0][0]


# COMMAND ----------

# MAGIC %md
# MAGIC ####Passing the environments dynamically

# COMMAND ----------

dbutils.widgets.text(name='env',defaultValue='',label='Enter the Environment')
env = dbutils.widgets.get('env')

# COMMAND ----------

# MAGIC %md
# MAGIC ####Defining functions to use catalog and create schemas dynamically

# COMMAND ----------

def create_bronze_schema(environment,path,schema_name):
    print(f'Using {environment}catalog')
    spark.sql(f"USE CATALOG '{environment}catalog'")
    print(f"Creating {schema_name} schema in {path}")
    spark.sql(f"CREATE SCHEMA IF NOT EXISTS `{schema_name}` MANAGED LOCATION '{path}/{schema_name}'")


# COMMAND ----------

def create_silver_schema(environment,path,schema_name):
    print(f'Using {environment}catalog')
    spark.sql(f"USE CATALOG '{env}catalog'")
    print(f"Creating {schema_name} schema in {path}")
    spark.sql(f"CREATE SCHEMA IF NOT EXISTS `{schema_name}` MANAGED LOCATION '{path}/{schema_name}'")

# COMMAND ----------

def create_gold_schema(environment,path,schema_name):
    print(f'Using {environment}catalog')
    spark.sql(f"USE CATALOG '{env}catalog'")
    print(f"Creating {schema_name} schema in {path}")
    spark.sql(f"CREATE SCHEMA IF NOT EXISTS `{schema_name}` MANAGED LOCATION '{path}/{schema_name}'")

# COMMAND ----------

create_bronze_schema(env,bronze_path,'bronze')
create_silver_schema(env,silver_path,'silver')
create_gold_schema(env,gold_path,'gold')
