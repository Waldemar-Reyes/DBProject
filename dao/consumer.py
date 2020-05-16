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
        query = "select * from orders natural inner join makes natural inner join consumer where consid = %s;"
        cursor.execute(query, (consid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPayMethodByConsumerId(self, consid):
        cursor = self.conn.cursor()
        query = "select * from pay_method natural inner join owns natural inner join consumer where consid = %s;"
        cursor.execute(query, (consid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getReservationByConsumerId(self, consid):
        cursor = self.conn.cursor()
        query = "select * from reservation natural inner join requests natural inner join consumer where consid = %s;"
        cursor.execute(query, (consid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByConsumerId(self, consid):
        cursor = self.conn.cursor()
        query = "select * from resources natural inner join asks natural inner join reservation natural inner join requests natural inner join consumer where consid = %s;"
        cursor.execute(query, (consid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def populateMakes(self, odid, consid):
        cursor = self.conn.cursor()
        query = "insert into makes(odid, consid) values (%s, %s) returning odid;"
        cursor.execute(query, (odid, consid,))
        odid = cursor.fetchone()[0]
        self.conn.commit()
        return odid

    def insert(self, consusername):
        cursor = self.conn.cursor()
        query = "insert into consumer(consusername) values (%s) returning consid;"
        cursor.execute(query, (consusername,))
        consid = cursor.fetchone()[0]
        self.conn.commit()
        return consid

    def insertConsumerAsNewUsers(self, uid, consusername):
        cursor = self.conn.cursor()
        query = "insert into consumer(uid, consusername) values (%s, %s) returning consid;"
        cursor.execute(query, (uid, consusername,))
        consid = cursor.fetchone()[0]
        self.conn.commit()
        return consid

    def update(self, consid, uid, consusername):
        cursor = self.conn.cursor()
        query = "update consumer set uid = %s, consusername = %s where consid = %s;"
        cursor.execute(query, (uid, consusername, consid,))
        self.conn.commit()
        return consid

    def delete(self, consid):
        cursor = self.conn.cursor()
        query = "delete from consumer where consid = %s;"
        cursor.execute(query, (consid,))
        self.conn.commit()
        return consid
