## Sistema de Citas Médicas – API con FastAPI
<p align="center"> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" width="60"/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="60"/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/fastapi/fastapi-original.svg" width="60"/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg" width="60"/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg" width="60"/> </p>

## Introducción

Este proyecto consiste en el desarrollo de una API para gestionar citas médicas, realizada como actividad para la materia de Programación Distribuida.

La idea principal del laboratorio fue crear un pequeño microservicio capaz de guardar información en una base de datos y permitir que diferentes clientes puedan consultar o modificar esos datos mediante peticiones HTTP.

Para esto se utilizó FastAPI en Python, conectado a una base de datos MySQL/MariaDB.
El entorno de desarrollo se ejecutó utilizando WSL, lo que permitió trabajar con herramientas de Linux desde Windows.

El sistema permite registrar citas, consultarlas, cancelarlas y realizar algunas operaciones adicionales que facilitan la gestión de la información.

## Tecnologías utilizadas

Durante el desarrollo de este proyecto se utilizaron las siguientes tecnologías:

Python como lenguaje principal.

FastAPI para la creación de la API.

MySQL / MariaDB para el almacenamiento de los datos.

WSL (Windows Subsystem for Linux) para ejecutar el servidor de base de datos.

GitHub para el control de versiones y almacenamiento del repositorio.

aiomysql como librería para conectar Python con la base de datos de forma asíncrona.

El uso de programación async permite que el servidor pueda manejar varias solicitudes al mismo tiempo sin bloquearse mientras se realizan consultas en la base de datos.

## Arquitectura del sistema

El funcionamiento general del sistema sigue una estructura sencilla típica de un microservicio.

El cliente envía una solicitud HTTP.

FastAPI recibe la solicitud.

La API realiza una consulta o modificación en la base de datos.

La base de datos responde.

La API devuelve la respuesta al cliente.

En forma resumida:

Cliente → API FastAPI → Base de datos MySQL

Este flujo permite que múltiples clientes puedan interactuar con el sistema al mismo tiempo.

Base de datos

Para este sistema se creó una base de datos llamada:

citas_db

Dentro de esta base de datos se creó la tabla principal:

citas

La tabla contiene los siguientes campos:

id → identificador de la cita

paciente → nombre del paciente

fecha → fecha de la cita

estado → indica si la cita está activa o cancelada

El campo estado permite manejar la cancelación o reactivación de citas sin perder la información registrada.

Funcionalidades del sistema

El sistema permite realizar varias operaciones relacionadas con las citas médicas.

Crear una cita

Permite registrar una nueva cita indicando el nombre del paciente y la fecha.

POST /citas
Listar todas las citas

Devuelve todas las citas almacenadas en la base de datos.

GET /citas
Buscar citas por paciente

Permite consultar las citas asociadas a un paciente específico.

GET /citas/paciente/{paciente}
Cancelar una cita

Cambia el estado de la cita a cancelada.

PUT /citas/cancelar/{id}
Funciones adicionales

Como parte de la actividad en clase y la actividad independiente, se agregaron algunas funciones extra.

Listar citas activas

Muestra únicamente las citas que están activas.

GET /citas/activas
Contar citas registradas

Devuelve el número total de citas almacenadas.

GET /citas/count
Reactivar una cita cancelada

Permite volver a activar una cita que había sido cancelada anteriormente.

PUT /citas/reactivar/{id}
Actualizar la fecha de una cita

Permite modificar la fecha de una cita ya registrada.

PUT /citas/{id}
Eliminar una cita

Elimina una cita de la base de datos.

DELETE /citas/{id}
Buscar citas por fecha

Devuelve todas las citas programadas para una fecha específica.

GET /citas/fecha/{fecha}
Ejecución del proyecto

## Para ejecutar el proyecto se deben seguir los siguientes pasos.

1. Clonar el repositorio
git clone [URL_DEL_REPOSITORIO](https://github.com/Esteban-Developer/app-citas.git)
2. Entrar al directorio del proyecto
cd citas_api
3. Crear un entorno virtual
python -m venv venv
4. Activar el entorno virtual

En Windows:

venv\Scripts\activate

## En Linux o WSL:

source venv/bin/activate
5. Instalar dependencias
pip install fastapi uvicorn aiomysql
6. Ejecutar el servidor
uvicorn main:app --reload
Documentación de la API

FastAPI genera automáticamente una interfaz para probar los endpoints.

Se puede acceder desde el navegador en la siguiente dirección:

http://127.0.0.1:8000/docs

En esta página es posible probar todos los endpoints de la API y ver las respuestas que devuelve el servidor.

 ## Conclusión

Este proyecto permitió aplicar conceptos básicos de APIs REST, manejo de bases de datos y programación asíncrona.
Además, sirvió como introducción a la forma en que funcionan los microservicios dentro de sistemas distribuidos.

Aunque es un sistema sencillo, muestra cómo una API puede interactuar con una base de datos para almacenar y consultar información de manera organizada.