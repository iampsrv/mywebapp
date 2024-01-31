from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# This dictionary will act as a fake database
todos = {}

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    todo_id = len(todos) + 1
    todos[todo_id] = request.form['todo_item']
    return redirect(url_for('index'))

@app.route('/remove/<int:todo_id>')
def remove_todo(todo_id):
    todos.pop(todo_id, None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(port=5001, debug=True)
