import eel
import sqlite3
from win32api import GetSystemMetrics
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

# Set web files folder and optionally specify which file types to check for eel.expose()
#   *Default allowed_extensions are: ['.js', '.html', '.txt', '.htm', '.xhtml']
eel.init('templates', allowed_extensions=['.js', '.html', '.txt'])


# Initialisation
@eel.expose
def initDB_py():
    db = sqlite3.connect("weaponDB.db")
    
    data = []
    cursor = db.execute("SELECT weaponColl, weaponType, weaponPrice FROM mainData ORDER BY weaponPrice ASC")

    for item in cursor:
        data.append(item)
    
    return data

# Set/Get points
@eel.expose
def process_py(s):
    if s.isdigit():
        with open("vp.txt","w") as file:
            file.write(s)
        return "yes"
    return "no"

@eel.expose
def getPoints_py():
    with open("vp.txt") as file:
        a = file.readline().strip()
    return a


# Sorting by Weapon Types
@eel.expose
def sortSMG_py():
    db = sqlite3.connect("weaponDB.db")
    
    data = []
    cursor = db.execute("SELECT weaponColl, weaponType, weaponPrice FROM mainData WHERE weaponType = 'Stinger' OR weaponType = 'Spectre' ORDER BY weaponPrice ASC")

    for item in cursor:
        data.append(item)

    return data

@eel.expose
def sortRifle_py():
    db = sqlite3.connect("weaponDB.db")
    
    data = []
    cursor = db.execute("SELECT weaponColl, weaponType, weaponPrice FROM mainData WHERE weaponType = 'Bulldog' OR weaponType = 'Guardian' OR weaponType = 'Phantom' OR weaponType = 'Vandal' ORDER BY weaponPrice ASC")

    for item in cursor:
        data.append(item)

    return data

@eel.expose
def sortShot_py():
    db = sqlite3.connect("weaponDB.db")
    
    data = []
    cursor = db.execute("SELECT weaponColl, weaponType, weaponPrice FROM mainData WHERE weaponType = 'Bucky' OR weaponType = 'Judge' ORDER BY weaponPrice ASC")

    for item in cursor:
        data.append(item)

    return data

@eel.expose
def sortSniper_py():
    db = sqlite3.connect("weaponDB.db")
    
    data = []
    cursor = db.execute("SELECT weaponColl, weaponType, weaponPrice FROM mainData WHERE weaponType = 'Marshal' OR weaponType = 'Operator' ORDER BY weaponPrice ASC")

    for item in cursor:
        data.append(item)

    return data

@eel.expose
def sortMel_py():
    db = sqlite3.connect("weaponDB.db")
    
    data = []
    cursor = db.execute("SELECT weaponColl, weaponType, weaponPrice FROM mainData WHERE weaponType = 'Melee' ORDER BY weaponPrice ASC")

    for item in cursor:
        data.append(item)

    return data

@eel.expose
def sortSidearms_py():
    db = sqlite3.connect("weaponDB.db")
    
    data = []
    cursor = db.execute("SELECT weaponColl, weaponType, weaponPrice FROM mainData WHERE weaponType = 'Classic' OR weaponType = 'Shorty' OR weaponType = 'Frenzy' OR weaponType = 'Ghost' OR weaponType = 'Sherrif' ORDER BY weaponPrice ASC")

    for item in cursor:
        data.append(item)

    return data

@eel.expose
def sortHeavy_py():
    db = sqlite3.connect("weaponDB.db")
    
    data = []
    cursor = db.execute("SELECT weaponColl, weaponType, weaponPrice FROM mainData WHERE weaponType = 'Ares' OR weaponType = 'Odin' ORDER BY weaponPrice ASC")

    for item in cursor:
        data.append(item)

    return data


# Searching DB
@eel.expose
def searchDB_py(lst):
    col = "%{}%".format(lst[0])
    type_ = "%{}%".format(lst[1])
    print(col, type_)
    db = sqlite3.connect("weaponDB.db")

    data = []
    cursor = db.execute("SELECT weaponColl, weaponType, weaponPrice FROM mainData WHERE weaponColl LIKE ? AND weaponType LIKE ?",(col,type_))
    
    for item in cursor:
        data.append(item)

    return data


# Sorting by Edition
@eel.expose
def sortEdSelect_py():
    db = sqlite3.connect("weaponDB.db")
    
    data = []
    cursor = db.execute("SELECT weaponColl, weaponType, weaponPrice FROM mainData WHERE weaponEdition = 'Select' ORDER BY weaponPrice ASC")

    for item in cursor:
        data.append(item)

    return data

@eel.expose
def sortEdDuxe_py():
    db = sqlite3.connect("weaponDB.db")
    
    data = []
    cursor = db.execute("SELECT weaponColl, weaponType, weaponPrice FROM mainData WHERE weaponEdition = 'Deluxe' ORDER BY weaponPrice ASC")

    for item in cursor:
        data.append(item)

    return data

@eel.expose
def sortEdPrem_py():
    db = sqlite3.connect("weaponDB.db")
    
    data = []
    cursor = db.execute("SELECT weaponColl, weaponType, weaponPrice FROM mainData WHERE weaponEdition = 'Premium' ORDER BY weaponPrice ASC")

    for item in cursor:
        data.append(item)

    return data

@eel.expose
def sortEdEx_py():
    db = sqlite3.connect("weaponDB.db")
    
    data = []
    cursor = db.execute("SELECT weaponColl, weaponType, weaponPrice FROM mainData WHERE weaponEdition = 'Exclusive' ORDER BY weaponPrice ASC")

    for item in cursor:
        data.append(item)

    return data

@eel.expose
def sortEdUltra_py():
    db = sqlite3.connect("weaponDB.db")
    
    data = []
    cursor = db.execute("SELECT weaponColl, weaponType, weaponPrice FROM mainData WHERE weaponEdition = 'Ultra' ORDER BY weaponPrice ASC")

    for item in cursor:
        data.append(item)

    return data

def runWeb():
    eel.start('index.html', size=(width,height) ,port=8000)

runWeb()
