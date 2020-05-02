from flask import jsonify
from dao.user import UserDAO

class UserHandler:
    def build_user_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['ufirstname'] = row[1]
        return result
      
     def build_reservation_attributes(self, uid, ufirstname):
        result = {}
        result['uid'] = uid
        result['ufirstname'] = ufirstname
        return result

    def insertUserJson(self, json):
        user = json['ufirstname']
        if user:
            dao = UserDAO()
            uid= dao.insert(ufirstname)
            result = self.build_reservation_attributes(uid, ufirstname)
            return jsonify(User=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def updateUser(self, uid, form):
        dao = ReservationDAO()
        if not dao.getUserById(uid):
            return jsonify(Error="User not found."), 404
        else:
            if len(form) != 1:
                return jsonify(Error="Malformed update request"), 400
            else:
                ufirstname = form['ufirstname']
                if ufirstname:
                    dao.update(uid, ufirstname)
                    result = self.build_user_attributes(uid, ufirstname)
                    return jsonify(User=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def deleteUser(self, uid):
        dao = UserDAO()
        if not dao.getUserById(resid):
            return jsonify(Error="user not found."), 404
        else:
            dao.delete(uid)
            return jsonify(DeleteStatus="OK"), 200
