-- This file contains the definitions of the tables used in the application.
--
-- Company table
create table company(compid serial primary key not null, compname varchar(20) not null);

-- Consumer table
create table consumer(consid serial primary key not null, consusername varchar(20) not null);

-- Pay Method table
create table pay_method(pmid serial primary key not null, pmname varchar(20) not null);

-- Request table
create table reservation(resid serial primary key not null, resname varchar(20) not null, restype varchar(20) not null, resprice double precision not null, reslocation varchar(20), resstock int not null, restime varchar(20) not null);

-- Resources table
create table resources(rid serial primary key not null, rname varchar(20) not null, rtype varchar(20) not null, rprice double precision not null, rlocation varchar(20), rstock int not null);

-- Supplier table
create table supplier(sid serial primary key not null, susername varchar(20) not null, scompany varchar(20) not null);

-- System Admin table
create table sys_adm(said serial primary key not null, sausername varchar(20) not null);

-- Users table
create table users(uid serial primary key not null, ufirstname varchar(20) not null, ulastname varchar(20) not null);

-- Order table
create table orders(odid serial primary key not null, resid integer references reservation(resid), odnumber int not null, odtime int not null);

-- Consumer to Pay Method Table
create table owns(pmid integer references pay_method(pmid), consid integer references consumer(consid), primary key (pmid, consid) not null );

-- Consumer to Orders Table
create table makes(odid integer references orders(odid), consid integer references consumer(consid), primary key (odid, consid) not null);

-- Order to Resources Table
create table belongs(rid integer references resources(rid), odid integer references orders(odid), primary key (rid, odid) not null, odquantity int not null);

-- Pay Method to Orders Table
create table pays(odid integer references orders(odid), pmid integer references pay_method(pmid), primary key (odid, pmid) not null);

-- Supplier to Company Table
create table works(compid integer references company(compid), sid integer references supplier(sid), primary key (compid, sid) not null);

-- Supplier to Resources Table
create table supplies(sid integer references supplier(sid), rid integer references resources(rid), primary key (sid, rid) not null);

-- System Admin to Users Table
create table manages(uid integer references users(uid), said integer references sys_adm(said), primary key (uid, said) not null);

-- Reservations to Resources Table
create table asks(resid integer references reservation(resid), rid integer references resources(rid), primary key (resid, rid) not null, resquantity int not null);

-- Consumer to Reservations Table
create table requests(resid integer references reservation(resid), consid integer references consumer(consid), primary key (resid, consid) not null);
