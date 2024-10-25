from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

# Función de ejemplo que se ejecutará en el DAG
def print_message():
    print("¡Hola desde Airflow!")

# Definición de los parámetros por defecto
default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2024, 10, 25),  # Cambia la fecha a tu preferencia
}

# Inicialización del DAG
dag = DAG(
    'mi_dag_basico',  # Nombre del DAG
    default_args=default_args,
    description='Un DAG básico que imprime un mensaje.',
    schedule_interval=timedelta(days=1),  # Se ejecuta diariamente
)

# Tarea 1: Operador Dummy
start = DummyOperator(
    task_id='start',
    dag=dag,
)

# Tarea 2: Operador Python
print_task = PythonOperator(
    task_id='print_task',
    python_callable=print_message,
    dag=dag,
)

# Definición del flujo de tareas
start >> print_task  # Ejecutar start seguido de print_task
