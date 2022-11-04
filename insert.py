import sqlite3

db = sqlite3.connect("weaponDB.db")

with open("gun data.csv") as file:
    file.readline()
    for line in file:
        Id, Coll, Type, Price = line.strip().split(',')
        Price = int(Price)
        Id = int(Id)
        
        if Price == 875 or Price == 1750:
            Ed = "Select"
        elif Price == 1275 or Price == 2550:
            Ed = "Deluxe"
        elif Price == 1775 or Price == 3550:
            Ed = "Premium"
        elif Price == 2675 or Price == 5350 or Price == 2175 or Price == 4350:
            Ed = "Exclusive"
        else:
            Ed = "Ultra"
            
        db.execute('INSERT INTO mainData VALUES (?,?,?,?,?)',(Id, Coll, Type, Ed, Price))

    db.commit()

db.close()
