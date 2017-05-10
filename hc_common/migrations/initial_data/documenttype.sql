insert into hc_common_documenttype (id, name, description, status) values (1, 'DNI', 'DNI', 'Active');
insert into hc_common_documenttype (id, name, description, status) values (2, 'CI', 'CI', 'Active');
insert into hc_common_documenttype (id, name, description, status) values (3, 'LE', 'LE', 'Active');
insert into hc_common_documenttype (id, name, description, status) values (4, 'LC', 'LC', 'Active');
insert into hc_common_documenttype (id, name, description, status) values (5, 'Pas', 'Pas', 'Active');
insert into hc_common_documenttype (id, name, description, status) values (6, 'Otro', 'Otro', 'Active');
SELECT setval('hc_common_documenttype_id_seq', 6);
