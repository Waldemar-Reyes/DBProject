from flask import Flask, jsonify, request
# Import Cross-Origin Resource Sharing to enable
# services on other ports on this machine or on other
# machines to access this app
from flask_cors import CORS

from handler.company import CompanyHandler
from handler.consumer import ConsumerHandler
from handler.orders import OrdersHandler
from handler.paymethod import PayMethodHandler
# from handler.reservation import ReservationHandler
from handler.resources import ResourcesHandler
from handler.supplier import SupplierHandler
from handler.systemadmin import SysAdmHandler
from handler.users import UsersHandler

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


@app.route('/DSRLapp/consumer/<int:consid>/orders')
def getOrdersByConsumerId(consid):
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


# Orders

@app.route('/DSRLapp/orders', methods=['GET', 'POST'])
def getAllOrders():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return OrdersHandler().insertOrdersJson(request.json)
    else:
        if not request.args:
            return OrdersHandler().getAllOrders()
        else:
            return OrdersHandler().searchOrders(request.args)


@app.route('/DSRLapp/orders/<int:odid>', methods=['GET', 'PUT', 'DELETE'])
def getOrdersById(odid):
    if request.method == 'GET':
        return OrdersHandler().getOrdersById(odid)
    elif request.method == 'PUT':
        return OrdersHandler().updateOrders(odid, request.form)
    elif request.method == 'DELETE':
        return OrdersHandler().deleteOrders(odid)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/DSRLapp/orders/<int:odid>/consumer')
def getConsumerByOrdersId(odid):
    return OrdersHandler().getConsumerByOrdersId(odid)


@app.route('/DSRLapp/orders/<int:odid>/reservation')
def getReservationByOrdersId(odid):
    return OrdersHandler().getReservationByOrdersId(odid)


@app.route('/DSRLapp/orders/<int:odid>/supplier')
def getSupplierByOrdersId(odid):
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


# TODO May be deleted in near future
# Was not completely implemented for this test
#
# Reservation
#
# @app.route('/DSRLapp/reservations', methods=['GET', 'POST'])
# def getAllReservations():
#     if request.method == 'POST':
#         print("REQUEST: ", request.json)
#         return ReservationHandler().insertReservationJson(request.json)
#     else:
#         if not request.args:
#             return ReservationHandler().getAllReservation()
#         else:
#             return ReservationHandler().searchReservation(request.args)
#
#
# @app.route('/DSRLapp/reservations/<int:resid>', methods=['GET', 'PUT', 'DELETE'])
# def getReservationsById(resid):
#     if request.method == 'GET':
#         return ReservationHandler().getReservationById(resid)
#     elif request.method == 'PUT':
#         return ReservationHandler().updateReservation(resid, request.form)
#     elif request.method == 'DELETE':
#         return ReservationHandler().deleteReservation(resid)
#     else:
#         return jsonify(Error="Method not allowed."), 405
#
#
# @app.route('/DSRLapp/reservations/<int:resid>/resources')
# def getResourcesByReservationId(resid):
#     return ReservationHandler.getResourcesByReservationId(resid)


# Resources

@app.route('/DSRLapp/resources', methods=['GET', 'POST'])
def getAllResources():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return ResourcesHandler().insertResourcesJson(request.json)
    else:
        if not request.args:
            return ResourcesHandler().getAllResources()
        else:
            return ResourcesHandler().searchResources(request.args)


@app.route('/DSRLapp/resources/<int:rid>', methods=['GET', 'PUT', 'DELETE'])
def getResourcesById(rid):
    if request.method == 'GET':
        return ResourcesHandler().getResourcesById(rid)
    elif request.method == 'PUT':
        return ResourcesHandler().updateResources(rid, request.form)
    elif request.method == 'DELETE':
        return ResourcesHandler().deleteResources(rid)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/DSRLapp/resources/<int:rid>/company')
def getCompanyByResourcesId(rid):
    return ResourcesHandler().getCompanyByResourcesId(rid)


@app.route('/DSRLapp/resources/<int:rid>/consumer')
def getConsumerByResourcesId(rid):
    return ResourcesHandler().getConsumerByResourcesId(rid)


# Supplier

@app.route('/DSRLapp/supplier', methods=['GET', 'POST'])
def getAllSuppliers():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return SupplierHandler().insertSupplierJson(request.json)
    else:
        if not request.args:
            return SupplierHandler().getAllSupplier()
        else:
            return SupplierHandler().searchSupplier(request.args)


@app.route('/DSRLapp/supplier/<int:sid>', methods=['GET', 'PUT', 'DELETE'])
def getSupplierById(sid):
    if request.method == 'GET':
        return SupplierHandler().getSupplierById(sid)
    elif request.method == 'PUT':
        return SupplierHandler().updateSupplier(sid, request.form)
    elif request.method == 'DELETE':
        return SupplierHandler().deleteSupplier(sid)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/DSRLapp/supplier/<int:sid>/company')
def getCompanyBySupplierId(sid):
    return SupplierHandler().getCompanyBySupplierId(sid)


@app.route('/DSRLapp/supplier/<int:sid>/orders')
def getOrdersBySupplierId(sid):
    return SupplierHandler().getOrdersBySupplierId(sid)


@app.route('/DSRLapp/supplier/<int:sid>/paymethod')
def getPayMethodBySupplierId(sid):
    return SupplierHandler().getPayMethodBySupplierId(sid)


@app.route('/DSRLapp/supplier/<int:sid>/reservation')
def getReservationBySupplierId(sid):
    return SupplierHandler().getReservationBySupplierId(sid)


@app.route('/DSRLapp/supplier/<int:sid>/resources')
def getResourcesBySupplierId(sid):
    return SupplierHandler().getResourcesBySupplierId(sid)


# System Admin

@app.route('/DSRLapp/systemadmin', methods=['GET', 'POST'])
def getAllSysAdm():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return SysAdmHandler().insertSysAdmJson(request.json)
    else:
        if not request.args:
            return SysAdmHandler().getAllSysAdm()
        else:
            return SysAdmHandler().searchSysAdm(request.args)


@app.route('/DSRLapp/systemadmin/<int:said>', methods=['GET', 'PUT', 'DELETE'])
def getSysAdmById(said):
    if request.method == 'GET':
        return SysAdmHandler().getSysAdmById(said)
    elif request.method == 'PUT':
        return SysAdmHandler().updateSysAdm(said, request.form)
    elif request.method == 'DELETE':
        return SysAdmHandler().deleteSysAdm(said)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/DSRLapp/systemadmin/<int:said>/company')
def getCompanyBySysAdmId(said):
    return SysAdmHandler().getCompanyBySysAdmId(said)


@app.route('/DSRLapp/systemadmin/<int:said>/consumer')
def getConsumerBySysAdmId(said):
    return SysAdmHandler().getConsumerBySysAdmId(said)


@app.route('/DSRLapp/systemadmin/<int:said>/supplier')
def getSupplierBySysAdmId(said):
    return SysAdmHandler().getSupplierBySysAdmId(said)


@app.route('/DSRLapp/systemadmin/<int:said>/users')
def getUsersBySysAdmId(said):
    return SysAdmHandler().getUsersBySysAdmId(said)


# Users

@app.route('/DSRLapp/users', methods=['GET', 'POST'])
def getAllUsers():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return UsersHandler().insertUsersJson(request.json)
    else:
        if not request.args:
            return UsersHandler().getAllUsers()
        else:
            return UsersHandler().searchUsers(request.args)


@app.route('/DSRLapp/users/<int:uid>', methods=['GET', 'PUT', 'DELETE'])
def getUsersById(uid):
    if request.method == 'GET':
        return UsersHandler().getUsersById(uid)
    elif request.method == 'PUT':
        return UsersHandler().updateUsers(uid, request.form)
    elif request.method == 'DELETE':
        return UsersHandler().deleteUsers(uid)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/DSRLapp/users/<int:uid>/consumer')
def getConsumerByUsersId(uid):
    return UsersHandler().getConsumerByUsersId(uid)


@app.route('/DSRLapp/users/<int:uid>/supplier')
def getSupplierByUsersId(uid):
    return UsersHandler().getSupplierByUsersId(uid)


@app.route('/DSRLapp/users/<int:uid>/SysAdm')
def getSysAdmByUsersId(uid):
    return UsersHandler().getSysAdmByUsersId(uid)


if __name__ == '__main__':
    app.run()
