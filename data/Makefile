all:

prepare:
	docker-compose up -d
restore:
	docker-compose down
clean-mariadb: prepare
	@-echo 'DROP TABLE movie;' | mysql -h 127.0.0.1 -P 3306 -u mariadb-user --password='mariadb-pass' mariadb-demo
