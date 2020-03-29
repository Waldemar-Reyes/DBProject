-- This file contains the definitions of the tables used in the application.
--
-- Company table
create table company(compid serial primary key, compname varchar(20));

-- Consumer table
create table consumer(consid serial primary key, consusername varchar(20));

-- Order table
create table orders(odid serial primary key, odnumber int);

-- Pay Method table
create table pay_method(pmid serial primary key, pmname varchar(20));

-- Reservation table
create table reservation(resid serial primary key, restime varchar(20));

-- Resource table
create table resource(rid serial primary key, rname varchar(20), rprice int, rlocation varchar(20), ramount int);

-- Supplier table
create table supplier(sid serial primary key, susername varchar(20), scompany varchar(20));

-- System Admin table
create table sys_adm(said serial primary key, sausername varchar(20));

-- User table
create table user(uid serial primary key, ufirstname varchar(20), ulastname varchar(20));


---- Supplies table
--create table supplies(pid integer references Parts(pid), sid integer references
--Supplier(sid), qty integer, primary key(pid, sid));
--
---- PartSales table
--create table partsales(psaleid serial primary key, pid integer references Parts(pid),
--sid integer references Supplier(sid), sqty integer, sprice float, sdate Date);
