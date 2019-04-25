
-- 1. 创建数据库bank, 并指定为utf8编码格式

-- 2. 创建账户表(acct, utf8编码格式), 包含如下字段
--	acct_no   	账号，字符串类型，长度32字符
--	acct_name 	户名，字符串类型，长度128字符
--	cust_no   	客户编号，字符串类型，长度32字符
--	acct_type	账户类型, 整数型(1-存款账户 2-贷款账户)
--	reg_date	开户日期, 日期类型
--	status		账户状态(1-正常 2-注销 3-挂失 4-冻结)
--	balance   	数字类型，最长16位，2位小数

-- 3. 至少插入五笔数据(要求数据尽量看上去真实)

-- 4. 编写如下SQL语句
-- 1)查找某个客户账户信息(以客户编号做条件)
-- 2)查找余额大于等于5000的账户信息
-- 3)查找余额大于等于5000的贷款账户信息
-- 4)查找账户名称以'D'开头的所有账户信息
-- 5)查找所有账户信息，并按照金额倒序排列
-- 6)统计每种状态的账户笔数
-- 7)查询账户余额的最大值、最小值、平均值、总金额
-- 8)查询账户余额最大的前3笔订单

create DATABASE bank DEFAULT CHARSET = utf8;
SHOW DATABASES;
USE bank;
SELECT DATABASE();
SHOW TABLES ;
create table acct(
  acct_no VARCHAR(32),
  acct_name VARCHAR(128),
  cust_no VARCHAR(32),
  acct_type int,
  reg_date DATETIME,
  status int,
  balance DECIMAL(16,2)
) DEFAULT CHARSET = utf8;

desc acct;
SELECT *
FROM acct;
INSERT INTO acct VALUES
  ('ac0001001','Hank','a0001',2,now(),1,489.11);
INSERT INTO acct VALUES
  ('ac0002001','David','a0002',1,now(),1,50000);
INSERT INTO acct VALUES
  ('ac0003001','Dennis','a0003',1,sysdate(),3,1289.2);
INSERT INTO acct VALUES
  ('ac0004001','Bob','a0004',2,now(),2,12.8);
INSERT INTO acct VALUES
  ('ac0005001','Brad','a0005',1,now(),4,500);
INSERT INTO acct VALUES
  ('ac0006001','Jason','a0006',1,now(),1,1666500);
INSERT INTO acct VALUES
  ('ac0006002','Jason','a0006',2,now(),1,197881.01);

SELECT * FROM acct;

SELECT * FROM acct
WHERE cust_no = 'a0006';

SELECT *
FROM acct
WHERE balance >= 5000;

SELECT *
FROM acct
WHERE (balance >= 5000 and acct_type = 2);

SELECT *
FROM acct
WHERE acct_name like 'D%';

SELECT *
FROM acct
ORDER BY balance DESC;

SELECT status,count(*)
FROM acct
GROUP BY status;

SELECT min(balance) '最小金额',
  max(balance) '最大金额',
  avg(balance) '平均金额',
  sum(balance) '金额总和'
FROM acct;

SELECT *
FROM acct
ORDER BY  balance DESC
LIMIT 0,3;


ALTER TABLE acct add PRIMARY KEY(acct_no);
ALTER TABLE acct MODIFY acct_name
    VARCHAR(32) NOT NULL ;
ALTER TABLE acct MODIFY acct_type
    INT NOT NULL ;
ALTER TABLE acct MODIFY status
    int DEFAULT 1;

CREATE TABLE customer(
  cust_no VARCHAR(32) PRIMARY KEY,
  tel_no  VARCHAR(32) NOT NULL ,
  cust_name VARCHAR(64) NOT NULL ,
  address VARCHAR(128) NOT NULL
) DEFAULT CHARSET = utf8;

INSERT into customer VALUES
  ('a0001','13259473832','David','西安雁塔区');

SELECT cust_name,tel_no FROM customer
WHERE cust_no in
      (SELECT DISTINCT cust_no FROM acct WHERE acct_type = 2);

SELECT a.acct_no,a.acct_name,a.acct_type,a.balance,
        b.cust_no,b.tel_no,b.address
FROM acct a ,customer b
WHERE a.cust_no = b.cust_no;




