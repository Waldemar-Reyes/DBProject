from config.dbconfig import pg_config
import psycopg2


class UsersDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "select * from users;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUsersById(self, uid):
        cursor = self.conn.cursor()
        query = "select * from users where uid = %s;"
        cursor.execute(query, (uid,))
        result = cursor.fetchone()
        return result

    def getUsersByFirstname(self, ufirstname):
        cursor = self.conn.cursor()
        query = "select * from users where ufirstname = %s;"
        cursor.execute(query, (ufirstname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUsersByLastname(self, ulastname):
        cursor = self.conn.cursor()
        query = "select * from users where ulastname = %s;"
        cursor.execute(query, (ulastname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUsersByFirstnameandLastname(self, ufirstname, ulastname):
        cursor = self.conn.cursor()
        query = "select * from users where ufirstname = %s and ulastname = %s;"
        cursor.execute(query, (ufirstname, ulastname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getConsumerByUsersId(self, uid):
        cursor = self.conn.cursor()
        query = "select consid, consusername from consumer natural inner join users where uid = %s;"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierByUsersId(self, uid):
        cursor = self.conn.cursor()
        query = "select sid, susername, scompany from supplier natural inner join users where uid = %s;"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSysAdmByUsersId(self, uid):
        cursor = self.conn.cursor()
        query = "select said, sausername from sys_adm natural inner join users where uid = %s;"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, ufirstname, ulastname):
        cursor = self.conn.cursor()
        query = "insert into users(ufirstname, ulastname) values (%s, %s) returning uid;"
        cursor.execute(query, (ufirstname, ulastname,))
        uid = cursor.fetchone()[0]
        self.conn.commit()
        return uid

    def update(self, uid, ufirstname, ulastname):
        cursor = self.conn.cursor()
        query = "update users set ufirstname = %s, ulastname = %s where uid = %s;"
        cursor.execute(query, (ufirstname, ulastname, uid,))
        self.conn.commit()
        return uid

    def delete(self, uid):
        cursor = self.conn.cursor()
        query = "delete from users where uid = %s;"
        cursor.execute(query, (uid,))
        self.conn.commit()
        return uid
