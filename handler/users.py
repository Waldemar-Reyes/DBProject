from flask import jsonify
from dao.users import UsersDAO


class UsersHandler:
    def build_user_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['ufirstname'] = row[1]
        result['ulastname'] = row[2]
        return result
      
    def build_user_attributes(self, uid, ufirstname, ulastname):
        result = {}
        result['uid'] = uid
        result['ufirstname'] = ufirstname
        result['ulastname'] = ulastname
        return result

    def searchUserss(self, args):
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

    def insertUsersJson(self, json):
        uid = json['uid']
        ufirstname = json['ufirstname']
        ulastname = json['ulastname']
        if uid and ufirstname and ulastname:
            dao = UsersDAO()
            uid = dao.insert(ufirstname, ulastname)
            result = self.build_user_attributes(uid, ufirstname, ulastname)
            return jsonify(Supplier=result), 201
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
                    return jsonify(Supplier=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def deleteUsers(self, uid):
        dao = UsersDAO()
        if not dao.getUsersById(uid):
            return jsonify(Error="User not found."), 404
        else:
            dao.delete(uid)
            return jsonify(DeleteStatus="OK"), 200
