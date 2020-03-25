# -*- coding: utf-8 -*-
from config.dbconfig import pg_config
import psycopg2

class OrderDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllOrder(self):
        cursor = self.conn.cursor()
        query = "select * from order;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getOrderById(self, oid):
            cursor = self.conn.cursor()
            query = "select * from order where oid = %s;"
            cursor.execute(query, (oid,))
            result = cursor.fetchone()
            return result

    def getPartsBySupplierId(self, said):
        cursor = self.conn.cursor()
        query = "select pid, pname, pmaterial, pcolor, pprice, qty from parts natural inner join system admin natural inner join supplies where said = %s;"
        cursor.execute(query, (said,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getOrderByNumber(self, onumber):
        cursor = self.conn.cursor()
        query = "select * from order where onumber = %s;"
        cursor.execute(query, (onumber,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, onumber):
        cursor = self.conn.cursor()
        query = "insert into order(onumber) values (%s) returning oid;"
        cursor.execute(query, (onumber))
        oid = cursor.fetchone()[0]
        self.conn.commit()
        return oid
