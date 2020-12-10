![Push Build][push-button]
![Release Build][release-button]
![License][license-button]
![Version][version-button]
![Status][status-button]

[push-button]: https://github.com/radupetre/net-speed-checker/workflows/build-push/badge.svg
[release-button]: https://github.com/radupetre/net-speed-checker/workflows/build-release/badge.svg
[license-button]: https://img.shields.io/pypi/l/net-speed-checker
[version-button]: https://img.shields.io/pypi/v/net-speed-checker
[status-button]: https://img.shields.io/pypi/status/net-speed-checker
[speedtest-cli]: https://github.com/sivel/speedtest-cli

# Net Speed Checker

net-speed-checker is a Python3 library for taking net speed measurements and persisting the measurements in RDBS.

### Features


### Installation

```sh
$ pip install net-speed-checker
```

### Usage

```sh
python3 check_speed.py $PROCESS_NAME $DBMS $USER $SCHEMA $SERVER_PORT $PASSWORD
```

or

```sh
python3 check_speed.py local_dev mysql admin my_schema mysql-url.com:3306 pa$$w0rd
```

or

```sh
python3 -c 'from net_speed_checker import check_speed; check_speed.measure("local_dev", "mysql", "admin", "my_schema", "mysql-url.com:3306", "pa$$w0rd")'
```

### Schema DDL

```sql
create table speed_measurement
(
	id int auto_increment
		primary key,
	client_name varchar(100) null,
	client_ip varchar(100) null,
	client_lat float null,
	client_lon float null,
	client_isp varchar(100) null,
	client_cc varchar(100) null,
	server_url varchar(100) null,
	server_lat float null,
	server_lon float null,
	server_cc varchar(100) null,
	server_city varchar(100) null,
	server_ping float null,
	upload float null,
	download float null,
	timestamp datetime not null,
	success tinyint(1) not null,
	message varchar(100) not null
);
```
Mentions
----
This library is using [sivel/speedtest-cli][speedtest-cli]

License
----

MIT


