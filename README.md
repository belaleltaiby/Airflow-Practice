# Airflow-Practice
This repository contains configurations for running Apache Airflow with Docker Compose. The setup includes multiple DAGs and Docker Compose files for managing Airflow workflows in a local development environment.

#DAGs
1- our_dag_with_python_operator_v03
Description: A DAG that uses Python operators to demonstrate XCom usage.

2- dag_with_cron_expression_v2
Description: A simple DAG with a cron expression schedule.

3- our_first_dag_v4
Description: A basic DAG with multiple Bash operators.

#Docker Compose
The Docker Compose file sets up a local Airflow environment with the following services:
PostgreSQL: Used as the metadata database for Airflow.
Airflow Webserver: Provides the Airflow web interface.
Airflow Scheduler: Manages scheduling and execution of DAGs.
Airflow Init: Initializes the Airflow database and creates the default user.
