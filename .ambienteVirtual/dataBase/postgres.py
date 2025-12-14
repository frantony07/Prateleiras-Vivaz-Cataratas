import psycopg2 as pg
hostname= 'localhost'
database = 'stock'
username ='frantony07'
pwd = 'santi14072005'
port_id = 5432
conn = None
cur=  None
try:
    conn =pg.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id
    )
    cur = conn.cursor()
    create_script = ''' CREATE TABLE IF NOT EXISTS  product (
                        id int PRIMARY KEY,
                        name varchar(40) NOT NULL,
                        stock int ,
                        unidade_medida int,
                        valudade varchar(10),
                        stock_minimo int
    )'''
    cur.execute(create_script)

    
    cur.execute('SELECT * FROM  product')
    print(cur.fetchall())
    conn.commit()

    print("Conexión exitosa ✔️")
except Exception as erro:
    print(erro)

finally:
    if cur is not None:
        cur.close()

    if conn is not None:
        conn.close()

