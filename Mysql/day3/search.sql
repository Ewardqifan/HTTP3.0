# 子查询，一个查询语句中嵌套另一个

SELECT *
FROM orders
WHERE amt > (SELECT avg(amt)
             FROM orders);

# 查询所有客户名字以Ｄ开头的订单
SELECT *
FROM orders
WHERE cust_id IN
      (SELECT DISTINCT cust_id
       FROM customer
       WHERE cust_name LIKE 'D%');

SELECT *
FROM customer
WHERE cust_id NOT IN
      (SELECT DISTINCT cust_id
       FROM orders);

# 内链接
SELECT
  a.order_id,
  a.amt,
  b.cust_name,
  b.tel_no
FROM orders a, customer b
WHERE a.cust_id = b.cust_id;

SELECT
  a.order_id,
  a.amt,
  b.cust_name,
  b.tel_no
FROM orders a INNER JOIN customer b
    ON a.cust_id = b.cust_id;

#外连接（左连接与右连接）
SELECT
  a.order_id,
  a.amt,
  b.cust_name,
  b.tel_no
FROM orders a LEFT JOIN customer b # 输出全部的orders然后匹配customer
    ON a.cust_id = b.cust_id;

SELECT
  a.order_id,
  a.amt,
  b.cust_name,
  b.tel_no
FROM orders a RIGHT JOIN customer b
    ON a.cust_id = b.cust_id;

# 作业
CREATE TABLE orders_detail (
  order_id   VARCHAR(32),
  product_id VARCHAR(32),
  amt        DECIMAL(16, 2)
)
  DEFAULT CHARSET = utf8;

DESC orders_detail;

INSERT INTO orders_detail VALUES
  ('201801010001', 'p001', 100),
  ('201801010003', 'p002', 200),
  ('201801010004', 'p003', 480);

SELECT
  a.order_id,
  a.order_date,
  b.cust_name,
  c.product_id,
  c.amt
FROM orders a, customer b, orders_detail c
WHERE (a.cust_id = b.cust_id) AND (a.order_id = c.order_id);

UPDATE orders
SET tel_no = NULL
WHERE cust_id = 'c0003';

# 约束
CREATE TABLE t1 (
  stu_no    VARCHAR(32) PRIMARY KEY, #主键
  stu_name  VARCHAR(32) NOT NULL, #非空
  id_car_no VARCHAR(32) UNIQUE #唯一
);
INSERT INTO t1 VALUES
  ('001', 'Jerry', '513822199001011111');

ALTER TABLE t1
  CHANGE id_car_no id_card_no VARCHAR(32);

INSERT INTO t1 VALUES
  #       ('002',NULL,'513822199401242144'),
  ('003', 'Jeson', '513822199401242144');

DELETE FROM t1
WHERE stu_no = '003';

INSERT INTO t1
VALUES ('003', 'Tom', '513822199001011111');

INSERT INTO t1 (stu_no, stu_name)
VALUES ('001', 'Dokas');

CREATE TABLE t2 (
  id     INT PRIMARY KEY AUTO_INCREMENT,
  name   VARCHAR(32),
  status INT             DEFAULT 0
);
INSERT INTO t2 VALUES (NULL, 'Jerry', 1);
INSERT INTO t2 (id, name) VALUES (NULL, 'Tom');
UPDATE t2
SET name = 'John'
WHERE id = 2;

# 外键约束，现有主键后才可以插入信息
# 删除已经关联的主键×　插入主键中没有的信息×
# 表的存储引擎必须位innoDB
# 两个表的字段类型必须一致，注意编码格式的影响
CREATE TABLE course (
  course_id VARCHAR(32) PRIMARY KEY,
  name      VARCHAR(32)
)
  DEFAULT CHARSET = utf8;

CREATE TABLE teacher (
  id        INT PRIMARY KEY AUTO_INCREMENT, #　自增长必须是主键哦
  name      VARCHAR(32),
  course_id VARCHAR(32), #与上面的保持一致
  CONSTRAINT fk_coures FOREIGN KEY (course_id)
  REFERENCES course (course_id)
)
  DEFAULT CHARSET = utf8;

INSERT INTO course VALUES
  ('0001', 'python');

INSERT INTO teacher VALUES
  (1, 'Jerry', '0001'); -- 可以插入

DELETE FROM course
WHERE course_id = '0001';

INSERT teacher VALUES
  (NULL, 'Tom', '0002');

CREATE TABLE t6 (
  id        INT,
  name      VARCHAR(32),
  status    INT,
  course_id VARCHAR(4),
  tel_no    VARCHAR(32)
)
  DEFAULT CHARSET = utf8;

ALTER TABLE t6
  ADD PRIMARY KEY (id);
ALTER TABLE t6
  MODIFY id INT AUTO_INCREMENT;
ALTER TABLE t6
  MODIFY status INT DEFAULT 0;
ALTER TABLE t6
  MODIFY tel_no VARCHAR(32);
ALTER TABLE t6
  MODIFY tel_no VARCHAR(32) UNIQUE;
ALTER TABLE t6
  ADD CONSTRAINT fk_course_id
FOREIGN KEY (course_id) REFERENCES course (course_id);

#查看导出目录
SHOW VARIABLES LIKE 'secure_file%';

#文件导出
SELECT *
FROM orders
INTO OUTFILE '/var/lib/mysql-files/orders.csv'
FIELDS TERMINATED BY ',' #字段分隔符
LINES TERMINATED BY '\n'; #行分割符

#文件导入
LOAD DATA INFILE '/var/lib/mysql-files/orders.csv'
INTO TABLE orders
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';

# 表的复制
CREATE TABLE orders_new
  SELECT *
  FROM orders;

CREATE TABLE orders_new
  SELECT *
  FROM orders
  WHERE 1 = 0; #只复制表结构，形成空表。不会将key的属性复制过去。

#表的重名名
ALTER TABLE orders
  RENAME TO orders_bak;










