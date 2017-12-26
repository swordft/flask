from flask.ext.wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required
from flask import Flask,redirect,render_template
app = Flask(__name__)
app.config['SECRET_KEY'] = 'xiaofang'

class NameForm(Form):
    name = StringField('What is your name?',validators=[Required()])
    submit = SubmitField('Submit')

@app.route('/form',methods=['GET','POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('form.html',form=form,name=name)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9092,debug=True)
