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


def def_test():
    print("testing ----------------")


with DAG(
    dag_id="test_dag_1",
    description="Dag for testing purposes",
    default_args=default_args,
    params=default_params,
    start_date=datetime(2021, 1, 1),
    schedule="0 0 * * *",
    catchup=False,
    tags=["test"],
) as dag:
    
    def_test_task = PythonOperator(
        task_id="def_test_task",
        python_callable=def_test,
    )

    def_test_task
