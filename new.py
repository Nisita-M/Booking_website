from flask import Flask,render_template,request
from pymongo import MongoClient as conns
import certifi


app = Flask(__name__)
conn = conns("mongodb+srv://admin:admin@nitmongodb.xmpou3t.mongodb.net/?retryWrites=true&w=majority&appName=nitmongoDB&ssl_cert_reqs=CERT_NONE",tlsCAFile=certifi.where())
db =  conn['NITT']
coll=db['Bookings']
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/admin')
def admin():
  return render_template('admin.html')

@app.route('/book',methods = ['GET','POST'])
def book():
  if request.method== 'POST':
    hd = {
      'name':request.form.get('name'),
      'hotel':request.form.get('hotel'),
      'phone':request.form.get('phone'),
      'ppn': int(request.form.get('ppn')),
      'nop':int(request.form.get('nop'))

      }
    hotelData = coll.find_one({'name': hd['name']})
    total_price =(int(hotelData['ppn']) * int ({hd['ppn']}) ) + (( int ({hd['nop']}) - int (hotelData['nop']) * 200 ))
@app.route('/addHotel', methods = ['GET','POST'])
def addHotel():
  if request.method=='POST':
    hd = {
      'name':request.form.get('name'),
      'city':request.form.get('loc'),
      'phone':request.form.get('phone'),
      'ppn': int(request.form.get('ppn')),
      'nop':int(request.form.get('nop'))

      }
    coll.insert_one(hd)
    print(' hotel data inserted')
  return render_template('addHotel.html')

@app.route('/viewBookings')
def viewBooking():
  return render_template('viewBookings.html',bookings=coll.find())


if __name__ == '__main__':
  app.run(debug=True,port=4000)
