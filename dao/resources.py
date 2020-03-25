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
        query = "select rid, rname, rprice, ramount, rlocation from resources;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesById(self, rid):
        cursor = self.conn.cursor()
        query = "select rid, rname, rprice, ramount, rlocation from resources where rid = %s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result

    def getResourcesByPrice(self, price):
        cursor = self.conn.cursor()
        query = "select * from resources where rprice = %s;"
        cursor.execute(query, (price,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByAmount(self, amount):
        cursor = self.conn.cursor()
        query = "select * from resources where ramount = %s;"
        cursor.execute(query, (amount,))
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

    def getResourcesByPriceandAmount(self, price, amount):
        cursor = self.conn.cursor()
        query = "select * from resources where rprice = %s and ramount = %s;"
        cursor.execute(query, (price, amount))
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
    
    def getResourcesByAmountandLocation(self, amount, location):
        cursor = self.conn.cursor()
        query = "select * from resources where ramount = %s and rlocation = %s;"
        cursor.execute(query, (amount, location))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getResourcesByPriceandAmountandLocation(self, price, amount, location):
        cursor = self.conn.cursor()
        query = "select * from resources where rprice = %s and ramount = %s and rlocation = %s;"
        cursor.execute(query, (price, amount, location))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByPartId(self, pid):
        cursor = self.conn.cursor()
        query = "select sid, sname, scity, sphone from parts natural inner join supplier natural inner join supplies where pid = %s;"
        cursor.execute(query, (pid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, rname, rprice, ramount, rlocation):
        cursor = self.conn.cursor()
        query = "insert into resources(rname, rprice, ramount, rlocation) values (%s, %s, %s, %s) returning rid;"
        cursor.execute(query, (rname, rprice, ramount, rlocation,))
        rid = cursor.fetchone()[0]
        self.conn.commit()
        return rid

    def delete(self, rid):
        cursor = self.conn.cursor()
        query = "delete from resources where rid = %s;"
        cursor.execute(query, (rid,))
        self.conn.commit()
        return rid

    def update(self, rid, rname, rprice, ramount, rlocation):
        cursor = self.conn.cursor()
        query = "update resources set rname = %s, rprice = %s, ramount = %s, rlocation = %s where rid = %s;"
        cursor.execute(query, (rname, rprice, ramount, rlocation, rid,))
        self.conn.commit()
        return rid

    def getCountByResourceId(self):
        cursor = self.conn.cursor()
        query = "select rid, rname, sum(stock) from resources natural inner join supplier group by sid, susername order by susername;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result