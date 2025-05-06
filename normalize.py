import pandas as pd
import glob
import os

def normalize_file(filepath, store_name):
    df = pd.read_csv(filepath)

    # カラム名を小文字＋前後の空白を削除
    df.columns = [col.strip().lower() for col in df.columns]

    # カラム名の変換マップ
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

    # 商品名の統一（仮）
    df['item_name'] = df['item_name'].replace({
        'tshirt': 'Tシャツ',
        'Tシャツ': 'Tシャツ',
        'シャツ': 'Tシャツ'
    })

    # 日付を YYYY-MM-DD 形式に変換
    df['sale_date'] = pd.to_datetime(df['sale_date'], errors='coerce').dt.strftime('%Y-%m-%d')

    # 店舗名列を追加
    df['store_name'] = store_name

    return df[['sale_date', 'item_name', 'quantity', 'unit_price', 'store_name']]

def main():
    csv_files = glob.glob('data/*.csv')
    all_data = []

    for file in csv_files:
        store = os.path.basename(file).split('_')[1]  # store_a_2025.csv → a
        df = normalize_file(file, f'store_{store}')
        all_data.append(df)

    merged = pd.concat(all_data, ignore_index=True)
    merged.to_csv('data/normalized_sales.csv', index=False)

    # ✅ ここで print する！
    print("✅ データ結合完了！")
    print(merged.head())  # ← ここ大事！

if __name__ == '__main__':
    try:
        main()
        print("✅ 処理完了！normalized_sales.csv を出力しました。")
    except Exception as e:
        print("❌ エラーが発生しました:", e)

