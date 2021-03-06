from flask import jsonify
from dao.paymethod import PayMethodDAO
from dao.consumer import ConsumerDAO


class PayMethodHandler:
    def build_payment_dict(self, row):
        result = {}
        result['pmid'] = row[0]
        result['pmname'] = row[1]
        return result

    def build_consumer_dict(self, row):
        result = {}
        result['consid'] = row[0]
        result['uid'] = row[1]
        result['consusername'] = row[2]
        return result

    def build_supplier_dict(self, row):
        result = {}
        result['sid'] = row[0]
        result['uid'] = row[1]
        result['susername'] = row[2]
        result['scompany'] = row[3]
        return result

    def build_payment_attributes(self, pmid, pmname):
        result = {}
        result['pmid'] = pmid
        result['pmname'] = pmname
        return result

    def getAllPayMethod(self):
        dao = PayMethodDAO()
        payment_list = dao.getAllPayMethod()
        result_list = []
        for row in payment_list:
            result = self.build_payment_dict(row)
            result_list.append(result)
        return jsonify(PayMethod=result_list)

    def getPayMethodById(self, pmid):
        dao = PayMethodDAO()
        row = dao.getPayMethodById(pmid)
        if not row:
            return jsonify(Error="Payment Not Found"), 404
        else:
            paymethod = self.build_payment_dict(row)
        return jsonify(PayMethod=paymethod)

    def searchPayMethod(self, args):
        pmname = args.get('pmname')
        dao = PayMethodDAO()
        payment_list = []
        if (len(args) == 1) and pmname:
            payment_list = dao.getPayMethodByName(pmname)
        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in payment_list:
            result = self.build_payment_dict(row)
            result_list.append(result)
        return jsonify(PayMethod=result_list)

    def getConsumerByPayMethodId(self, pmid):
        dao = PayMethodDAO()
        if not dao.getPayMethodById(pmid):
            return jsonify(Error="Payment Not Found"), 404
        consumer_list = dao.getConsumerByPayMethodId(pmid)
        result_list = []
        for row in consumer_list:
            result = self.build_consumer_dict(row)
            result_list.append(result)
        return jsonify(PayMethod=result_list)

    def getSupplierByPayMethodId(self, pmid):
        dao = PayMethodDAO()
        if not dao.getPayMethodById(pmid):
            return jsonify(Error="Payment Not Found"), 404
        supplier_list = dao.getSupplierByPayMethodId(pmid)
        result_list = []
        for row in supplier_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(PayMethod=result_list)

    def insertPayMethodJson(self, json):
        pmname = json['pmname']
        consid = json['consid']
        if not ConsumerDAO().getConsumerById(consid):
            return jsonify(Error="Consumer Not Found"), 404
        if pmname and consid:
            dao = PayMethodDAO()
            pmid = dao.insert(pmname.lower())
            dao.insertPayMethodOfConsumer(pmid, consid)
            result = self.build_payment_attributes(pmid, pmname)
            return jsonify(PayMethod=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def updatePayMethod(self, pmid, form):
        dao = PayMethodDAO()
        if not dao.getPayMethodById(pmid):
            return jsonify(Error="Payment not found."), 404
        else:
            if len(form) != 1:
                return jsonify(Error="Malformed update request"), 400
            else:
                pmname = form['pmname']
                if pmname:
                    dao.update(pmid, pmname)
                    result = self.build_payment_attributes(pmid, pmname)
                    return jsonify(PayMethod=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def deletePayMethod(self, pmid):
        dao = PayMethodDAO()
        if not dao.getPayMethodById(pmid):
            return jsonify(Error="Payment not found."), 404
        else:
            dao.delete(pmid)
            return jsonify(DeleteStatus="OK"), 200
