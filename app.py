from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

# In-memory database
items = []


def add_item_to_list(item_list, item):
    """Pure function used for unit testing."""
    if item:
        item_list.append(item)
    return item_list

@app.route('/')
def index():
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add_item():
    item = request.form.get('item')
    add_item_to_list(items, item)
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete_item(index):
    if index < len(items):
        items.pop(index)
    return redirect(url_for('index'))

@app.route('/update/<int:index>', methods=['POST'])
def update_item(index):
    if index < len(items):
        items[index] = request.form.get('new_item')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
