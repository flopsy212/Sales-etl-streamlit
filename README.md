# 🧾 売上データETL＋可視化パイプライン

複数店舗から届く形式バラバラな売上CSVを自動で整形・統合し、SQLiteに格納。  
Streamlitで可視化することで、**非エンジニアでも売上状況を簡単に確認できるWebアプリ**を構築しました。

---

## 📌 背景と目的

- 各店舗の売上CSVが日付・列名・商品名表記などバラバラ  
- Excelでの手作業が多く、集計や報告に時間がかかっていた  
- 「整形 → 格納 → 可視化」の流れを自動化し、属人化を解消

---

## 🛠 使用技術

- Python（pandas）
- SQLite
- Streamlit
- Altair
- Mermaid（構成図作成）

---

## 📁 ディレクトリ構成

Sales-etl-streamlit/
├── data/ # 元データCSV格納用
├── db/ # SQLite DB格納先
├── normalize.py # CSV整形スクリプト
├── etl.py # DB格納スクリプト
├── app.py # Streamlitアプリ
├── requirements.txt # 使用ライブラリ一覧
└── README.md # 本ドキュメント


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

🚀 実行方法
リポジトリをクローン

git clone https://github.com/flopsy212/Sales-etl-streamlit.git
cd Sales-etl-streamlit
ライブラリをインストール


pip install -r requirements.txt
データ整形とDB格納


python normalize.py
python etl.py
Streamlitアプリの起動


streamlit run app.py
📷 アプリ画面イメージ
（スクリーンショットやGIFをここに貼ってください）

✍ Qiita記事（詳細解説）
Qiita記事はこちら

💬 今後の展望
データ量増加に対応できるDWH（BigQuery等）への移行

Airflow等を使ったETLの自動化・定期実行

KPI可視化・多角的分析への拡張

🧑‍💻 作者情報
flopsy_tech
業務改善・自動化に関心を持ち、VBAやPythonで業務効率化を経験。
現在はデータエンジニア志望として、データ基盤やパイプライン構築に注力中。



