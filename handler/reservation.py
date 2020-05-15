import datetime
from flask import jsonify
from dao.reservation import ReservationDAO
from dao.resources import ResourcesDAO
from dao.orders import OrdersDAO


class ReservationHandler:
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

    def build_consumer_dict(self, row):
        result = {}
        result['consid'] = row[0]
        result['uid'] = row[1]
        result['consusername'] = row[2]
        return result

    def build_order_dict(self, row):
        result = {}
        result['odid'] = row[0]
        result['odnumber'] = row[1]
        result['odtime'] = row[2]
        return result

    def build_resource_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['rname'] = row[1]
        result['rtype'] = row[2]
        result['rprice'] = row[3]
        result['rlocation'] = row[3]
        result['rstock'] = row[5]
        return result

    def build_supplier_dict(self, row):
        result = {}
        result['sid'] = row[0]
        result['uid'] = row[1]
        result['susername'] = row[2]
        result['scompany'] = row[3]
        return result

    def build_reservation_attributes(self, resid, resname, restype, resprice, resstock, reslocation, restime):
        result = {}
        result['resid'] = resid
        result['resname'] = resname
        result['restype'] = restype
        result['resprice'] = resprice
        result['resstock'] = resstock
        result['reslocation'] = reslocation
        result['restime'] = restime
        return result

    def getAllReservation(self):
        dao = ReservationDAO()
        payment_list = dao.getAllReservation()
        result_list = []
        for row in payment_list:
            result = self.build_reservation_dict(row)
            result_list.append(result)
        return jsonify(Reservation=result_list)

    def getReservationById(self, resid):
        dao = ReservationDAO()
        row = dao.getReservationById(resid)
        if not row:
            return jsonify(Error="Reservation Not Found"), 404
        else:
            reservation = self.build_reservation_dict(row)
        return jsonify(Reservation=reservation)

    def searchReservation(self, args):
        resid = args.get('resid')
        resname = args.get('resname')
        restype = args.get('restype')
        resprice = args.get('resprice')
        resstock = args.get('resstock')
        reslocation = args.get('reslocation')
        restime = args.get('restime')
        dao = ReservationDAO()
        reservation_list = []
        if (len(args) == 6) and resname and restype and resprice and resstock and reslocation and restime:
            reservation_list = dao.getReservationByNameandTypeandPriceandStockandLocationandTime(resname, restype, resprice, resstock, reslocation, restime)
        if (len(args) == 5) and resname and restype and resprice and resstock and reslocation:
            reservation_list = dao.getReservationByNameandTypeandPriceandStockandLocation(resname, restype, resprice, resstock, reslocation)
        if (len(args) == 5) and resname and restype and resprice and resstock and restime:
            reservation_list = dao.getReservationByNameandTypeandPriceandStockandTime(resname, restype, resprice, resstock, restime)
        if (len(args) == 5) and resname and restype and resprice and reslocation and restime:
            reservation_list = dao.getReservationByNameandTypeandPriceandLocationandTime(resname, restype, resprice, reslocation, restime)
        if (len(args) == 5) and resname and restype and resstock and reslocation and restime:
            reservation_list = dao.getReservationByNameandTypeandStockandLocationandTime(resname, restype, resstock, reslocation, restime)
        if (len(args) == 5) and resname and resprice and resstock and reslocation and restime:
            reservation_list = dao.getReservationByNameandPriceandStockandLocationandTime(resname, resprice, resstock, reslocation, restime)
        if (len(args) == 5) and restype and resprice and resstock and reslocation and restime:
            reservation_list = dao.getReservationByTypeandPriceandStockandLocationandTime(restype, resprice, resstock, reslocation, restime)
        if (len(args) == 4) and resname and restype and resprice and resstock:
            reservation_list = dao.getReservationByNameandTypeandPriceandStock(resname, restype, resprice, resstock)
        if (len(args) == 4) and resname and restype and resprice and reslocation:
            reservation_list = dao.getReservationByNameandTypeandPriceandLocation(resname, restype, resprice, reslocation)
        if (len(args) == 4) and resname and restype and resprice and restime:
            reservation_list = dao.getReservationByNameandTypeandPriceandTime(resname, restype, resprice, restime)
        if (len(args) == 4) and resname and restype and resstock and reslocation:
            reservation_list = dao.getReservationByNameandTypeandStockandLocation(resname, restype, resstock, reslocation)
        if (len(args) == 4) and resname and restype and resstock and restime:
            reservation_list = dao.getReservationByNameandTypeandStockandTime(resname, restype, resstock, restime)
        if (len(args) == 4) and resname and restype and reslocation and restime:
            reservation_list = dao.getReservationByNameandTypeandLocationandTime(resname, restype, reslocation, restime)
        if (len(args) == 4) and resname and resprice and resstock and reslocation:
            reservation_list = dao.getReservationByNameandPriceandStockandLocation(resname, resprice, resstock, reslocation)
        if (len(args) == 4) and resname and resprice and resstock and restime:
            reservation_list = dao.getReservationByNameandPriceandStockandTime(resname, resprice, resstock, restime)
        if (len(args) == 4) and resname and resprice and reslocation and restime:
            reservation_list = dao.getReservationByNameandPriceandLocationandTime(resname, resprice, reslocation, restime)
        if (len(args) == 4) and resname and resstock and reslocation and restime:
            reservation_list = dao.getReservationByNameandStockandLocationandTime(resname, resstock, reslocation, restime)
        if (len(args) == 4) and restype and resprice and resstock and reslocation:
            reservation_list = dao.getReservationByTypeandPriceandStockandLocation(restype, resprice, resstock, reslocation)
        if (len(args) == 4) and restype and resprice and resstock and restime:
            reservation_list = dao.getReservationByTypeandPriceandStockandTime(restype, resprice, resstock, restime)
        if (len(args) == 4) and restype and resprice and reslocation and restime:
            reservation_list = dao.getReservationByTypeandPriceandLocationandTime(restype, resprice, reslocation, restime)
        if (len(args) == 4) and restype and resstock and reslocation and restime:
            reservation_list = dao.getReservationByTypeandStockandLocationandTime(restype, resstock, reslocation, restime)
        if (len(args) == 4) and resprice and resstock and reslocation and restime:
            reservation_list = dao.getReservationByPriceandStockandLocationandTime(resprice, resstock, reslocation, restime)
        if (len(args) == 3) and resname and restype and resprice:
            reservation_list = dao.getReservationByNameandTypeandPrice(resname, restype, resprice)
        if (len(args) == 3) and resname and restype and resstock:
            reservation_list = dao.getReservationByNameandTypeandStock(resname, restype, resstock)
        if (len(args) == 3) and resname and restype and reslocation:
            reservation_list = dao.getReservationByNameandTypeandLocation(resname, restype, reslocation)
        if (len(args) == 3) and resname and restype and restime:
            reservation_list = dao.getReservationByNameandTypeandTime(resname, restype, restime)
        if (len(args) == 3) and resname and resprice and resstock:
            reservation_list = dao.getReservationByNameandPriceandStock(resname, resprice, resstock)
        if (len(args) == 3) and resname and resprice and reslocation:
            reservation_list = dao.getReservationByNameandPriceandLocation(resname, resprice, reslocation)
        if (len(args) == 3) and resname and resprice and restime:
            reservation_list = dao.getReservationByNameandPriceandTime(resname, resprice, restime)
        if (len(args) == 3) and resname and resstock and reslocation:
            reservation_list = dao.getReservationByNameandStockandLocation(resname, resstock, reslocation)
        if (len(args) == 3) and resname and resstock and restime:
            reservation_list = dao.getReservationByNameandStockandTime(resname, resstock, restime)
        if (len(args) == 3) and resname and reslocation and restime:
            reservation_list = dao.getReservationByNameandLocationandTime(resname, reslocation, restime)
        if (len(args) == 3) and restype and resprice and resstock:
            reservation_list = dao.getReservationByTypeandPriceandStock(restype, resprice, resstock)
        if (len(args) == 3) and restype and resprice and reslocation:
            reservation_list = dao.getReservationByTypeandPriceandLocation(restype, resprice, reslocation)
        if (len(args) == 3) and restype and resprice and restime:
            reservation_list = dao.getReservationByTypeandPriceandTime(restype, resprice, restime)
        if (len(args) == 3) and restype and resstock and reslocation:
            reservation_list = dao.getReservationByTypeandStockandLocation(restype, resstock, reslocation)
        if (len(args) == 3) and restype and resstock and restime:
            reservation_list = dao.getReservationByTypeandStockandTime(restype, resstock, restime)
        if (len(args) == 3) and restype and reslocation and restime:
            reservation_list = dao.getReservationByTypeandLocationandTime(restype, reslocation, restime)
        if (len(args) == 3) and resprice and resstock and reslocation:
            reservation_list = dao.getReservationByPriceandStockandLocation(resprice, resstock, reslocation)
        if (len(args) == 3) and resprice and resstock and restime:
            reservation_list = dao.getReservationByPriceandStockandTime(resprice, resstock, restime)
        if (len(args) == 3) and resprice and reslocation and restime:
            reservation_list = dao.getReservationByPriceandLocationandTime(resprice, reslocation, restime)
        if (len(args) == 3) and resstock and reslocation and restime:
            reservation_list = dao.getReservationByStockandLocationandTime(resstock, reslocation, restime)
        if (len(args) == 2) and resname and restype:
            reservation_list = dao.getReservationByNameandType(resname, restype)
        if (len(args) == 2) and resname and resprice:
            reservation_list = dao.getReservationByNameandPrice(resname, resprice)
        if (len(args) == 2) and resname and resstock:
            reservation_list = dao.getReservationByNameandStock(resname, resstock)
        if (len(args) == 2) and resname and reslocation:
            reservation_list = dao.getReservationByNameandLocation(resname, reslocation)
        if (len(args) == 2) and resname and restime:
            reservation_list = dao.getReservationByNameandTime(resname, restime)
        if (len(args) == 2) and restype and resprice:
            reservation_list = dao.getReservationByTypeandPrice(restype, resprice)
        if (len(args) == 2) and restype and resstock:
            reservation_list = dao.getReservationByTypeandStock(restype, resstock)
        if (len(args) == 2) and restype and reslocation:
            reservation_list = dao.getReservationByTypeandLocation(restype, reslocation)
        if (len(args) == 2) and restype and restime:
            reservation_list = dao.getReservationByTypeandTime(restype, restime)
        if (len(args) == 2) and resprice and resstock:
            reservation_list = dao.getReservationByPriceandStock(resprice, resstock)
        if (len(args) == 2) and resprice and reslocation:
            reservation_list = dao.getReservationByPriceandLocation(resprice, reslocation)
        if (len(args) == 2) and resprice and restime:
            reservation_list = dao.getReservationByPriceandTime(resprice, restime)
        if (len(args) == 2) and resstock and reslocation:
            reservation_list = dao.getReservationByStockandLocation(resstock, reslocation)
        if (len(args) == 2) and resstock and restime:
            reservation_list = dao.getReservationByStockandTime(resstock, restime)
        if (len(args) == 2) and reslocation and restime:
            reservation_list = dao.getReservationByLocationandTime(reslocation, restime)
        if (len(args) == 1) and resname:
            reservation_list = dao.getReservationByName(resname)
        if (len(args) == 1) and restype:
            reservation_list = dao.getReservationByType(restype)
        if (len(args) == 1) and resprice:
            reservation_list = dao.getReservationByPrice(resprice)
        if (len(args) == 1) and resstock:
            reservation_list = dao.getReservationByStock(resstock)
        if (len(args) == 1) and reslocation:
            reservation_list = dao.getReservationByLocation(reslocation)
        if (len(args) == 1) and restime:
            reservation_list = dao.getReservationByTime(restime)
        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in reservation_list:
            result = self.build_reservation_dict(row)
            result_list.append(result)
        return jsonify(Reservation=result_list)

    def getConsumerByReservationId(self, resid):
        dao = ReservationDAO()
        if not dao.getReservationById(resid):
            return jsonify(Error="Reservation Not Found"), 404
        consumer_list = dao.getConsumerByReservationId(resid)
        result_list = []
        for row in consumer_list:
            result = self.build_consumer_dict(row)
            result_list.append(result)
        return jsonify(Reservation=result_list)

    def getOrdersByReservationId(self, resid):
        dao = ReservationDAO()
        if not dao.getReservationById(resid):
            return jsonify(Error="Reservation Not Found"), 404
        order_list = dao.getOrdersByReservationId(resid)
        result_list = []
        for row in order_list:
            result = self.build_order_dict(row)
            result_list.append(result)
        return jsonify(Reservation=result_list)

    def getResourcesByReservationId(self, resid):
        dao = ReservationDAO()
        if not dao.getReservationById(resid):
            return jsonify(Error="Reservation Not Found"), 404
        resource_list = dao.getResourcesByReservationId(resid)
        result_list = []
        for row in resource_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Reservation=result_list)

    def getSupplierByReservationId(self, resid):
        dao = ReservationDAO()
        if not dao.getReservationById(resid):
            return jsonify(Error="Reservation Not Found"), 404
        supplier_list = dao.getSupplierByReservationId(resid)
        result_list = []
        for row in supplier_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Reservation=result_list)

    def insertReservationJson(self, json):
        resname = json['resname']
        restype = json['restype']
        resprice = json['resprice']
        resstock = json['resstock']
        reslocation = json['reslocation']
        restime = json['restime']
        if reslocation == 'Ponce':
            reslocation = '18.0107279,-66.6141375'
        elif reslocation == 'Mayaguez':
            reslocation = '18.201108,-67.1401665'
        elif reslocation == 'San Juan':
            reslocation = '18.46542,-66.1172515'
        if ',' in reslocation and len(reslocation) != 1:
            reslocation = "https://maps.google.com/?q=" + reslocation
        if resname and restype and resprice and resstock and reslocation and restime:
            if restime == "default":
                restime = datetime.datetime.now()
            restime = restime.strftime("%Y-%m-%d %H:%M:%S")
            availableStock = ResourcesDAO().getAvailableStockByResourceNameandType(resname, restype, resstock)
            neededStock = int(resstock)
            differenceStock = availableStock-neededStock
            if differenceStock>0:
                dao = ReservationDAO()
                resid = dao.insert(resname, restype, resprice, resstock, reslocation, restime)
                result = self.build_reservation_attributes(resid, resname, restype, resprice, resstock, reslocation, restime)
                OrdersDAO().insert(resid, resid, restime)
                updateid = ResourcesDAO().getToUpdateId(resname, restype, resstock)
                ResourcesDAO().updateStockAfterReservation(updateid, differenceStock)
                return jsonify(Reservation=result), 201
            else:
                dao = ReservationDAO()
                resid = dao.insert(resname, restype, resprice, resstock, reslocation, restime)
                result = self.build_reservation_attributes(resid, resname, restype, resprice, resstock, reslocation, restime)
                return jsonify(Reservation=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400


    def updateReservation(self, resid, form):
        dao = ReservationDAO()
        if not dao.getReservationById(resid):
            return jsonify(Error="Reservation not found."), 404
        else:
            if len(form) != 6:
                return jsonify(Error="Malformed update request"), 400
            else:
                resname = form['resname']
                restype = form['restype']
                resprice = form['resprice']
                resstock = form['resstock']
                reslocation = form['reslocation']
                restime = form['restime']
                if resname and restype and resprice and resstock and reslocation and restime:
                    dao.update(resid, resname, restype, resprice, resstock, reslocation, restime)
                    result = self.build_reservation_attributes(resid, resname, restype, resprice, resstock, reslocation, restime)
                    return jsonify(Reservation=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def deleteReservation(self, resid):
        dao = ReservationDAO()
        if not dao.getReservationById(resid):
            return jsonify(Error="Reservation not found."), 404
        else:
            dao.delete(resid)
            return jsonify(DeleteStatus="OK"), 200
