from flask import Flask, request, jsonify, redirect

app = Flask(__name__)

# In-memory storage for todos
todos = []

@app.route('/')
def home():
    return redirect('https://github.com/dantefasano/python-todo-list-API#readme')

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_todo():
    data = request.get_json()
    if not data or 'label' not in data:
        return jsonify({"error": "Invalid input"}), 400
    todo = {
        "done": data.get("done", False),
        "label": data["label"]
    }
    todos.append(todo)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if position < 0 or position >= len(todos):
        return jsonify({"error": "Invalid position"}), 404
    todos.pop(position)
    return jsonify(todos)

if __name__ == '__main__':
    app.run(debug=True) 