from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

todos = {}
next_todo_id = 1  # Global variable to keep track of the next todo ID

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    global next_todo_id  # Use the global variable to track the next ID
    todos[next_todo_id] = request.form['todo_item']
    next_todo_id += 1  # Increment the ID for the next todo item
    return redirect(url_for('index'))

@app.route('/remove/<int:todo_id>')
def remove_todo(todo_id):
    todos.pop(todo_id, None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
