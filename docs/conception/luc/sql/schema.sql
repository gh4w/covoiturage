
-- select * from sqlite_master


drop table if exists Utilisateur;

create table Utilisateur (
    id integer primary key,
    login text not null
);

drop table if exists Personne;

create table Personne (
    id integer primary key,
    nom text not null,
    prenom text not null,
    foreign key (id) references Utilisateur(id)
);

drop table if exists Vehicule;

create table Vehicule (
    id integer primary key,
    id_proprietaire integer not null,
    nom text not null,
    foreign key (id_proprietaire) references Utilisateur(id)
);
