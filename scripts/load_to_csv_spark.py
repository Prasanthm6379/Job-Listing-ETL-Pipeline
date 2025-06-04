from pyspark.sql import SparkSession
from pyspark.sql.functions import concat_ws
import os
import shutil

spark = SparkSession.builder.appName("JOB-Loader").getOrCreate()

df = spark.read.json("data/cleaned_jobs_spark/cleaned_jobs.json")

df = df.withColumn("tags_skills", concat_ws(",", "tags_skills"))

# Write to CSV (single file)
output_folder = "data/jobs"
df.coalesce(1).write.csv(output_folder, header=True, mode="overwrite")

# Rename the generated CSV part file to jobs.csv
files = os.listdir(output_folder)
csv_files = [f for f in files if f.endswith(".csv")]

print("Cleaned jobs loaded successfully and written to CSV")

if len(csv_files) == 1:
    src = os.path.join(output_folder, csv_files[0])
    dst = os.path.join(output_folder, "jobs.csv")
    shutil.move(src, dst)
    print(f"Renamed {csv_files[0]} to jobs.csv")
else:
    print(f"Expected one CSV file, found {len(csv_files)}. Files: {csv_files}")
