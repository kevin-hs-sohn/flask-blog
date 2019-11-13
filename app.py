from flask import Flask, render_template

app = Flask(__name__)
posts = [
    {
        "post_id": 1,
        "title": "First Post",
        "content": "Hello World!",
        "author": "Kevin",
        "date": "March 29, 2019",
    },
    {
        "post_id": 2,
        "title": "Second Post",
        "content": "Goodbye World!",
        "author": "Qria",
        "date": "June 7, 2019",
    }
]

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    post = posts[post_id-1]
    return render_template('posts.html',post=post)