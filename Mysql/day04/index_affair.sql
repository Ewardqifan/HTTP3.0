
# 加入索引
CREATE TABLE index_test(
  id int PRIMARY KEY ,
  cert_no VARCHAR(32),
  name VARCHAR(32),
  UNIQUE(cert_no),
  index(name)
);

INSERT into index_test VALUES
  (1,'0001','Jerry');
INSERT into index_test VALUES
  (2,'0001','Jerry');

# 删除索引
DROP INDEX cert_no on index_test;
DROP INDEX name on index_test;

#　修改表的方式添加索引
CREATE UNIQUE index idx_cert_no
  on index_test(cert_no);


# ============================================
# 数据库事务
# ============================================
CREATE TABLE acct(
  acct_no VARCHAR(32),
  acct_name VARCHAR(32),
  balance DECIMAL(16,2)
);
INSERT into acct VALUES
  ('0001','Jerry','1000'),
  ('0002','Tom','2000');

# 开启事务
start TRANSACTION ;
UPDATE acct set balance = balance - 100
  WHERE acct_no='0001';
UPDATE acct SET balance = balance + 100
WHERE acct_no = '0002';
COMMIT ; # rollback是回滚撤回上述的暂时操作


# 权限管理
# 授权
GRANT SELECT on eshop.*
to 'Tom'@'%'
IDENTIFIED BY '123456';

GRANT all PRIVILEGES on eshop.*
to 'Jerry'@'localhost'
IDENTIFIED BY '123456';

# 更新权限
FLUSH PRIVILEGES ;

# 查看权限
SELECT * FROM mysql.db
WHERE user = 'Jerry'\G;


REVOKE DELETE on eshop.*
    FROM 'Jerry'@'localhost';

# 查看存储引擎
show engines;

#更改存储引擎
alter table t3 ENGINE InnoDB


# 查看数据存储目录
show global variables like '%datadir';

