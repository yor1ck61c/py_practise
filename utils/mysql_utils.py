import pymysql


class ConMysql:

    config = {
        "host": "127.0.0.1",
        "port": "3306",
        "user": "root",
        "password": "0601",
        "charset": "utf8",
        "cursor_class": pymysql.cursors.DictCursor
    }

    def __init__(self, config): {

    }