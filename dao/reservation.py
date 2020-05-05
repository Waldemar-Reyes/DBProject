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
        query = "select resid, resname, restype, resprice, resstock, reslocation, restime from reservation;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getReservationById(self, resid):
        cursor = self.conn.cursor()
        query = "select resid, resname, restype, resprice, resstock, reslocation, restime from reservation where resid = %s;"
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
    
    def getReservationByName(self, resname):
        cursor = self.conn.cursor()
        query = "select * from reservation where resname = %s;"
        cursor.execute(query, (resname,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getReservationByType(self, restype):
        cursor = self.conn.cursor()
        query = "select * from reservation where restype = %s;"
        cursor.execute(query, (restype,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getReservationByPrice(self, price):
        cursor = self.conn.cursor()
        query = "select * from reservation where resprice = %s;"
        cursor.execute(query, (price,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getReservationByStock(self, stock):
        cursor = self.conn.cursor()
        query = "select * from reservation where resstock = %s;"
        cursor.execute(query, (stock,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getReservationByLocation(self, location):
        cursor = self.conn.cursor()
        query = "select * from reservation where reslocation = %s;"
        cursor.execute(query, (location,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getReservationByPriceandStock(self, price, stock):
        cursor = self.conn.cursor()
        query = "select * from reservation where resprice = %s and resstock = %s;"
        cursor.execute(query, (price, stock))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getReservationByPriceandLocation(self, price, location):
        cursor = self.conn.cursor()
        query = "select * from reservation where resprice = %s and reslocation = %s;"
        cursor.execute(query, (price, location))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getReservationByStockandLocation(self, stock, location):
        cursor = self.conn.cursor()
        query = "select * from reservation where resstock = %s and reslocation = %s;"
        cursor.execute(query, (stock, location))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getReservationByPriceandStockandLocation(self, price, stock, location):
        cursor = self.conn.cursor()
        query = "select * from reservation where resprice = %s and resstock = %s and reslocation = %s;"
        cursor.execute(query, (price, stock, location))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getReservationByNameandPrice(self, name, price):
        cursor = self.conn.cursor()
        query = "select * from reservation where resname = %s and resprice = %s;"
        cursor.execute(query, (name, price))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getReservationByNameandStock(self, name, stock):
        cursor = self.conn.cursor()
        query = "select * from reservation where resname = %s and resstock = %s;"
        cursor.execute(query, (name, stock))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getReservationByNameandLocation(self, name, location):
        cursor = self.conn.cursor()
        query = "select * from reservation where resname = %s and reslocation = %s;"
        cursor.execute(query, (name, location))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getReservationByNameandPriceandStock(self, name, price, stock):
        cursor = self.conn.cursor()
        query = "select * from reservation where resname = %s and resprice = %s and resstock = %s;"
        cursor.execute(query, (name, price, stock))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getReservationByNameandPriceandLocation(self, name, price, location):
        cursor = self.conn.cursor()
        query = "select * from reservation where resname = %s and resprice = %s and reslocation = %s;"
        cursor.execute(query, (name, price, location))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getReservationByNameandStockandLocation(self, name, stock, location):
        cursor = self.conn.cursor()
        query = "select * from reservation where resname = %s and resstock = %s and reslocation = %s;"
        cursor.execute(query, (name, stock, location))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getReservationByNameandPriceandStockandLocation(self, name, price, stock, location):
        cursor = self.conn.cursor()
        query = "select * from reservation where resname = %s and resprice = %s and resstock = %s and reslocation = %s;"
        cursor.execute(query, (name, price, stock, location))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getReservationByNameandType(self, name, restype):
        cursor = self.conn.cursor()
        query = "select * from reservation where resname = %s and restype = %s;"
        cursor.execute(query, (name, restype))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getReservationByTypeandPrice(self, restype, price):
        cursor = self.conn.cursor()
        query = "select * from reservation where restype = %s and resprice = %s;"
        cursor.execute(query, (restype, price))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getReservationByTypeandStock(self, restype, stock):
        cursor = self.conn.cursor()
        query = "select * from reservation where restype = %s and resstock = %s;"
        cursor.execute(query, (restype, stock))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getReservationByTypeandLocation(self, restype, location):
        cursor = self.conn.cursor()
        query = "select * from reservation where restype = %s and reslocation = %s;"
        cursor.execute(query, (restype, location))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getReservationByTypeandPriceandStock(self, restype, price, stock):
        cursor = self.conn.cursor()
        query = "select * from reservation where restype = %s and resprice = %s and resstock = %s;"
        cursor.execute(query, (restype, price, stock))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getReservationByTypeandPriceandLocation(self, restype, price, location):
        cursor = self.conn.cursor()
        query = "select * from reservation where restype = %s and resprice = %s and reslocation = %s;"
        cursor.execute(query, (restype, price, location))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getReservationByTypeandStockandLocation(self, restype, stock, location):
        cursor = self.conn.cursor()
        query = "select * from reservation where restype = %s and resstock = %s and reslocation = %s;"
        cursor.execute(query, (restype, stock, location))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getReservationByNameandTypeandPrice(self, name, restype, price):
        cursor = self.conn.cursor()
        query = "select * from reservation where resname = %s and restype = %s and resprice = %s;"
        cursor.execute(query, (name, restype, price))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getReservationByNameandTypeandStock(self, name, restype, stock):
        cursor = self.conn.cursor()
        query = "select * from reservation where resname = %s and restype = %s and resstock = %s;"
        cursor.execute(query, (name, restype, stock))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getReservationByNameandTypeandLocation(self, name, restype, location):
        cursor = self.conn.cursor()
        query = "select * from reservation where resname = %s and restype = %s and reslocation = %s;"
        cursor.execute(query, (name, restype, location))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getReservationByNameandTypeandPriceandStock(self, name, restype, price, stock):
        cursor = self.conn.cursor()
        query = "select * from reservation where resname = %s and restype = %s and resprice = %s and resstock = %s;"
        cursor.execute(query, (name, restype, price, stock))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getReservationByNameandTypeandPriceandLocation(self, name, restype, price, location):
        cursor = self.conn.cursor()
        query = "select * from reservation where resname = %s and restype = %s and resprice = %s and reslocation = %s;"
        cursor.execute(query, (name, restype, price, location))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getReservationByTypeandPriceandStockandLocation(self, restype, price, stock, location):
        cursor = self.conn.cursor()
        query = "select * from reservation where restype = %s and resprice = %s and resstock = %s and reslocation = %s;"
        cursor.execute(query, (restype, price, stock, location))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getReservationByNameandTypeandPriceandStockandLocation(self, name, restype, price, stock, location):
        cursor = self.conn.cursor()
        query = "select * from reservation where resname = %s and restype = %s and resprice = %s and resstock = %s and reslocation = %s;"
        cursor.execute(query, (name, restype, price, stock, location))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getReservationByNameandTime(self, name, time):
        cursor = self.conn.cursor()
        query = "select * from reservation where resname = %s and restime = %s;"
        cursor.execute(query, (name, time))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getReservationByTypeandTime(self, restype, time):
        cursor = self.conn.cursor()
        query = "select * from reservation where restype = %s and restime = %s;"
        cursor.execute(query, (restype, time))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getReservationByPriceandTime(self, price, time):
        cursor = self.conn.cursor()
        query = "select * from reservation where resprice = %s and restime = %s;"
        cursor.execute(query, (price, time))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getReservationByStockandTime(self, stock, time):
        cursor = self.conn.cursor()
        query = "select * from reservation where resstock = %s and restime = %s;"
        cursor.execute(query, (stock, time))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getReservationByLocationandTime(self, location, time):
        cursor = self.conn.cursor()
        query = "select * from reservation where reslocation = %s and restime = %s;"
        cursor.execute(query, (location, time))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getReservationByNameandTypeandTime(self, name, restype, time):
        cursor = self.conn.cursor()
        query = "select * from reservation where resname = %s and restype = %s and restime = %s;"
        cursor.execute(query, (name, restype, time))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getReservationByNameandPriceandTime(self, name, price, time):
        cursor = self.conn.cursor()
        query = "select * from reservation where resname = %s and resprice = %s and restime = %s;"
        cursor.execute(query, (name, price, time))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getReservationByNameandStockandTime(self, name, stock, time):
        cursor = self.conn.cursor()
        query = "select * from reservation where resname = %s and resstock = %s and restime = %s;"
        cursor.execute(query, (name, stock, time))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getReservationByNameandLocationandTime(self, name, location, time):
        cursor = self.conn.cursor()
        query = "select * from reservation where resname = %s and reslocation = %s and restime = %s;"
        cursor.execute(query, (name, location, time))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getReservationByTypeandPriceandTime(self, restype, price, time):
        cursor = self.conn.cursor()
        query = "select * from reservation where restype = %s and resprice = %s and restime = %s;"
        cursor.execute(query, (restype, price, time))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getReservationByTypeandLocationandTime(self, restype, location, time):
        cursor = self.conn.cursor()
        query = "select * from reservation where restype = %s and reslocation = %s and restime = %s;"
        cursor.execute(query, (restype, location, time))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getReservationByTypeandStockandTime(self, restype, stock, time):
        cursor = self.conn.cursor()
        query = "select * from reservation where restype = %s and resstock = %s and restime = %s;"
        cursor.execute(query, (restype, stock, time))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getReservationByPriceandStockandTime(self, price, stock, time):
        cursor = self.conn.cursor()
        query = "select * from reservation where resprice = %s and resstock = %s and restime = %s;"
        cursor.execute(query, (price, stock, time))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getReservationByPriceandLocationandTime(self, price, location, time):
        cursor = self.conn.cursor()
        query = "select * from reservation where resprice = %s and reslocation = %s and restime = %s;"
        cursor.execute(query, (price, location, time))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getReservationByStockandLocationandTime(self, stock, location, time):
        cursor = self.conn.cursor()
        query = "select * from reservation where resstock = %s and reslocation = %s and restime = %s;"
        cursor.execute(query, (stock, location, time))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getReservationByNameandTypeandPriceandTime(self, name, restype, price, time):
        cursor = self.conn.cursor()
        query = "select * from reservation where resname = %s and restype = %s and resprice = %s and restime = %s;"
        cursor.execute(query, (name, restype, price, time))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getReservationByNameandTypeandStockandTime(self, name, restype, stock, time):
        cursor = self.conn.cursor()
        query = "select * from reservation where resname = %s and restype = %s and resstock = %s and restime = %s;"
        cursor.execute(query, (name, restype, stock, time))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getReservationByNameandTypeandLocationandTime(self, name, restype, location, time):
        cursor = self.conn.cursor()
        query = "select * from reservation where resname = %s and restype = %s and reslocation = %s and restime = %s;"
        cursor.execute(query, (name, restype, location, time))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getReservationByNameandPriceandStockandTime(self, name, price, stock, time):
        cursor = self.conn.cursor()
        query = "select * from reservation where resname = %s and resprice = %s and resstock = %s and restime = %s;"
        cursor.execute(query, (name, price, stock, time))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getReservationByNameandPriceandLocationandTime(self, name, price, location, time):
        cursor = self.conn.cursor()
        query = "select * from reservation where resname = %s and resprice = %s and reslocation = %s and restime = %s;"
        cursor.execute(query, (name, price, location, time))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getReservationByNameandStockandLocationandTime(self, name, stock, location, time):
        cursor = self.conn.cursor()
        query = "select * from reservation where resname = %s and resstock = %s and reslocation = %s and restime = %s;"
        cursor.execute(query, (name, stock, location, time))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getReservationByTypeandPriceandStockandTime(self, restype, price, stock, time):
        cursor = self.conn.cursor()
        query = "select * from reservation where restype = %s and resprice = %s and resstock = %s and restime = %s;"
        cursor.execute(query, (restype, price, stock, time))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getReservationByTypeandPriceandLocationandTime(self, restype, price, location, time):
        cursor = self.conn.cursor()
        query = "select * from reservation where restype = %s and resprice = %s and reslocation = %s and restime = %s;"
        cursor.execute(query, (restype, price, location, time))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getReservationByTypeandStockandLocationandTime(self, restype, stock, location, time):
        cursor = self.conn.cursor()
        query = "select * from reservation where restype = %s and resstock = %s and reslocation = %s and restime = %s;"
        cursor.execute(query, (restype, stock, location, time))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getReservationByPriceandStockandLocationandTime(self, price, stock, location, time):
        cursor = self.conn.cursor()
        query = "select * from reservation where resprice = %s and resstock = %s and reslocation = %s and restime = %s;"
        cursor.execute(query, (price, stock, location, time))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getReservationByNameandTypeandPriceandStockandTime(self, name, restype, price, stock, time):
        cursor = self.conn.cursor()
        query = "select * from reservation where resname = %s and restype = %s and resprice = %s and resstock = %s and restime = %s;"
        cursor.execute(query, (name, restype, price, stock, time))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getReservationByNameandTypeandPriceandLocationandTime(self, name, restype, price, location, time):
        cursor = self.conn.cursor()
        query = "select * from reservation where resname = %s and restype = %s and resprice = %s and reslocation = %s and restime = %s;"
        cursor.execute(query, (name, restype, price, location, time))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getReservationByTypeandPriceandStockandLocationandTime(self, restype, price, stock, location, time):
        cursor = self.conn.cursor()
        query = "select * from reservation where restype = %s and resprice = %s and resstock = %s and reslocation = %s and restime = %s;"
        cursor.execute(query, (restype, price, stock, location, time))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getReservationByNameandTypeandPriceandStockandLocationandTime(self, name, restype, price, stock, location, time):
        cursor = self.conn.cursor()
        query = "select * from reservation where resname = %s and restype = %s and resprice = %s and resstock = %s and reslocation = %s and restime = %s;"
        cursor.execute(query, (name, restype, price, stock, location, time))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getReservationByNameandTypeandStockandLocation(self, name, restype, stock, location):
        cursor = self.conn.cursor()
        query = "select * from reservation where resname = %s and restype = %s and resstock = %s and reslocation = %s;"
        cursor.execute(query, (name, restype, stock, location))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getReservationByNameandTypeandStockandLocationandTime(self, name, restype, stock, location, time):
        cursor = self.conn.cursor()
        query = "select * from reservation where resname = %s and restype = %s and resstock = %s and reslocation = %s and restime = %s;"
        cursor.execute(query, (name, restype, stock, location, time))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getReservationByNameandPriceandStockandLocationandTime(self, name, price, stock, location, time):
        cursor = self.conn.cursor()
        query = "select * from reservation where resname = %s and resprice = %s and resstock = %s and reslocation = %s and restime = %s;"
        cursor.execute(query, (name, price, stock, location, time))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getConsumerByReservationId(self, resid):
        cursor = self.conn.cursor()
        query = "select consid, consuseresname from consumer natural inner join reservation where resid = %s;"
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
        query = "select rid, rname, rtype, rprice, rstock, rlocation from resources natural inner join reservation where resid = %s;"
        cursor.execute(query, (resid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierByReservationId(self, resid):
        cursor = self.conn.cursor()
        query = "select sid, suseresname, scompany from supplier natural inner join reservations where resid = %s;"
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
