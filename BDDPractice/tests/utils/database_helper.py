import mysql.connector

class databaseHelper(object):

    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = "Pbhilare123!"
        self.database = "world"

    def database_connect(self):
        self.connection = mysql.connector.connect(host=self.host, user=self.user, password=self.password,
                                                  database=self.database, auth_plugin='mysql_native_password')

    def execute_select_sql(self, query):
        try:
            self.database_connect()
            cursor = self.connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()

            for count in result:
                print(count)

            cursor.close()
        except Exception as e:
            raise Exception("The database is not connected")
        finally:
            self.connection.close()

        return result

if __name__ == '__main__':
    dbConnect = databaseHelper()
    # dbConnect.execute_select_sql("SELECT count(*) FROM world.city where CountryCode = 'IND' and District = 'Maharashtra'")
    dbConnect.execute_select_sql(
        "SELECT * FROM world.city where CountryCode = 'IND' and District = 'Maharashtra'")