# -*- coding: utf-8 -*-
from config.dbconfig import pg_config
import psycopg2

class SysAdmDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllSysAdm(self):
        cursor = self.conn.cursor()
        query = "select * from system admin;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSysAdmById(self, said):
            cursor = self.conn.cursor()
            query = "select * from system admin where said = %s;"
            cursor.execute(query, (said,))
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

    def getSysAdmnByUsername(self, sausername):
        cursor = self.conn.cursor()
        query = "select * from system admin where sausername = %s;"
        cursor.execute(query, (sausername,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, sausername):
        cursor = self.conn.cursor()
        query = "insert into supplier(sausername) values (%s) returning said;"
        cursor.execute(query, (sausername))
        said = cursor.fetchone()[0]
        self.conn.commit()
        return said
