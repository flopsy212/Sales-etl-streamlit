-- 店舗マスタ
CREATE TABLE stores (
    store_id INTEGER PRIMARY KEY AUTOINCREMENT,
    store_name TEXT NOT NULL,
    raw_name TEXT
);

-- 商品マスタ
CREATE TABLE items (
    item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_name TEXT NOT NULL,
    category TEXT NOT NULL,
    raw_name TEXT
);

-- 売上実績
CREATE TABLE sales (
    sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
    sale_date DATE NOT NULL,
    store_id INTEGER NOT NULL,
    item_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    unit_price INTEGER NOT NULL,
    source_file TEXT,
    FOREIGN KEY (store_id) REFERENCES stores(store_id),
    FOREIGN KEY (item_id) REFERENCES items(item_id)
);

