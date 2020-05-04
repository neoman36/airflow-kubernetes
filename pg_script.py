from psycopg2 import connect


def main():
    conn = connect(
        'host=192.168.1.67 port=5432 dbname=mydb user=test_user password=root')
    cur = conn.cursor()

    cur.execute("SELECT * FROM  employees LIMIT 10")
    for row in cur.fetchall():
        print(row)


if __name__ == '__main__':
    main()
