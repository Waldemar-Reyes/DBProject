from config.dbconfig import pg_config
import psycopg2


class ReservationDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllReservation(self):
        cursor = self.conn.cursor()
        query = "select * from reservation;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getReservationById(self, resid):
        cursor = self.conn.cursor()
        query = "select * from reservation where resid = %s;"
        cursor.execute(query, (resid,))
        result = cursor.fetchone()
        return result

    def getReservationByTime(self, restime):
        cursor = self.conn.cursor()
        query = "select * from reservation where restime = %s;"
        cursor.execute(query, (restime,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getConsumerByReservationId(self, resid):
        cursor = self.conn.cursor()
        query = "select consid, consusername from consumer natural inner join reservation where resid = %s;"
        cursor.execute(query, (resid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getOrdersByReservationId(self, resid):
        cursor = self.conn.cursor()
        query = "select odid, odnumber from orders natural inner join reservation where resid = %s;"
        cursor.execute(query, (resid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByReservationId(self, resid):
        cursor = self.conn.cursor()
        query = "select rid, rname, rprice, ramount, rlocation from resources natural inner join reservation where resid = %s;"
        cursor.execute(query, (resid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierByReservationId(self, resid):
        cursor = self.conn.cursor()
        query = "select sid, susername, scompany from supplier natural inner join reservations where resid = %s;"
        cursor.execute(query, (resid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, restime):
        cursor = self.conn.cursor()
        query = "insert into reservation(restime) values (%s) returning resid;"
        cursor.execute(query, (restime,))
        resid = cursor.fetchone()[0]
        self.conn.commit()
        return resid

    def update(self, resid, restime):
        cursor = self.conn.cursor()
        query = "update reservation set restime = %s where resid = %s;"
        cursor.execute(query, (restime, resid,))
        self.conn.commit()
        return resid

    def delete(self, resid):
        cursor = self.conn.cursor()
        query = "delete from reservation where resid = %s;"
        cursor.execute(query, (resid,))
        self.conn.commit()
        return resid
