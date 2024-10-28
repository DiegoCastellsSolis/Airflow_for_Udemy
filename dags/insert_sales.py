from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.hooks.base_hook import BaseHook
from sqlalchemy import create_engine
import pandas as pd
from datetime import datetime

# Función para insertar datos en la base de datos
def insert_data():
    # Crear un DataFrame con ventas de la carpeta data
    df = pd.read_csv('/opt/airflow/data/ventas.csv') 
    
    # Obtener la conexión de Airflow
    conn = BaseHook.get_connection('NOVA_BI_STAGING')
    connection_string = f"postgresql+psycopg2://{conn.login}:{conn.password}@{conn.host}:{conn.port}/{conn.schema}"

    # Crear la conexión a la base de datos
    engine = create_engine(connection_string)

    # Insertar el DataFrame en la base de datos como una nueva tabla llamada "empleados"
    df.to_sql('sales', engine, if_exists='replace', index=False)

# Definir el DAG
with DAG(
    'insert_sales',
    schedule_interval=None,  # Cambia esto si deseas un horario
    start_date=datetime(2024, 10, 28),
    catchup=False
) as dag:
    
    # Definir la tarea que insertará los datos
    insert_data_task = PythonOperator(
        task_id='insert_data_sales',
        python_callable=insert_data
    )

# Establecer el flujo de trabajo (si hay más tareas, aquí puedes definir el orden)
insert_data_task
