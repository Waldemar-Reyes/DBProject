# -*- coding: utf-8 -*-
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

    def getPartsBySupplierId(self, said):
        cursor = self.conn.cursor()
        query = "select pid, pname, pmaterial, pcolor, pprice, qty from parts natural inner join system admin natural inner join supplies where said = %s;"
        cursor.execute(query, (said,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getConsumerByUsername(self, consusername):
        cursor = self.conn.cursor()
        query = "select * from consumer where consusername = %s;"
        cursor.execute(query, (consusername,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getConsumerByPremium(self, conspremium):
        cursor = self.conn.cursor()
        query = "select * from consumer where conspremium = %s;"
        cursor.execute(query, (conspremium,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, consusername):
        cursor = self.conn.cursor()
        query = "insert into consumer(consusername) values (%s) returning consid;"
        cursor.execute(query, (consusername))
        consid = cursor.fetchone()[0]
        self.conn.commit()
        return consid
