import os
import time
from django.db import connections
from django.db.utils import OperationalError

def wait_for_db():
    """Ждем пока БД будет готова"""
    max_retries = 30
    retry_count = 0
    
    while retry_count < max_retries:
        try:
            conn = connections['default']
            conn.cursor()
            print("Database is available!")
            return True
        except OperationalError:
            retry_count += 1
            print(f"Waiting for database... (attempt {retry_count}/{max_retries})")
            time.sleep(1)
    
    raise Exception("Could not connect to database after 30 seconds")

if __name__ == '__main__':
    wait_for_db()
