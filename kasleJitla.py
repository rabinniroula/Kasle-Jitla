import requests
import json
import codecs
import sys
import getopt

states = json.load(codecs.open('states.json', 'r', 'utf-8-sig'))
districts = json.load(codecs.open('districts.json', 'r', 'utf-8-sig'))
constituencies = json.load(codecs.open('constituencies.json', 'r', 'utf-8-sig'))

rootUrl = 'https://result.election.gov.np/JSONFiles/Election2079/HOR/FPTP'

def getResult(d, c):
    res = requests.get(f'{rootUrl}/HOR-{d}-{c}.json')
    for cands in json.loads(res.text):
        print("{0:30} \t {1}".format(cands['CandidateName'], cands['TotalVoteReceived']))
    exit()

if __name__ == '__main__':
    args = sys.argv[1:]
    if (len(args) != 0):
        try:
            opts, args = getopt.getopt(args, 's:d:c:')
        except getopt.GetoptError as err:
            print(err)
        for opt, arg in opts:
            if opt in ['-s']:
                s = arg
            elif opt in ['-d']:
                d = arg
            elif opt in ['-c']:
                c = arg
        getResult(d, c)

    for id, state in enumerate(states):
        print(f'{id+1}. {state}')
    s = int(input('Enter the id of your province.\n>').strip())
    if s < 1 or s > 7:
        print('Invalid Input!')
        exit()
    distsInState = [dist for dist in districts if dist['parentId']==s]
    for dist in distsInState:
        print(f"{dist['id']}. {dist['name']}")
    d = int(input('\n\nEnter the id of your district.\n>').strip())
    con = [con for con in constituencies if con['distId'] == d]
    consNo = con[0]['consts']
    c = int(input(f'\n\nYour district has {consNo} constituencies. Which would you like to select?\n>').strip())

    getResult(d, c)