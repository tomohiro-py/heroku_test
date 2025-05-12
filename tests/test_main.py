from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_employees():
    """社員一覧を取得するAPIのテスト"""
    # Arrange: テストの準備（このケースでは特に準備は不要）
    
    # Act: APIを呼び出し
    response = client.get("/api/employees")
    
    # Assert: レスポンスの検証
    assert response.status_code == 200
    
    # レスポンスの内容を確認
    employees = response.json()
    assert len(employees) == 3  # サンプルデータの数
    
    # 最初の社員データの内容を確認
    first_employee = employees[0]
    assert first_employee["employee_id"] == 1
    assert first_employee["name"] == "山田 太郎"
    assert first_employee["department"] == "営業部"
    assert first_employee["position"] == "課長"
    assert first_employee["email"] == "yamada@example.com"
    assert first_employee["phone"] == "090-1234-5678"

def test_get_employee():
    """特定の社員情報を取得するAPIのテスト"""
    # Arrange: テストの準備（このケースでは特に準備は不要）
    
    # Act: APIを呼び出し
    response = client.get("/api/employees/1")
    
    # Assert: レスポンスの検証
    assert response.status_code == 200
    data = response.json()
    assert data["employee_id"] == 1
    assert data["name"] == "山田 太郎"
    assert data["department"] == "営業部"
    assert data["position"] == "課長"
    assert data["email"] == "yamada@example.com"
    assert data["phone"] == "090-1234-5678"

def test_get_employee_not_found():
    """存在しない社員IDでAPIを呼び出した場合のテスト"""
    # Arrange: テストの準備（このケースでは特に準備は不要）
    
    # Act: APIを呼び出し
    response = client.get("/api/employees/999")
    
    # Assert: レスポンスの検証
    assert response.status_code == 404
    assert response.json()["detail"] == "社員が見つかりません"

def test_get_employees_by_department():
    """部署別の社員一覧を取得するAPIのテスト"""
    # Arrange: テストの準備（このケースでは特に準備は不要）
    
    # Act: APIを呼び出し
    response = client.get("/api/employees/department/営業部")
    
    # Assert: レスポンスの検証
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["employee_id"] == 1
    assert data[0]["name"] == "山田 太郎"
    assert data[0]["department"] == "営業部" 