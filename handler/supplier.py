from flask import jsonify
from dao.supplier import SupplierDAO
from dao.users import UsersDAO
from dao.company import CompanyDAO


class SupplierHandler:
    def build_supplier_dict(self, row):
        result = {}
        result['sid'] = row[0]
        result['uid'] = row[1]
        result['susername'] = row[2]
        result['scompany'] = row[3]
        return result

    def build_company_dict(self, row):
        result = {}
        result['compid'] = row[0]
        result['compname'] = row[1]
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

    def build_supplier_attributes(self, sid, uid, susername, scompany):
        result = {}
        result['sid'] = sid
        result['uid'] = uid
        result['susername'] = susername
        result['scompany'] = scompany
        return result

    def getAllSupplier(self):
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
            suppliers = self.build_supplier_dict(row)
        return jsonify(Suppliers=suppliers)

    def searchSupplier(self, args):
        susername = args.get('susername')
        scompany = args.get('scompany')
        dao = SupplierDAO()
        supplier_list = []
        if (len(args) == 1) and susername:
            supplier_list = dao.getSupplierByUsername(susername)
        elif (len(args) == 1) and scompany:
            supplier_list = dao.getSupplierByCompany(scompany)
        elif (len(args) == 2) and susername and scompany:
            supplier_list = dao.getSupplierByUsernameandCompany(susername, scompany)
        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in supplier_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Supplier=result_list)

    def getCompanyBySupplierId(self, sid):
        dao = SupplierDAO()
        if not dao.getSupplierById(sid):
            return jsonify(Error="Supplier Not Found"), 404
        company_list = dao.getCompanyBySupplierId(sid)
        result_list = []
        for row in company_list:
            result = self.build_company_dict(row)
            result_list.append(result)
        return jsonify(Supplier=result_list)

    def getOrdersBySupplierId(self, sid):
        dao = SupplierDAO()
        if not dao.getSupplierById(sid):
            return jsonify(Error="Supplier Not Found"), 404
        orders_list = dao.getOrdersBySupplierId(sid)
        result_list = []
        for row in orders_list:
            result = self.build_order_dict(row)
            result_list.append(result)
        return jsonify(Supplier=result_list)

    def getPayMethodBySupplierId(self, sid):
        dao = SupplierDAO()
        if not dao.getSupplierById(sid):
            return jsonify(Error="Supplier Not Found"), 404
        payment_list = dao.getPayMethodBySupplierId(sid)
        result_list = []
        for row in payment_list:
            result = self.build_payment_dict(row)
            result_list.append(result)
        return jsonify(Supplier=result_list)

    def getReservationBySupplierId(self, sid):
        dao = SupplierDAO()
        if not dao.getSupplierById(sid):
            return jsonify(Error="Supplier Not Found"), 404
        reservation_list = dao.getReservationBySupplierId(sid)
        result_list = []
        for row in reservation_list:
            result = self.build_reservation_dict(row)
            result_list.append(result)
        return jsonify(Supplier=result_list)

    def getResourcesBySupplierId(self, sid):
        dao = SupplierDAO()
        if not dao.getSupplierById(sid):
            return jsonify(Error="Supplier Not Found"), 404
        resources_list = dao.getResourcesBySupplierId(sid)
        result_list = []
        for row in resources_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Supplier=result_list)

    def insertSupplierJson(self, json):
        ufirstname = None
        ulastname = None
        compid = None
        susername = json['susername']
        scompany = json['scompany']
        if len(json) == 3:
            compid = json['compid']
        elif len(json) == 4:
            ufirstname = json['ufirstname']
            ulastname = json['ulastname']
        elif len(json) == 5:
            ufirstname = json['ufirstname']
            ulastname = json['ulastname']
            compid = json['compid']
        if susername and scompany and ufirstname and ulastname and compid:
            if not CompanyDAO().getCompanyById(compid):
                return jsonify(Error="Company Not Found"), 404
            uid = UsersDAO().insert(ufirstname, ulastname)
            sid = SupplierDAO().insertSupplierAsNewUsers(uid, susername, scompany)
            CompanyDAO().supplierWorksForCompany(compid, sid)
            self.build_user_attributes(uid, ufirstname, ulastname)
            result = self.build_supplier_attributes(sid, uid, susername, scompany)
            return jsonify(Supplier=result), 201
        elif susername and scompany and ufirstname and ulastname:
            uid = UsersDAO().insert(ufirstname, ulastname)
            sid = SupplierDAO().insertSupplierAsNewUsers(uid, susername, scompany)
            self.build_user_attributes(uid, ufirstname, ulastname)
            result = self.build_supplier_attributes(sid, uid, susername, scompany)
            return jsonify(Supplier=result), 201
        elif susername and scompany and compid:
            if not CompanyDAO().getCompanyById(compid):
                return jsonify(Error="Company Not Found"), 404
            uid = ""
            sid = SupplierDAO().insert(susername, scompany)
            CompanyDAO().supplierWorksForCompany(compid, sid)
            result = self.build_supplier_attributes(sid, uid, susername, scompany)
            return jsonify(Supplier=result), 201
        elif susername and scompany:
            uid = ""
            sid = SupplierDAO().insert(susername, scompany)
            result = self.build_supplier_attributes(sid, uid, susername, scompany)
            return jsonify(Supplier=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def updateSupplier(self, sid, form):
        dao = SupplierDAO()
        if not dao.getSupplierById(sid):
            return jsonify(Error="Supplier not found."), 404
        else:
            if len(form) == 3:
                uid = form['uid']
                susername = form['susername']
                scompany = form['scompany']
                if susername and scompany and uid:
                    dao.update(sid, uid, susername, scompany)
                    result = self.build_supplier_attributes(sid, uid, susername, scompany)
                    return jsonify(Supplier=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400
            elif len(form) == 4:
                uid = form['uid']
                susername = form['susername']
                scompany = form['scompany']
                compid = form['compid']
                if susername and scompany and uid and compid:
                    if not CompanyDAO().getCompanyById(compid):
                        return jsonify(Error="Company Not Found"), 404
                    dao.updateSupplierWithCompany(sid, uid, susername, scompany, compid)
                    result = self.build_supplier_attributes(sid, uid, susername, scompany)
                    return jsonify(Supplier=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400
            else:
                return jsonify(Error="Malformed update request"), 400

    def deleteSupplier(self, sid):
        dao = SupplierDAO()
        if not dao.getSupplierById(sid):
            return jsonify(Error="Supplier not found."), 404
        else:
            dao.delete(sid)
            return jsonify(DeleteStatus="OK"), 200
