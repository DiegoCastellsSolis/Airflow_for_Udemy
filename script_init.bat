echo "instancia de docker disparada"
docker-compose up -d
echo "imagenes deployadas"
echo ""

echo "ingresando a la consola de airflow"
docker exec -it airflow-pgadmin-metabase-airflow-1 bash

REM  EJECUTARLAS CUANDO INGRESES A LA CONSOLA DE AIRFLOW
REM  airflow users create --username admin --password admin --firstname admin --lastname admin --role Admin --email admin@example.com
REM  
REM  airflow webserver
REM  
REM  airflow scheduler

REM exit

echo "usuario de airflow"
echo "airflow webserver funcionando"
echo "airflow scheduler funcionando"
