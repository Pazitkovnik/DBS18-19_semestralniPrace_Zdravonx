/*
Created		03.12.2018
Modified		24.01.2019
Project		
Model		
Company		
Author		
Version		
Database		mySQL 5 
*/


drop table IF EXISTS Authority;
drop table IF EXISTS User;
drop table IF EXISTS IntervalValue;
drop table IF EXISTS Kontrola_ZP;
drop table IF EXISTS Status_pristroje;
drop table IF EXISTS Servisni_Firma;
drop table IF EXISTS Servis_ZP;
drop table IF EXISTS stupen_ochrany;
drop table IF EXISTS Nakup;
drop table IF EXISTS Pristroj_Dokument;
drop table IF EXISTS Dokument;
drop table IF EXISTS Oddeleni;
drop table IF EXISTS Typ;
drop table IF EXISTS Dodavatel;
drop table IF EXISTS Pristroj;


Create table Pristroj (
	id_pristroj Int NOT NULL AUTO_INCREMENT,
	id_typ Int NOT NULL,
	id_oddeleni Int NOT NULL,
	id_dodavatel Int NOT NULL,
	nazev Varchar(20),
	inv_cislo Varchar(20),
	vyr_cislo Varchar(20),
	umdns Varchar(20),
	id_stupen Int NOT NULL,
	id_status Int NOT NULL,
	UNIQUE (id_pristroj),
 Primary Key (id_pristroj,id_typ,id_oddeleni,id_dodavatel,id_stupen,id_status)) ENGINE = MyISAM;

Create table Dodavatel (
	id_dodavatel Int NOT NULL AUTO_INCREMENT,
	jmeno Varchar(20),
	telefon Varchar(20),
	UNIQUE (id_dodavatel),
 Primary Key (id_dodavatel)) ENGINE = MyISAM;

Create table Typ (
	id_typ Int NOT NULL AUTO_INCREMENT,
	nazev Varchar(20),
	UNIQUE (id_typ),
 Primary Key (id_typ)) ENGINE = MyISAM;

Create table Oddeleni (
	id_oddeleni Int NOT NULL AUTO_INCREMENT,
	nazev Varchar(20),
	UNIQUE (id_oddeleni),
 Primary Key (id_oddeleni)) ENGINE = MyISAM;

Create table Dokument (
	id_dokument Int NOT NULL AUTO_INCREMENT,
	nazev Varchar(20),
	UNIQUE (id_dokument),
 Primary Key (id_dokument)) ENGINE = MyISAM;

Create table Pristroj_Dokument (
	id_dokument Int NOT NULL,
	id_pristroj Int NOT NULL,
 Primary Key (id_dokument,id_pristroj)) ENGINE = MyISAM;

Create table Nakup (
	id_nakup Int NOT NULL AUTO_INCREMENT,
	por_cena Varchar(20),
	datum_porizeni Date,
	id_user Int NOT NULL,
	id_pristroj Int NOT NULL,
	UNIQUE (id_nakup),
 Primary Key (id_nakup,id_user,id_pristroj)) ENGINE = MyISAM;

Create table stupen_ochrany (
	id_stupen Int NOT NULL AUTO_INCREMENT,
	nazev Varchar(20),
	UNIQUE (id_stupen),
 Primary Key (id_stupen)) ENGINE = MyISAM;

Create table Servis_ZP (
	id_servis Int NOT NULL AUTO_INCREMENT,
	id_firma Int NOT NULL,
	id_status Int NOT NULL,
	datum_uvedeni Datetime,
	poznamky Varchar(150),
	datum_stazeni Datetime,
	id_pristroj Int NOT NULL,
 Primary Key (id_servis,id_firma,id_status,id_pristroj)) ENGINE = MyISAM;

Create table Servisni_Firma (
	id_firma Int NOT NULL AUTO_INCREMENT,
	nazev_firmy Varchar(40),
	UNIQUE (id_firma),
 Primary Key (id_firma)) ENGINE = MyISAM;

Create table Status_pristroje (
	id_status Int NOT NULL AUTO_INCREMENT,
	status_pristroje Varchar(20),
	UNIQUE (id_status),
 Primary Key (id_status)) ENGINE = MyISAM;

Create table Kontrola_ZP (
	id_kontrola Int NOT NULL AUTO_INCREMENT,
	datum_kontroly Datetime,
	poznamky Varchar(150),
	id_status Int NOT NULL,
	id_interval Int NOT NULL,
	id_pristroj Int NOT NULL,
	id_user Int NOT NULL,
	UNIQUE (id_kontrola),
 Primary Key (id_kontrola,id_status,id_interval,id_pristroj,id_user)) ENGINE = MyISAM;

Create table IntervalValue (
	id_interval Int NOT NULL AUTO_INCREMENT,
	hodnota_intervalu Int,
	UNIQUE (id_interval),
 Primary Key (id_interval)) ENGINE = MyISAM;

Create table User (
	id_user Int NOT NULL AUTO_INCREMENT,
	id_authority Int NOT NULL,
	user_login Varchar(40),
	user_password_hash Varchar(400),
	user_firstname Varchar(20),
	user_surname Varchar(20),
	UNIQUE (id_user),
 Primary Key (id_user,id_authority)) ENGINE = MyISAM;

Create table Authority (
	id_authority Int NOT NULL AUTO_INCREMENT,
	authority_type Varchar(20),
	UNIQUE (id_authority),
 Primary Key (id_authority)) ENGINE = MyISAM;


Alter table Pristroj_Dokument add Foreign Key (id_pristroj) references Pristroj (id_pristroj) on delete  restrict on update  restrict;
Alter table Servis_ZP add Foreign Key (id_pristroj) references Pristroj (id_pristroj) on delete  restrict on update  restrict;
Alter table Kontrola_ZP add Foreign Key (id_pristroj) references Pristroj (id_pristroj) on delete  restrict on update  restrict;
Alter table Nakup add Foreign Key (id_pristroj) references Pristroj (id_pristroj) on delete  restrict on update  restrict;
Alter table Pristroj add Foreign Key (id_dodavatel) references Dodavatel (id_dodavatel) on delete  restrict on update  restrict;
Alter table Pristroj add Foreign Key (id_typ) references Typ (id_typ) on delete  restrict on update  restrict;
Alter table Pristroj add Foreign Key (id_oddeleni) references Oddeleni (id_oddeleni) on delete  restrict on update  restrict;
Alter table Pristroj_Dokument add Foreign Key (id_dokument) references Dokument (id_dokument) on delete  restrict on update  restrict;
Alter table Pristroj add Foreign Key (id_stupen) references stupen_ochrany (id_stupen) on delete  restrict on update  restrict;
Alter table Servis_ZP add Foreign Key (id_firma) references Servisni_Firma (id_firma) on delete  restrict on update  restrict;
Alter table Servis_ZP add Foreign Key (id_status) references Status_pristroje (id_status) on delete  restrict on update  restrict;
Alter table Kontrola_ZP add Foreign Key (id_status) references Status_pristroje (id_status) on delete  restrict on update  restrict;
Alter table Pristroj add Foreign Key (id_status) references Status_pristroje (id_status) on delete  restrict on update  restrict;
Alter table Kontrola_ZP add Foreign Key (id_interval) references IntervalValue (id_interval) on delete  restrict on update  restrict;
Alter table Kontrola_ZP add Foreign Key (id_user) references User (id_user) on delete  restrict on update  restrict;
Alter table Nakup add Foreign Key (id_user) references User (id_user) on delete  restrict on update  restrict;
Alter table User add Foreign Key (id_authority) references Authority (id_authority) on delete  restrict on update  restrict;


/* Users permissions */


