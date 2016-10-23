import random
NUM_PEOPLE = 2871
NUM_AGENCIES = 89
NUM_PREFERENCES = 17
PERSON_PROBS = []
AGENCY_PROBS = []
def createMatchDB(personProbs, agencyProbs):
    personFile = open('personProbs.csv', 'w')
    agencyFile = open('agencyProbs.csv', 'w')
    for i in range(NUM_PEOPLE):
        if random.random() < personProbs[0]:
            personFile.write('1')
        else:
            personFile.write('0')
        for j in range(1,NUM_PREFERENCES):
            if random.random() < personProbs[j]:
                personFile.write(',1')
            else:
                personFile.write(',0')
        personFile.write('\n')
    personFile.close()
    for i in range(NUM_AGENCIES):
        if random.random() < agencyProbs[0]:
            agencyFile.write('1')
        else:
            agencyFile.write('0')
        for j in range(1,NUM_PREFERENCES):
            if random.random() < agencyProbs[j]:
                agencyFile.write(',1')
            else:
                agencyFile.write(',0')
        agencyFile.write('\n')
    agencyFile.close()
    
