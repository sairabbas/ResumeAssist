from io import BytesIO
from flask import Flask, render_template, url_for, flash, redirect, request, send_file, send_from_directory
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_login import UserMixin
from flask_login import current_user, login_required, login_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm, QuestionnaireForm
from generate_resume import createPDF

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
@app.route("/submit", methods =['POST', 'GET'])
def submit():
    if request.method=='POST': #if validate_on_submit
        #takes all form data and writes into text file
        form=request.form
        with open("user.txt", "w") as user:
            user.write(str(form.get("userName")) + "\n")
            user.write(str(form.get("userEmail")))
            user.write(" | " + str(form.get("userPhone")) + " | ")
            user.write(str(form.get("userPortfolio")))
            user.write("\n\n")
        user.close()

        with open("education.txt", "w") as education:
            education.write("\n")
            education.write(str(form.get("schoolName")) + " | ")
            education.write(str(form.get("schoolStartDate")) + " - ")
            education.write(str(form.get("schoolEndDate"))+ "\n")
            education.write(str(form.get("schoolDegree"))+ "\n")
            education.write("GPA: " + str(form.get("schoolGPA")) + "\n")
            education.write("Related Courses: " + str(form.get("schoolCourses")))
            education.write("\n\n")
        education.close()

        with open("project.txt", "w") as project:
            project.write("\n")
            project.write(str(form.get("projectTitle")) + " | ")
            project.write(str(form.get("projectTime")) + "\n")
            project.write(str(form.get("projectTech")) + "\n")
            project.write(str(form.get("projectDescription")))
            project.write("\n\n")

            if(str(form.get("projectTitle2")) != None or str(form.get("projectTitle2")) != "None"):
              project.write(str(form.get("projectTitle2")) + " | ")
              project.write(str(form.get("projectTime2")) + "\n")
              project.write(str(form.get("projectTech2")) + "\n")
              project.write(str(form.get("projectDescription2")))
              project.write("\n\n")

            if(str(form.get("projectTitle3")) != None or str(form.get("projectTitle3")) != "None"):
              project.write(str(form.get("projectTitle3")) + " | ")
              project.write(str(form.get("projectTime3")) + "\n")
              project.write(str(form.get("projectTech3")) + "\n")
              project.write(str(form.get("projectDescription3")))
              project.write("\n\n")
        project.close()

        with open("work.txt", "w") as work:
            work.write("\n")
            work.write(str(form.get("workCompany")) + " | ")
            work.write(str(form.get("workStartDate")) + " - ")
            work.write(str(form.get("workEndDate")) + "\n")
            work.write(str(form.get("workTitle")) + "\n")
            work.write(str(form.get("workDescription")))
            work.write("\n\n")

            if(str(form.get("workCompany2")) != None or str(form.get("workCompany2")) != "None"):
              work.write(str(form.get("workCompany2")) + " | ")
              work.write(str(form.get("workStartDate2")) + " - ")
              work.write(str(form.get("workEndDate2")) + "\n")
              work.write(str(form.get("workTitle2")) + "\n")
              work.write(str(form.get("workDescription2")))
              work.write("\n\n")

            if(str(form.get("workCompany3")) != None or str(form.get("workCompany3")) != "None"):
              work.write(str(form.get("workCompany3")) + " | ")
              work.write(str(form.get("workStartDate3")) + " - ")
              work.write(str(form.get("workEndDate3")) + "\n")
              work.write(str(form.get("workTitle3")) + "\n")
              work.write(str(form.get("workDescription3")))
              work.write("\n\n")
        work.close()

        with open("skill.txt", "w") as skills:
            skills.write("\n")
            skills.write(str(form.get("skills")))
            skills.write("\n\n")
        skills.close()

        createPDF()
        file = open("resume.pdf", "rb")
        thisFile = ResumeList(name=file.name, resume=file.read(), user_id=current_user.id)
        db.session.add(thisFile)
        db.session.commit()
    return redirect(url_for('dashboard'))


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            flash('Account already exists, please try again.')
        else:
            hashed_password = form.password.data
            user = User(username=form.username.data,
                        email=form.email.data,
                        password=hashed_password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('dashboard'))
    return render_template('register.html', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if form.password.data == user.password:
                login_user(user, remember=form.remember.data)
                return redirect(url_for('dashboard'))
        flash('Incorrect username or password, please try again.')
    return render_template('login.html', form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/dashboard')
@login_required
def dashboard():
    resumes = ResumeList.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', resumes=resumes, name=current_user.username)


@app.route('/questionnaire', methods=['GET', 'POST'])
@login_required
def questionnaire():
    form = QuestionnaireForm()

    return render_template('questionnaire.html', form=form)


@app.route("/upload", methods=["GET", "POST"])
@login_required
def upload():
    if request.method == "POST":
        file = request.files['inputFile']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        else:
            thisFile = ResumeList(name=file.filename, resume=file.read(), user_id=current_user.id)
            db.session.add(thisFile)
            db.session.commit()
            return redirect(url_for("dashboard"))
    return render_template("upload.html")


@app.route('/selection')
@login_required
def selection():
    return render_template('selection.html')


@app.route('/download<id>')
@login_required
def download(id):
    file_data = ResumeList.query.filter_by(id=id).first()
    return send_file(BytesIO(file_data.resume), attachment_filename=file_data.name, as_attachment=True)


@app.route('/view<id>')
@login_required
def view(id):
    resume = ResumeList.query.filter_by(id=id).first()
    return send_file(BytesIO(resume.resume), attachment_filename=resume.name)


@app.route('/delete<id>')
@login_required
def delete(id):
    ResumeList.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for("dashboard"))


@app.route('/temp')
def temp():
    return render_template('temp1.html')


if __name__ == '__main__':
    app.run(debug=True)
