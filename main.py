from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from typing import List, Optional
from pydantic import BaseModel
from datetime import date

app = FastAPI(title="社員マスターAPI")

# 社員データのモデル
class Employee(BaseModel):
    employee_id: int
    name: str
    department: str
    position: str
    hire_date: date
    email: str
    phone: Optional[str] = None

# サンプルデータ
employees = [
    Employee(
        employee_id=1,
        name="山田 太郎",
        department="営業部",
        position="課長",
        hire_date=date(2015, 4, 1),
        email="yamada@example.com",
        phone="090-1234-5678"
    ),
    Employee(
        employee_id=2,
        name="佐藤 花子",
        department="人事部",
        position="主任",
        hire_date=date(2018, 7, 1),
        email="sato@example.com",
        phone="090-8765-4321"
    ),
    Employee(
        employee_id=3,
        name="鈴木 一郎",
        department="開発部",
        position="部長",
        hire_date=date(2010, 4, 1),
        email="suzuki@example.com"
    )
]

@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>社員マスターAPI_NEW!</title>
            <style>
                body {
                    font-family: 'Arial', sans-serif;
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                    background-color: #f0f8ff;
                }
                h1 {
                    color: #4a90e2;
                    text-align: center;
                }
                .container {
                    background-color: white;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                }
                .endpoint {
                    margin: 10px 0;
                    padding: 10px;
                    background-color: #f8f9fa;
                    border-radius: 5px;
                }
                code {
                    background-color: #e9ecef;
                    padding: 2px 5px;
                    border-radius: 3px;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>✨ 社員マスターAPI ✨</h1>
                <p>以下のエンドポイントが利用可能です：</p>
                <div class="endpoint">
                    <code>GET /api/employees</code> - 全社員一覧を取得
                </div>
                <div class="endpoint">
                    <code>GET /api/employees/{employee_id}</code> - 特定の社員情報を取得
                </div>
                <div class="endpoint">
                    <code>GET /api/employees/department/{department}</code> - 部署別の社員一覧を取得
                </div>
            </div>
        </body>
    </html>
    """

@app.get("/api/employees", response_model=List[Employee])
async def get_employees():
    return employees

@app.get("/api/employees/{employee_id}", response_model=Employee)
async def get_employee(employee_id: int):
    for employee in employees:
        if employee.employee_id == employee_id:
            return employee
    raise HTTPException(status_code=404, detail="社員が見つかりません")

@app.get("/api/employees/department/{department}", response_model=List[Employee])
async def get_employees_by_department(department: str):
    return [emp for emp in employees if emp.department == department]

@app.get("/api/hello")
async def hello():
    return {"message": "こんにちは！テスト！"} 