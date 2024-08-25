from flask import Flask, jsonify

app = Flask(__name__)

# Lista de nombres de personas
people = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"},
    {"id": 4, "name": "Diana"}
]  

# Endpoint para obtener la lista de personas
@app.route('/api/people', methods=['GET'])
def get_people():
    return jsonify(people)

if __name__ == '__main__':
    app.run(debug=True)
