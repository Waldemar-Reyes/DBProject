from flask import jsonify
from dao.resources import ResourcesDAO


class ResourcesHandler:
    def build_resource_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['rname'] = row[1]
        result['rtype'] = row[2]
        result['rprice'] = row[3]
        result['rlocation'] = row[3]
        result['rstock'] = row[5]
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

    def build_resource_attributes(self, rid, rname, rtype, rprice, rlocation, rstock):
        result = {}
        result['rid'] = rid
        result['rname'] = rname
        result['rtype'] = rtype
        result['rprice'] = rprice
        result['rlocation'] = rlocation
        result['rstock'] = rstock
        return result

    def getAllResources(self):
        dao = ResourcesDAO()
        payment_list = dao.getAllResources()
        result_list = []
        for row in payment_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def getResourcesById(self, rid):
        dao = ResourcesDAO()
        row = dao.getResourcesById(rid)
        if not row:
            return jsonify(Error="Resource Not Found"), 404
        else:
            resources = self.build_resource_dict(row)
        return jsonify(Resources=resources)

    def searchResources(self, args):
        rid = args.get('rid')
        rname = args.get('rname')
        rtype = args.get('rtype')
        rprice = args.get('rprice')
        rlocation = args.get('rlocation')
        rstock = args.get('rstock')
        dao = ResourcesDAO()
        resources_list = []
        if (len(args) == 5) and rname and rtype and rprice and rstock and rlocation:
            resources_list = dao.getResourcesByNameandTypeandPriceandStockandLocation(rname, rtype, rprice, rstock, rlocation)
        if (len(args) == 4) and rname and rtype and rprice and rstock:
            resources_list = dao.getResourcesByNameandTypeandPriceandStock(rname, rtype, rprice, rstock)
        if (len(args) == 4) and rname and rtype and rprice and rlocation:
            resources_list = dao.getResourcesByNameandTypeandPriceandLocation(rname, rtype, rprice, rlocation)
        if (len(args) == 4) and rname and rtype and rstock and rlocation:
            resources_list = dao.getResourcesByNameandTypeandStockandLocation(rname, rtype, rstock, rlocation)
        if (len(args) == 4) and rname and rprice and rstock and rlocation:
            resources_list = dao.getResourcesByNameandPriceandStockandLocation(rname, rprice, rstock, rlocation)
        if (len(args) == 4) and rtype and rprice and rstock and rlocation:
            resources_list = dao.getResourcesByTypeandPriceandStockandLocation(rtype, rprice, rstock, rlocation)
        if (len(args) == 3) and rname and rtype and rprice:
            resources_list = dao.getResourcesByNameandTypeandPrice(rname, rtype, rprice)
        if (len(args) == 3) and rname and rtype and rstock:
            resources_list = dao.getResourcesByNameandTypeandStock(rname, rtype, rstock)
        if (len(args) == 3) and rname and rtype and rlocation:
            resources_list = dao.getResourcesByNameandTypeandLocation(rname, rtype, rlocation)
        if (len(args) == 3) and rname and rprice and rstock:
            resources_list = dao.getResourcesByNameandPriceandStock(rname, rprice, rstock)
        if (len(args) == 3) and rname and rprice and rlocation:
            resources_list = dao.getResourcesByNameandPriceandLocation(rname, rprice, rlocation)
        if (len(args) == 3) and rname and rstock and rlocation:
            resources_list = dao.getResourcesByNameandStockandLocation(rname, rstock, rlocation)
        if (len(args) == 3) and rtype and rprice and rstock:
            resources_list = dao.getResourcesByTypeandPriceandStock(rtype, rprice, rstock)
        if (len(args) == 3) and rtype and rprice and rlocation:
            resources_list = dao.getResourcesByTypeandPriceandLocation(rtype, rprice, rlocation)
        if (len(args) == 3) and rtype and rstock and rlocation:
            resources_list = dao.getResourcesByTypeandStockandLocation(rtype, rstock, rlocation)
        if (len(args) == 3) and rprice and rstock and rlocation:
            resources_list = dao.getResourcesByPriceandStockandLocation(rprice, rstock, rlocation)
        if (len(args) == 2) and rname and rtype:
            resources_list = dao.getResourcesByNameandType(rname, rtype)
        if (len(args) == 2) and rname and rprice:
            resources_list = dao.getResourcesByNameandPrice(rname, rprice)
        if (len(args) == 2) and rname and rstock:
            resources_list = dao.getResourcesByNameandStock(rname, rstock)
        if (len(args) == 2) and rname and rlocation:
            resources_list = dao.getResourcesByNameandLocation(rname, rlocation)
        if (len(args) == 2) and rtype and rprice:
            resources_list = dao.getResourcesByTypeandPrice(rtype, rprice)
        if (len(args) == 2) and rtype and rstock:
            resources_list = dao.getResourcesByTypeandStock(rtype, rstock)
        if (len(args) == 2) and rtype and rlocation:
            resources_list = dao.getResourcesByTypeandLocation(rtype, rlocation)
        if (len(args) == 2) and rprice and rstock:
            resources_list = dao.getResourcesByPriceandStock(rprice, rstock)
        if (len(args) == 2) and rprice and rlocation:
            resources_list = dao.getResourcesByPriceandLocation(rprice, rlocation)
        if (len(args) == 2) and rstock and rlocation:
            resources_list = dao.getResourcesByStockandLocation(rstock, rlocation)
        if (len(args) == 1) and rname:
            resources_list = dao.getResourcesByName(rname)
        if (len(args) == 1) and rtype:
            resources_list = dao.getResourcesByType(rtype)
        if (len(args) == 1) and rprice:
            resources_list = dao.getResourcesByPrice(rprice)
        if (len(args) == 1) and rstock:
            resources_list = dao.getResourcesByStock(rstock)
        if (len(args) == 1) and rlocation:
            resources_list = dao.getResourcesByLocation(rlocation)
        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in resources_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def getCompanyByResourcesId(self, rid):
        dao = ResourcesDAO()
        if not dao.getResourcesById(rid):
            return jsonify(Error="Resource Not Found"), 404
        company_list = dao.getCompanyByResourcesId(rid)
        result_list = []
        for row in company_list:
            result = self.build_company_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def getConsumerByResourcesId(self, rid):
        dao = ResourcesDAO()
        if not dao.getResourcesById(rid):
            return jsonify(Error="Resource Not Found"), 404
        consumer_list = dao.getConsumerByResourcesId(rid)
        result_list = []
        for row in consumer_list:
            result = self.build_consumer_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def insertResourcesJson(self, json):
        rname = json['rname']
        rtype = json['rtype']
        rprice = json['rprice']
        rlocation = json['rlocation']
        rstock = json['rstock']
        if rname and rtype and rprice and rlocation and rstock:
            dao = ResourcesDAO()
            rid = dao.insert(rname, rtype, rprice, rlocation, rstock)
            result = self.build_resource_attributes(rid, rname, rtype, rprice, rlocation, rstock)
            return jsonify(Resoure=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def updateResources(self, rid, form):
        dao = ResourcesDAO()
        if not dao.getResourcesById(rid):
            return jsonify(Error="Resource not found."), 404
        else:
            if len(form) != 5:
                return jsonify(Error="Malformed update request"), 400
            else:
                rname = form['rname']
                rtype = form['rtype']
                rprice = form['rprice']
                rlocation = form['rlocation']
                rstock = form['rstock']
                if rname and rtype and rprice and rlocation and rstock:
                    dao.update(rid, rname, rtype, rprice, rlocation, rstock)
                    result = self.build_resource_attributes(rid, rname, rtype, rprice, rlocation, rstock)
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
