from flask import jsonify
from dao.reservation import ReservationDAO

class ReservationHandler:
    def build_reservation_dict(self, row):
        result = {}
        result['resid'] = row[0]
        result['restime'] = row[1]
        return result
      
     def build_reservation_attributes(self, resid, restime):
        result = {}
        result['resid'] = resid
        result['restime'] = restime
        return result

    def insertReservationJson(self, json):
        reservation = json['restime']
        if reservation:
            dao = ReservationDAO()
            resid = dao.insert(restime)
            result = self.build_reservation_attributes(resid, restime)
            return jsonify(Reservation=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def updateReservation(self, resid, form):
        dao = ReservationDAO()
        if not dao.getreservationById(resid):
            return jsonify(Error="Reservation not found."), 404
        else:
            if len(form) != 1:
                return jsonify(Error="Malformed update request"), 400
            else:
                restime = form['restime']
                if restime:
                    dao.update(resid, restime)
                    result = self.build_reservation_attributes(resid, restime)
                    return jsonify(Reservation=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def deletereservation(self, resid):
        dao = ReservationDAO()
        if not dao.getReservationById(resid):
            return jsonify(Error="Reservation not found."), 404
        else:
            dao.delete(resid)
            return jsonify(DeleteStatus="OK"), 200
