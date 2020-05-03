from flask import jsonify
from dao.users import UsersDAO


class UsersHandler:
    def build_user_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['ufirstname'] = row[1]
        result['ulastname'] = row[2]
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
    
    def build_systemadmin_dict(self, row):
        result = {}
        result['said'] = row[0]
        result['sausername'] = row[1]
        return result
      
    def build_user_attributes(self, uid, ufirstname, ulastname):
        result = {}
        result['uid'] = uid
        result['ufirstname'] = ufirstname
        result['ulastname'] = ulastname
        return result

    def getAllUsers(self):
        dao = UsersDAO()
        users_list = dao.getAllUsers()
        result_list = []
        for row in users_list:
            result = self.build_user_dict(row)
            result_list.append(result)
        return jsonify(Users=result_list)

    def getUsersById(self, sid):
        dao = UsersDAO()
        row = dao.getUsersById(sid)
        if not row:
            return jsonify(Error="User Not Found"), 404
        else:
            part = self.build_user_dict(row)
        return jsonify(Users=part)

    def searchUsers(self, args):
        ufirstname = args.get('ufirstname')
        ulastname = args.get('ulastname')
        dao = UsersDAO()
        users_list = []
        if (len(args) == 2) and ufirstname and ulastname:
            users_list = dao.getUsersByFirstnameandLastname(ufirstname, ulastname)
        elif (len(args) == 1) and ufirstname:
            users_list = dao.getUsersByFirstname(ufirstname)
        elif (len(args) == 1) and ulastname:
            users_list = dao.getUsersByLastname(ulastname)
        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in users_list:
            result = self.build_user_dict(row)
            result_list.append(result)
        return jsonify(User=result_list)

    def getConsumerByUsersId(self, uid):
        dao = UsersDAO()
        if not dao.getUsersById(uid):
            return jsonify(Error="User Not Found"), 404
        consumer_list = dao.getConsumerByUsersId(uid)
        result_list = []
        for row in consumer_list:
            result = self.build_consumer_dict(row)
            result_list.append(result)
        return jsonify(User=result_list)

    def getSupplierByUsersId(self, uid):
        dao = UsersDAO()
        if not dao.getUsersById(uid):
            return jsonify(Error="User Not Found"), 404
        supplier_list = dao.getSupplierByUsersId(uid)
        result_list = []
        for row in supplier_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(User=result_list)

    def getSysAdmByUsersId(self, uid):
        dao = UsersDAO()
        if not dao.getUsersById(uid):
            return jsonify(Error="User Not Found"), 404
        sysadm_list = dao.getSysAdmByUsersId(uid)
        result_list = []
        for row in sysadm_list:
            result = self.build_systemadmin_dict(row)
            result_list.append(result)
        return jsonify(User=result_list)

    def insertUsersJson(self, json):
        ufirstname = json['ufirstname']
        ulastname = json['ulastname']
        if ufirstname and ulastname:
            dao = UsersDAO()
            uid = dao.insert(ufirstname, ulastname)
            result = self.build_user_attributes(uid, ufirstname, ulastname)
            return jsonify(Users=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def updateUsers(self, uid, form):
        dao = UsersDAO()
        if not dao.getUsersById(uid):
            return jsonify(Error="User not found."), 404
        else:
            if len(form) != 2:
                return jsonify(Error="Malformed update request"), 400
            else:
                ufirstname = form['ufirstname']
                ulastname = form['ulastname']
                if ufirstname and ulastname:
                    dao.update(uid, ufirstname, ulastname)
                    result = self.build_user_attributes(uid, ufirstname, ulastname)
                    return jsonify(Users=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def deleteUsers(self, uid):
        dao = UsersDAO()
        if not dao.getUsersById(uid):
            return jsonify(Error="User not found."), 404
        else:
            dao.delete(uid)
            return jsonify(DeleteStatus="OK"), 200
