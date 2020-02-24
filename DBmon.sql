/*
.mode column
.headers on
*/

/*БД проект-серверная, для учета объектов мониторинга*/
create table pc
(
	id integer not null primary key, -- ключ ID сервера
	name text, 						 -- название
	ipadress text, 					 -- IP adress
	os text 						 -- операционная система
);
insert into pc values(1, 'zp-dseriy', '10.200.4.67', '');
insert into pc values(2, 'dima-PC', '10.200.5.167', '');
insert into pc values(3, 'server1', '192.168.0.1', '');
insert into pc values(4, 'server-SQL', '192.168.92.169','');
insert into pc values(5, 'NAS', '192.168.92.111','');

/*БД серверная, для консолидации данных по состоянию системы клиентов*/
create table serv
(
	id integer not null primary key, -- ключ ID записи
	name text, 						 -- DNS имя сервера - объекта мониторинга
	ipadress text, 					 -- IP adress сервера - объекта мониторинга
	os text, 						 -- операционная сервера - объекта мониторинга
	time_d text,					 -- дата сканирования системы сервера - объекта мониторинга
	time_t text,					 -- время сканирования системы сервера - объекта мониторинга
	cpu_name text,				     -- Имя процессора
	cpu_percent real,				 -- загрузка CPU, общая за 1 сек
	cpu_count_l integer,			 -- колличество логических процессоров
	cpu_count_f integer,			 -- колличество физических процессоров
	ram_total integer,				 -- общий объем RAM, в Гб
	ram_percent integer,			 -- % использования памяти
	ram_used integer,				 -- объем используемой памяти
	disk_total integer, 			 -- общий объем дисков
	disk_percent integer, 			 -- % использования дисков
	disk_used integer				 -- используемый объем диска
);
/*БД клиентская, для сбора данных по состоянию системы*/
create table client
(
	id integer not null primary key, -- ключ ID записи
	name text, 						 -- DNS имя сервера - объекта мониторинга
	ipadress text, 					 -- IP adress сервера - объекта мониторинга
	os text, 						 -- операционная сервера - объекта мониторинга
	time_d text,					 -- дата сканирования системы сервера - объекта мониторинга
	time_t text,					 -- время сканирования системы сервера - объекта мониторинга
	cpu_name text,				     -- Имя процессора
	cpu_percent real,				 -- загрузка CPU, общая за 1 сек
	cpu_count_l integer,			 -- коллиество логических процессоров
	cpu_count_f integer,			 -- коллиество физических процессоров
	ram_total integer,				 -- общий объем RAM, в Гб
	ram_percent integer,			 -- % использования памяти
	ram_used integer,				 -- объем используемой памяти
	disk_total integer, 			 -- общий объем дисков
	disk_percent integer, 			 -- % использования дисков
	disk_used integer				 -- используемый объем диска
);
delete from client
where code like '%7%' or code like '%6%';