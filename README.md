# 🧾 売上データETL＋可視化パイプライン

複数店舗から届く形式バラバラな売上CSVを自動で整形・統合し、SQLiteに格納。  
Streamlitで可視化することで、**非エンジニアでも売上状況を簡単に確認できるWebアプリ**を構築しました。

---

## 📌 背景と目的

- 各店舗の売上CSVが**日付・列名・商品名表記などバラバラ**
- Excelでの手作業が多く、**集計や報告に時間がかかっていた**
- **整形 → 格納 → 可視化**の流れを自動化し、属人化を解消したい

---

## 💡 解決したこと

- 列名や商品名の**表記ゆれを統一**
- SQLiteへ格納し、**JOINしやすいスキーマで構造化**
- Streamlitで**直感的に売上データを可視化**

---

## 🛠 使用技術

| 処理 | 技術 |
|------|------|
| データ整形 | Python（pandas） |
| DB格納 | SQLite（schema.sql） |
| 可視化 | Streamlit / Altair |
| スクリプト管理 | GitHub / Mermaid（構成図） |

---

## 📁 ディレクトリ構成

ec_sales_pipeline/
├── data/ # 店舗別の生CSV
├── db/ # SQLiteデータ
├── normalize.py # 正規化処理
├── etl.py # DB格納処理
├── app.py # Streamlitアプリ
├── schema.sql # テーブル定義
├── README.md
├── requirements.txt
└── .gitignore
---

## 🚀 実行方法

```bash
# 1. 正規化
python normalize.py

# 2. SQLiteへ格納
python etl.py

# 3. Webで可視化
streamlit run app.py
```

## 📷 アプリ画面イメージ（例）
📊 商品別売上のAltairグラフ

## 📍 店舗ごとのフィルター機能付き表
※ スクリーンショットは後から貼り付けてください

## 🧠 工夫・学び・つまずいた点
T-shirt／シャツなど同義表現の自動統一（マッピング処理）

正規化されたDBスキーマ設計の基礎

StreamlitでのUI設計（営業や上司に見せやすい画面づくり）

「データを“整える”ことの意味」を実感

## 💼 想定ユースケース
店舗別の売上を社内で毎週共有したいとき

営業・販促担当が非エンジニアでもデータを確認したいとき

バラバラなCSVを定期的に整備・保存したいとき

## 🔮 今後の展望
Altairでの色分け・インサイト表示の強化

日付フィルターや期間指定機能の追加

GitHub Actionsで定期実行（週次バッチ処理）

👉 解説記事はこちら：[Qiitaリンク](https://qiita.com/flopsy_tech/items/def6a3f746bfd440c3f6)


