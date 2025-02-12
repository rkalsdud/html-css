from flask import render_template
from flask_login import login_required
import requests
from . import main


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/todos')
@login_required
def todos():
    DUMMYJSON_URL = "https://dummyjson.com/todos"
    response = requests.get(DUMMYJSON_URL)
    todos=response.json()['todos']
    return render_template('todo.html', todos=todos)
