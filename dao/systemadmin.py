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
        query = "select * from sys_adm;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSysAdmById(self, said):
        cursor = self.conn.cursor()
        query = "select * from sys_adm where said = %s;"
        cursor.execute(query, (said,))
        result = cursor.fetchone()
        return result

    def getSysAdmnByUsername(self, sausername):
        cursor = self.conn.cursor()
        query = "select * from sys_adm where sausername = %s;"
        cursor.execute(query, (sausername,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getCompanyBySysAdmId(self, said):
        cursor = self.conn.cursor()
        # TODO Check
        query = "select * from company natural inner join works natural inner join supplier natural inner join sys_adm where said = %s;"
        cursor.execute(query, (said,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getConsumerBySysAdmId(self, said):
        cursor = self.conn.cursor()
        # TODO Check
        query = "select * from consumer natural inner join sys_adm where said = %s"
        cursor.execute(query, (said,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierBySysAdmId(self, said):
        cursor = self.conn.cursor()
        # TODO Check
        query = "select * from supplier natural inner join sys_adm where said = %s"
        cursor.execute(query, (said,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUsersBySysAdmId(self, said):
        cursor = self.conn.cursor()
        # TODO Check
        query = "select * from users natural inner join sys_adm where said = %s"
        cursor.execute(query, (said,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, sausername):
        cursor = self.conn.cursor()
        query = "insert into sys_adm(sausername) values (%s) returning said;"
        cursor.execute(query, (sausername,))
        said = cursor.fetchone()[0]
        self.conn.commit()
        return said

    def insertSysAdmAsNewUsers(self, uid, sausername):
        cursor = self.conn.cursor()
        query = "insert into sys_adm(uid, sausername) values (%s, %s) returning said;"
        cursor.execute(query, (uid, sausername,))
        said = cursor.fetchone()[0]
        self.conn.commit()
        return said

    def update(self, said, uid, sausername):
        cursor = self.conn.cursor()
        query = "update sys_adm set uid = %s, sausername = %s where said = %s;"
        cursor.execute(query, (uid, sausername, said,))
        self.conn.commit()
        return said

    def delete(self, said):
        cursor = self.conn.cursor()
        query = "delete from sys_adm where said = %s;"
        cursor.execute(query, (said,))
        self.conn.commit()
        return said
