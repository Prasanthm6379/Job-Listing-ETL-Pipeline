import subprocess

def run_script(script_path):
    print(f"\nRunning {script_path}...\n")
    result = subprocess.run(["python3", script_path], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(f"Error while running {script_path}:\n{result.stderr}")
        exit(1)

if __name__ == "__main__":
    scripts = [
        "scripts/fetch_jobs.py",
        "scripts/clean_transform_spark.py",
        "scripts/load_to_csv_spark.py"
    ]

    for script in scripts:
        run_script(script)

    print("\nAll ETL steps completed successfully!")
