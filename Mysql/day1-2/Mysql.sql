-- 创建表

CREATE TABLE orders (
  order_id     VARCHAR(32), -- 订单编号
  cust_id      VARCHAR(32), -- 客户编号
  order_date   DATETIME, -- 下单时间，日期时间类
  status       INT, -- 状态
  products_num INT, -- 商品数量，整数
  amt          DECIMAL(16, 2) -- 订单总金额
  -- 最长16位，小数2位
)
  DEFAULT CHARSET = utf8;

-- 插入信息

INSERT INTO orders VALUES
  ('201801010001', 'c0001', now(), 1, 1, 100.00);

-- 查询表中数据
SELECT *
FROM orders;

-- 向表中插入指定字段
INSERT INTO orders (order_id, cust_id)
VALUES ('201801010002', 'c0002');

-- 一个SQL语句插入多笔数据
INSERT INTO orders VALUES
  ('201801010003', 'c0003', now(), 1, 1, 200.00),
  ('201801010004', 'c0004', now(), 1, 1, 480.00);

-- 指定字段查询
SELECT
  order_id,
  cust_id
FROM orders;

-- 查询指定字段，并且起别名,别名用双引号引用
SELECT
  order_id "订单编号",
  cust_id  "客户编号"
FROM orders;

-- 带一个条件查询

SELECT *
FROM orders
WHERE order_id = '201801010003';

-- 带多个条件查询

SELECT *
FROM orders
WHERE order_id = '201801010003' OR status = 1; -- OR表示满足其中一个

-- 枚举,只可以填写括号后的值
CREATE TABLE enum_test (
  name   VARCHAR(32),
  sex    ENUM ('boy', 'girl'),
  course SET ('music', 'dance', 'paint')
);
INSERT INTO enum_test
VALUES ('jerry', 'girl', 'music,dance');

INSERT INTO enum_test
VALUES ('Tom', 'boy', 'musice,football'); -- 错误

--  时间类型数据
SELECT
  now(),
  sysdate(); -- 取当前时间
SELECT
  curdate(),
  curtime(); -- 取出当前日期，时间
SELECT
  year(now()),
  month(now()),
  day(now()); -- 取出当前年月日
SELECT
  DATE(now()),
  TIME(now()); -- 取出当前系统时间中的日期，时间部分

-- 修改数据
UPDATE orders
SET status = 2
WHERE order_id = '201801010001';

-- 删除表
DELETE FROM orders
WHERE order_id = '201801010002';

-- 更多查询语句
SELECT *
FROM orders
WHERE amt > 200;

SELECT *
FROM orders
WHERE status <> 2;

SELECT *
FROM orders
WHERE (cust_id = 'c0002' OR cust_id = 'c0003')
      AND status = 1;

SELECT *
FROM orders
WHERE amt BETWEEN 200 AND 300;

SELECT *
FROM orders
WHERE cust_id IN ('c0003', 'c0004');

CREATE TABLE customer (
  cust_id   VARCHAR(32),
  cust_name VARCHAR(32),
  tel_no    VARCHAR(32)
)
  DEFAULT CHARSET = utf8;

INSERT INTO customer VALUES
  ('c0001', 'Jerry', '13512345678'),
  ('c0002', 'Dekie', '13522334455'),
  ('c0003', 'Dokas', '13544445555');

-- 模糊查询
SELECT *
FROM customer
WHERE cust_name LIKE 'D%';

SELECT *
FROM customer
WHERE tel_no LIKE '%44%55%'; -- 44前面和后面　55前面和后面　包含任意个字符

UPDATE customer
SET tel_no = NULL
WHERE cust_id = 'c0003';

SELECT *
FROM customer
WHERE tel_no IS NULL;

SELECT
  order_id,
  amt
FROM orders
ORDER BY amt DESC;

SELECT *
FROM orders
LIMIT 2; -- 显示前两条

SELECT *
FROM orders
ORDER BY amt DESC
LIMIT 2; -- 先排序后显示


INSERT INTO customer VALUES
  ('c0004', 'Shirley', '13512345678'),
  ('c0005', 'Charlie', '13522334455'),
  ('c0006', 'Edward', '13544445555'),
  ('c0007', 'Job', '13544445555'),
  ('c0008', 'Elizabeth', '13548945555'),
  ('c0009', 'Ross', '13544467555'),
  ('c0010', 'Rachel', '13544223555');

-- 利用limit分页　每页3笔数据

SELECT *
FROM customer
LIMIT 0, 3;
SELECT *
FROM customer
LIMIT 3, 3;
SELECT *
FROM customer
LIMIT 6, 3;
SELECT *
FROM customer
LIMIT 9, 3;

-- 去重
SELECT DISTINCT (cust_name)
FROM customer;

-- 聚合函数(max,min,avg,sum,count)

SELECT
  max(amt) '最大金额',
  min(amt) '最小金额',
  avg(amt) '平均金额',
  sum(amt) '订单总金额'
FROM orders;

SELECT count(*)
FROM customer
WHERE tel_no LIKE '135%';

-- 分组
SELECT
  cust_name,
  count(*)
FROM customer
GROUP BY cust_name;

SELECT
  status,
  sum(amt)
FROM orders
GROUP BY status;

-- 过滤
SELECT
  status,
  sum(amt)
FROM orders
GROUP BY status
HAVING sum(amt) > 500;
-- having 过滤语句只能和group搭配
-- where　只能用表中有的字段作为条件使用
-- 先分组再聚合

-- 表结构调整，添加字段
CREATE TABLE student (
  stu_no   VARCHAR(32),
  stu_name VARCHAR(128)
);
-- 添加到最后
ALTER TABLE student
  ADD age INT;
-- 将id字段添加到第一个字段
ALTER TABLE student
  ADD id INT
  FIRST;
-- 将tel_no添加到stu_name　后面
ALTER TABLE student
  ADD tel_no VARCHAR(32)
  AFTER stu_name;

-- 修改字段类型
--  修改student表中stu_name字段长度为64
ALTER TABLE student
  MODIFY stu_name VARCHAR(64);

-- 改字段名称
-- 将student表age字段改为stu_age
ALTER TABLE student
    CHANGE age stu_age int;

-- 删除字段
-- 删除student表id字段
ALTER TABLE student DROP id;
