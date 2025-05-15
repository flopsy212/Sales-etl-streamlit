# 🧾 売上データETL＋可視化パイプライン

複数店舗から届く形式バラバラな売上CSVを自動で整形・統合し、SQLiteに格納。  
非エンジニアでも使える、**売上CSVの整形〜可視化**を1クリックで実現する軽量ETLダッシュボード。
Streamlitで可視化することで、**非エンジニアでも売上状況を簡単に確認できるWebアプリ**を構築しました。

![Python](https://img.shields.io/badge/python-3.10-blue)
![Streamlit](https://img.shields.io/badge/streamlit-%E2%AD%90-red)
![SQLite](https://img.shields.io/badge/sqlite-db-lightgrey)

---

## 📌 背景と目的

### 💡 課題
- 小売や飲食など複数店舗の売上集計では、提出されるCSV形式がバラバラ（列名、日付形式、商品名の表記ゆれなど）。
- 毎回Excelで手作業による整形・集計が必要となり、30分以上の時間と属人性が発生。

### 🔧 解決アプローチ
- PythonスクリプトでCSVを自動整形・正規化し、SQLiteに格納。
- Streamlitで可視化することで、**非エンジニアでも分析できるUI**を提供。

### ✅ 成果
- 毎回30分以上かかっていた作業を数秒に短縮。
- 手作業によるミス削減、業務の標準化・効率化に成功。

---

## 🛠 使用技術

- Python（pandas）
- SQLite
- Streamlit
- Altair
- Mermaid（構成図作成）

---

## 📁 ディレクトリ構成

```plaintext
Sales-etl-streamlit/
├── data/            # 元データCSV格納用
├── db/              # SQLite DB格納先
├── normalize.py     # CSV整形スクリプト
├── etl.py           # DB格納スクリプト
├── app.py           # Streamlitアプリ
├── requirements.txt # 使用ライブラリ一覧
└── README.md        # 本ドキュメント
```

---

## 🔄 処理フロー

```mermaid
graph TD
    A[CSVファイル] --> B[normalize.py（整形処理）]
    B --> C[normalized_sales.csv]
    C --> D[etl.pyでDB格納]
    D --> E[sales.db（3テーブル）]
    E --> F[Streamlitで読み込み]
    F --> G[Webで表示・分析]
```

## 🚀 実行方法

 1. リポジトリをクローン
```bash
git clone https://github.com/flopsy212/Sales-etl-streamlit.git
cd Sales-etl-streamlit
```

 2. 必要なライブラリをインストール
  ```
pip install -r requirements.txt
```

 3. データ整形（CSV → 正規化CSV）
 ```
python normalize.py
```

 4. SQLiteデータベースへの格納
```
python etl.py
```

 5. Streamlitアプリを起動
```
streamlit run app.py
```

## 📷 アプリ画面イメージ

![アプリ画面1](https://github.com/user-attachments/assets/ab39ccd4-9124-4059-b3f9-97d6d8360444)

![アプリ画面2](https://github.com/user-attachments/assets/309b3da5-5751-4347-9223-aad40431fa88)


✍ Qiita記事（詳細解説）
[Qiita記事はこちら](https://qiita.com/flopsy_tech/items/def6a3f746bfd440c3f6)

## 💬 今後の展望

- ✅ **DWH対応（BigQueryなど）**
- 🔄 **ETL自動化（Airflow）**
- 📊 **KPIやダッシュボード拡張**
- 📡 API連携による外部データ取り込み
- ☁️ クラウド対応（AWS Lambda や GCS などでの自動実行）
- 🧠 シンプルな売上予測モデルの実装（scikit-learn など）


[GitHubプロフィール](https://github.com/flopsy212)
