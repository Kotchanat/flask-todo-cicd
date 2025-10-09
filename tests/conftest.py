import pytest
from app import create_app, db

@pytest.fixture
def app():
    """สร้าง Flask app สำหรับ test"""
    app = create_app('testing')
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    """สร้าง client สำหรับส่ง request"""
    return app.test_client()
