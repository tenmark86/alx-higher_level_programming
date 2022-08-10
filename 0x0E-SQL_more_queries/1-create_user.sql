-- create the mysql server user "user_0d_1", should have all privileges
-- and password should be set ti user_0d_1_pw
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pw';
GRANT ALL PRIVILEGES ON *.* to 'user_0d_1'@'localhost';
