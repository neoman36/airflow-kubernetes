import datetime as dt
from time import sleep

from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.subdag_operator import SubDagOperator

args = {
    'owner': 'airflow',
    'start_date': dt.datetime(2020, 2, 11),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=1),
    'depends_on_past': False,
}


def first_step():
    for i in range(5):
        print(f'Step {i}')
        sleep(1)
    return 5


def second_step():
    for i in range(5):
        print(f'Step {i}')
        sleep(1)


def other_step():
    for i in range(5):
        print(f'Step {i}')
        sleep(1)


def other_step_2():
    for i in range(5):
        print(f'Step {i}')
        sleep(1)


main_dag = DAG(dag_id='fake', default_args=args, schedule_interval=None)

with DAG(dag_id='fake', default_args=args, schedule_interval=None) as dag:
    first_step_dataset = PythonOperator(
        task_id='first_step',
        python_callable=first_step,
        dag=dag
    )
    second_step_op = PythonOperator(
        task_id='second_step',
        python_callable=second_step,
        dag=dag
    )

    with DAG(dag_id='fake.sub_fake', default_args=args, schedule_interval=None) as sub_dug:
        other_step_op = PythonOperator(
            task_id='other_step',
            python_callable=other_step,
            dag=sub_dug
        )

        other_step_2_op = PythonOperator(
            task_id='other_step_2',
            python_callable=other_step_2,
            dag=sub_dug
        )

        other_step_op >> other_step_2_op

        run_sub_dag = SubDagOperator(
            task_id='sub_fake',
            subdag=sub_dug,
            dag=dag,
        )

    first_step_dataset >> second_step_op >> run_sub_dag
