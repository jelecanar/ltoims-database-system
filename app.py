import mariadb

print("===================================")
print(" LTO Information Management System ")
print("===================================")

try:
    conn = mariadb.connect(
        host="localhost",
        user="root",
        password="yourpassword",
        database="JimlethDB"
    )

    cursor = conn.cursor()

    print("\nDatabase Connected Successfully")

    cursor.execute("SHOW TABLES")

    print("\nAvailable Tables:")
    for table in cursor:
        print("•", table[0])

    print("\nSystem Features:")
    print("✓ Driver Management")
    print("✓ Vehicle Registration")
    print("✓ Traffic Violation Monitoring")
    print("✓ Appointments")
    print("✓ Payment Processing")
    print("✓ Notifications")

    conn.close()

except mariadb.Error as e:
    print("Database Error:", e)
