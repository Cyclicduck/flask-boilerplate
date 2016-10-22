from flask_wtf import Form
#<<<<<<< HEAD
from wtforms import TextField, PasswordField, IntegerField, StringField,BooleanField
#=======
#from wtforms import TextField, PasswordField
#from wtforms import StringField, BooleanField
#>>>>>>> af1add2edbfeab75cc5ec0756fb8e49fab9513ac
from wtforms.validators import DataRequired, EqualTo, Length

# Set your classes here.


class RegisterForm(Form):
    name = TextField(
        'Username', validators=[DataRequired(), Length(min=6, max=25)]
    )
    email = TextField(
        'Email', validators=[DataRequired(), Length(min=6, max=40)]
    )
    password = PasswordField(
        'Password', validators=[DataRequired(), Length(min=6, max=40)]
    )
    confirm = PasswordField(
        'Repeat Password',
        [DataRequired(),
        EqualTo('password', message='Passwords must match')]
    )


class LoginForm(Form):
    name = TextField('Username', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default = False)


class ForgotForm(Form):
    email = TextField(
        'Email', validators=[DataRequired(), Length(min=6, max=40)]
    )

class QuestionForm(Form):
    answer = IntegerField('Answer', [DataRequired()])
