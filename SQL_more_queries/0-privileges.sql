--  lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server 
SELECT CONCAT('SHOW GRANTS FOR ''',user,'''@''',host,''';') FROM mysql.user;
