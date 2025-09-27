import pyspark
import pandas as pd

df = pd.read_csv("dataSet.csv")
print(df.head())
# df.show()
 
print(type(df))




# from pyspark.sql import SparkSession

from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.appName("example").getOrCreate()

# Read CSV with Spark
df = spark.read.csv("dataSet.csv", header=True, inferSchema=True)

df.show()

print("this is schema")
df.printSchema()
