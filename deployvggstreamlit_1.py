
import os
from pyngrok import ngrok

def run_streamlit():
    # Membuka tunnel ngrok dengan parameter bind_tls
    public_url = ngrok.connect(addr=8501)
    print(f"Streamlit app is live at: {public_url}")

    # Menjalankan Streamlit
    os.system('streamlit run app.py')

# Langkah 5: Jalankan Streamlit
run_streamlit()
