from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner':'belal',
    'retries':5,
    'retry_delay': timedelta(minutes=2)

}

with DAG(
    dag_id='our_first_dag_v4',
    default_args = default_args,
    description='This is our first dag that we write',
    start_date=datetime(2024,5,18,0),
    schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command="echo hello world"
    )

    task2= BashOperator(
        task_id='second_task',
        bash_command="echo hey, I am task2 and will be running after task1"
    )

    task3= BashOperator(
        task_id='third_task',
        bash_command="echo hey, I am task3 and will be running after task1 like task2"
    )
    #task1.set_downstream(task2)
    #task1.set_downstream(task3)

    task1 >> task2
    task1 >> task3
    #or task1 >> [task2, task3]