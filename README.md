## Sistema de Citas con Microservicios
<p align="center"> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" width="60"/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="60"/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/fastapi/fastapi-original.svg" width="60"/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg" width="60"/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg" width="60"/> </p>
Proyecto académico para demostrar comunicación HTTP entre microservicios utilizando FastAPI y MySQL.

## CONTEXTO
Proyecto sencillo desarrollado con FastAPI para simular un sistema de gestión de citas médicas usando una arquitectura de microservicios.

El sistema está dividido en dos servicios independientes:

Servicio de Pacientes

Servicio de Citas

El servicio de citas se comunica con el servicio de pacientes mediante peticiones HTTP, verificando que el paciente exista antes de registrar una cita.

## Tecnologías utilizadas
Python

FastAPI

MySQL

aiomysql

httpx

Uvicorn

Estas herramientas permiten construir APIs rápidas y simular la comunicación entre servicios en una arquitectura distribuida.

## Estructura del proyecto
<img width="249" height="226" alt="image" src="https://github.com/user-attachments/assets/c892ff15-32ac-4c27-bc4b-242210f00ad5" />

## Base de datos
citas_db
Tabla pacientes:
id
nombre
edad
Tabla citas:
id
paciente_id
fecha
estado
paciente_id funciona como relación con la tabla de pacientes.
## Arquitectura del sistema
<img width="247" height="234" alt="image" src="https://github.com/user-attachments/assets/2dbd5b5d-2203-4965-b373-385fd454ad7b" />


El servicio de citas consulta al servicio de pacientes antes de registrar una nueva cita.
## EJECUCION DEL PROYECTO
Clonar el proyecto
git clone https://github.com/Esteban-Developer/app-citas-microservicios.git
cd app-citas-microservicios
Crear y activar entorno virtual

Windows:

python -m venv .venv
.venv\Scripts\activate
Linux / WSL:

python3 -m venv .venv
source .venv/bin/activate
## IMPORTANTE PARA QUE LES FUNCIONE MUCHACHOS (LA INSTALACION DE DEPENDENCIAS)
pip install -r requirements.txt

## Ejecutar los microservicios
Abrir dos terminales.

Servicio de pacientes
cd pacientes_service
uvicorn main:app --reload --port 8001

Servicio de citas
cd citas_api
uvicorn main:app --reload --port 8000

## Probar la API

FastAPI genera documentación automática.

Servicio pacientes:

http://127.0.0.1:8001/docs

Servicio citas:

http://127.0.0.1:8000/docs

Desde ahí se pueden probar los endpoints.

## Flujo básico del sistema

Registrar un paciente

Crear una cita asociada a ese paciente

Consultar citas registradas

Cancelar o reactivar citas

Si el paciente no existe, el sistema no permite crear la cita.

## Autor

## Esteban Murillo Gómez

Desarrollado como práctica de arquitectura de microservicios con FastAPI.

GitHub:
https://github.com/Esteban-Developer
