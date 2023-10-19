from flask import  url_for,render_template, flash, redirect
from myblog import app
from myblog.forms import RegistrationForm, LoginForm
from myblog.model import User, Post


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
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
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