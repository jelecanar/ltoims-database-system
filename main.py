from db import get_connection

try:
    conn = get_connection()
    cursor = conn.cursor()

    print("=== LTO Information Management System ===")
    print("Database Connected Successfully")

    cursor.execute("SHOW TABLES")

    print("\nTables inside JimlethDB:")
    for table in cursor:
        print("-", table[0])

    conn.close()

except Exception as e:
    print("Connection Error:", e)
