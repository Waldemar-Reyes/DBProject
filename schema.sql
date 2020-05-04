-- This file contains the definitions of the tables used in the application.
--
-- Company table
create table company(compid serial primary key, compname varchar(20));

-- Consumer table
create table consumer(consid serial primary key, consusername varchar(20));

-- Orders table
create table orders(odid serial primary key, odnumber int);

-- Pay Method table
create table pay_method(pmid serial primary key, pmname varchar(20));

-- Reservation table
create table reservation(resid serial primary key, restime varchar(20));

-- Resources table
create table resources(rid serial primary key, rname varchar(20), rtype varchar(20), rprice double_precision, rlocation varchar(20), ramount int);

-- Supplier table
create table supplier(sid serial primary key, susername varchar(20), scompany varchar(20));

-- System Admin table
create table sys_adm(said serial primary key, sausername varchar(20));

-- Users table
create table users(uid serial primary key, ufirstname varchar(20), ulastname varchar(20));

-- Request table
create table request(reqid serial primary key, consid integer references consumer(consid), reqname varchar(20), reqtype varchar(20), reqprice int, reqlocation varchar(20), reqamount int);

-- Consumer to Pay Method Table
create table owns(pmid integer references pay_method(pmid), consid integer references consumer(consid), primary key (pmid, consid));

-- Consumer to Orders Table
create table makes(odid integer references orders(odid), consid integer references consumer(consid), primary key (odid, consid));

-- Consumer to Request Table
create table requests(reqid integer references request(reqid), consid integer references consumer(consid), primary key (reqid, consid));

-- Orders to Resources Table
create table belongs(rid integer references resources(rid), odid integer references orders(odid), primary key (rid, odid), quantity int);

-- Pay Method to Orders Table
create table pays(odid integer references orders(odid), pmid integer references pay_method(pmid), primary key (odid, pmid));

-- Supplier to Company Table
create table works(compid integer references company(compid), sid integer references supplier(sid), primary key (compid, sid));

-- Supplier to Resources Table
create table supplies(sid integer references supplier(sid), rid integer references resources(rid), primary key (sid, rid));

-- System Admin to Users Table
create table manages(uid integer references users(uid), said integer references sys_adm(said), primary key (uid, said));

-- Request to Resources Table
create table asks(reqid integer references request(reqid), rid integer references resources(rid), primary key (reqid, rid));
