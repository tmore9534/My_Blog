from datetime import datetime
from flask import Flask, url_for,render_template, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm


app=Flask(__name__)

app.config['SECRET_KEY']='19d895c43ecfd78685edefc3f860c65f'
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///site.db'

db=SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(20), unique=True, nullable=False)
    email=db.Column(db.String(120), unique=True, nullable=False)
    image_file=db.Column(db.String(60), nullable=False, default='default.jpg')
    password=db.Column(db.String(60), nullable=False)
    posts=db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"  

class Post(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title= db.Column(db.String(100), nullable=False)
    date_posted=db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content=db.Column(db.Text, nullable=False)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"  



posts=[
    {
        'author':'Tushar More',
        'title':'Blog post 1',
        'content':'first post content',
        'date_posted':'21 aug 2022'
    },

    {
        'author':'Akash Joshi',
        'title':"Blog post 2",
        'content':'second post content',
        'date_posted':'22 aug 2022'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html",posts=posts, title='title')

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route('/login', methods=["POST", "GET"])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data=="password":
            flash(f'You have been logged in!','success')
            return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)

@app.route('/register',  methods=["POST", "GET"])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'succfroess')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

if __name__=="__main__":
    app.run(debug=True)



if __name__=="__main__":
    app.run(debug=True)
