# Deteksi Produk Halal & Haram

Project ini bertujuan untuk mengklasifikasikan produk halal dan haram menggunakan **Python** dengan metode **Cosine Similarity** dan **K-Nearest Neighbor (KNN)** yang berbasis WEBSITE. Sistem ini memanfaatkan data berupa teks (nama produk, komposisi, deskripsi) untuk menentukan tingkat kesamaan dan kategori produk.

---

## 📌 Deskripsi

Project ini bekerja dengan dua pendekatan utama:

### 1. **Cosine Similarity**

Digunakan untuk mengukur tingkat kemiripan antara teks produk baru dengan dataset halal/haram. Semakin tinggi nilai kesamaan, semakin dekat kategori produk tersebut.

### 2. **K-Nearest Neighbor (KNN)**

Metode klasifikasi yang menentukan kategori produk berdasarkan sejumlah tetangga terdekat (k). Digunakan untuk memperkuat hasil prediksi berbasis dataset.

---

## 🛠 Teknologi

* Python 3
* Flask
* Scikit-learn
* Pandas
* NLTK / Sastrawi (opsional untuk preprocessing bahasa Indonesia)

---

## ▶️ Cara Menjalankan

Jalankan prediksi:

```
python app.py
```

## 📊 Output

Sistem akan menampilkan:

Hasil dari produk **Haram** atau **Halal**
