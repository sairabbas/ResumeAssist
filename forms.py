from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Optional

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Rememeber Me')
    submit = SubmitField('Sign In')

#TO TEST ENCODE DECODE
class Test(FlaskForm):
    schoolName = StringField('School Name', validators=[DataRequired(), Length(min=3, max=40)])
    schoolDegree = StringField('School Degree', validators=[DataRequired(), Length(min=10, max=40)])
    schoolGPA = StringField('School GPA', validators=[DataRequired(), Length(min=1, max=6)])
    schoolStartDate = StringField('Start Date', validators=[DataRequired(), Length(min=3, max=40)])
    schoolEndDate = StringField('End Date', validators=[DataRequired(), Length(min=3, max=40)])


class QuestionnaireForm(FlaskForm):
    userName = StringField('Your Full Name', validators=[DataRequired(), Length(min=3, max=40)])
    userPhone = StringField('Your Phone Number xxx.xxx.xxxx', validators=[DataRequired(), Length(min=12, max=12)])
    userEmail = StringField('Your Email', validators=[DataRequired(), Length(min=3, max=40)])
    userPortfolio = StringField('Your Porfolio Site', validators=[Length(min=3, max=40)])

    schoolName = StringField('School Name', validators=[DataRequired(), Length(min=3, max=40)])
    schoolDegree = StringField('School Degree', validators=[DataRequired(), Length(min=3, max=40)])
    schoolGPA = StringField('School GPA', validators=[DataRequired(), Length(min=1, max=6)])
    schoolStartDate = StringField('Start Date', validators=[DataRequired(), Length(min=3, max=40)])
    schoolEndDate = StringField('End Date', validators=[DataRequired(), Length(min=3, max=40)])
    schoolCourses = StringField('Relevant Coursework', validators=[DataRequired(), Length(min=3, max=120)])

    projectTitle = StringField('Project Title', validators=[DataRequired(), Length(min=3, max=40)])
    projectTech = StringField('Technology used For Project', validators=[DataRequired(), Length(min=3, max=40)])
    projectDescription1 = StringField('Project Description:', validators=[DataRequired(), Length(min=10, max=500)])
    projectDescription11 = StringField('Project Description:', validators=[DataRequired(), Length(min=10, max=500)])
    projectDescription111 = StringField('Project Description:', validators=[DataRequired(), Length(min=10, max=500)])
    projectTime = StringField('Time Frame (Start - End)', validators=[DataRequired(), Length(min=3, max=40)])

    projectTitle2 = StringField('Project Title ', validators=[Optional()])
    projectTech2 = StringField('Technology used For Project', validators=[Optional(), Length(min=3, max=40)])
    projectDescription2 = StringField('Project Description:', validators=[DataRequired(), Length(min=10, max=500)])
    projectDescription22 = StringField('Project Description:', validators=[DataRequired(), Length(min=10, max=500)])
    projectDescription222 = StringField('Project Description:', validators=[DataRequired(), Length(min=10, max=500)])
    projectTime2 = StringField('Time Frame (Start - End)')

    projectTitle3 = StringField('Project Title')
    projectTech3 = StringField('Technology used For Project', validators=[Optional(), Length(min=3, max=40)])
    projectDescription3 = StringField('Project Description:', validators=[DataRequired(), Length(min=10, max=500)])
    projectDescription33 = StringField('Project Description:', validators=[DataRequired(), Length(min=10, max=500)])
    projectDescription333 = StringField('Project Description:', validators=[DataRequired(), Length(min=10, max=500)])
    projectTime3 = StringField('Time Frame (Start - End)')

    workTitle = StringField('Work title', validators=[DataRequired(), Length(min=3, max=40)])
    workCompany = StringField("Company", validators=[DataRequired(), Length(min=3, max=40)])
    workStartDate = StringField('Work Start Date', validators=[DataRequired(), Length(min=3, max=40)])
    workEndDate = StringField('Work End Date', validators=[DataRequired(), Length(min=3, max=40)])
    workDescription1 = StringField('Work Description:', validators=[DataRequired(), Length(min=10, max=100)])
    workDescription11 = StringField('Work Description:', validators=[DataRequired(), Length(min=10, max=100)])
    workDescription111 = StringField('Work Description:', validators=[DataRequired(), Length(min=10, max=100)])

    workTitle2 = StringField('Work title', validators=[Optional()])
    workCompany2 = StringField("Company", validators=[Optional()])
    workStartDate2 = StringField('Work Start Date', validators=[Optional()])
    workEndDate2 = StringField('Work End Date', validators=[Optional()])
    workDescription2 = StringField('Work Description:', validators=[DataRequired(), Length(min=10, max=100)])
    workDescription22 = StringField('Work Description:', validators=[DataRequired(), Length(min=10, max=100)])
    workDescription222 = StringField('Work Description:', validators=[DataRequired(), Length(min=10, max=100)])

    workTitle3 = StringField('Work title', validators=[Optional()])
    workCompany3 = StringField("Company", validators=[Optional()])
    workStartDate3 = StringField('Work Start Date', validators=[Optional()])
    workEndDate3 = StringField('Work End Date', validators=[Optional()])
    workDescription3 = StringField('Work Description:', validators=[DataRequired(), Length(min=10, max=100)])
    workDescription33 = StringField('Work Description:', validators=[DataRequired(), Length(min=10, max=100)])
    workDescription333 = StringField('Work Description:', validators=[DataRequired(), Length(min=10, max=100)])

    skills = StringField('Skills or Technologies you Know', validators=[DataRequired(), Length(min=3, max=500)])

    # submit = SubtmitField('Submit')
