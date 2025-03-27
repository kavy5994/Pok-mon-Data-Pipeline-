# Pok-mon-Data-Pipeline-
1️⃣ Data Source: Pokémon API / Other Open Datasets
Use the PokéAPI to fetch Pokémon data (stats, types, evolutions).

Alternatively, use Kaggle datasets (e.g., Pokémon battles, abilities, and game statistics).

2️⃣ Set Up a Linux Environment
Use a local Linux VM, WSL on Windows, or a cloud VM (AWS EC2, GCP Compute Engine).

Install FastAPI (pip install fastapi[all]) and serve Pokémon data from your API.

3️⃣ Deploy Airbyte & Build a Custom Connector
Deploy Airbyte on your Linux machine (docker-compose up).

Create an Airbyte REST API Source Connector that pulls data from your FastAPI.

Set up MinIO as an S3-compatible storage destination.

4️⃣ Automate Data Syncing with Dagster
Install Dagster (pip install dagster dagster-webserver dagster-airbyte).

Set up a scheduled incremental sync from Airbyte into MinIO.

Store structured Pokémon data in DuckDB.

5️⃣ Model Data with dbt
Install dbt (pip install dbt-duckdb).

Transform Pokémon data into analytical models (e.g., top Pokémon by power, effectiveness against types).

6️⃣ CI/CD with GitHub Actions
Automate pipeline deployments (FastAPI, Airbyte, dbt) in GitHub Actions.

7️⃣ Query DuckDB with DBeaver
Connect DBeaver to DuckDB and run queries to analyze Pokémon battle stats.


📌 Tech Stack (Fully Open-Source)
✅ Linux → Base environment (Ubuntu, Debian, or Fedora)
✅ FastAPI → Serve API endpoints (fastapi + uvicorn)
✅ Airbyte → ELT tool for extracting data from APIs & loading it
✅ MinIO → Open-source S3-compatible object storage
✅ Dagster → Modern data orchestrator (alternative to Airflow)
✅ DuckDB → Fast OLAP database for analytics
✅ dbt → SQL transformations and modeling (supports DuckDB)
✅ DBeaver → Open-source SQL client for querying data
✅ GitHub Actions → CI/CD automation
