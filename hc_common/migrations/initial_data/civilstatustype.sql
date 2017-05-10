insert into hc_common_civilstatustype (id, name, description, status) values (1, 'Soltero', 'Soltero', 'Active');
insert into hc_common_civilstatustype (id, name, description, status) values (2, 'Casado', 'Casado', 'Active');
insert into hc_common_civilstatustype (id, name, description, status) values (3, 'Divorciado', 'Divorciado', 'Active');
insert into hc_common_civilstatustype (id, name, description, status) values (4, 'Viudo', 'Viudo', 'Active');
SELECT setval('hc_common_civilstatustype_id_seq', 4);
