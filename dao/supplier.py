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
    
    def getSupplierByUsernameandCompany(self, username, company):
        cursor = self.conn.cursor()
        query = "select * from supplier where susername = %s and scompany = %s;"
        cursor.execute(query, (username, company))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getCompanyBySupplierId(self, sid):
        cursor = self.conn.cursor()
        query = "select sid, susername, scompany, compid, compname from company natural inner join works natural inner join supplier where sid = %s;"
        cursor.execute(query, (sid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getOrdersBySupplierId(self, sid):
        cursor = self.conn.cursor()
        query = "select sid, susername, scompany, odid, odnumber, odtime from orders natural inner join belongs natural inner join resources natural inner join supplies natural inner join supplier where sid = %s;"
        cursor.execute(query, (sid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPayMethodBySupplierId(self, sid):
        cursor = self.conn.cursor()
        query = "select sid, susername, scompany, pmid, pmname from pay_method natural inner join pays natural inner join orders natural inner join belongs natural inner join resources natural inner join supplies natural inner join supplier where sid = %s;"
        cursor.execute(query, (sid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getReservationBySupplierId(self, sid):
        cursor = self.conn.cursor()
        query = "select sid, susername, scompany, resid, resname, restype, resprice, resstock, reslocation, restime from reservation natural inner join asks natural inner join resources natural inner join supplies natural inner join supplier where sid = %s;"
        cursor.execute(query, (sid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierId(self, sid):
        cursor = self.conn.cursor()
        query = "select sid, susername, scompany, rid, rname, rtype, rprice, rstock, rlocation from resources natural inner join supplies natural inner join supplier where sid = %s;"
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

    def updateSupplierWithCompany(self, sid, uid, susername, scompany, compid):
        cursor = self.conn.cursor()
        query = "update supplier set uid = %s, susername = %s, scompany = %s where sid = %s;"
        cursor.execute(query, (uid, susername, scompany, sid,))
        self.conn.commit()
        if not self.getWorksPair(compid, sid):
            query = "insert into works(compid, sid) values (%s, %s);"
            cursor.execute(query, (compid, sid,))
            self.conn.commit()
        else:
            oldcompid = self.getOldCompid(compid, sid)
            query = "update works set compid = %s, sid = %s where compid = %s and sid = %s;"
            cursor.execute(query, (compid, sid, oldcompid[0][0], sid,))
            self.conn.commit()
        return sid

    def getWorksPair(self, compid, sid):
        cursor = self.conn.cursor()
        query = "select * from works where compid = %s and sid = %s;"
        cursor.execute(query, (compid, sid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getOldCompid(self, compid, sid):
        cursor = self.conn.cursor()
        query = "select compid from works where compid = %s and sid = %s;"
        cursor.execute(query, (compid, sid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def delete(self, sid):
        cursor = self.conn.cursor()
        query = "delete from supplier where sid = %s;"
        cursor.execute(query, (sid,))
        self.conn.commit()
        return sid
