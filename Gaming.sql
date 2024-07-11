use gaming;
-- to change the current directory to payment schemas
create table details(user_id int auto_increment primary key, username varchar(50) not null,level_no varchar(50) not null, friends_list varchar(150) not null, score int not null, login_date date default(CURRENT_DATE) ,time varchar(50));
-- create a table called details which has columns user_id whose datatype is int ,username whose datatype is varchar of size 50,level_no,friends_list,score, login_date,time
SELECT * FROM gaming.details;
-- it is used to print all the rows and columns of table details and database payment