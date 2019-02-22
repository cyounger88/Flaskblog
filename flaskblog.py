from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'c501ddd523b95eb5d6612076ebba0c61'

posts = [
    {
        'author': 'Christopher Younger',
        'title': 'Blog Post 1',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Christopher williams',
        'title': 'Blog Post 2',
        'date_posted': 'April 25, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)