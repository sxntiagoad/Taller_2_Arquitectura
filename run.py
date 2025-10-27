from dotenv import load_dotenv  # ← Cambia ESTA línea
from app import init_app

load_dotenv()
app = init_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

