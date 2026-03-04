import pymysql
import pytest
import os
@pytest.fixture(scope="module")
def db_connection():
    connection = pymysql.connect(
        host=os.getenv("DB_HOST","localhost"),
        user=os.getenv("DB_USER","root"),
        password=os.getenv("DB_PASSWORD","root"),
        database=os.getenv("DB_NAME","testdb")
    
    )
    yield connection
    connection.close()

def test_create_table_for_db(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("CREATE TABLE users( name VARCHAR(100), email VARCHAR(100))")
    db_connection.commit()

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

