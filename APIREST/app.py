from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import mysql.connector

app = Flask(__name__)

# Configuración de la base de datos MySQL sin autenticación
db = mysql.connector.connect(
    host="localhost",
    user="",
    password="",
    database="heladeria"
)


# Definición del cursor para ejecutar consultas
cursor = db.cursor()

# Ruta para crear un nuevo sabor de helado en la base de datos
@app.route('/create', methods=['POST'])
def create_sabor():
    data = request.get_json()
    sabor = data.get('sabor')
    if sabor:
        cursor.execute("INSERT INTO sabores (sabor) VALUES (%s)", (sabor,))
        db.commit()
        return jsonify({'message': 'Sabor de helado creado exitosamente'}), 201
    else:
        return jsonify({'message': 'Datos incompletos'}), 400

# Ruta para obtener todos los sabores de helado en la base de datos
@app.route('/sabores', methods=['GET'])
def get_sabores():
    cursor.execute("SELECT * FROM sabores")
    sabores = cursor.fetchall()
    sabores_list = [{'id': sabor[0], 'sabor': sabor[1]} for sabor in sabores]
    return jsonify(sabores_list)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000, debug=True)