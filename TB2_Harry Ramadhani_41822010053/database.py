import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="perpustakaan"
    )

def add_buku_to_db(buku):
    db = connect_db()
    cursor = db.cursor()
    query = "INSERT INTO buku (judul, penulis, penerbit, tahun_terbit, konten, ikhtisar) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (buku.judul, buku.penulis, buku.penerbit, buku.tahun_terbit, buku.konten, buku.ikhtisar)
    cursor.execute(query, values)
    db.commit()
    cursor.close()
    db.close()

def get_all_buku_from_db():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT judul, penulis, penerbit, tahun_terbit, konten, ikhtisar FROM buku")
    results = cursor.fetchall()
    cursor.close()
    db.close()
    return results
