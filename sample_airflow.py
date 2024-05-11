from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

# Define default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 5, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Instantiate the DAG
dag = DAG(
    'sample_ec2_deploy_dag',
    default_args=default_args,
    description='A simple DAG to deploy to EC2 instance',
    schedule_interval=timedelta(days=1),
)

# Define tasks in the DAG
task_deploy_to_ec2 = BashOperator(
    task_id='deploy_to_ec2',
    bash_command='echo "Deploying to EC2 instance"',
    dag=dag,
)

task_cleanup = BashOperator(
    task_id='cleanup',
    bash_command='echo "Cleaning up"',
    dag=dag,
)

# Define task dependencies
task_deploy_to_ec2 >> task_cleanup

