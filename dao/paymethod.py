from config.dbconfig import pg_config
import psycopg2


class PayMethodDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllPayMethod(self):
        cursor = self.conn.cursor()
        query = "select * from pay_method;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPayMethodById(self, pmid):
        cursor = self.conn.cursor()
        query = "select * from pay_method where pmid = %s;"
        cursor.execute(query, (pmid,))
        result = cursor.fetchone()
        return result

    def getPayMethodByName(self, pmname):
        cursor = self.conn.cursor()
        query = "select * from pay_method where pmname = %s;"
        cursor.execute(query, (pmname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getConsumerByPayMethodId(self, pmid):
        cursor = self.conn.cursor()
        query = "select pmid, pmname, consid, consusername from consumer natural inner join owns natural inner join pay_method where pmid = %s;"
        cursor.execute(query, (pmid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierByPayMethodId(self, pmid):
        cursor = self.conn.cursor()
        query = "select pmid, pmname, sid, susername, scompany from supplier natural inner join supplies natural inner join resources natural inner join belongs natural inner join orders natural inner join pays natural inner join pay_method where pmid = %s;"
        cursor.execute(query, (pmid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insertPayMethodOfConsumer(self, pmid, consid):
        cursor = self.conn.cursor()
        query = "insert into owns(pmid, consid) values (%s, %s) returning pmid;"
        cursor.execute(query, (pmid, consid,))
        pmid = cursor.fetchone()[0]
        self.conn.commit()
        return pmid

    def insertNewConsumerandPayMethod(self, consid):
        cursor = self.conn.cursor()
        query = "insert into pay_method(pmname) values ('free') returning pmid;"
        cursor.execute(query)
        pmid = cursor.fetchone()[0]
        query = "insert into owns(pmid, consid) values (%s, %s) returning pmid;"
        cursor.execute(query, (pmid, consid,))
        self.conn.commit()
        return pmid

    def insert(self, pmname):
        cursor = self.conn.cursor()
        query = "insert into pay_method(pmname) values (%s) returning pmid;"
        cursor.execute(query, (pmname,))
        pmid = cursor.fetchone()[0]
        self.conn.commit()
        return pmid

    def update(self, pmid, pmname):
        cursor = self.conn.cursor()
        query = "update pay_method set pmname = %s where pmid = %s;"
        cursor.execute(query, (pmname, pmid,))
        self.conn.commit()
        return pmid

    def delete(self, pmid):
        cursor = self.conn.cursor()
        query = "delete from pay_method where pmid = %s;"
        cursor.execute(query, (pmid,))
        self.conn.commit()
        return pmid
