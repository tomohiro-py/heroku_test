# ✨ 社員マスターAPI ✨

## 🚀 デプロイ先
https://heroku-test-20250513-8a4cf67bc366.herokuapp.com/

## 📚 APIドキュメント
Swagger UIでAPIドキュメントを確認できます：
https://heroku-test-20250513-8a4cf67bc366.herokuapp.com/docs

## 🔍 サンプルURL

### 全社員一覧
https://heroku-test-20250513-8a4cf67bc366.herokuapp.com/api/employees

### 特定の社員情報（ID: 1）
https://heroku-test-20250513-8a4cf67bc366.herokuapp.com/api/employees/1

### 部署別社員一覧（営業部）
https://heroku-test-20250513-8a4cf67bc366.herokuapp.com/api/employees/department/営業部

## 🛠 技術スタック
- FastAPI
- Python 3.11
- Heroku

## 🚀 ローカル環境での起動方法

### Linux/Mac
```bash
uvicorn main:app --reload
```

### Windows
```bash
python -m uvicorn main:app --reload
```

## 🧪 テスト

### Linux/Mac
```bash
pytest
```

### Windows
```bash
python -m pytest
```

## 📝 ライセンス
MIT