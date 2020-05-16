from flask import jsonify
from dao.consumer import ConsumerDAO
from dao.users import UsersDAO
from dao.paymethod import PayMethodDAO


class ConsumerHandler:
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

    def build_payment_dict(self, row):
        result = {}
        result['pmid'] = row[0]
        result['pmname'] = row[1]
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

    def build_resource_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['rname'] = row[1]
        result['rtype'] = row[2]
        result['rprice'] = row[3]
        result['rlocation'] = row[3]
        result['rstock'] = row[5]
        return result

    def build_user_attributes(self, uid, ufirstname, ulastname):
        result = {}
        result['uid'] = uid
        result['ufirstname'] = ufirstname
        result['ulastname'] = ulastname
        return result

    def build_consumer_attributes(self, consid, uid, consusername):
        result = {}
        result['consid'] = consid
        result['uid'] = uid
        result['consusername'] = consusername
        return result

    def getAllConsumer(self):
        dao = ConsumerDAO()
        consumer_list = dao.getAllConsumer()
        result_list = []
        for row in consumer_list:
            result = self.build_consumer_dict(row)
            result_list.append(result)
        return jsonify(Consumer=result_list)

    def getConsumerById(self, consid):
        dao = ConsumerDAO()
        row = dao.getConsumerById(consid)
        if not row:
            return jsonify(Error="Consumer Not Found"), 404
        else:
            consumer = self.build_consumer_dict(row)
        return jsonify(Consumer=consumer)

    def searchConsumer(self, args):
        consusername = args.get('consusername')
        dao = ConsumerDAO()
        consumer_list = []
        if (len(args) == 1) and consusername:
            consumer_list = dao.getConsumerByUsername(consusername)
        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in consumer_list:
            result = self.build_consumer_dict(row)
            result_list.append(result)
        return jsonify(Consumer=result_list)

    def getOrdersByConsumerId(self, consid):
        dao = ConsumerDAO()
        if not dao.getConsumerById(consid):
            return jsonify(Error="Consumer Not Found"), 404
        order_list = dao.getOrdersByConsumerId(consid)
        result_list = []
        for row in order_list:
            result = self.build_order_dict(row)
            result_list.append(result)
        return jsonify(Consumer=result_list)

    def getPayMethodByConsumerId(self, consid):
        dao = ConsumerDAO()
        if not dao.getConsumerById(consid):
            return jsonify(Error="Consumer Not Found"), 404
        payment_list = dao.getPayMethodByConsumerId(consid)
        result_list = []
        for row in payment_list:
            result = self.build_payment_dict(row)
            result_list.append(result)
        return jsonify(Consumer=result_list)

    def getReservationByConsumerId(self, consid):
        dao = ConsumerDAO()
        if not dao.getConsumerById(consid):
            return jsonify(Error="Consumer Not Found"), 404
        reservation_list = dao.getReservationByConsumerId(consid)
        result_list = []
        for row in reservation_list:
            result = self.build_reservation_dict(row)
            result_list.append(result)
        return jsonify(Consumer=result_list)

    def getResourcesByConsumerId(self, consid):
        dao = ConsumerDAO()
        if not dao.getConsumerById(consid):
            return jsonify(Error="Consumer Not Found"), 404
        resource_list = dao.getResourcesByConsumerId(consid)
        result_list = []
        for row in resource_list:
            result = self.getResourcesByConsumerId(row)
            result_list.append(result)
        return jsonify(Consumer=result_list)

    def insertConsumerJson(self, json):
        consusername = json['consusername']
        ufirstname = json['ufirstname']
        ulastname = json['ulastname']
        if consusername and ufirstname and ulastname:
            uid = UsersDAO().insert(ufirstname, ulastname)
            consid = ConsumerDAO().insertConsumerAsNewUsers(uid, consusername)
            PayMethodDAO().insertNewConsumerandPayMethod(consid)
            self.build_user_attributes(uid, ufirstname, ulastname)
            result = self.build_consumer_attributes(consid, uid, consusername)
            return jsonify(Consumer=result), 201
        elif consusername:
            uid = ""
            consid = ConsumerDAO().insert(consusername)
            result = self.build_consumer_attributes(consid, uid, consusername)
            return jsonify(Consumer=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def updateConsumer(self, consid, form):
        dao = ConsumerDAO()
        if not dao.getConsumerById(consid):
            return jsonify(Error="Consumer not found."), 404
        else:
            if len(form) != 2:
                return jsonify(Error="Malformed update request"), 400
            else:
                uid = form['uid']
                consusername = form['consusername']
                if consusername and uid:
                    dao.update(consid, uid, consusername)
                    result = self.build_consumer_attributes(consid, uid, consusername)
                    return jsonify(Consumer=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def deleteConsumer(self, consid):
        dao = ConsumerDAO()
        if not dao.getConsumerById(consid):
            return jsonify(Error="Consumer not found."), 404
        else:
            dao.delete(consid)
            return jsonify(DeleteStatus="OK"), 200
