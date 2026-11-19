import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="custodio",
    password="1997",
    database="tasks"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE tasks")
"""mycursor.execute("SHOW DATABASES")

for cursor in mycursor:
    print(cursor)"""

#mycursor.execute("CREATE TABLE todo_list (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL)")



def addtasks():
    added_taks = input("Enter a task for todo list!\n")
    sql = "INSERT INTO todo_list (name) VALUES (%s)"
    value = added_taks
    mycursor.execute(sql, (value,))
    mydb.commit()



def showTasks():
    mycursor.execute("SELECT * FROM todo_list")
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)



def deleteTaks():
    sql = "DELETE FROM todo_list WHERE id = %s"
    id = int(input("Enter a id to todo list!\n"))
    mycursor.execute(sql, (id,))
    mydb.commit()

def updateTaks():
    id = int(input("Enter a id item you like update!"))
    update_name = input("Update item in todo list!\n")
    sql = "UPDATE todo_list SET name = %s WHERE id = %s "
    val = (update_name, id)
    mycursor.execute(sql, val)
    mydb.commit()



while True:
    print("1.Add tasks in todo list!") #ok
    print("2.Show tasks in todo list!")
    print("3.Delete item in todo list!")
    print("4.Update item in todo list!")
    print("0.Exit the todo list!")
    choice = input("Choose 0 a 4!\n")

    if choice == "1":
        addtasks()

    if choice == "2":
        showTasks()

    if choice == "3":
        deleteTaks()

    if choice == "4":
        updateTaks()

    if choice == "0":
        print("Bye, exit the programg!")
        break