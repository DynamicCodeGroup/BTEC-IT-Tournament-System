import os, time

def get(db, cursor):
    dbConnect = db
    db = cursor
    os.system('cls')

    print('''Data Deletion Manager
    
    (?) Enter the ID of the team entry you would like to delete.
        - ID can be found on the view page
        - It looks like ...====ID[13]
        - Only enter the ID number''')

    entryID = int(input('\n\nId:  '))
    result = db.execute(f'SELECT * FROM Players WHERE id = {entryID}').fetchone()

    if result == None:
        print(f'ID "{entryID}" not found!')
        time.sleep(2)
        pass
    else:
        print('Deleting now...')
        db.execute(f'DELETE FROM Players WHERE id = {entryID}')
        time.sleep(0.67)