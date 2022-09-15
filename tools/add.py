import os, time

def get(db, cursor):
    dbConnect = db
    db = cursor
    os.system('cls')

    chooseFromADMC = ['coding', 'maths', 'art', 'poetry', 'music']
    chooseFromSPRT = ['football', 'race', 'basketball', 'discus', 'javelin']


    print('Score System Manager\n\n')
    tname = input('Enter Team Name: ')

    tmembers = '| '
    playerCount = 0
    teamType = 'solo'
    print('\n\n You can add a team (5 PLAYERS) or a person for Solo Team (MAX 1 PLAYER).\n\n-> Type SUBMIT to stop adding members.\n-> You can only SUBMIT with either 1 player or 5 players\n-> Auto Submit is enabled for 5 players.')
    while True:
        if playerCount == 5:
            break
        tMembersAppend = input('Enter Player(s): ')
        if tMembersAppend == '':
            pass
            print('No empty name allowed!')
        elif tMembersAppend == 'SUBMIT':
            if playerCount == 1 or playerCount == 5:
                if playerCount == 5:
                    teamType = 'Team'
                break
            else:
                print('You can not submit yet!')
                pass
        else:
            tmembers = tmembers + tMembersAppend + ' | '
            playerCount += 1
            pass
    
    os.system('cls')
    
    ADMCevent = 0
    SPRTevent = 0
    eventsChoosen = []
    print('You have to select 5 Events for this team. Choose atleast 1 from each category\n\n (A) Art, Coding, Maths, Music, Poetry\n (B) Basketball, Discus, Football, Javelin, Race')
    while True:
        if (ADMCevent + SPRTevent) == 5:
            if ADMCevent == 0 or SPRTevent == 0:
                print('You must choose atleast 1 from each section!')
                time.sleep(2)
                ADMCevent = 0
                SPRTevent = 0
                eventsChoosen = []
                os.system('cls')
                print('You have to select 5 Events for this team. Choose atleast 1 from each category\n\n (A) Art, Coding, Maths, Music, Poetry\n (B) Basketball, Discus, Football, Javelin, Race')
            else:
                break
        tEventsAppend = input('Enter Event: ').lower()
        if tEventsAppend not in chooseFromADMC and tEventsAppend not in chooseFromSPRT:
            print('Invalid Event')
            pass
        elif tEventsAppend in eventsChoosen:
            print('You can not choose the same event. EC: EVENT-ALREADY-EXISTS')
        else:
            eventsChoosen.append(tEventsAppend)
            if tEventsAppend in chooseFromADMC:
                ADMCevent += 1
            else:
                SPRTevent += 1

    os.system('cls')

    eventScore = []
    chooseFromPlace = ['#1', '#2', '#3', '#4']

    scoreDict = {
        '#1': 4,
        '#2': 3,
        '#3': 2,
        '#4': 1
    }

    eventIndex = 0
    print('Now enter what place the team came in for each event.\n-> Choose from #1 or #2 or #3 or #4')

    while True:
        if eventIndex == 5: #Goes up till 5 events
            break
        event = eventsChoosen[eventIndex]
        placement = input(f'Enter placement for {event}: ')
        if placement not in chooseFromPlace:
            print('Invalid Placement Code.')
        else:
            if event in chooseFromADMC:
                scoreAdd = scoreDict[placement]
                scoreAdd -= 1
                eventScore.append(scoreAdd)
                eventIndex += 1
            else:
                scoreAdd = scoreDict[placement]
                eventScore.append(scoreAdd)
                eventIndex += 1

    confirmAppend = False

    while True:
        os.system('cls')
        print('Review Team Data---------')
        print(f'''
    Team Name: {tname}
    Members:   {tmembers}
    ---------------------
    {eventsChoosen[0]} | Score: {eventScore[0]}
    {eventsChoosen[1]} | Score: {eventScore[1]}
    {eventsChoosen[2]} | Score: {eventScore[2]}
    {eventsChoosen[3]} | Score: {eventScore[3]}
    {eventsChoosen[4]} | Score: {eventScore[4]}
    ====================

    (?) To confirm data entry, type YES.
    (!) To cancel data entry, type NO.

    ''')
        choice = input('Are the fields above correct?  ').upper()
        if choice == 'YES':
            confirmAppend = True
            break
        elif choice == 'NO':
            break
        else:
            pass

    if confirmAppend == True:
        db.execute(f'''
        INSERT INTO Players (name, type, team, event1, score1, event2, score2, event3, score3, event4, score4, event5, score5)
        VALUES ('{tname}', '{teamType}', '{tmembers}', '{eventsChoosen[0]}', {eventScore[0]}, '{eventsChoosen[1]}', {eventScore[1]}, '{eventsChoosen[2]}', {eventScore[2]}, '{eventsChoosen[3]}', {eventScore[3]}, '{eventsChoosen[4]}', {eventScore[4]});
        ''')

        dbConnect.commit()
    else:
        pass