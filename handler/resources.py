from flask import jsonify
from dao.resources import ResourcesDAO


class ResourcesHandler:
    def build_resource_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['rname'] = row[1]
        result['rprice'] = row[2]
        result['rlocation'] = row[3]
        result['ramount'] = row[4]
        return result
      
    def build_resource_attributes(self, rid, rname, rprice, rlocation, ramount):
        result = {}
        result['rid'] = rid
        result['rname'] = rname
        result['rprice'] = rprice
        result['rlocation'] = rlocation
        result['ramount'] = ramount
        return result

    def insertResourcesJson(self, json):
        rname = json['rname']
        rprice = json['rprice']
        rlocation = json['rlocation']
        ramount = json['ramount']
        if rname and rprice and rlocation and ramount:
            dao = ResourcesDAO()
            rid = dao.insert(rname, rprice, rlocation, ramount)
            result = self.build_resource_attributes(rid, rname, rprice, rlocation, ramount)
            return jsonify(Resoure=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def updateResources(self, rid, form):
        dao = ResourcesDAO()
        if not dao.getResourcesById(rid):
            return jsonify(Error="Resource not found."), 404
        else:
            if len(form) != 4:
                return jsonify(Error="Malformed update request"), 400
            else:
                rname = form['rname']
                rprice = form['rprice']
                rlocation = form['rlocation']
                ramount = form['ramount']
                if rname and rprice and rlocation and ramount:
                    dao.update(rid, rname, rprice, rlocation, ramount)
                    result = self.build_resource_attributes(rid, rname, rprice, rlocation, ramount)
                    return jsonify(Resource=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def deleteResources(self, rid):
        dao = ResourcesDAO()
        if not dao.getResourcesById(rid):
            return jsonify(Error="Resource not found."), 404
        else:
            dao.delete(rid)
            return jsonify(DeleteStatus="OK"), 200
