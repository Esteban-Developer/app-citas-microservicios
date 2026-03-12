from fastapi import FastAPI, HTTPException
from database import connect_db
import asyncio
import httpx

app = FastAPI()

# Crear cita
@app.post("/citas")
async def crear_cita(paciente_id: int, fecha: str):

    if not paciente_id or not fecha:
        raise HTTPException(status_code=400, detail="Paciente y fecha son obligatorios")

    # verificar paciente en el servicio de pacientes
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://127.0.0.1:8001/pacientes/{paciente_id}")

    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="El paciente no existe")

    await asyncio.sleep(2)

    try:
        conn = await connect_db()
        cursor = await conn.cursor()

        sql = "INSERT INTO citas (paciente_id, fecha, estado) VALUES (%s,%s,%s)"
        await cursor.execute(sql, (paciente_id, fecha, "activa"))

        await conn.commit()

        return {"mensaje": "Cita creada correctamente"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear cita: {str(e)}")


# Listar citas
@app.get("/citas")
async def listar_citas():

    try:
        conn = await connect_db()
        cursor = await conn.cursor()

        await cursor.execute("SELECT * FROM citas")
        citas = await cursor.fetchall()

        if not citas:
            raise HTTPException(status_code=404, detail="No hay citas registradas")

        return {"citas": citas}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Buscar cita por paciente
@app.get("/citas/paciente/{paciente_id}")
async def buscar_por_paciente(paciente_id: int):

    try:
        conn = await connect_db()
        cursor = await conn.cursor()

        await cursor.execute(
            "SELECT * FROM citas WHERE paciente_id=%s",
            (paciente_id,)
        )

        citas = await cursor.fetchall()

        if not citas:
            raise HTTPException(status_code=404, detail="El paciente no tiene citas")

        return {"citas": citas}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Cancelar cita
@app.put("/citas/cancelar/{id}")
async def cancelar_cita(id: int):

    try:
        conn = await connect_db()
        cursor = await conn.cursor()

        await cursor.execute(
            "UPDATE citas SET estado='cancelada' WHERE id=%s",
            (id,)
        )

        await conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Cita no encontrada")

        return {"mensaje": "Cita cancelada correctamente"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Listar citas activas
@app.get("/citas/activas")
async def citas_activas():

    try:
        conn = await connect_db()
        cursor = await conn.cursor()

        await cursor.execute(
            "SELECT * FROM citas WHERE estado='activa'"
        )

        citas = await cursor.fetchall()

        if not citas:
            raise HTTPException(status_code=404, detail="No hay citas activas")

        return {"citas_activas": citas}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Contar citas
@app.get("/citas/count")
async def contar_citas():

    try:
        conn = await connect_db()
        cursor = await conn.cursor()

        await cursor.execute("SELECT COUNT(*) FROM citas")
        total = await cursor.fetchone()

        return {"total_citas": total[0]}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Reactivar cita
@app.put("/citas/reactivar/{id}")
async def reactivar_cita(id: int):

    try:
        conn = await connect_db()
        cursor = await conn.cursor()

        await cursor.execute(
            "UPDATE citas SET estado='activa' WHERE id=%s",
            (id,)
        )

        await conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Cita no encontrada")

        return {"mensaje": "Cita reactivada correctamente"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Actualizar fecha
@app.put("/citas/{id}")
async def actualizar_fecha(id: int, fecha: str):

    if not fecha:
        raise HTTPException(status_code=400, detail="La fecha es obligatoria")

    try:
        conn = await connect_db()
        cursor = await conn.cursor()

        await cursor.execute(
            "UPDATE citas SET fecha=%s WHERE id=%s",
            (fecha, id)
        )

        await conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Cita no encontrada")

        return {"mensaje": "Fecha actualizada correctamente"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Eliminar cita
@app.delete("/citas/{id}")
async def eliminar_cita(id: int):

    try:
        conn = await connect_db()
        cursor = await conn.cursor()

        await cursor.execute(
            "DELETE FROM citas WHERE id=%s",
            (id,)
        )

        await conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Cita no encontrada")

        return {"mensaje": "Cita eliminada correctamente"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Listar citas por fecha
@app.get("/citas/fecha/{fecha}")
async def citas_por_fecha(fecha: str):

    try:
        conn = await connect_db()
        cursor = await conn.cursor()

        await cursor.execute(
            "SELECT * FROM citas WHERE fecha=%s",
            (fecha,)
        )

        citas = await cursor.fetchall()

        if not citas:
            raise HTTPException(status_code=404, detail="No hay citas para esa fecha")

        return {"citas": citas}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))