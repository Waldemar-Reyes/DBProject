from config.dbconfig import pg_config
import psycopg2


class ResourcesDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllResources(self):
        cursor = self.conn.cursor()
        query = "select rid, rname, rtype, rprice, rstock, rlocation from resources;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesById(self, rid):
        cursor = self.conn.cursor()
        query = "select rid, rname, rtype, rprice, rstock, rlocation from resources where rid = %s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result

    def getResourcesByName(self, rname):
        cursor = self.conn.cursor()
        query = "select * from resources where rname = %s;"
        cursor.execute(query, (rname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByType(self, rtype):
        cursor = self.conn.cursor()
        query = "select * from resources where rtype = %s;"
        cursor.execute(query, (rtype,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByPrice(self, price):
        cursor = self.conn.cursor()
        query = "select * from resources where rprice = %s;"
        cursor.execute(query, (price,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByStock(self, stock):
        cursor = self.conn.cursor()
        query = "select * from resources where rstock = %s;"
        cursor.execute(query, (stock,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByLocation(self, location):
        cursor = self.conn.cursor()
        query = "select * from resources where rlocation = %s;"
        cursor.execute(query, (location,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByPriceandStock(self, price, stock):
        cursor = self.conn.cursor()
        query = "select * from resources where rprice = %s and rstock = %s;"
        cursor.execute(query, (price, stock))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByPriceandLocation(self, price, location):
        cursor = self.conn.cursor()
        query = "select * from resources where rprice = %s and rlocation = %s;"
        cursor.execute(query, (price, location))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByStockandLocation(self, stock, location):
        cursor = self.conn.cursor()
        query = "select * from resources where rstock = %s and rlocation = %s;"
        cursor.execute(query, (stock, location))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByPriceandStockandLocation(self, price, stock, location):
        cursor = self.conn.cursor()
        query = "select * from resources where rprice = %s and rstock = %s and rlocation = %s;"
        cursor.execute(query, (price, stock, location))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByNameandPrice(self, name, price):
        cursor = self.conn.cursor()
        query = "select * from resources where rname = %s and rprice = %s;"
        cursor.execute(query, (name, price))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByNameandStock(self, name, stock):
        cursor = self.conn.cursor()
        query = "select * from resources where rname = %s and rstock = %s;"
        cursor.execute(query, (name, stock))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByNameandLocation(self, name, location):
        cursor = self.conn.cursor()
        query = "select * from resources where rname = %s and rlocation = %s;"
        cursor.execute(query, (name, location))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByNameandPriceandStock(self, name, price, stock):
        cursor = self.conn.cursor()
        query = "select * from resources where rname = %s and rprice = %s and rstock = %s;"
        cursor.execute(query, (name, price, stock))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByNameandPriceandLocation(self, name, price, location):
        cursor = self.conn.cursor()
        query = "select * from resources where rname = %s and rprice = %s and rlocation = %s;"
        cursor.execute(query, (name, price, location))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByNameandStockandLocation(self, name, stock, location):
        cursor = self.conn.cursor()
        query = "select * from resources where rname = %s and rstock = %s and rlocation = %s;"
        cursor.execute(query, (name, stock, location))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByNameandPriceandStockandLocation(self, name, price, stock, location):
        cursor = self.conn.cursor()
        query = "select * from resources where rname = %s and rprice = %s and rstock = %s and rlocation = %s;"
        cursor.execute(query, (name, price, stock, location))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByNameandType(self, name, rtype):
        cursor = self.conn.cursor()
        query = "select * from resources where rname = %s and rtype = %s;"
        cursor.execute(query, (name, rtype))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTypeandPrice(self, rtype, price):
        cursor = self.conn.cursor()
        query = "select * from resources where rtype = %s and rprice = %s;"
        cursor.execute(query, (rtype, price))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTypeandStock(self, rtype, stock):
        cursor = self.conn.cursor()
        query = "select * from resources where rtype = %s and rstock = %s;"
        cursor.execute(query, (rtype, stock))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTypeandLocation(self, rtype, location):
        cursor = self.conn.cursor()
        query = "select * from resources where rtype = %s and rlocation = %s;"
        cursor.execute(query, (rtype, location))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTypeandPriceandStock(self, rtype, price, stock):
        cursor = self.conn.cursor()
        query = "select * from resources where rtype = %s and rprice = %s and rstock = %s;"
        cursor.execute(query, (rtype, price, stock))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTypeandPriceandLocation(self, rtype, price, location):
        cursor = self.conn.cursor()
        query = "select * from resources where rtype = %s and rprice = %s and rlocation = %s;"
        cursor.execute(query, (rtype, price, location))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTypeandStockandLocation(self, rtype, stock, location):
        cursor = self.conn.cursor()
        query = "select * from resources where rtype = %s and rstock = %s and rlocation = %s;"
        cursor.execute(query, (rtype, stock, location))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByNameandTypeandPrice(self, name, rtype, price):
        cursor = self.conn.cursor()
        query = "select * from resources where rname = %s and rtype = %s and rprice = %s;"
        cursor.execute(query, (name, rtype, price))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByNameandTypeandStock(self, name, rtype, stock):
        cursor = self.conn.cursor()
        query = "select * from resources where rname = %s and rtype = %s and rstock = %s;"
        cursor.execute(query, (name, rtype, stock))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByNameandTypeandLocation(self, name, rtype, location):
        cursor = self.conn.cursor()
        query = "select * from resources where rname = %s and rtype = %s and rlocation = %s;"
        cursor.execute(query, (name, rtype, location))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByNameandTypeandPriceandStock(self, name, rtype, price, stock):
        cursor = self.conn.cursor()
        query = "select * from resources where rname = %s and rtype = %s and rprice = %s and rstock = %s;"
        cursor.execute(query, (name, rtype, price, stock))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByNameandTypeandPriceandLocation(self, name, rtype, price, location):
        cursor = self.conn.cursor()
        query = "select * from resources where rname = %s and rtype = %s and rprice = %s and rlocation = %s;"
        cursor.execute(query, (name, rtype, price, location))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTypeandPriceandStockandLocation(self, rtype, price, stock, location):
        cursor = self.conn.cursor()
        query = "select * from resources where rtype = %s and rprice = %s and rstock = %s and rlocation = %s;"
        cursor.execute(query, (rtype, price, stock, location))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByNameandTypeandPriceandStockandLocation(self, name, rtype, price, stock, location):
        cursor = self.conn.cursor()
        query = "select * from resources where rname = %s and rtype = %s and rprice = %s and rstock = %s and rlocation = %s;"
        cursor.execute(query, (name, rtype, price, stock, location))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByNameandTypeandStockandLocation(self, name, rtype, stock, location):
        cursor = self.conn.cursor()
        query = "select * from resources where rname = %s and rtype = %s and rstock = %s and rlocation = %s;"
        cursor.execute(query, (name, rtype, stock, location))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getConsumerByResourcesId(self, rid):
        cursor = self.conn.cursor()
        query = "select * from consumer natural inner join requests natural inner join reservation natural inner join asks natural inner join resources where rid = %s;"
        cursor.execute(query, (rid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCompanyByResourcesId(self, rid):
        cursor = self.conn.cursor()
        query = "select * from company natural inner join works natural inner join supplier natural inner join supplies natural inner join resources where rid = %s;"
        cursor.execute(query, (rid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getStockByResourceNameandType(self, rname, rtype, rstock):
        # TODO Code that search for whole rstock
        # cursor = self.conn.cursor()
        # query = "set @fstock = (select sum(rstock) from resources where rname = %s and rtype =%s)"
        # result = cursor.execute(query, (rname, rtype,))
        cursor = self.conn.cursor()
        query = "set @fstock = (select rstock from resources where rname = %rname and rtype = %rtype and rstock > %rstock order by rstock asc limit 1)"
        result = cursor.execute(query, (rname, rtype, rstock,))
        return result

    def getToUpdateId(self, rname, rtype, rstock):
        cursor = self.conn.cursor()
        query = "set @fstock = (select rid from resources where rname = %rname and rtype = %rtype and rstock > %rstock order by rstock asc limit 1)"
        result = cursor.execute(query, (rname, rtype, rstock,))
        return result

    def updateStockAfterReservation(self, rid, rstock):
        cursor = self.conn.cursor()
        query = "update resources set rstock = %s where rid =%s;"
        result = cursor.execute(query, (rstock, rid))
        return result

    def insert(self, rname, rtype, rprice, rstock, rlocation):
        cursor = self.conn.cursor()
        query = "insert into resources(rname, rtype, rprice, rstock, rlocation) values (%s, %s, %s, %s, %s) returning rid;"
        cursor.execute(query, (rname, rtype, rprice, rstock, rlocation,))
        rid = cursor.fetchone()[0]
        self.conn.commit()
        return rid

    def update(self, rid, rname, rtype, rprice, rstock, rlocation):
        cursor = self.conn.cursor()
        query = "update resources set rname = %s, rtype = %s, rprice = %s, rstock = %s, rlocation = %s where rid = %s;"
        cursor.execute(query, (rname, rtype, rprice, rstock, rlocation, rid,))
        self.conn.commit()
        return rid

    def delete(self, rid):
        cursor = self.conn.cursor()
        query = "delete from resources where rid = %s;"
        cursor.execute(query, (rid,))
        self.conn.commit()
        return rid
