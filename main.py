from flask import Flask, jsonify, request
from handler.company import CompanyHandler
from handler.consumer import ConsumerHandler
from handler.orders import OrdersHandler
from handler.paymethod import PayMethodHandler
# from handler.reservation import ReservationHandler
# from handler.resources import ResourceHandler
# from handler.supplier import SupplierHandler
# from handler.systemadmin import PartHandler
# from handler.users import UserHandler
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

@app.route('/DSRLapp/company', methods=['GET', 'POST'])
def getAllCompany():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return CompanyHandler().insertCompanyJson(request.json)
    else:
        if not request.args:
            return CompanyHandler().getAllCompany()
        else:
            return CompanyHandler().searchCompany(request.args)


@app.route('/DSRLapp/company/<int:compid>', methods=['GET', 'PUT', 'DELETE'])
def getCompanyById(compid):
    if request.method == 'GET':
        return CompanyHandler().getCompanyById(compid)
    elif request.method == 'PUT':
        return CompanyHandler().updateCompany(compid, request.json)
    elif request.method == 'DELETE':
        return CompanyHandler().deleteCompany(compid)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/DSRLapp/company/<int:compid>/consumer')
def getConsumerByCompanyId(compid):
    return CompanyHandler().getConsumerByCompanyId(compid)


@app.route('/PartDSRLappApp/company/<int:compid>/resources')
def getResourcesByCompanyId(compid):
    return CompanyHandler().getResourcesByCompanyId(compid)


@app.route('/DSRLapp/company/<int:compid>/supplier')
def getSupplierByCompanyId(compid):
    return CompanyHandler().getSupplierByCompanyId(compid)


# Consumer

@app.route('/DSRLapp/consumer', methods=['GET', 'POST'])
def getAllConsumer():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return ConsumerHandler().insertConsumerJson(request.json)
    else:
        if not request.args:
            return ConsumerHandler().getAllConsumer()
        else:
            return ConsumerHandler().searchConsumer(request.args)


@app.route('/DSRLapp/consumer/<int:consid>', methods=['GET', 'PUT', 'DELETE'])
def getCConsumerById(consid):
    if request.method == 'GET':
        return ConsumerHandler().getConsumerById(consid)
    elif request.method == 'PUT':
        return ConsumerHandler().updateConsumer(consid, request.form)
    elif request.method == 'DELETE':
        return ConsumerHandler().deleteConsumer(consid)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/DSRLapp/consumer/<int:consid>/order')
def getOrderByConsumerId(consid):
    return ConsumerHandler().getOrdersByConsumerId(consid)


@app.route('/DSRLapp/consumer/<int:consid>/paymethod')
def getPayMethodByConsumerId(consid):
    return ConsumerHandler().getPayMethodByConsumerId(consid)


@app.route('/DSRLapp/consumer/<int:consid>/reservation')
def getReservationByConsumerId(consid):
    return ConsumerHandler().getReservationByConsumerId(consid)


@app.route('/DSRLapp/consumer/<int:consid>/resources')
def getResourcesByConsumerId(consid):
    return ConsumerHandler().getResourcesByConsumerId(consid)


# Order

@app.route('/DSRLapp/order', methods=['GET', 'POST'])
def getAllOrder():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return OrdersHandler().insertOrdersJson(request.json)
    else:
        if not request.args:
            return OrdersHandler().getAllOrders()
        else:
            return OrdersHandler().searchOrders(request.args)


@app.route('/DSRLapp/order/<int:odid>', methods=['GET', 'PUT', 'DELETE'])
def getOrderById(odid):
    if request.method == 'GET':
        return OrdersHandler().getOrdersById(odid)
    elif request.method == 'PUT':
        return OrdersHandler().updateOrders(odid, request.form)
    elif request.method == 'DELETE':
        return OrdersHandler().deleteOrders(odid)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/DSRLapp/order/<int:odid>/consumer')
def getConsumerByOrderId(odid):
    return OrdersHandler().getConsumerByOrdersId(odid)


@app.route('/DSRLapp/order/<int:odid>/reservation')
def getReservationByOrderId(odid):
    return OrdersHandler().getReservationByOrdersId(odid)


@app.route('/DSRLapp/order/<int:odid>/supplier')
def getSupplierByOrderId(odid):
    return OrdersHandler().getSupplierByOrdersId(odid)


# Payment

@app.route('/DSRLapp/paymethod', methods=['GET', 'POST'])
def getAllPayMethod():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return PayMethodHandler().insertPayMethodJson(request.json)
    else:
        if not request.args:
            return PayMethodHandler().getAllPayMethod()
        else:
            return PayMethodHandler().searchPayMethod(request.args)


@app.route('/DSRLapp/paymethod/<int:pmid>', methods=['GET', 'PUT', 'DELETE'])
def getPayMethodById(pmid):
    if request.method == 'GET':
        return PayMethodHandler().getPayMethodById(pmid)
    elif request.method == 'PUT':
        return PayMethodHandler().updatePayMethod(pmid, request.form)
    elif request.method == 'DELETE':
        return PayMethodHandler().deletePayMethod(pmid)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/DSRLapp/paymethod/<int:pmid>/consumer')
def getConsumerByPayMethodId(pmid):
    return PayMethodHandler().getConsumerByPayMethodId(pmid)


@app.route('/DSRLapp/paymethod/<int:pmid>/supplier')
def getSupplierByPayMethodId(pmid):
    return PayMethodHandler().getSupplierByPayMethodId(pmid)


# Reservations

@app.route('/DSRLapp/reservations', methods=['GET', 'POST'])
def getAllReservations():
    if request.method == 'POST':
        # return print("REQUEST: ", request.json)
        return jsonify('ReservationsHandler().insertReservationsJson(request.json)'), 201
    else:
        if not request.args:
            return jsonify("ReservationsHandler().getAllReservations()"), 200
        else:
            return jsonify('ReservationsHandler().searchReservations(request.args)'), 200


@app.route('/DSRLapp/reservations/<int:resid>', methods=['GET', 'PUT', 'DELETE'])
def getReservationsById(resid):
    if request.method == 'GET':
        return jsonify('ReservationsHandler().getReservationsById(resid)'), 200
    elif request.method == 'PUT':
        return jsonify('ReservationsHandler().updateReservations(resid, request.form)'), 200
    elif request.method == 'DELETE':
        return jsonify('ReservationsHandler().deleteReservations(resid)'), 200
    else:
        return jsonify('jsonify(Error="Method not allowed."), 405'), 405


@app.route('/DSRLapp/reservations/<int:resid>/resources')
def getResourcesByReservationId(resid):
    return jsonify('ReservationsHandler().getResourcesByReservationId(resid)'), 200


# Resources

@app.route('/DSRLapp/resources', methods=['GET', 'POST'])
def getAllResources():
    if request.method == 'POST':
        # return print("REQUEST: ", request.json)
        return jsonify('ResourcesHandler().insertResourcesJson(request.json)'), 201
    else:
        if not request.args:
            return jsonify("ResourcesHandler().getAllResources()"), 200
        else:
            return jsonify('ResourcesHandler().searchResources(request.args)'), 200


@app.route('/DSRLapp/resources/<int:rid>', methods=['GET', 'PUT', 'DELETE'])
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

@app.route('/DSRLapp/supplier', methods=['GET', 'POST'])
def getAllSuppliers():
    if request.method == 'POST':
        # return print("REQUEST: ", request.json)
        return jsonify('SupplierHandler().insertSupplierJson(request.json)'), 201
    else:
        if not request.args:
            return jsonify("SupplierHandler().getAllSupplier()"), 200
        else:
            return jsonify('SupplierHandler().searchSupplier(request.args)'), 200


@app.route('/DSRLapp/supplier/<int:sid>', methods=['GET', 'PUT', 'DELETE'])
def getSupplierById(sid):
    if request.method == 'GET':
        return jsonify('SupplierHandler().getSupplierById(sid)'), 200
    elif request.method == 'PUT':
        return jsonify('SupplierHandler().updateSupplier(sid, request.form)'), 200
    elif request.method == 'DELETE':
        return jsonify('SupplierHandler().deleteSupplier(sid)'), 200
    else:
        return jsonify('jsonify(Error="Method not allowed."), 405'), 405


@app.route('/DSRLapp/supplier/<int:sid>/company')
def getCompanyBySupplierId(sid):
    return jsonify('SupplierHandler().getCompanyBySupplierId(sid)'), 200


@app.route('/DSRLapp/supplier/<int:sid>/resource')
def getResourcesBySupplierId(sid):
    return jsonify('SupplierHandler().getResourcesBySupplierId(sid)'), 200


# System Admin

@app.route('/DSRLapp/systemadmin', methods=['GET', 'POST'])
def getAllSysAdm():
    if request.method == 'POST':
        # return print("REQUEST: ", request.json)
        return jsonify('SystemadminHandler().insertSystemadminJson(request.json)'), 201
    else:
        if not request.args:
            return jsonify("SystemadminHandler().getAllSystemadmin()"), 200
        else:
            return jsonify('SystemadminHandler().searchSystemadmin(request.args)'), 200


@app.route('/DSRLapp/systemadmin/<int:said>', methods=['GET', 'PUT', 'DELETE'])
def getSysAdmById(said):
    if request.method == 'GET':
        return jsonify('SystemadminHandler().getSystemadminById(said)'), 200
    elif request.method == 'PUT':
        return jsonify('SystemadminHandler().updateSystemadmin(said, request.form)'), 200
    elif request.method == 'DELETE':
        return jsonify('SystemadminHandler().deleteSystemadmin(said)'), 200
    else:
        return jsonify('jsonify(Error="Method not allowed."), 405'), 405


@app.route('/DSRLapp/systemadmin/<int:said>/user')
def getUserBySysAdmId(said):
    return jsonify('SystemadminHandler().getUserBySysAdmId(sid)'), 200


# User

@app.route('/DSRLapp/user', methods=['GET', 'POST'])
def getAllUser():
    if request.method == 'POST':
        # return print("REQUEST: ", request.json)
        return jsonify('UserHandler().insertUserJson(request.json)'), 201
    else:
        if not request.args:
            return jsonify("UserHandler().getAllUser()"), 200
        else:
            return jsonify('UserHandler().searchUser(request.args)'), 200


@app.route('/DSRLapp/user/<int:uid>', methods=['GET', 'PUT', 'DELETE'])
def getUserById(uid):
    if request.method == 'GET':
        return jsonify('UserHandler().getUserById(uid)'), 200
    elif request.method == 'PUT':
        return jsonify('UserHandler().updateUser(uid, request.form)'), 200
    elif request.method == 'DELETE':
        return jsonify('UserHandler().deleteUser(uid)'), 200
    else:
        return jsonify('jsonify(Error="Method not allowed."), 405'), 405


@app.route('/DSRLapp/user/<int:uid>/consumer')
def getConsumerByUserId(uid):
    return jsonify('UserHandler().getConsumerByUserId(uid)'), 200


@app.route('/DSRLapp/user/<int:uid>/supplier')
def getSupplierByUserId(uid):
    return jsonify('UserHandler().getSupplierByUserId(uid)'), 200


@app.route('/DSRLapp/user/<int:uid>/SysAdm')
def getSysAdmByUserId(uid):
    return jsonify('UserHandler().getSysAdmByUserId(uid)'), 200


if __name__ == '__main__':
    app.run()
