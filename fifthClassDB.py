import pymysql

schema_name = "freedb_7687hg"

# Establishing a connection to DB
conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_geritest', passwd='74tk5Wn@4hXM!rz', db=schema_name)
conn.autocommit(True)

# Getting a cursor from Database
cursor = conn.cursor()

# Inserting data into table
# statementToExecute = "CREATE TABLE `"+schema_name+"`.`users_271`(`id` INT NOT NULL,`name` VARCHAR(45) NOT NULL, PRIMARY KEY (`id`));"
# cursor.execute(statementToExecute)

cursor.close()
conn.close()

#################

# INSERT DATA TO DB

schema_name = "freedb_7687hg"

# Establishing a connection to DB
conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_geritest', passwd='74tk5Wn@4hXM!rz', db=schema_name)
conn.autocommit(True)

# Getting a cursor from Database
cursor = conn.cursor()

# Inserting data into table
cursor.execute("INSERT into SCHEMA_NAME.users_271 (name, id) VALUES ('rotem', 24)")

cursor.close()
conn.close()


########################
# GET DATA FRON DB

schema_name = "freedb_7687hg"

# Establishing a connection to DB
conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_geritest', passwd='74tk5Wn@4hXM!rz', db=schema_name)

# Getting a cursor from Database
cursor = conn.cursor()

# Getting all data from table “users”
cursor.execute("SELECT * FROM SCHEMA_NAME.users_271;")

# Iterating table and printing all users
for row in cursor:
    print(row)

cursor.close()
conn.close()

######################