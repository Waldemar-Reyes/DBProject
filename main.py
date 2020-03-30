from flask import Flask, jsonify, request
from handler.systemadmin import PartHandler
from handler.supplier import SupplierHandler
# from handler.company import CompanyHandler
# from handler.consumer import ConsumerHandler
# from handler.order import OrderHandler
# from handler.paymethod import PayMethodHandler
# from handler.reservations import ReservationHandler
# from handler.resources import ResourceHandler
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


@app.route('/PartApp/parts', methods=['GET', 'POST'])
def getAllParts():
    if request.method == 'POST':
        # cambie a request.json pq el form no estaba bregando
        # parece q estaba poseido por satanas ...
        # DEBUG a ver q trae el json q manda el cliente con la nueva pieza
        print("REQUEST: ", request.json)
        return PartHandler().insertPartJson(request.json)
    else:
        if not request.args:
            return PartHandler().getAllCompany()
        else:
            return PartHandler().searchParts(request.args)


@app.route('/PartApp/parts/<int:pid>', methods=['GET', 'PUT', 'DELETE'])
def getPartById(pid):
    if request.method == 'GET':
        return PartHandler().getPartById(pid)
    elif request.method == 'PUT':
        return PartHandler().updatePart(pid, request.form)
    elif request.method == 'DELETE':
        return PartHandler().deletePart(pid)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/PartApp/parts/<int:pid>/suppliers')
def getSuppliersByPartId(pid):
    return PartHandler().getSuppliersByPartId(pid)


@app.route('/PartApp/suppliers', methods=['GET', 'POST'])
def getAllSuppliers():
    if request.method == 'POST':
        return SupplierHandler().insertSupplier(request.form)
    else:
        if not request.args:
            return SupplierHandler().getAllSuppliers()
        else:
            return SupplierHandler().searchSuppliers(request.args)


@app.route('/PartApp/suppliers/<int:sid>',
           methods=['GET', 'PUT', 'DELETE'])
def getSupplierById(sid):
    if request.method == 'GET':
        return SupplierHandler().getSupplierById(sid)
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass
    else:
        return jsonify(Error="Method not allowed"), 405


@app.route('/PartApp/suppliers/<int:sid>/parts')
def getPartsBySuplierId(sid):
    return SupplierHandler().getPartsBySupplierId(sid)


@app.route('/PartApp/parts/countbypartid')
def getCountByPartId():
    return PartHandler().getCountByPartId()


## Company

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


@app.route('/PartApp/company/<int:compid>/supplier')
def getSupplierByCompanyId(compid):
    return jsonify('CompanyHandler().getSupplierByCompanyId(compid)'), 200


@app.route('/PartApp/company/<int:compid>/consumer')
def getConsumerByCompanyId(compid):
    return jsonify('CompanyHandler().getConsumerByCompanyId(compid)'), 200


@app.route('/PartApp/company/<int:compid>/resources')
def getResourcesByCompanyId(compid):
    return jsonify('CompanyHandler().getResourcesByCompanyId(compid)'), 200

## Consumer

@app.route('/PartApp/consumer', methods=['GET', 'POST'])
def getAllConsumer():
    if request.method == 'POST':
        #return print("REQUEST: ", request.json)
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


@app.route('/PartApp/consumer/<int:consid>/resources')
def getResourcesByConsumerId(consid):
    return jsonify('ConsumerHandler().getResourcesByConsumerId(consid)'), 200


@app.route('/PartApp/consumer/<int:consid>/order')
def getOrderByConsumerId(consid):
    return jsonify('ConsumerHandler().getOrderByConsumerId(consid)'), 200


@app.route('/PartApp/consumer/<int:consid>/paymethod')
def getPayMethodByConsumerId(consid):
    return jsonify('ConsumerHandler().getPayMethodByConsumerId(consid)'), 200


@app.route('/PartApp/consumer/<int:consid>/reservation')
def getReservationByConsumerId(consid):
    return jsonify('ConsumerHandler().getReservationByConsumerId(consid)'), 200

## Order

@app.route('/PartApp/order', methods=['GET', 'POST'])
def getAllOrder():
    if request.method == 'POST':
        #return print("REQUEST: ", request.json)
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


@app.route('/PartApp/order/<int:oid>/supplier')
def getSupplierByOrderId(oid):
    return jsonify('OrderHandler().getSupplierByOrderId(oid)'), 200


@app.route('/PartApp/order/<int:oid>/consumer')
def getConsumerByOrderId(oid):
    return jsonify('OrderHandler().getConsumerByOrderId(oid)'), 200


@app.route('/PartApp/order/<int:oid>/reservation')
def getReservationByOrderId(oid):
    return jsonify('OrderHandler().getReservationByOrderId(oid)'), 200

## Payment

@app.route('/PartApp/paymethod', methods=['GET', 'POST'])
def getAllPayMethod():
    if request.method == 'POST':
        #return print("REQUEST: ", request.json)
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


@app.route('/PartApp/paymethod/<int:pmid>/supplier')
def getSupplierByPayMethodId(pmid):
    return jsonify('PaymethodHandler().getSupplierByPayMethodId(pmid)'), 200


@app.route('/PartApp/paymethod/<int:pmid>/consumer')
def getConsumerByPayMethodId(pmid):
    return jsonify('PaymethodHandler().getConsumerByPayMethodId(pmid)'), 200

## Reservations

@app.route('/PartApp/reservations', methods=['GET', 'POST'])
def getAllReservations():
    if request.method == 'POST':
        #return print("REQUEST: ", request.json)
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


@app.route('/PartApp/reservations/<int:resid>/order')
def getOrderByReservationsId(resid):
    return jsonify('ReservationsHandler().getOrderByReservationsId(resid)'), 200


@app.route('/PartApp/reservations/<int:resid>/supplier')
def getSupplierByReservationsId(resid):
    return jsonify('ReservationsHandler().getSupplierByReservationsId(resid)'), 200


@app.route('/PartApp/reservations/<int:resid>/consumer')
def getConsumerByReservationsId(resid):
    return jsonify('ReservationsHandler().getConsumerByReservationsId(resid)'), 200

## Resources

@app.route('/PartApp/resources', methods=['GET', 'POST'])
def getAllResources():
    if request.method == 'POST':
        #return print("REQUEST: ", request.json)
        return jsonify('ResourcesHandler().insertResourcesJson(request.json)'), 201
    else:
        if not request.args:
            return jsonify("ResourcesHandler().getAllResources()"), 200
        else:
            return jsonify('ResourcesHandler().searchResources(request.args)'), 200


@app.route('/PartApp/resources/<int:rid>', methods=['GET', 'PUT', 'DELETE'])
def getReservationsById(rid):
    if request.method == 'GET':
        return jsonify('ResourcesHandler().getResourcesById(rid)'), 200
    elif request.method == 'PUT':
        return jsonify('ResourcesHandler().updateResources(rid, request.form)'), 200
    elif request.method == 'DELETE':
        return jsonify('ResourcesHandler().deleteResources(rid)'), 200
    else:
        return jsonify('jsonify(Error="Method not allowed."), 405'), 405


@app.route('/PartApp/resources/<int:rid>/supplier')
def getSupplierByResourcesId(rid):
    return jsonify('ResourcesHandler().getSupplierByResourcesId(rid)'), 200


@app.route('/PartApp/resources/<int:rid>/consumer')
def getConsumerByResourcesId(rid):
    return jsonify('ResourcesHandler().getConsumerByResourcesId(rid)'), 200


@app.route('/PartApp/resources/<int:rid>/company')
def getCompanyByResourcesId(rid):
    return jsonify('ResourcesHandler().getCompanyByResourcesId(rid)'), 200

@app.route('/PartApp/resources/countbyresourceid')
def getCountByResourceId():
    return jsonify('ResourcesHandler().getCountByResourceId()'), 200

## Supplier

@app.route('/PartApp/supplier', methods=['GET', 'POST'])
def getAllSuppliers():
    if request.method == 'POST':
        #return print("REQUEST: ", request.json)
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


@app.route('/PartApp/supplier/<int:sid>/resource')
def getResourcesBySupplierId(sid):
    return jsonify('SupplierHandler().getResourcesBySupplierId(sid)'), 200


@app.route('/PartApp/supplier/<int:sid>/company')
def getCompanyBySupplierId(sid):
    return jsonify('SupplierHandler().getCompanyBySupplierId(sid)'), 200


@app.route('/PartApp/supplier/<int:sid>/order')
def getOrderBySupplierId(sid):
    return jsonify('SupplierHandler().getOrderBySupplierId(sid)'), 200


@app.route('/PartApp/supplier/<int:sid>/paymethod')
def getPayMethodBySupplierId(sid):
    return jsonify('SupplierHandler().getPayMethodBySupplierId(sid)'), 200


@app.route('/PartApp/supplier/<int:sid>/reservations')
def getReservationBySupplierId(sid):
    return jsonify('SupplierHandler().getReservationBySupplierId(sid)'), 200

## System Admin

@app.route('/PartApp/systemadmin', methods=['GET', 'POST'])
def getAllSysAdm():
    if request.method == 'POST':
        #return print("REQUEST: ", request.json)
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


@app.route('/PartApp/systemadmin/<int:said>/supplier')
def getSupplierBySysAdmId(said):
    return jsonify('SystemadminHandler().getSupplierBySysAdmId(sid)'), 200


@app.route('/PartApp/systemadmin/<int:said>/consumer')
def getConsumerBySysAdmId(said):
    return jsonify('SystemadminHandler().getConsumerBySysAdmId(sid)'), 200


@app.route('/PartApp/systemadmin/<int:said>/company')
def getCompanyBySysAdmId(said):
    return jsonify('SystemadminHandler().getCompanyBySysAdmId(sid)'), 200


@app.route('/PartApp/systemadmin/<int:said>/user')
def getUserBySysAdmId(said):
    return jsonify('SystemadminHandler().getUserBySysAdmId(sid)'), 200

## User

@app.route('/PartApp/user', methods=['GET', 'POST'])
def getAllUser():
    if request.method == 'POST':
        #return print("REQUEST: ", request.json)
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


@app.route('/PartApp/user/<int:uid>/company')
def getCompanyByUserId(uid):
    return jsonify('UserHandler().getCompanyByUserId(uid)'), 200

if __name__ == '__main__':
    app.run()
