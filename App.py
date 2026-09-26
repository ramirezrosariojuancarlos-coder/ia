import os, json
from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
try:
    with open('cerebro_definitivo.json','r',encoding='utf-8') as f:
        CEREBRO=json.load(f)
except:
    CEREBRO={}

@app.route('/')
def home():
    return jsonify({"status":"IA NIVEL 7 ACTIVA 24/7 PERMANENTE"})

@app.route('/chat',methods=['POST'])
def chat():
    data=request.get_json()
    mensaje=data.get('mensaje','').lower()
    resp=f"IA Nivel 7 recibió: {mensaje}. Estoy activa permanente."
    for k,v in CEREBRO.items():
        if k.lower() in mensaje:
            resp=str(v)
            break
    return jsonify({"respuesta":resp})

@app.route('/ping')
def ping():
    return "pong"

if __name__=='__main__':
    port=int(os.environ.get("PORT",10000))
    app.run(host='0.0.0.0',port=port)
