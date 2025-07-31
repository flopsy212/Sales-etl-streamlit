# etl.py

import pandas as pd
import sqlite3
from pathlib import Path
from normalize import normalize_store_name, normalize_item_name, normalize_category, clean_price

def load_and_clean_csv(file_path):
    # 拡張子チェックやファイル名から店舗推定も可能
    if "store_a" in file_path.name:
        df = pd.read_csv(file_path)
        df.columns = ["Date", "StoreName", "Item", "Category", "Quantity", "UnitPrice"]
    elif "store_b" in file_path.name:
        df = pd.read_csv(file_path)
        df.columns = ["Date", "StoreName", "Item", "Category", "Quantity", "UnitPrice"]
        df["UnitPrice"] = df["UnitPrice"].apply(clean_price)

    # 整形
    df["Date"] = pd.to_datetime(df["Date"])
    df["Norm_StoreName"] = df["StoreName"].apply(normalize_store_name)
    df["Norm_Item"] = df["Item"].apply(normalize_item_name)
    df["Norm_Category"] = df["Category"].apply(normalize_category)
    df["SourceFile"] = file_path.name
    return df

def insert_into_db(df, db_path="db/sales.db"):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    for _, row in df.iterrows():
        # 店舗マスタ登録
        cur.execute("INSERT OR IGNORE INTO stores (store_name, raw_name) VALUES (?, ?)",
                    (row["Norm_StoreName"], row["StoreName"]))
        cur.execute("SELECT store_id FROM stores WHERE store_name = ?", (row["Norm_StoreName"],))
        store_id = cur.fetchone()[0]

        # 商品マスタ登録
        cur.execute("INSERT OR IGNORE INTO items (item_name, category, raw_name) VALUES (?, ?, ?)",
                    (row["Norm_Item"], row["Norm_Category"], row["Item"]))
        cur.execute("SELECT item_id FROM items WHERE item_name = ? AND category = ?",
                    (row["Norm_Item"], row["Norm_Category"]))
        item_id = cur.fetchone()[0]

        # 売上データ登録
        cur.execute("""
            INSERT INTO sales (sale_date, store_id, item_id, quantity, unit_price, source_file)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (row["Date"], store_id, item_id, row["Quantity"], row["UnitPrice"], row["SourceFile"]))

    conn.commit()
    conn.close()

def main():
    data_dir = Path("data")
    for file_path in data_dir.glob("*.csv"):
        df = load_and_clean_csv(file_path)
        insert_into_db(df)

if __name__ == "__main__":
    main()
    
