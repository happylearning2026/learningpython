-- 创建商品信息表
-- CREATE TABLE products (
--     product_id SERIAL PRIMARY KEY,
--     product_name VARCHAR(255) NOT NULL,
--     price DECIMAL(10, 2),
--     description TEXT
-- );

-- 插入一些测试数据
-- INSERT INTO products (product_name, price, description) VALUES ('苹果', 5.00, '新鲜红苹果');
-- INSERT INTO products (product_name, price, description) VALUES ('香蕉', 3.50, '进口香蕉');
-- INSERT INTO products (product_name, price, description) VALUES ('橙子', 4.20, '甜橙子');
INSERT INTO products (product_name, price, description) VALUES ('葡萄', 8.00, '紫葡萄');

-- 查询所有商品信息
SELECT * FROM products;


select 1;