import pymysql
import sys
import logging
import datetime

host = "localhost"
port = 3306
database = "ssg"
username = "root"
password = "root"

def main():
    try:
        # DB Connection 생성
        conn = pymysql.connect(host=host, user=username, password=password, database=database, port=port,
                               use_unicode=True, charset='utf8')
        cursor = conn.cursor()

    except:
        logging.error("에러")
        sys.exit(1)

    # cursor.execute("show tables")
    # print(cursor.fetchall())

    # query = "INSERT INTO product_sales_info (product_stars,review_count,product_sell_total_count) VALUE (5.00,200,300)"
    query = "UPDATE product_sales_info SET created_at = %s, modified_at = %s WHERE product_info_id = %s"
    values = (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 4)
    cursor.execute(query,values)
    conn.commit()

    conn.close()


if __name__ == '__main__':
    main()