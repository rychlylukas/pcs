from flask import Blueprint, render_template
from .forms import formulartest
from .views import blueprint

@blueprint.route('/vypis_rychly', methods=['GET'])
def Vypis_rychly():
    pole=[[0,1], [2,3], [20,30]]
    pole[0][1]=pole[0][1]+1
    return render_template("public/vypis_rychly.tmpl", data = pole)

@blueprint.route('/formular_rychly', methods=['GET', "POST"])
def formularrychly():
    form=formulartest()
    if form.validate_on_submit():
        return str(form.a.data * form.b.data)
    return render_template("public/formularrychly.tmpl", form = form)
