#------------------------------------------------------------
#        Script MySQL.
#------------------------------------------------------------


#------------------------------------------------------------
# Table: User
#------------------------------------------------------------

CREATE TABLE User(
        id        Int  Auto_increment  NOT NULL ,
        firstname Varchar (100) NOT NULL ,
        lastname  Varchar (100) NOT NULL
	,CONSTRAINT User_PK PRIMARY KEY (id)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Artricle
#------------------------------------------------------------

CREATE TABLE Artricle(
        id              Int  Auto_increment  NOT NULL ,
        name_art        Varchar (100) NOT NULL ,
        description_art Text NOT NULL ,
        create_at       Datetime NOT NULL ,
        update_at       Datetime NOT NULL ,
        file_art        Text NOT NULL ,
        id_User         Int NOT NULL
	,CONSTRAINT Artricle_PK PRIMARY KEY (id)

	,CONSTRAINT Artricle_User_FK FOREIGN KEY (id_User) REFERENCES User(id)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: commenter
#------------------------------------------------------------

CREATE TABLE commenter(
        id          Int NOT NULL ,
        id_Artricle Int NOT NULL
	,CONSTRAINT commenter_PK PRIMARY KEY (id,id_Artricle)

	,CONSTRAINT commenter_User_FK FOREIGN KEY (id) REFERENCES User(id)
	,CONSTRAINT commenter_Artricle0_FK FOREIGN KEY (id_Artricle) REFERENCES Artricle(id)
)ENGINE=InnoDB;

