from flask import Flask,render_template,request
from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

FAI=Flask(__name__)


class Nameform(Form):
    name=StringField(validators=[DataRequired()])
    submit=SubmitField('submit')
@FAI.route('/web_form',methods=['GET','POST'])
def web_form():
    form=Nameform()
    if request.method=='POST':
        uf=Nameform(request.form)
        if uf.validate():
            return uf.data
    return render_template('web_form.html',form=form)

if __name__=='__main__':
    FAI.run(debug=True)