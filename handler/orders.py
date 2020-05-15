import datetime
from flask import jsonify
from dao.orders import OrdersDAO


class OrdersHandler:
    def build_order_dict(self, row):
        result = {}
        result['odid'] = row[0]
        result['resid'] = row[1]
        result['odnumber'] = row[2]
        result['odtime'] = row[3]
        return result

    def build_consumer_dict(self, row):
        result = {}
        result['consid'] = row[0]
        result['uid'] = row[1]
        result['consusername'] = row[2]
        return result

    def build_reservation_dict(self, row):
        result = {}
        result['resid'] = row[0]
        result['resname'] = row[1]
        result['restype'] = row[2]
        result['resprice'] = row[3]
        result['resstock'] = row[4]
        result['reslocation'] = row[5]
        result['restime'] = row[6]
        return result

    def build_supplier_dict(self, row):
        result = {}
        result['sid'] = row[0]
        result['uid'] = row[1]
        result['susername'] = row[2]
        result['scompany'] = row[3]
        return result

    def build_order_attributes(self, odid, resid, odnumber, odtime):
        result = {}
        result['odid'] = odid
        result['resid'] = resid
        result['odnumber'] = odnumber
        result['odtime'] = odtime
        return result

    def getAllOrders(self):
        dao = OrdersDAO()
        order_list = dao.getAllOrders()
        result_list = []
        for row in order_list:
            result = self.build_order_dict(row)
            result_list.append(result)
        return jsonify(Orders=result_list)

    def getOrdersById(self, odid):
        dao = OrdersDAO()
        row = dao.getOrdersById(odid)
        if not row:
            return jsonify(Error="Orders Not Found"), 404
        else:
            orders = self.build_order_dict(row)
        return jsonify(Orders=orders)

    def searchOrders(self, args):
        odnumber = args.get('odnumber')
        dao = OrdersDAO()
        order_list = []
        if (len(args) == 1) and odnumber:
            order_list = dao.getOrdersByNumber(odnumber)
        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in order_list:
            result = self.build_order_dict(row)
            result_list.append(result)
        return jsonify(Orders=result_list)

    def getConsumerByOrdersId(self, odid):
        dao = OrdersDAO()
        if not dao.getOrdersById(odid):
            return jsonify(Error="Orders Not Found"), 404
        consumer_list = dao.getConsumerByOrdersId(odid)
        result_list = []
        for row in consumer_list:
            result = self.build_consumer_dict(row)
            result_list.append(result)
        return jsonify(Orders=result_list)

    def getReservationByOrdersId(self, odid):
        dao = OrdersDAO()
        if not dao.getOrdersById(odid):
            return jsonify(Error="Orders Not Found"), 404
        reservation_list = dao.getReservationByOrdersId(odid)
        result_list = []
        for row in reservation_list:
            result = self.build_reservation_dict(row)
            result_list.append(result)
        return jsonify(Orders=result_list)

    def getSupplierByOrdersId(self, odid):
        dao = OrdersDAO()
        if not dao.getOrdersById(odid):
            return jsonify(Error="Orders Not Found"), 404
        supplier_list = dao.getSupplierByOrdersId(odid)
        result_list = []
        for row in supplier_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Orders=result_list)

    def insertOrdersJson(self, json):
        resid = json['resid']
        odnumber = json['odnumber']
        odtime = json['odtime']
        if odtime.lower() == "default":
            odtime = datetime.datetime.now()
        odtime = odtime.strftime("%Y-%m-%d %H:%M:%S")
        if resid and odnumber and odtime:
            dao = OrdersDAO()
            odid = dao.insert(resid, odnumber, odtime)
            result = self.build_order_attributes(odid, resid, odnumber, odtime)
            return jsonify(Orders=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def updateOrders(self, odid, form):
        dao = OrdersDAO()
        if not dao.getOrdersById(odid):
            return jsonify(Error="Orders not found."), 404
        else:
            if len(form) != 3:
                return jsonify(Error="Malformed update request"), 400
            else:
                resid = form['resid']
                odnumber = form['odnumber']
                odtime = form['odtime']
                if resid and odnumber and odtime:
                    dao.update(odid, resid, odnumber, odtime)
                    result = self.build_order_attributes(odid, resid, odnumber, odtime)
                    return jsonify(Orders=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def deleteOrders(self, odid):
        dao = OrdersDAO()
        if not dao.getOrdersById(odid):
            return jsonify(Error="Orders not found."), 404
        else:
            dao.delete(odid)
            return jsonify(DeleteStatus="OK"), 200
