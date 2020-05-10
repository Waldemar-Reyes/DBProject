-- File to generate data. This is for reference only and its purpose is to have some controled data for testing.

-- Populate users table
INSERT INTO users (ufirstname,ulastname) VALUES ('Cristina','Díaz'),('Fernando','Guzman'),('Jose','Cano'),('Julia','Delgado'),('Marta','Jimenez'),('Antonio','Herrera'),('Antonio','Marti'),('Lucia','Martines'),('Jorge','Leon'),('Maria','Rodriguez');
INSERT INTO users (ufirstname,ulastname) VALUES ('Jorge','Alonso'),('Enrique','Torres'),('Manuel','Merino'),('Alejandra','Santos'),('Jose','Utera'),('Maria','Martinez'),('Juan','Calvo'),('Rafael','Chaves'),('Miguel','Angel'),('Josefa','Fernandez');
INSERT INTO users (ufirstname,ulastname) VALUES ('Iona','Moss'),('Darius','Key'),('Nasim','Padilla'),('Madison','Valdez'),('Quemby','Kaufman'),('Devin','Clemons'),('Kirk','Stark'),('Henry','Rose'),('Nerea','Haynes'),('Jamal','Palmer');
INSERT INTO users (ufirstname,ulastname) VALUES ('Rana','Bradshaw'),('Rudyard','Simmons'),('Fritz','Head'),('Kiara','Cruz'),('Bradley','Jimenez'),('Aspen','Shepherd'),('Beau','Boone'),('Sylvester','Mcconnell'),('Nicole','Hopper'),('Katell','Frank');
INSERT INTO users (ufirstname,ulastname) VALUES ('Elvis','Roy'),('Daniel','Talley'),('Abra','Carpenter'),('Edan','Lambert'),('Kay','Skinner'),('Whitney','Barlow'),('Samson','Wiley'),('Cailin','Mckenzie'),('Chancellor','Jackson'),('Jared','Glenn');
INSERT INTO users (ufirstname,ulastname) VALUES ('Quentin','Mcfarland'),('Lee','Roth'),('Jane','Johnson'),('Kylynn','Holden'),('Brett','Martinez'),('Colt','Owens'),('Neil','Meyers'),('Elvis','Cook'),('Keith','Foster'),('Cecilia','Morse');
--INSERT INTO users (ufirstname,ulastname) VALUES ('Oliver','Le'),('Kato','Knight'),('Clarke','Barrera'),('Dalton','Briggs'),('Illiana','Finch'),('Cadman','Zamora'),('Christine','Mccarty'),('Ima','English'),('Jonas','Marquez'),('Jocelyn','Parsons');
--INSERT INTO users (ufirstname,ulastname) VALUES ('Abbot','Graves'),('Amal','Simon'),('Fitzgerald','Ramsey'),('Xavier','Love'),('Duncan','Cote'),('Caleb','Boyer'),('Brock','Cole'),('Elton','Sloan'),('Griffith','Thornton'),('Sade','Mckenzie');
--INSERT INTO users (ufirstname,ulastname) VALUES ('Aspen','Hicks'),('Barclay','Carr'),('Margaret','Moon'),('Holly','Schultz'),('April','Mcbride'),('Ulysses','Ball'),('Fatima','Chang'),('Carter','Kinney'),('Zorita','Sargent'),('Chester','Barry');
--INSERT INTO users (ufirstname,ulastname) VALUES ('Destiny','Alston'),('Henry','Medina'),('Cruz','Kim'),('Blossom','Travis'),('Lynn','Wolf'),('Julian','Castaneda'),('Denton','Schneider'),('Price','Ellison'),('Ori','Bryant'),('Lois','Stuart');
--INSERT INTO users (ufirstname,ulastname) VALUES ('Chandler','Love'),('Florence','Cleveland'),('Jin','Best'),('Buffy','Montoya'),('Mason','Vargas'),('Evan','Franks'),('Jarrod','Robles'),('Simone','Maldonado'),('Stacey','Calderon'),('Sophia','Rivers');
--INSERT INTO users (ufirstname,ulastname) VALUES ('Holly','Schneider'),('Devin','Humphrey'),('Imani','Boyle'),('Ina','Stone'),('Katell','Valdez'),('Remedios','Velazquez'),('Zenia','Johns'),('Joshua','Schwartz'),('Karyn','Cain'),('Deborah','Odonnell');

-- Populate company table
INSERT INTO company (compname) VALUES ('Wal-Mart'),('Sams'),('Cosco'),('SuperMax'),('Econo'),('Selectos'),('Walgreens'),('CVS'),('Marshalls'),('Burlington'),('Puma'),('Total'),('HomeDepot'),('H&A Trucking'),('Gonzalez Trading');

-- Populate sys_adm table
INSERT INTO sys_adm (uid,sausername) VALUES ('1','Admin1'),('2','Admin2'),('3','Admin3'),('4','Admin4'),('5','Admin5'),('6','Admin6'),('7','Admin7'),('8','Admin8'),('9','Admin9'),('10','Admin10');

-- Populate consumer table
INSERT INTO consumer (uid,consusername) VALUES ('11','Consumer1'),('12','Consumer2'),('13','Consumer3'),('14','Consumer4'),('15','Consumer5'),('16','Consumer'),('17','Consumer7'),('18','Consumer8'),('19','Consumer9'),('20','Consumer10');

-- Populate supplier table
INSERT INTO supplier(uid,susername,scompany) VALUES
('21','Supplier1','USPS'),
('22','Supplier2','FedEx'),
('23','Supplier3','PR Supplies Group'),
('24','Supplier4','Crowley'),
('25','Supplier5','Maersk'),
('26','Supplier6','Dueñas Trailers'),
('27','Supplier7','Puma'),
('28','Supplier8','Total'),
('29','Supplier9','Med Co.'),
('30','Supplier10','Medical Supply');

-- Link relations between supplier who works for a company - works(compid, sid)
INSERT INTO works VALUES 
(1,1),(1,3),(1,4),(1,5),(1,6),(1,10),
(2,1),(2,2),(2,3),(2,4),(2,5),(2,9),(2,10),
(3,1),(3,2),(3,4),(3,5),(3,6),(3,9),
(4,3),(4,4),(4,5),
(5,4),(5,5),(5,6),
(6,3),(6,4),(6,5),(6,6),
(7,1),(7,4),(7,9),(7,10),
(8,2),(8,5),(8,9),(8,10),
(9,2),(9,4),(9,5),(9,6),
(10,1),(10,3),(10,4),(10,5),
(11,1),(11,7),
(12,2),(12,3),(12,8),
(13,1),(13,3),(13,4),(13,5),(13,6),(13,8),
(14,3),(14,7),
(15,6),(15,8);

-- Populate resources table
INSERT INTO resources (rname,rtype,rprice,rlocation,rstock) VALUES
('Dasani','Agua Embotellada','4.99','','48'),
('Salutaris','Agua Embotellada','3.99','','57'),
('Dasani','Agua 5 Galones','3.00','','24'),
('Kingdom Water','Agua 5 Galones','2.50','','46'),
('Panadol','Medicamentos','1.50','','197'),
('Claritin','Medicamentos','2.00','','76'),
('Tums','Medicamentos','1.10','','48'),
('Gerber','Comida De Bebes','0.69','','276'),
('Tuna','Comida Enlatada','0.59','','149'),
('Pollo','Comida Enlatada','0.79','','128'),
('Chef Boyardee','Comida Enlatada','1.10','','63'),
('Arroz','Comida Seca','1.25','','168'),
('Galletas','Comida Seca','1.50','','42'),
('Hielera Ponce Tropical','Hielo','1.50','','97'),
('Regular','Gasolina Galon','2.10','','1024'),
('Diesel','Gasolina Galon','1.57','','1025'),
('Propano','Gas Galon','1.90','','1044'),
('Desfibrilador','Equipo Medico','359.99','','8'),
('Camilla','Equipo Medico','199.99','','40'),
('Bulldozer','Maquinaria Pesada','54.99','','5'),
('Excavadora','Maquinaria Pesada','59.99','','7'),
('Sierra','Herramientas','7.89','','20'),
('Taladro','Herramientas','4.89','','20'),
('Tshirt','Ropa','7.99','','124'),
('Mahones','Ropa','9.99','','89'),
('Honda','Generador','1200','','25'),
('Generac','Generador','2400','','10'),
('Duracell','Baterias','1.09','','194'),
('Energizer','Baterias','1.19','','141');

-- Link relations between resources supplied by a supplier - supplies(sid, rid)
INSERT INTO supplies VALUES 
(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),(1,9),(1,10),(1,11),(1,12),(1,13),(1,14),(1,18),(1,22),(1,23),(1,24),(1,25),(1,27),(1,28),(1,29),
(2,1),(2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(2,8),(2,9),(2,10),(2,11),(2,12),(2,13),(2,14),(2,18),(2,22),(2,23),(2,24),(2,25),(2,26),(2,28),(2,29),
(3,1),(3,2),(3,3),(3,4),(3,5),(3,6),(3,7),(3,8),(3,9),(3,10),(3,11),(3,12),(3,13),(3,14),(3,17),(3,18),(3,19),(3,20),(3,21),(3,22),(3,23),(3,24),(3,25),(3,26),(3,27),(3,28),(3,29),
(4,1),(4,2),(4,3),(4,4),(4,5),(4,6),(4,7),(4,8),(4,9),(4,10),(4,11),(4,12),(4,13),(4,14),(4,17),(4,18),(4,19),(4,20),(4,21),(4,22),(4,23),(4,24),(4,25),(4,26),(4,27),(4,28),(4,29),
(5,1),(5,2),(5,3),(5,4),(5,5),(5,6),(5,7),(5,8),(5,9),(5,10),(5,11),(5,12),(5,13),(5,14),(5,17),(5,18),(5,19),(5,20),(5,21),(5,22),(5,23),(5,24),(5,25),(5,26),(5,27),(5,28),(5,29),
(6,1),(6,2),(6,3),(6,4),(6,8),(6,9),(6,10),(6,11),(6,12),(6,13),(6,14),(6,17),(6,22),(6,23),(6,24),(6,25),(6,26),(6,27),(6,28),(6,29),
(7,15),(7,16),
(8,15),(8,16),(8,17),
(9,5),(9,6),(9,7),(9,18),(9,19),(9,29),
(10,5),(10,6),(10,7),(10,18),(10,19),(10,28);
