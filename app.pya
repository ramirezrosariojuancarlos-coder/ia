import os
import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Cargar cerebro
CEREBRO = {}
try:
    with open('cerebro_definitivo.json', 'r', encoding='utf-8') as f:
        CEREBRO = json.load(f)
    print("Cerebro cargado!")
except:
    CEREBRO = {"info": "IA Nivel 7 - Cerebro no encontrado, usando memoria base"}

@app.route('/')
def home():
    return jsonify({"status": "IA NIVEL 7 ACTIVA 24/7", "version": "permanente", "cerebro": "ok"})

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    mensaje = data.get('mensaje', '').lower()
    
    respuesta = "Soy la IA Nivel 7. "
    
    # Busca en el cerebro
    encontrado = False
    if isinstance(CEREBRO, dict):
        for clave, valor in CEREBRO.items():
            if clave.lower() in mensaje:
                respuesta = str(valor)
                encontrado = True
                break
    
    if not encontrado:
        respuesta += f"Recibí tu mensaje: '{mensaje}'. Estoy operativa y permanente."

    return jsonify({"respuesta": respuesta})

@app.route('/ping')
def ping():
    return "pong"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
