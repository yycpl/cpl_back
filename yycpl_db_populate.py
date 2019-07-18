# Database Connection to PostgreSQL Calgary Library Project Database using Psycopg2:

# import psycopg2:
import psycopg2 as pg2

# Create connection with PostgreSQL DB:
conn = pg2.connect(database='Calgary Library Project Database', user='postgres', password='Chachee@21')

# Open cursor to perform Database Operations:
cur = conn.cursor()

# Executes command to populate CPL DB Tables:
cur.execute("INSERT INTO priority (priority_desc)"
            "VALUES('Not urgent and not very important'),"
            "('Urgent to someone but not that important'),"
            "('Not urgent but very important'),"
            "('Urgent and important')")

cur.execute("INSERT INTO impact (impact_desc)"
            "VALUES('Something we need to improve'), "
            "('Something we are doing well and should do more of'), "
            "('Something that can/does put us in a difficult spot'), "
            "('Something that we should consider taking on')")

cur.execute("INSERT INTO category (category_name) "
            "VALUES('Programs'),"
            "('Services'),"
            "('Collections'),"
            "('Bookable Items'),"
            "('Faciliites'),"
            "('Patrons')")

cur.execute("INSERT INTO branch (branch_name)"
            "VALUES('Bowness'),"
            "('Central'),"
            "('Country Hills'),"
            "('Crowfoot'),"
            "('Fish Creek'),"
            "('Forest Lawn'),"
            "('Giuffre Family'),"
            "('Judith Umbach'),"
            "('Louise Riley'),"
            "('Memorial Park'),"
            "('Nicholls Family'),"
            "('Nose Hill'),"
            "('Quarry Park'),"
            "('Rocky Ridge'),"
            "('Saddletowne'),"
            "('Sage Hill'),"
            "('Seton'),"
            "('Shawnessy'),"
            "('Signal Hill'),"
            "('Southwood'),"
            "('Village Square')")

cur.execute("INSERT INTO sub_category (sub_cat_desc)"
            "VALUES('Adults'),"
            "('Careers'),"
            "('Childrens'),"
            "('Communications'),"
            "('Equipment'),"
            "('Families'),"
            "('Furniture'),"
            "('Health & Safety'),"
            "('Indigenous'),"
            "('Instruments'),"
            "('IT'),"
            "('Literacy Collection'),"
            "('Maintenance'),"
            "('Newcomers/ESL'),"
            "('Parents'),"
            "('Pre-Teens'),"
            "('Rooms'),"
            "('Security'),"
            "('Spaces'),"
            "('Special Services'),"
            "('Stacks'),"
            "('Support'),"
            "('Teens'),"
            "('World Languages)')")

# Commit changes to the DB:
conn.commit()

# Close communication with DB:
cur.close()
conn.close()