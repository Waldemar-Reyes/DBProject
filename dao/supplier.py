from config.dbconfig import pg_config
import psycopg2


class SupplierDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllSupplier(self):
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
    
    def getSupplierByUsername(self, username):
        cursor = self.conn.cursor()
        query = "select * from supplier where susername = %s;"
        cursor.execute(query, (username,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierByCompany(self, company):
        cursor = self.conn.cursor()
        query = "select * from supplier where scompany = %s;"
        cursor.execute(query, (company,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getCompanyBySupplierId(self, sid):
        cursor = self.conn.cursor()
        query = "select * from company natural inner join works natural inner join supplier where sid = %s;"
        cursor.execute(query, (sid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getOrdersBySupplierId(self, sid):
        cursor = self.conn.cursor()
        query = "select * from orders natural inner join belongs natural inner join resources natural inner join supplies natural inner join supplier where sid = %s;"
        cursor.execute(query, (sid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPayMethodBySupplierId(self, sid):
        cursor = self.conn.cursor()
        query = "select * from pay_method natural inner join pays natural inner join orders natural inner join belongs natural inner join resources natural inner join supplies natural inner join supplier where sid = %s;"
        cursor.execute(query, (sid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getReservationBySupplierId(self, sid):
        cursor = self.conn.cursor()
        query = "select * from reservation natural inner join asks natural inner join resources natural inner join supplies natural inner join supplier where sid = %s;"
        cursor.execute(query, (sid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierId(self, sid):
        cursor = self.conn.cursor()
        query = "select * from resources natural inner join supplies natural inner join supplier where sid = %s;"
        cursor.execute(query, (sid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, susername, scompany):
        cursor = self.conn.cursor()
        query = "insert into supplier(susername, scompany) values (%s, %s) returning sid;"
        cursor.execute(query, (susername, scompany,))
        sid = cursor.fetchone()[0]
        self.conn.commit()
        return sid

    def insertSupplierAsNewUsers(self, uid, susername, scompany):
        cursor = self.conn.cursor()
        query = "insert into supplier(uid, susername, scompany) values (%s, %s, %s) returning sid;"
        cursor.execute(query, (uid, susername, scompany,))
        sid = cursor.fetchone()[0]
        self.conn.commit()
        return sid

    def update(self, sid, uid, susername, scompany):
        cursor = self.conn.cursor()
        query = "update supplier set uid = %s, susername = %s, scompany = %s where sid = %s;"
        cursor.execute(query, (uid, susername, scompany, sid,))
        self.conn.commit()
        return sid

    def delete(self, sid):
        cursor = self.conn.cursor()
        query = "delete from supplier where sid = %s;"
        cursor.execute(query, (sid,))
        self.conn.commit()
        return sid
