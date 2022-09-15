import os

def get(db, cursor):
	dbConnect = db
	db = cursor
	os.system('cls')

	db.execute("SELECT * FROM Players")
	data = db.fetchall()
	
	for row in data:
		name, s1, s2, s3, s4, s5 = row[1], row[4], row[5], row[6], row[7], row[8]
		e1, e2, e3, e4, e5 = row[9], row[10], row[11], row[12], row[13]
		player, entryId = row[3], row[0]
		total = s1 + s2 + s3 + s4 + s5
		
		print(f'Team: {name}\nPlayers: {player}\n-------------------\n{e1}: {s1}\n{e2}: {s2}\n{e3}: {s3}\n{e4}: {s4}\n{e5}: {s5}\nTOTAL: {total}\n==============ID[{entryId}]\n')
	input('\n\nEnter to dismiss')