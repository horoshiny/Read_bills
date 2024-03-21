import mysql.connector
# Import necessary libraries
from readd import all


mydb = mysql.connector.connect(
  host="localhost",
  user="shiny",
  password="Srisheshi3",
  database="readingbills"
)
#mycursor = mydb.cursor()
'''
mycursor.execute(
    "CREATE TABLE `readingbills` ("
    "  `id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `Date` date NOT NULL,"
    "  `Prices` double NOT NULL,"
    "  PRIMARY KEY (`id`)"
    ")"
)
'''
def get_all(connection):
    cursor = connection.cursor()
    query="SELECT * FROM readingbills.readingbills"
    cursor.execute(query)

    response=[]

    for (idprices,Date, Prices) in cursor:
        response.append({
            'id':id,
            'Date':Date,
            'Prices':Prices
        })
    return response

def new_prod(connection,readingbills):
    cursor=connection.cursor()
    query=("INSERT INTO readingbills" 
           "(Date,Prices)"
           "VALUES(%s ,%s)")
    data=(readingbills['Date'],readingbills['Prices'])
    cursor.execute(query,data)
    connection.commit()

    return cursor.lastrowid


if __name__=='__main__':
    connection=mydb
    print(new_prod(connection,all()
    ))
