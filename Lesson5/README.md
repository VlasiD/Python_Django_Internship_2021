The program creates the database table for a dataset with CityId cities in different countries of the world.\
Dataset was received from txt file -  https://worldweather.wmo.int/en/json/full_city_list.txt\
txt file.\

The program has:
1. `add_to_db()` method - adds received data to the database.\
Database after inserting values:\
![image](https://user-images.githubusercontent.com/53980298/147470124-0a9e0399-c4c7-45b4-bd6f-2e1cec26509a.png)

2. `select_from_db()` method - retrieves entries from the database.\
For example, let's get list of ukrainian cities from the database:\
`cursor.execute("SELECT city FROM city WHERE country='Ukraine'")` \
`cursor.fetchall()`\
Output:\
`Received data on request:  [('Dnipro',), ('Donetsk',), ('Kharkiv',), ('Kherson',), ('Kyiv',), ('Luhansk',), ('Lviv',),
 ('Odesa',), ('Simferopol',), ('Uzhorod',), ('Vinnitsa',)]`

3. `delete_from_db()` method - deletes entries from the database.\
For example, let's delete all russian cities from the database:\
`cursor.execute("DELETE FROM city WHERE Country='Russian Federation'")`\

4. `update_data()` method - updates data in the database.\
For example, let's set new value for cityID:\
`cursor.execute("UPDATE city set cityID=5000 WHERE id=50")`\