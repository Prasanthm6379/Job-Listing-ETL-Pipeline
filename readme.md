# Job Listing ETL Pipeline

A comprehensive ETL (Extract, Transform, Load) pipeline that aggregates remote job listings from RemoteOK API, processes them using Apache Spark, and generates analytics-ready datasets for data visualization and analysis.

## 🚀 Overview

This pipeline automatically fetches job listings from RemoteOK, cleans and transforms the data using PySpark, and outputs structured CSV files ready for analysis. The processed data includes job details, skills requirements, location information, and metadata for comprehensive job market analysis.

## 📊 Features

- **Automated Data Extraction**: Fetches real-time job listings from RemoteOK API
- **Robust Data Processing**: Uses Apache Spark for scalable data transformation
- **Data Quality Assurance**: Handles special characters, missing values, and data validation
- **Skills Analytics**: Counts and analyzes skill requirements per job posting
- **Multiple Output Formats**: Generates both JSON and CSV outputs for flexibility
- **Error Handling**: Comprehensive exception handling for network, parsing, and I/O operations
- **Visual Analytics**: Includes dashboard visualizations for job market insights

## 🏗️ Architecture

```
Raw Data (API) → Extract → Transform (Spark) → Load (CSV) → Visualize
```

### Data Flow
1. **Extract**: Fetch job listings from RemoteOK API
2. **Transform**: Clean and structure data using PySpark
3. **Load**: Export to CSV format for analysis tools
4. **Analyze**: Generate insights through data visualization

## 📁 Project Structure

```
job-etl-pipeline/
├── data/
│   ├── cleaned_jobs_spark/
│   │   ├── cleaned_jobs.json      # Processed JSON data
│   │   └── _SUCCESS               # Spark success marker
│   └── jobs/
│       ├── jobs.csv               # Final CSV output
│       └── _SUCCESS               # Spark success marker
├── scripts/
│   ├── fetch_jobs.py              # Data extraction script
│   ├── clean_transform_spark.py   # Data transformation script
│   ├── load_to_csv_spark.py       # Data loading script
│   └── run_job.py                 # Pipeline orchestrator
└── visuals/
    └── Jobs.pdf                   # Analytics dashboard
```

## 🛠️ Prerequisites

### System Requirements
- Python 3.7+
- Apache Spark 3.x
- Java 8 or 11 (for Spark)

### Python Dependencies
```bash
pip install requests pyspark
```

### Environment Setup
```bash
# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## 🚦 Getting Started

### Quick Start
Run the complete ETL pipeline with a single command:

```bash
python3 scripts/run_job.py
```

### Manual Execution
Execute individual pipeline stages:

```bash
# Step 1: Extract data from API
python3 scripts/fetch_jobs.py

# Step 2: Transform data using Spark
python3 scripts/clean_transform_spark.py

# Step 3: Load data to CSV
python3 scripts/load_to_csv_spark.py
```

## 📋 Pipeline Components

### 1. Data Extraction (`fetch_jobs.py`)
- Fetches job listings from RemoteOK API
- Implements robust error handling for network requests
- Saves raw JSON data to `data/raw_jobs.json`
- Skips the first element (API metadata) to get clean job listings

**Key Features:**
- HTTP error handling with `raise_for_status()`
- JSON parsing validation
- File I/O error management

### 2. Data Transformation (`clean_transform_spark.py`)
- Processes raw JSON using PySpark
- Cleans company names and job titles (removes semicolons)
- Calculates skill count for each job posting
- Handles array data types for tags/skills

**Transformations Applied:**
- Column renaming for clarity
- Special character sanitization
- Skill count calculation using `size()` function
- Schema normalization

### 3. Data Loading (`load_to_csv_spark.py`)
- Converts processed JSON to CSV format
- Flattens array columns (tags_skills) to comma-separated strings
- Outputs single CSV file with headers
- Automatically renames Spark part files to standard names

### 4. Pipeline Orchestration (`run_job.py`)
- Executes all ETL steps in sequence
- Captures and displays script outputs
- Implements error handling with exit codes
- Provides progress feedback

## 📊 Data Schema

### Input Schema (RemoteOK API)
```json
{
  "id": "string",
  "company": "string",
  "position": "string", 
  "tags": ["array of skills"],
  "location": "string",
  "date": "timestamp",
  "apply_url": "string"
}
```

### Output Schema (CSV)
```csv
id,company_name,job_title,tags_skills,country,date_posted,apply_url,skill_count
```

## 📈 Analytics Insights

The pipeline generates data suitable for analyzing:

- **Job Market Trends**: Distribution of jobs by location and time
- **Skills Demand**: Most requested technical skills
- **Company Analysis**: Top hiring companies and their requirements
- **Remote Work Patterns**: Geographic distribution of remote opportunities
- **Skill Complexity**: Average skills required per job type

### Sample Analytics
- Jobs requiring 20+ skills indicate senior/specialized positions
- Frontend and DevOps roles show highest skill requirements
- Geographic distribution spans global remote opportunities

## 🔧 Configuration

### Spark Configuration
The pipeline uses default Spark settings optimized for single-machine processing:
- Application name: "JobCleaner" / "JOB-Loader"
- Output coalesced to single file for easier handling
- Overwrite mode for iterative development

### API Configuration
- Source: RemoteOK API (`https://remoteok.com/api`)
- Rate limiting: Respects API guidelines
- Data freshness: Real-time job listings

## 🐛 Troubleshooting

### Common Issues

**Network Connectivity**
```bash
Error fetching data: Connection timeout
```
*Solution*: Check internet connection and API availability

**Spark Configuration**
```bash
Java gateway process exited before sending its port number
```
*Solution*: Ensure Java 8/11 is installed and JAVA_HOME is set

**File Permissions**
```bash
Error writing file: Permission denied
```
*Solution*: Check write permissions for data directories

### Debug Mode
Add verbose logging by modifying scripts:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 🚀 Future Enhancements

- **Real-time Processing**: Implement streaming ETL with Kafka/Spark Streaming
- **Data Validation**: Add schema validation and data quality checks
- **Multiple Sources**: Integrate additional job boards (Indeed, LinkedIn, etc.)
- **Machine Learning**: Job recommendation engine based on skills matching
- **Alerting**: Automated notifications for data pipeline failures
- **Scheduling**: Cron job or Airflow integration for automated runs

## 📞 Support

For questions or issues:
- Create an issue in the repository
- Check existing documentation
- Review error logs in the terminal output

---

**Built with ❤️ using Python, Apache Spark, and RemoteOK API**