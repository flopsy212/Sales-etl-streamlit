✅ プロジェクト概要（仮タイトル）
「バラバラな売上データを正規化して統合するETLパイプライン（Python × SQL）」

🎯 プロジェクトの目的（READMEにも書く）
「複数店舗から届く異なるフォーマットの売上データを自動で統合・整形し、分析可能な状態でDBに保存する仕組みを構築する」

想定する課題例：
ファイルの列名や形式が店舗ごとにバラバラ

商品名の表記ゆれ（例：「Tシャツ」「tshirt」など）

日付形式が統一されていない

単位や通貨の違い

保存先のDBスキーマをしっかり設計したい

🛠 使用技術（予定）
項目	技術
データ処理	Python（pandas）
データベース	SQLite or PostgreSQL（ローカルでOK）
スキーマ設計	SQL（CREATE文あり）
可視化	Streamlit（任意） or SQLの出力
スケジューリング	GitHub Actions（簡易化でもOK）
バージョン管理	GitHub（READMEに構成図付き）

📁 想定フォルダ構成（シンプルに）
pgsql
コピーする
編集する
ec_sales_pipeline/
├── data/
│   ├── store_a_2025.csv
│   ├── store_b_2025.csv
├── scripts/
│   ├── etl.py          ← メインスクリプト
│   ├── normalize.py    ← 整形処理用（分離してもOK）
├── db/
│   ├── schema.sql
│   └── sales.db
├── output/
│   └── reports/
├── README.md
├── requirements.txt
└── .gitignore
💡やることステップ（ざっくり）
🔹STEP1：CSVの設計とデータ準備（店舗A/B/Cで異なる形式）
列名が違う：Date vs 販売日

商品名が違う：tshirt, Tシャツ, Ｔシャツ

カラム不足や余分な情報が混在

🔹STEP2：ETLスクリプト作成（pandasで整形）
それぞれのCSVを吸い込み

商品名・カテゴリの正規化

日付型変換、NULL処理など

🔹STEP3：DBスキーマ設計とデータ格納
salesテーブル（商品、売上、店舗、日付、数量など）

商品マスタ、店舗マスタも使って正規化設計

🔹STEP4：SQLで分析（TOP商品、月別推移など）
SQLファイルにして明示的に管理

🔹STEP5（任意）：Streamlitなどで可視化
🔹STEP6：README＆Qiita記事でまとめて発信
