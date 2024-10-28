# Guía de Instalación y Uso de Apache Airflow con Docker

Este documento describe los pasos para desplegar Apache Airflow utilizando Docker y Docker Compose. Asegúrate de tener Docker y Docker Compose instalados en tu sistema antes de comenzar.

## Requisitos Previos

- **Docker**: [Instalación de Docker](https://docs.docker.com/get-docker/)
- **Docker Compose**: [Instalación de Docker Compose](https://docs.docker.com/compose/install/)

## Pasos para Desplegar Apache Airflow

1. **Clonar el Repositorio** (si es necesario)
   Si tienes un repositorio específico con la configuración de Docker y Airflow, clónalo en tu máquina local.

   ```bash
   git clone https://github.com/DiegoCastellsSolis/airflow-pgadmin-metabase.git
   cd airflow-pgadmin-metabase
    ```

2. **Ejecutar el Contenedor de Docker**
Abre una terminal y ejecuta el siguiente comando para levantar la instancia de Docker.
```bash
    echo "Instancia de Docker disparada"
    docker-compose up -d
    echo "Imágenes desplegadas"
    echo ""
```
3.**Acceder a la Consola de Airflow**
Una vez que los contenedores estén en funcionamiento, accede a la consola de Airflow utilizando el siguiente comando:  
```bash
    echo "Ingresando a la consola de Airflow"
    docker exec -it docker-airflow-pgadmin-metabase-airflow-1 bash
```

4.**Crear un Usuario de Airflow**
Ejecuta los siguientes comandos en la consola de Airflow para crear un usuario administrador:
```bash
airflow users create --username admin --password admin --firstname admin --lastname admin --role Admin --email admin@example.com
```

5.**Iniciar el Servidor Web y el Scheduler de Airflow**
Después de crear el usuario, ejecuta los siguientes comandos en la misma consola para iniciar el servidor web y el scheduler de Airflow:
```bash
    airflow webserver
    airflow scheduler
```

6.**Salir de la Consola de Airflow**
Puedes salir de la consola de Airflow con el comando exit.
```bash
    exit
```

7.**Acceso a la Interfaz de Usuario de Airflow**
Puedes acceder a la interfaz de usuario de Airflow abriendo un navegador y navegando a:
```bash
    http://localhost:8080
```
O en su defecto.
```bash
    http://localhost:8081
```