"""
df.write \
  .format("org.neo4j.spark.DataSource") \
  .mode("ErrorIfExists") \
  .option("url", "bolt://localhost:7687") \
  .option("labels", ":Person") \
  .save()
的等价写法如下：
result = (df.write
  .format("org.neo4j.spark.DataSource")
  .mode("ErrorIfExists")
  .option("url", "bolt://localhost:7687")
  .option("labels", ":Person")
  .save())

"""