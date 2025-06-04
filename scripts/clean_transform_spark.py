from pyspark.sql import SparkSession
from pyspark.sql.functions import size, col, regexp_replace
import os
import shutil

spark = SparkSession.builder.appName("JobCleaner").getOrCreate()

# Read JSON array with multiLine=True
df = spark.read.option("multiLine", True).json("data/raw_jobs.json")

df_clean = df.select(
    col("id"),
    regexp_replace(col("company"), ";", "_").alias("company_name"),
    regexp_replace(col("position"), ";", "_").alias("job_title"),
    col("tags").alias("tags_skills"),
    col("location").alias("country"),
    col("date").alias("date_posted"),
    col("apply_url")
)

df_clean = df_clean.withColumn("skill_count", size(col("tags_skills")))

output_folder = "data/cleaned_jobs_spark"
df_clean.coalesce(1).write.mode("overwrite").json(output_folder)
print("Raw jobs cleaned successfully and written to JSON")
# Rename the Spark output JSON file to cleaned_jobs.json
files = os.listdir(output_folder)
json_files = [f for f in files if f.endswith(".json")]

if len(json_files) == 1:
    src = os.path.join(output_folder, json_files[0])
    dst = os.path.join(output_folder, "cleaned_jobs.json")
    shutil.move(src, dst)
    print(f"Renamed {json_files[0]} to cleaned_jobs.json")
else:
    print(f"Expected one JSON file, found {len(json_files)}. Files: {json_files}")
