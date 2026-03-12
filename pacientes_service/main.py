from fastapi import FastAPI, HTTPException
from database import connect_db

app = FastAPI()


# Crear paciente
@app.post("/pacientes")
async def crear_paciente(nombre: str, edad: int):

    conn = await connect_db()
    cursor = await conn.cursor()

    sql = "INSERT INTO pacientes (nombre, edad) VALUES (%s,%s)"
    await cursor.execute(sql, (nombre, edad))
    await conn.commit()

    return {"mensaje": "Paciente creado"}


# Listar pacientes
@app.get("/pacientes")
async def listar_pacientes():

    conn = await connect_db()
    cursor = await conn.cursor()

    await cursor.execute("SELECT * FROM pacientes")
    pacientes = await cursor.fetchall()

    return {"pacientes": pacientes}


# Buscar paciente por id
@app.get("/pacientes/{id}")
async def buscar_paciente(id: int):

    conn = await connect_db()
    cursor = await conn.cursor()

    await cursor.execute("SELECT * FROM pacientes WHERE id=%s", (id,))
    paciente = await cursor.fetchone()

    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")

    return {"paciente": paciente}