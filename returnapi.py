from flask import *
from orderreturn import return_create


app= Flask(__name__)

@app.route('/')
def hello():
    return "Hello from OrderReturn !"

@app.route('/orderreturn',methods=['POST'])
def get_orderreturn():
    address= request.form.get('address')
    city= request.form.get('city')
    state= request.form.get('state')
    zipc= request.form.get('zip')

    customer_id= request.form.get('customer_id')
    order_id= request.form.get('order_id')

    address_comp = address + " " + city + " " + state + " " + zipc
    print(address_comp)

    orderreturnid=return_create(address_comp,customer_id, order_id)

    #return jsonify({'Order Id': orderreturnid})
    return redirect('http://yourservername/return_success.html?orderid='+str(orderreturnid))

if __name__== '__main__':
    app.run(debug=True,host='0.0.0.0')
