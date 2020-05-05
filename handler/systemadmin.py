from flask import jsonify
from dao.systemadmin import SysAdmDAO


class SysAdmHandler:
    def build_systemadmin_dict(self, row):
        result = {}
        result['said'] = row[0]
        result['sausername'] = row[1]
        return result

    def build_company_dict(self, row):
        result = {}
        result['compid'] = row[0]
        result['compname'] = row[1]
        return result

    def build_consumer_dict(self, row):
        result = {}
        result['consid'] = row[0]
        result['consusername'] = row[1]
        return result

    def build_supplier_dict(self, row):
        result = {}
        result['sid'] = row[0]
        result['susername'] = row[1]
        result['scompany'] = row[2]
        return result

    def build_user_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['ufirstname'] = row[1]
        result['ulastname'] = row[2]
        return result

    def build_systemadmin_attributes(self, said, sausername):
        result = {}
        result['said'] = said
        result['sausername'] = sausername
        return result

    def getAllSysAdm(self):
        dao = SysAdmDAO()
        sysadm_list = dao.getAllSysAdm()
        result_list = []
        for row in sysadm_list:
            result = self.build_systemadmin_dict(row)
            result_list.append(result)
        return jsonify(SysAdm=result_list)

    def getSysAdmById(self, said):
        dao = SysAdmDAO()
        row = dao.getSysAdmById(said)
        if not row:
            return jsonify(Error="System Admin Not Found"), 404
        else:
            sysadm = self.build_supplier_dict(row)
        return jsonify(SysAdm=sysadm)

    def searchSysAdm(self, args):
        sausername = args.get('sausername')
        dao = SysAdmDAO()
        sysadm_list = []
        if (len(args) == 1) and sausername:
            sysadm_list = dao.getSysAdmnByUsername(sausername)
        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in sysadm_list:
            result = self.build_systemadmin_dict(row)
            result_list.append(result)
        return jsonify(SysAdm=result_list)

    def getCompanyBySysAdmId(self, said):
        dao = SysAdmDAO()
        if not dao.getSysAdmById(said):
            return jsonify(Error="System Admin Not Found"), 404
        company_list = dao.getCompanyBySysAdmId(said)
        result_list = []
        for row in company_list:
            result = self.build_company_dict(row)
            result_list.append(result)
        return jsonify(SysAdm=result_list)

    def getConsumerBySysAdmId(self, said):
        dao = SysAdmDAO()
        if not dao.getSysAdmById(said):
            return jsonify(Error="System Admin Not Found"), 404
        consumer_list = dao.getConsumerBySysAdmId(said)
        result_list = []
        for row in consumer_list:
            result = self.build_consumer_dict(row)
            result_list.append(result)
        return jsonify(SysAdm=result_list)

    def getSupplierBySysAdmId(self, said):
        dao = SysAdmDAO()
        if not dao.getSysAdmById(said):
            return jsonify(Error="System Admin Not Found"), 404
        supplier_list = dao.getSupplierBySysAdmId(said)
        result_list = []
        for row in supplier_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(SysAdm=result_list)

    def getUsersBySysAdmId(self, said):
        dao = SysAdmDAO()
        if not dao.getSysAdmById(said):
            return jsonify(Error="System Admin Not Found"), 404
        users_list = dao.getUsersBySysAdmId(said)
        result_list = []
        for row in users_list:
            result = self.build_user_dict(row)
            result_list.append(result)
        return jsonify(SysAdm=result_list)

    def insertSysAdmJson(self, json):
        sausername = json['sausername']
        if sausername:
            dao = SysAdmDAO()
            said = dao.insert(sausername)
            result = self.build_systemadmin_attributes(said, sausername)
            return jsonify(SysAdm=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def updateSysAdm(self, said, form):
        dao = SysAdmDAO()
        if not dao.getSysAdmById(said):
            return jsonify(Error="System Admin not found."), 404
        else:
            if len(form) != 1:
                return jsonify(Error="Malformed update request"), 400
            else:
                sausername = form['sausername']
                if sausername:
                    dao.update(said, sausername)
                    result = self.build_systemadmin_attributes(said, sausername)
                    return jsonify(SysAdm=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def deleteSysAdm(self, said):
        dao = SysAdmDAO()
        if not dao.getSysAdmById(said):
            return jsonify(Error="System Admin not found."), 404
        else:
            dao.delete(said)
            return jsonify(DeleteStatus="OK"), 200
