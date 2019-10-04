from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.models import Address
from app.forms import NewAddressForm, DeleteAddressForm, CityStateFromZipForm
import requests
import untangle

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

@app.route('/addresses/<int:address_id>/delete', methods=['POST'])
def delete_address(address_id):
    form = DeleteAddressForm()
    address = Address.query.get_or_404(address_id)
    db.session.delete(address)
    db.session.commit()
    return redirect(url_for('addresses_index'))

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

@app.route('/city_state_lookup_by_zip', methods=['GET', 'POST'])
def city_state_lookup_by_zip():
    form = CityStateFromZipForm()
    if form.validate_on_submit():
         # Implement a zipcodes table here to lookup in DB prior to making API call
        response = requests.get('http://production.shippingapis.com/ShippingAPITest.dll?API=CityStateLookup&XML=<CityStateLookupRequest USERID="544TURIN2145"><ZipCode ID= "0"><Zip5>{}</Zip5></ZipCode></CityStateLookupRequest>'.format(form.zip.data))
        obj = untangle.parse(response.content.decode("utf-8"))
        city = obj.CityStateLookupResponse.ZipCode.City.cdata
        state_abbreve = obj.CityStateLookupResponse.ZipCode.State.cdata
        zip = form.zip.data
        flash('{} is a zipcode in {}, {}.'.format(form.zip.data, city, state_abbreve))
    return render_template('city_state_lookup_by_zip.html', title="City/State Lookup by Zip", form=form)
