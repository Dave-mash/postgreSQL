from flask import Flask, request, jsonify
import os

from database import InitializeDb

app = Flask(__name__)

db = InitializeDb(os.getenv('FLASK_DATABASE_URI'))
db.create_tables()
posts = []

@app.route('/posts', methods=['POST', 'GET'])
def posts_route():
    if request.methods == 'GET':
        return jsonify({ 'posts': posts })
    elif request.methods == 'POST':
        data = request.get_json()
        return jsonify({ "message": "You have successfully posted", "post": data })

@app.route('/posts/<int:postId>', methods=['GET'])
def post(postId):
    post = [post for post in posts if post['id'] == postId]

    if post:
        return jsonify({ "post": post[0] })

