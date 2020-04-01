from config.dbconfig import pg_config
import psycopg2

class SupplierDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllSuppliers(self):
        cursor = self.conn.cursor()
        query = "select * from supplier;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierById(self, sid):
            cursor = self.conn.cursor()
            query = "select * from supplier where sid = %s;"
            cursor.execute(query, (sid,))
            result = cursor.fetchone()
            return result
    
    def getSuppliersByUsername(self, username):
        cursor = self.conn.cursor()
        query = "select * from supplier where susername = %s;"
        cursor.execute(query, (username,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByCompany(self, company):
        cursor = self.conn.cursor()
        query = "select * from supplier where scompany = %s;"
        cursor.execute(query, (company,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getResourcesBySupplierId(self, sid):
        cursor = self.conn.cursor()
        query = "select rid, rname, rprice, ramount, rlocation from resources natural inner join supplier where sid = %s;"
        cursor.execute(query, (sid,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getCompanyBySupplierId(self, sid):
        cursor = self.conn.cursor()
        query = "select compid, compname from company natural inner join supplier where sid = %s;"
        cursor.execute(query, (sid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, susername, scompany):
        cursor = self.conn.cursor()
        query = "insert into supplier(susername, scompany) values (%s, %s) returning sid;"
        cursor.execute(query, (susername, scompany))
        sid = cursor.fetchone()[0]
        self.conn.commit()
        return sid