# -*- coding: utf-8 -*-
from config.dbconfig import pg_config
import psycopg2

class ReservationsDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllReservations(self):
        cursor = self.conn.cursor()
        query = "select * from resrevations;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getReservationsById(self, resid):
            cursor = self.conn.cursor()
            query = "select * from reservations where resid = %s;"
            cursor.execute(query, (resid,))
            result = cursor.fetchone()
            return result

    def getResourcesBySupplierId(self, sid):
        cursor = self.conn.cursor()
        query = "select rid, rname, rprice, ramount, rlocation from resources natural inner join supplier where sid = %s;"
        cursor.execute(query, (sid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getReservationByTime(self, restime):
        cursor = self.conn.cursor()
        query = "select * from reservation where restime = %s;"
        cursor.execute(query, (restime,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getOrderByReservationsId(self, resid):
        cursor = self.conn.cursor()
        query = "select oid, onumber from order natural inner join reservations where resid = %s;"
        cursor.execute(query, (resid,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getSupplierByReservationsId(self, resid):
        cursor = self.conn.cursor()
        query = "select sid, susername, scompany from supplier natural inner join reservations where resid = %s;"
        cursor.execute(query, (resid,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getConsumerByReservationsId(self, resid):
        cursor = self.conn.cursor()
        query = "select consid, consusername, conspremium from consumer natural inner join reservations where resid = %s;"
        cursor.execute(query, (resid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, restime):
        cursor = self.conn.cursor()
        query = "insert into reservation(restime) values (%s) returning resid;"
        cursor.execute(query, (restime))
        resid = cursor.fetchone()[0]
        self.conn.commit()
        return resid
