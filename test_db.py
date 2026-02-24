import pymysql
import pytest

@pytest.fixture(scope="module")
def db_connection():
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="root123",
        database="automation_db",
        port=3306
    )
    yield connection
    connection.close()


def test_create_user(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES ('Harshini', 'harshini@test.com')")
    db_connection.commit()
    assert cursor.rowcount == 1


def test_read_user(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM users WHERE email='harshini@test.com'")
    result = cursor.fetchone()
    assert result is not None


def test_update_user(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("UPDATE users SET name='Updated' WHERE email='harshini@test.com'")
    db_connection.commit()
    assert cursor.rowcount == 1


def test_delete_user(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("DELETE FROM users WHERE email='harshini@test.com'")
    db_connection.commit()
    assert cursor.rowcount == 1

