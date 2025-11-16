from flask import Flask, render_template, request
import joblib

# Inisialisasi Flask
app = Flask(__name__)

# Load model dan vectorizer
vectorizer = joblib.load('tfidf_vectorizer.pkl')
knn_model = joblib.load('knn_model.pkl')

# Fungsi prediksi
def prediksi_komposisi(teks):
    teks_vector = vectorizer.transform([teks])
    hasil = knn_model.predict(teks_vector)
    label = "Halal" if hasil[0] == 1 else "Haram"
    return label

# Routing halaman utama
@app.route('/', methods=['GET', 'POST'])
def index():
    hasil_prediksi = None
    if request.method == 'POST':
        komposisi = request.form['komposisi']
        hasil_prediksi = prediksi_komposisi(komposisi)
    
    return render_template('index.html', hasil=hasil_prediksi)

# Jalankan server
if __name__ == '__main__':
    app.run(debug=True)
