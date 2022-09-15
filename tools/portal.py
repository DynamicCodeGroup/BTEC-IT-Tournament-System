import tools.view as view
import tools.add as add
import tools.delete as delete

def tp(db, cursor, key):
	if key == 'V':
		view.get(db, cursor)
	
	if key == 'A':
		add.get(db, cursor)

	if key == 'D':
		delete.get(db, cursor)
	
	if key == 'X':
		exit('[PROG.TERMINATE]  Program requested to terminate all processes.')