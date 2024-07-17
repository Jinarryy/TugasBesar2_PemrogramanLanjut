CREATE DATABASE perpustakaan;

USE perpustakaan;

CREATE TABLE buku (
    id INT AUTO_INCREMENT PRIMARY KEY,
    judul VARCHAR(255) NOT NULL,
    penulis VARCHAR(255) NOT NULL,
    penerbit VARCHAR(255) NOT NULL,
    tahun_terbit YEAR NOT NULL,
    konten TEXT,
    ikhtisar TEXT
);