import pandas as pd
import glob
import os

def normalize_file(filepath, store_name):
    df = pd.read_csv(filepath, encoding='utf-8', quotechar='"')  

    df.columns = [col.strip().lower() for col in df.columns]

    col_map = {
        'item': 'item_name',
        '商品名': 'item_name',
        'date': 'sale_date',
        '売上日': 'sale_date',
        'qty': 'quantity',
        '数量': 'quantity',
        'price': 'unit_price',
        '単価': 'unit_price'
    }
    df = df.rename(columns=col_map)

    df['item_name'] = df['item_name'].replace({
        'tshirt': 'Tシャツ',
        'Tシャツ': 'Tシャツ',
        'シャツ': 'Tシャツ'
    })

    df['sale_date'] = pd.to_datetime(df['sale_date'], errors='coerce').dt.strftime('%Y-%m-%d')
    df['store_name'] = store_name

    print(f"✅ 読み込み成功: {filepath} → {df.shape}")
    return df[['sale_date', 'item_name', 'quantity', 'unit_price', 'store_name']]

def main():
    print("🔥 スクリプト開始")

    csv_files = glob.glob('data/*.csv')
    print(f"📁 CSVファイル一覧: {csv_files}")

    all_data = []
    for file in csv_files:
        store = os.path.basename(file).split('_')[1]
        df = normalize_file(file, f'store_{store}')
        all_data.append(df)

    merged = pd.concat(all_data, ignore_index=True)
    output_path = os.path.join(os.getcwd(), 'data', 'normalized_sales.csv')
    merged.to_csv(output_path, index=False)

    print("✅ 結合完了！")
    print("📝 出力先:", output_path)
    print(merged.head())

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print("❌ エラー:", e)
