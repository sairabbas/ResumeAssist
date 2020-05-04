import flask_login
from flask import Flask, render_template, url_for, flash, redirect, request, send_file
from flask_login import current_user, login_required, login_user, logout_user
from flask_login import LoginManager
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash
from io import BytesIO
from forms import RegistrationForm, LoginForm, QuestionnaireForm, Test
import encodeDecode

from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = '57916289bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(60))
    resumeList = db.relationship('ResumeList', backref='author', lazy='dynamic')

    def __repr__(self):
        return f'<user: {self.username}>'


# TO TEST ENCODE DECODE
""" class Info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    encoded = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) """


class ResumeList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    resume = db.Column(db.LargeBinary)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<post: {self.text}>'


@app.route("/")
@app.route("/home")
def home():
    logout_user()
    return render_template('home.html')


# TO TEST ENCODER DECODER
""" @app.route("/test", methods =['POST'])
def submit():
    form = Test()
    if form.validate_on_submit():
        #takes all form data and writes into text file
        with open("education.txt", "w") as education:
          education.write(str(form.school.data))
          education.write(str(form.degree.data))
          education.write(str(form.startDate.data))
          education.write(str(form.endDate.data))
          education.write(str(form.gpa.data))
          education.write(str(form.coursework.data))
        #store textfile as a encoded string of bytes
        info = Info(eductation = encodeDecode.encodeFile("education.txt"))
        db.session.add(info)
        db.session.commit() """


@app.route("/register", methods=['GET', 'POST'])
def register():
    error = None
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            error = "Username is already taken, please try again."
        else:
            hashed_password = form.password.data
            user = User(username=form.username.data,
                        email=form.email.data,
                        password=hashed_password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('dashboard'))
    return render_template('register.html', form=form, error=error)


@app.route("/login", methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if form.password.data == user.password:
                login_user(user, remember=form.remember.data)
                return redirect(url_for('dashboard'))
        error = "Incorrect username or password, please try again."
    return render_template('login.html', form=form, error=error)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/dashboard')
@login_required
def dashboard():
    User = current_user
    resumes = ResumeList.query.filter_by(id=User.id).all()
    return render_template('dashboard.html', resumes=resumes)


@app.route('/questionnaire', methods=['GET', 'POST'])
@login_required
def questionnaire():
    form = QuestionnaireForm()
    return render_template('questionnaire.html', form=form)


@app.route('/upload', methods=['POST'])
@login_required
def upload():
    file = request.files['inputFile']
    return file.name

@app.route('/selection')
@login_required
def selection():
    return render_template('selection.html')


@app.route('/download<id>')
@login_required
def download(id):
    file_data = ResumeList.query.filter_by(id=int(id)).first()
    return send_file(BytesIO(file_data.resume), attachment_filename=file_data.name, as_attachment=True)


@app.route('/view<id>')
@login_required
def view(id):
    file_data = ResumeList.query.filter_by(id=int(id)).first()
    return send_file(BytesIO(file_data.resume), attachment_filename=file_data.name)


@app.route('/delete<id>')
@login_required
def delete(id):
    ResumeList.query.filter_by(id=int(id)).delete()
    db.session.commit()
    return render_template('dashboard.html')


if __name__ == '__main__':
    app.run(debug=True)
