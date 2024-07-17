from flask import Flask, request, jsonify
from buku import Buku
from database import add_buku_to_db, get_all_buku_from_db
from logger import log_error

app = Flask(__name__)

# POST method to save a book
@app.route('/buku', methods=['POST'])
def add_buku():
    try:
        data = request.json
        buku = Buku(
            judul=data['judul'],
            penulis=data['penulis'],
            penerbit=data['penerbit'],
            tahun_terbit=data['tahun_terbit'],
            konten=data['konten'],
            ikhtisar=data['ikhtisar']
        )
        add_buku_to_db(buku)
        return jsonify({"message": "Buku added successfully"}), 201
    except Exception as e:
        log_error(f"Error adding buku: {e}")
        return jsonify({"error": "Failed to add buku"}), 500

# GET method to retrieve book data
@app.route('/buku', methods=['GET'])
def get_buku():
    try:
        buku_data = []
        results = get_all_buku_from_db()
        for row in results:
            buku_data.append({
                "judul": row[0],
                "penulis": row[1],
                "penerbit": row[2],
                "tahun_terbit": row[3],
                "konten": row[4],
                "ikhtisar": row[5]
            })
        return jsonify(buku_data), 200
    except Exception as e:
        log_error(f"Error retrieving buku: {e}")
        return jsonify({"error": "Failed to retrieve buku"}), 500

if __name__ == '__main__':
    app.run(debug=True)
