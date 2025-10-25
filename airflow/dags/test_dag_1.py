from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import timedelta, datetime


default_params = {

}

default_args = {
    "owner": "airflow",
    "retries": 0,
    "retry_delay": timedelta(minutes=1),
}


def def_test(**context):
    dag_run = context.get("dag_run")

    if dag_run.run_type == "manual":
        print("Triggered manually (API/UI/CLI)")
    elif dag_run.run_type == "scheduled":
        print("Triggered automatically by scheduler")
    elif dag_run.run_type == "dataset_triggered":
        print("Triggered by dataset dependency")
    else:
        print(f"Triggered by {dag_run.run_type}")


with DAG(
    dag_id="test_dag_1",
    description="Dag for testing purposes",
    default_args=default_args,
    params=default_params,
    start_date=datetime(2021, 1, 1),
    schedule="40 14 * * *", # every day at 14:40
    catchup=False,
    tags=["test"],
) as dag:
    
    def_test_task = PythonOperator(
        task_id="def_test_task",
        python_callable=def_test,
    )

    def_test_task
