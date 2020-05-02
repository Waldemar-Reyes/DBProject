from flask import jsonify
from dao.supplier import SupplierDAO


class SupplierHandler:
    def build_supplier_dict(self, row):
        result = {}
        result['sid'] = row[0]
        result['susername'] = row[1]
        result['scompany'] = row[2]
        return result

    def build_supplier_attributes(self, sid, susername, scompany):
        result = {}
        result['sid'] = sid
        result['susername'] = susername
        result['scompany'] = scompany
        return result

    def getAllSuppliers(self):
        dao = SupplierDAO()
        supplier_list = dao.getAllSupplier()
        result_list = []
        for row in supplier_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Suppliers=result_list)

    def getSupplierById(self, sid):
        dao = SupplierDAO()
        row = dao.getSupplierById(sid)
        if not row:
            return jsonify(Error="Supplier Not Found"), 404
        else:
            part = self.build_supplier_dict(row)
        return jsonify(Part=part)

    def searchSuppliers(self, args):
        susername = args.get('susername')
        scompany = args.get('scompany')
        dao = SupplierDAO()
        supplier_list = []
        if (len(args) == 2) and susername and scompany:
            # TODO Not yet implemented
            # supplier_list = dao.getSupplierByUsernameandCompany(susername, scompany)
            print("getSupplierByUsernameandCompany(susername, scompany)")
        elif (len(args) == 1) and susername:
            supplier_list = dao.getSupplierByUsername(susername)
        elif (len(args) == 1) and scompany:
            supplier_list = dao.getSupplierByCompany(scompany)
        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in supplier_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Supplier=result_list)

    # TODO Not yet implemented in DAO nor main
    #
    # def getPartsBySupplierId(self, sid):
    #     dao = SupplierDAO()
    #     if not dao.getSupplierById(sid):
    #         return jsonify(Error="Supplier Not Found"), 404
    #     parts_list = dao.getPartsBySupplierId(sid)
    #     result_list = []
    #     for row in parts_list:
    #         result = self.build_part_dict(row)
    #         result_list.append(result)
    #     return jsonify(PartsSupply=result_list)

    def insertSupplierJson(self, json):
        sid = json['sid']
        susername = json['susername']
        scompany = json['scompany']
        if sid and susername and scompany:
            dao = SupplierDAO()
            sid = dao.insert(susername, scompany)
            result = self.build_supplier_attributes(sid, susername, scompany)
            return jsonify(Supplier=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def updateSupplier(self, sid, form):
        dao = SupplierDAO()
        if not dao.getSupplierById(sid):
            return jsonify(Error="Supplier not found."), 404
        else:
            if len(form) != 2:
                return jsonify(Error="Malformed update request"), 400
            else:
                susername = form['susername']
                scompany = form['scompany']
                if susername and scompany:
                    dao.update(sid, susername, scompany)
                    result = self.build_supplier_attributes(sid, susername, scompany)
                    return jsonify(Supplier=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def deleteSupplier(self, sid):
        dao = SupplierDAO()
        if not dao.getSupplierById(sid):
            return jsonify(Error="Supplier not found."), 404
        else:
            dao.delete(sid)
            return jsonify(DeleteStatus="OK"), 200
