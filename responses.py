import random

isTrivia = False

def scav_hunt():
    scavNum = random.randint(1, 3)
    if scavNum == 1:
        scavItem = 'Pen'
    if scavNum == 2:
        scavItem = 'Charger'
    if scavNum == 3:
        scavItem = 'Pair of earphones'
    return scavItem


def ice_breaker():
    iceNum = random.randint(1, 3)
    if iceNum == 1:
        iceQ = 'Do you have any pets?'
    if iceNum == 2:
        iceQ = "What's an embarrasing moment you had?"
    if iceNum == 3:
        iceQ = "What's the worst movie you've ever watched?"
    return iceQ

def triv_q():
    trivNum = random.randint(1,1)
    if trivNum == 1:
        trivQ = 'What is the middle of the egg called?'
        a = 'akkle'
        b = 'yellow'
        c = 'yolk'
        correct = 3
        
    return trivQ,a,b,c,correct



def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == '!!games':
        scavHunt = '!!scav-hunt for a quick Scavenger Hunt :3'
        iceQ = '!!ice-q for some spicy ice breakers >:}'
        trivia = '!!trivia for some real headscratchers ;-;'
        return scavHunt + '\n' + iceQ + '\n' + trivia

    if p_message == '!!scav-hunt':
        scavItem = scav_hunt()
        return 'Find a ' + scavItem

    if p_message == '!!ice-q':
        iceQ = ice_breaker()
        return iceQ

    if p_message == '!!triva':
        trivQ,a,b,c,correct = triv_q()
        isTrivia == True
        return trivQ + a+b+c

    if isTrivia == True:
        if p_message == correct:
            isTrivia = False
            return 'Correct!!'
        if p_message != correct:
            isTrivia = False
            return 'Incorrect!'