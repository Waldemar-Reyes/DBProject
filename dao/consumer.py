from config.dbconfig import pg_config
import psycopg2


class ConsumerDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllConsumer(self):
        cursor = self.conn.cursor()
        query = "select * from consumer;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getConsumerById(self, consid):
        cursor = self.conn.cursor()
        query = "select * from consumer where consid = %s;"
        cursor.execute(query, (consid,))
        result = cursor.fetchone()
        return result

    def getConsumerByUsername(self, consusername):
        cursor = self.conn.cursor()
        query = "select * from consumer where consusername = %s;"
        cursor.execute(query, (consusername,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getOrdersByConsumerId(self, consid):
        cursor = self.conn.cursor()
        query = "select odid, odnumber from orders natural inner join consumer where consid = %s;"
        cursor.execute(query, (consid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPayMethodByConsumerId(self, consid):
        cursor = self.conn.cursor()
        query = "select pmid, pmname from pay_method  natural inner join consumer where consid = %s;"
        cursor.execute(query, (consid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getReservationByConsumerId(self, consid):
        cursor = self.conn.cursor()
        query = "select resid, restype, resprice, resstock, reslocation, restime from reservation natural inner join consumer where consid = %s;"
        cursor.execute(query, (consid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByConsumerId(self, consid):
        cursor = self.conn.cursor()
        query = "select rid, rname, rtype, rprice, rstock, rlocation from resources natural inner join consumer where consid = %s;"
        cursor.execute(query, (consid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, consusername):
        cursor = self.conn.cursor()
        query = "insert into consumer(consusername) values (%s) returning consid;"
        cursor.execute(query, (consusername,))
        consid = cursor.fetchone()[0]
        self.conn.commit()
        return consid

    def update(self, consid, consusername):
        cursor = self.conn.cursor()
        query = "update consumer set consusername = %s where consid = %s;"
        cursor.execute(query, (consusername, consid,))
        self.conn.commit()
        return consid

    def delete(self, consid):
        cursor = self.conn.cursor()
        query = "delete from consumer where consid = %s;"
        cursor.execute(query, (consid,))
        self.conn.commit()
        return consid
