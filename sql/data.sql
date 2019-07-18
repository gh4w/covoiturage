delete from  Utilisateur;
insert into Utilisateur(login) values('bob');

delete from Vehicule;
insert into Vehicule(
    id_proprietaire,
    nom
) values (
    (select id from Utilisateur where login = 'bob'),
    '206'
);
