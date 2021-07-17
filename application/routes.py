from application import app
from application import connect_to_monogodb
from flask import render_template, request


@app.route("/")
def index():
    return render_template("hotelIndex.html")


@app.route('/Gallery')
def Gallery():
    return render_template('Gallery.html')

@app.route('/services')
def services():
    return render_template('services.html')



@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/getBookingDetials', methods=['GET', 'POST'])
def getBookingDetials():
    if request.method == 'POST':
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        country= request.form.get('country')
        Email=request.form.get('Email')
        PhoneNumber=request.form.get('PhoneNumber')
        No_of_adult= request.form.get('No_of_adult')
        No_of_kids = request.form.get('No_of_kids')
        CheckIn = request.form.get('CheckIn')
        CheckOut = request.form.get('CheckOut')
        #result =
        '''  <h1>First Name : {}<h1>
                              <h1>Last Name : {}<h1> 
                              <h1>country: {}<h1>
                              <h1>email : {}<h1>
                              <h1>tel: {}<h1>
                              <h1>Adult : {}<h1>
                              <h1> Kids : {}<h1>
                              <h1> CheckIn : {}<h1>
                              <h1> CheckOut : {}<h1>'''

    #return result.format(firstname, lastname,country,Email,PhoneNumber,No_of_adult, No_of_kids,CheckIn,CheckOut)

    db = connect_to_monogodb()
    print(db.list_collection_names())
    cBookingDetials = db["BookingDetails"]

    cBookingDetials.insert({'firstname':firstname,'lastname':lastname,'country':country,'Email':Email,'PhoneNumber':PhoneNumber,
                            'No_of_adult':No_of_adult,'No_of_kids':No_of_kids,'CheckIn':CheckIn,'CheckOut':CheckOut})

    results = cBookingDetials.find()
    print(results)
    for row in results:
        print(row)
    message="Booking successfully complete"

    return render_template('hotelIndex.html',message=message)

@app.route('/booking')
def booking():
    return render_template('booking2.html')  # Using render function from flask