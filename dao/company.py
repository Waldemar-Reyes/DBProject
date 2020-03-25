# -*- coding: utf-8 -*-
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

    def getPartsBySupplierId(self, said):
        cursor = self.conn.cursor()
        query = "select pid, pname, pmaterial, pcolor, pprice, qty from parts natural inner join system admin natural inner join supplies where said = %s;"
        cursor.execute(query, (said,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCompanyByUsername(self, compname):
        cursor = self.conn.cursor()
        query = "select * from company where compname = %s;"
        cursor.execute(query, (compname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, compname):
        cursor = self.conn.cursor()
        query = "insert into company(compname) values (%s) returning compid;"
        cursor.execute(query, (compname))
        compid = cursor.fetchone()[0]
        self.conn.commit()
        return compid
