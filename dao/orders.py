from config.dbconfig import pg_config
import psycopg2


class OrdersDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllOrders(self):
        cursor = self.conn.cursor()
        query = "select * from orders;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getOrdersById(self, odid):
        cursor = self.conn.cursor()
        query = "select * from orders where odid = %s;"
        cursor.execute(query, (odid,))
        result = cursor.fetchone()
        return result

    def getOrdersByNumber(self, odnumber):
        cursor = self.conn.cursor()
        query = "select * from orders where odnumber = %s;"
        cursor.execute(query, (odnumber,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getOrdersByTime(self, odtime):
        cursor = self.conn.cursor()
        query = "select * from orders where odtime = %s;"
        cursor.execute(query, (odtime,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getOrdersByNummberandTime(self, odnumber, odtime):
        cursor = self.conn.cursor()
        query = "select * from orders where odnumber = %s and odtime = %s;"
        cursor.execute(query, (odnumber, odtime))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getConsumerByOrdersId(self, odid):
        cursor = self.conn.cursor()
        query = "select * from consumer natural inner join makes natural inner join orders where odid = %s;"
        cursor.execute(query, (odid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getReservationByOrdersId(self, odid):
        cursor = self.conn.cursor()
        # TODO Check and fix if needed
        query = "select * from reservation natural inner join orders where odid = %s"
        cursor.execute(query, (odid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierByOrdersId(self, odid):
        cursor = self.conn.cursor()
        query = "select * from supplier natural inner join supplies natural inner join resources natural inner join belongs natural inner join orders where odid = %s;"
        cursor.execute(query, (odid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insertPayMethodIntoOrder(self, odid, pmid):
        cursor = self.conn.cursor()
        query = "insert into pays(odid, pmid) values (%s, %s) returning odid;"
        cursor.execute(query, (odid, pmid,))
        odid = cursor.fetchone()[0]
        self.conn.commit()
        return odid

    def insert(self, resid, odnumber, odtime):
        cursor = self.conn.cursor()
        query = "insert into orders(resid, odnumber, odtime) values (%s, %s, %s) returning odid;"
        cursor.execute(query, (resid, odnumber, odtime,))
        odid = cursor.fetchone()[0]
        self.conn.commit()
        return odid

    def update(self, odid, resid, odnumber, odtime):
        cursor = self.conn.cursor()
        query = "update orders set resid = %s, odnumber = %s, odtime = %s where odid = %s;"
        cursor.execute(query, (resid, odnumber, odtime, odid,))
        self.conn.commit()
        return odid

    def delete(self, odid):
        cursor = self.conn.cursor()
        query = "delete from orders where odid = %s;"
        cursor.execute(query, (odid,))
        self.conn.commit()
        return odid
