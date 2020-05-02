from flask import jsonify
from dao.resource import ResoruceDAO

class ResoruceHandler:
    def build_resource_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['rname'] = row[1]
        return result
      
     def build_resource_attributes(self, rid, rname):
        result = {}
        result['rid'] = rid
        result['rname'] = rname
        return result

    def insertResourceJson(self, json):
        resource = json['rname']
        if resource:
            dao = ResoruceDAO()
            rid = dao.insert(rname)
            result = self.build_resource_attributes(rid, rname)
            return jsonify(Resoure=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def updateResource(self, rid, form):
        dao = ResourceDAO()
        if not dao.getResourceById(rid):
            return jsonify(Error="Resource not found."), 404
        else:
            if len(form) != 1:
                return jsonify(Error="Malformed update request"), 400
            else:
                rname = form['rname']
                if rname:
                    dao.update(rid, rname)
                    result = self.build_resource_attributes(rid, rname)
                    return jsonify(Resource=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def deleteResource(self, rid):
        dao = ResourceDAO()
        if not dao.getResourceById(rid):
            return jsonify(Error="Resource not found."), 404
        else:
            dao.delete(rid)
            return jsonify(DeleteStatus="OK"), 200
