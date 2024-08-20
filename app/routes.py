from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime

main = Blueprint('main', __name__)

# Ejemplo de base de datos en memoria con campo de imagen y fecha
posts = [
    {'id': 1, 'title': 'Post 1', 'content': 'Este es el contenido del post 1', 'date': '15 de agosto de 2024', 'image': None},
    {'id': 2, 'title': 'Post 2', 'content': 'Este es el contenido del post 2', 'date': '15 de agosto de 2024', 'image': None}
]

@main.route('/', methods=['GET'])
def home():
    search_query = request.args.get('search', '').lower()
    if search_query:
        filtered_posts = [post for post in posts if search_query in post['title'].lower() or search_query in post['content'].lower()]
    else:
        filtered_posts = posts
    return render_template('home.html', posts=filtered_posts)

@main.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        new_id = len(posts) + 1
        title = request.form['title']
        content = request.form['content']
        date = datetime.now().strftime('%d de %B de %Y')
        image = request.form.get('image', None)
        posts.append({'id': new_id, 'title': title, 'content': content, 'date': date, 'image': image})
        return redirect(url_for('main.home'))
    return render_template('add_edit.html', action="Agregar", post={})

@main.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    post = next((post for post in posts if post['id'] == id), None)
    if request.method == 'POST':
        post['title'] = request.form['title']
        post['content'] = request.form['content']
        post['image'] = request.form.get('image', None)
        return redirect(url_for('main.home'))
    return render_template('add_edit.html', action="Editar", post=post)

@main.route('/delete/<int:id>', methods=['GET'])
def delete(id):
    global posts
    posts = [post for post in posts if post['id'] != id]
    return redirect(url_for('main.home'))
