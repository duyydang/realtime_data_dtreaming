from pyspark import SparkContext

# Create a SparkContext
sc = SparkContext("local", "Simple App")

# Create an RDD from a list of numbers
data = [1, 2, 3, 4, 5]
rdd = sc.parallelize(data)

# Perform a transformation and an action
squared_rdd = rdd.map(lambda x: x * x)
result = squared_rdd.collect()

# Output the result
print("Squared Numbers:", result)

# Stop the SparkContext
sc.stop()
