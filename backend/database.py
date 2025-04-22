import sqlite3

def init_db():
    conn = sqlite3.connect('devices.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dispositivos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip TEXT NOT NULL,
            nome TEXT NOT NULL,
            trafego REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def adicionar_dispositivo(ip, nome, trafego):
    conn = sqlite3.connect('devices.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO dispositivos (ip, nome, trafego) VALUES (?, ?, ?)', (ip, nome, trafego))
    conn.commit()
    conn.close()

def listar_dispositivos():
    conn = sqlite3.connect('devices.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM dispositivos')
    dados = cursor.fetchall()
    conn.close()
    return dados

def remover_dispositivo(dispositivo_id):
    conn = sqlite3.connect('devices.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM dispositivos WHERE id = ?', (dispositivo_id,))
    conn.commit()
    conn.close()
