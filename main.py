from flask import Flask, jsonify, request
# from handler.company import CompanyHandler
# from handler.consumer import ConsumerHandler
# from handler.order import OrderHandler
# from handler.paymethod import PayMethodHandler
# from handler.reservations import ReservationHandler
# from handler.resources import ResourceHandler
# from handler.supplier import SupplierHandler
# from handler.systemadmin import PartHandler
# from handler.user import UserHandler
# Import Cross-Origin Resource Sharing to enable
# services on other ports on this machine or on other
# machines to access this app
from flask_cors import CORS, cross_origin

# Activate
app = Flask(__name__)
# Apply CORS to this app
CORS(app)


@app.route('/')
def greeting():
    return 'Greeting message. App running!'


# Company

@app.route('/PartApp/company', methods=['GET', 'POST'])
def getAllCompany():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return jsonify('CompanyHandler().insertCompanyJson(request.json)'), 201
    else:
        if not request.args:
            return jsonify('CompanyHandler().getAllCompany()'), 200
        else:
            return jsonify('CompanyHandler().searchCompanies(request.args)'), 200


@app.route('/PartApp/company/<int:compid>', methods=['GET', 'PUT', 'DELETE'])
def getCompanyById(compid):
    if request.method == 'GET':
        return jsonify('CompanyHandler().getCompanyById(compid)'), 200
    elif request.method == 'PUT':
        return jsonify('CompanyHandler().updateCompany(compid, request.form)'), 200
    elif request.method == 'DELETE':
        return jsonify('CompanyHandler().deleteCompany(compid)'), 200
    else:
        return jsonify(Error="Method not allowed."), 405

# Consumer

@app.route('/PartApp/consumer', methods=['GET', 'POST'])
def getAllConsumer():
    if request.method == 'POST':
        # return print("REQUEST: ", request.json)
        return jsonify('ConsumerHandler().insertConsumerJson(request.json)'), 201
    else:
        if not request.args:
            return jsonify("ConsumerHandler().getAllConsumer()"), 200
        else:
            return jsonify('ConsumerHandler().searchConsumer(request.args)'), 200


@app.route('/PartApp/consumer/<int:consid>', methods=['GET', 'PUT', 'DELETE'])
def getCConsumerById(consid):
    if request.method == 'GET':
        return jsonify('ConsumerHandler().getConsumerById(consid)'), 200
    elif request.method == 'PUT':
        return jsonify('ConsumerHandler().updateConsumer(consid, request.form)'), 200
    elif request.method == 'DELETE':
        return jsonify('ConsumerHandler().deleteConsumer(consid)'), 200
    else:
        return jsonify('jsonify(Error="Method not allowed."), 405'), 405


@app.route('/PartApp/consumer/<int:consid>/order')
def getOrderByConsumerId(consid):
    return jsonify('ConsumerHandler().getOrderByConsumerId(consid)'), 200


@app.route('/PartApp/consumer/<int:consid>/paymethod')
def getPayMethodByConsumerId(consid):
    return jsonify('ConsumerHandler().getPayMethodByConsumerId(consid)'), 200


@app.route('/PartApp/consumer/<int:consid>/reservation')
def getReservationByConsumerId(consid):
    return jsonify('ConsumerHandler().getReservationByConsumerId(consid)'), 200


# Order

@app.route('/PartApp/order', methods=['GET', 'POST'])
def getAllOrder():
    if request.method == 'POST':
        # return print("REQUEST: ", request.json)
        return jsonify('OrderHandler().insertOrderJson(request.json)'), 201
    else:
        if not request.args:
            return jsonify("OrderHandler().getAllOrder()"), 200
        else:
            return jsonify('OrderHandler().searchOrder(request.args)'), 200


@app.route('/PartApp/order/<int:oid>', methods=['GET', 'PUT', 'DELETE'])
def getOrderById(oid):
    if request.method == 'GET':
        return jsonify('OrderHandler().getOrderById(oid)'), 200
    elif request.method == 'PUT':
        return jsonify('OrderHandler().updateOrder(oid, request.form)'), 200
    elif request.method == 'DELETE':
        return jsonify('OrderHandler().deleteOrder(oid)'), 200
    else:
        return jsonify('jsonify(Error="Method not allowed."), 405'), 405


@app.route('/PartApp/order/<int:oid>/resources')
def getResourcesByOrderId(oid):
    return jsonify('OrderHandler().getSupplierByResourcesId(oid)'), 200


# Payment

@app.route('/PartApp/paymethod', methods=['GET', 'POST'])
def getAllPayMethod():
    if request.method == 'POST':
        # return print("REQUEST: ", request.json)
        return jsonify('PaymethodHandler().insertPaymethodJson(request.json)'), 201
    else:
        if not request.args:
            return jsonify("PaymethodHandler().getAllPaymethod()"), 200
        else:
            return jsonify('PaymethodHandler().searchPaymethod(request.args)'), 200


@app.route('/PartApp/paymethod/<int:pmid>', methods=['GET', 'PUT', 'DELETE'])
def getPayMethodById(pmid):
    if request.method == 'GET':
        return jsonify('PaymethodHandler().getPayMethodById(oid)'), 200
    elif request.method == 'PUT':
        return jsonify('PaymethodHandler().updatePaymethod(oid, request.form)'), 200
    elif request.method == 'DELETE':
        return jsonify('PaymethodHandler().deletePaymethod(oid)'), 200
    else:
        return jsonify('jsonify(Error="Method not allowed."), 405'), 405


@app.route('/PartApp/paymethod/<int:pmid>/order')
def getOrderByPayMethodId(pmid):
    return jsonify('PaymethodHandler().getOrderByPayMethodId(pmid)'), 200


# Reservations

@app.route('/PartApp/reservations', methods=['GET', 'POST'])
def getAllReservations():
    if request.method == 'POST':
        # return print("REQUEST: ", request.json)
        return jsonify('ReservationsHandler().insertReservationsJson(request.json)'), 201
    else:
        if not request.args:
            return jsonify("ReservationsHandler().getAllReservations()"), 200
        else:
            return jsonify('ReservationsHandler().searchReservations(request.args)'), 200


@app.route('/PartApp/reservations/<int:resid>', methods=['GET', 'PUT', 'DELETE'])
def getReservationsById(resid):
    if request.method == 'GET':
        return jsonify('ReservationsHandler().getReservationsById(resid)'), 200
    elif request.method == 'PUT':
        return jsonify('ReservationsHandler().updateReservations(resid, request.form)'), 200
    elif request.method == 'DELETE':
        return jsonify('ReservationsHandler().deleteReservations(resid)'), 200
    else:
        return jsonify('jsonify(Error="Method not allowed."), 405'), 405


@app.route('/PartApp/reservations/<int:resid>/resources')
def getResourcesByReservationId(resid):
    return jsonify('ReservationsHandler().getResourcesByReservationId(resid)'), 200


# Resources

@app.route('/PartApp/resources', methods=['GET', 'POST'])
def getAllResources():
    if request.method == 'POST':
        # return print("REQUEST: ", request.json)
        return jsonify('ResourcesHandler().insertResourcesJson(request.json)'), 201
    else:
        if not request.args:
            return jsonify("ResourcesHandler().getAllResources()"), 200
        else:
            return jsonify('ResourcesHandler().searchResources(request.args)'), 200


@app.route('/PartApp/resources/<int:rid>', methods=['GET', 'PUT', 'DELETE'])
def getResourcesById(rid):
    if request.method == 'GET':
        return jsonify('ResourcesHandler().getResourcesById(rid)'), 200
    elif request.method == 'PUT':
        return jsonify('ResourcesHandler().updateResources(rid, request.form)'), 200
    elif request.method == 'DELETE':
        return jsonify('ResourcesHandler().deleteResources(rid)'), 200
    else:
        return jsonify('jsonify(Error="Method not allowed."), 405'), 405


# Supplier

@app.route('/PartApp/supplier', methods=['GET', 'POST'])
def getAllSuppliers():
    if request.method == 'POST':
        # return print("REQUEST: ", request.json)
        return jsonify('SupplierHandler().insertSupplierJson(request.json)'), 201
    else:
        if not request.args:
            return jsonify("SupplierHandler().getAllSupplier()"), 200
        else:
            return jsonify('SupplierHandler().searchSupplier(request.args)'), 200


@app.route('/PartApp/supplier/<int:sid>', methods=['GET', 'PUT', 'DELETE'])
def getSupplierById(sid):
    if request.method == 'GET':
        return jsonify('SupplierHandler().getSupplierById(sid)'), 200
    elif request.method == 'PUT':
        return jsonify('SupplierHandler().updateSupplier(sid, request.form)'), 200
    elif request.method == 'DELETE':
        return jsonify('SupplierHandler().deleteSupplier(sid)'), 200
    else:
        return jsonify('jsonify(Error="Method not allowed."), 405'), 405


@app.route('/PartApp/supplier/<int:sid>/company')
def getCompanyBySupplierId(sid):
    return jsonify('SupplierHandler().getCompanyBySupplierId(sid)'), 200


@app.route('/PartApp/supplier/<int:sid>/resource')
def getResourcesBySupplierId(sid):
    return jsonify('SupplierHandler().getResourcesBySupplierId(sid)'), 200


# System Admin

@app.route('/PartApp/systemadmin', methods=['GET', 'POST'])
def getAllSysAdm():
    if request.method == 'POST':
        # return print("REQUEST: ", request.json)
        return jsonify('SystemadminHandler().insertSystemadminJson(request.json)'), 201
    else:
        if not request.args:
            return jsonify("SystemadminHandler().getAllSystemadmin()"), 200
        else:
            return jsonify('SystemadminHandler().searchSystemadmin(request.args)'), 200


@app.route('/PartApp/systemadmin/<int:said>', methods=['GET', 'PUT', 'DELETE'])
def getSysAdmById(said):
    if request.method == 'GET':
        return jsonify('SystemadminHandler().getSystemadminById(said)'), 200
    elif request.method == 'PUT':
        return jsonify('SystemadminHandler().updateSystemadmin(said, request.form)'), 200
    elif request.method == 'DELETE':
        return jsonify('SystemadminHandler().deleteSystemadmin(said)'), 200
    else:
        return jsonify('jsonify(Error="Method not allowed."), 405'), 405


@app.route('/PartApp/systemadmin/<int:said>/user')
def getUserBySysAdmId(said):
    return jsonify('SystemadminHandler().getUserBySysAdmId(sid)'), 200


# User

@app.route('/PartApp/user', methods=['GET', 'POST'])
def getAllUser():
    if request.method == 'POST':
        # return print("REQUEST: ", request.json)
        return jsonify('UserHandler().insertUserJson(request.json)'), 201
    else:
        if not request.args:
            return jsonify("UserHandler().getAllUser()"), 200
        else:
            return jsonify('UserHandler().searchUser(request.args)'), 200


@app.route('/PartApp/user/<int:uid>', methods=['GET', 'PUT', 'DELETE'])
def getUserById(uid):
    if request.method == 'GET':
        return jsonify('UserHandler().getUserById(uid)'), 200
    elif request.method == 'PUT':
        return jsonify('UserHandler().updateUser(uid, request.form)'), 200
    elif request.method == 'DELETE':
        return jsonify('UserHandler().deleteUser(uid)'), 200
    else:
        return jsonify('jsonify(Error="Method not allowed."), 405'), 405


@app.route('/PartApp/user/<int:uid>/consumer')
def getConsumerByUserId(uid):
    return jsonify('UserHandler().getConsumerByUserId(uid)'), 200


@app.route('/PartApp/user/<int:uid>/supplier')
def getSupplierByUserId(uid):
    return jsonify('UserHandler().getSupplierByUserId(uid)'), 200


@app.route('/PartApp/user/<int:uid>/SysAdm')
def getSysAdmByUserId(uid):
    return jsonify('UserHandler().getSysAdmByUserId(uid)'), 200


if __name__ == '__main__':
    app.run()
