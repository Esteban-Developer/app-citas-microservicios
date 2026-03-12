import aiomysql

async def connect_db():
    conn = await aiomysql.connect(
        host="localhost",
        user="root",
        password="",
        db="citas_db"
    )
    return conn