from flask import render_template, flash, redirect, url_for
from app import app, db
from app.models import Address
from app.forms import NewAddressForm

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/addresses')
def addresses_index():
    addresses = Address.query.all()
    return render_template('addresses_index.html', addresses=addresses)

@app.route('/addresses/<int:address_id>')
def show_address(address_id):
    address = Address.query.get_or_404(address_id)
    return  render_template('show_address.html', address=address)

@app.route('/addresses/new', methods=['GET', 'POST'])
def new_address():
    form = NewAddressForm()
    if form.validate_on_submit():
        address = Address(name=form.name.data, address=form.address.data, city=form.city.data, state=form.state.data, zip=form.zip.data)
        db.session.add(address)
        db.session.commit()
        flash('{} has been added to your addresses.'.format(form.address.data))
        return redirect(url_for('addresses_index'))
    return render_template('new_address.html', title="New Address", form=form)
