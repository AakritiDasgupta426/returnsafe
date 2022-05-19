import requests
import mysql.connector
import json

def return_create(address,customer_id,order_id):
    print("This is a test")
    maxreturnid = 0
    #create a connection to the database
    cnx = mysql.connector.connect(user='xxxx', password='xxxx',
                              host='yourservername',
                              database='dbname')
    cursor_outer = cnx.cursor()
    print('Got to step 1')

    #find maximum return id

    query_outer= ("select max(returnid) from orderreturn ")
    cursor_outer.execute(query_outer)

    for (returnid) in cursor_outer:
        maxreturnid = max(returnid)
        print('Max Retrun Id: ' + str(maxreturnid))
    cursor_outer.close()

    # add a new return order to the system
    add_return= ("insert into orderreturn"
                       "(returnid,returnorderid, customerid, address, completed,employeeid)"
                       "VALUES(%(return_id)s, %(return_order_id)s, %(customer_id)s, %(address_val)s,%(completed_val)s,%(employee_id)s)")

    return_data = {
            'return_id': maxreturnid + 1,
            'return_order_id': order_id,
            'customer_id': customer_id ,
            'address_val': address,
            'completed_val': 'N',
            'employee_id': 2001
            }

    cursor = cnx.cursor()
    cursor.execute(add_return,return_data)
    cnx.commit()
    cursor.close()

    return maxreturnid + 1
