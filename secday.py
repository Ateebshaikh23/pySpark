from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('dataFrame Practic').getOrCreate()

spark.read.option("header","True").csv('dataset.csv').show()