from config.dbconfig import pg_config
import psycopg2


class CompanyDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllCompany(self):
        cursor = self.conn.cursor()
        query = "select * from company;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCompanyById(self, compid):
        cursor = self.conn.cursor()
        query = "select * from company where compid = %s;"
        cursor.execute(query, (compid,))
        result = cursor.fetchone()
        return result

    def getCompanyByCompname(self, compname):
        cursor = self.conn.cursor()
        query = "select * from company where compname = %s;"
        cursor.execute(query, (compname,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getConsumerByCompanyId(self, compid):
        cursor = self.conn.cursor()
        query = "select compid, compname, consid, consusername from consumer natural inner join makes natural inner join orders natural inner join belongs natural inner join resources natural inner join supplies natural inner join supplier natural inner join works natural inner join company where compid = %s;"
        cursor.execute(query, (compid,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getResourcesByCompanyId(self, compid):
        cursor = self.conn.cursor()
        query = "select compid, compname, rid, rname, rtype, rprice, rstock, rlocation from resources natural inner join supplies natural inner join supplier natural inner join works natural inner join company where compid = %s;"
        cursor.execute(query, (compid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierByCompanyId(self, compid):
        cursor = self.conn.cursor()
        query = "select compid, compname, sid, susername, scompany from supplier natural inner join works natural inner join company where compid = %s"
        cursor.execute(query, (compid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def supplierWorksForCompany(self, compid, sid):
        cursor = self.conn.cursor()
        query = "insert into works(compid, sid) values (%s, %s);"
        cursor.execute(query, (compid, sid,))
        self.conn.commit()
        return compid

    def insert(self, compname):
        cursor = self.conn.cursor()
        query = "insert into company(compname) values (%s) returning compid;"
        cursor.execute(query, (compname,))
        compid = cursor.fetchone()[0]
        self.conn.commit()
        return compid

    def update(self, compid, compname):
        cursor = self.conn.cursor()
        query = "update company set compname = %s where compid = %s;"
        cursor.execute(query, (compname, compid,))
        self.conn.commit()
        return compid

    def delete(self, compid):
        cursor = self.conn.cursor()
        query = "delete from company where compid = %s;"
        cursor.execute(query, (compid,))
        self.conn.commit()
        return compid
