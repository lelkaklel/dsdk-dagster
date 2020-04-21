# create databases
CREATE DATABASE IF NOT EXISTS `test_run_storage`;
CREATE DATABASE IF NOT EXISTS `test_event_log_storage`;
CREATE DATABASE IF NOT EXISTS `test_schedule_storag`;

# create root user and grant rights
CREATE USER 'root'@'localhost' IDENTIFIED BY 'local';
GRANT ALL ON *.* TO 'root'@'%';
