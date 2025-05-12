from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_employees():
    """社員一覧を取得するAPIのテスト"""
    response = client.get("/api/employees")
    assert response.status_code == 200
    
    # レスポンスの内容を確認
    employees = response.json()
    assert len(employees) == 3  # サンプルデータの数
    
    # 最初の社員データの内容を確認
    first_employee = employees[0]
    assert first_employee["employee_id"] == "EMP001"
    assert first_employee["name"] == "山田 太郎"
    assert first_employee["department"] == "営業部"
    assert first_employee["position"] == "課長"
    assert first_employee["email"] == "yamada@example.com"
    assert first_employee["phone"] == "090-1234-5678" 