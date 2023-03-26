import random


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


def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == '!!games':
        scavHunt = '!!scav-hunt for a quick Scavenger Hunt :3'
        iceQ = '!!ice-q for some spicy ice breakers >:}'
        return scavHunt + '\n' + iceQ

    if p_message == '!!scav-hunt':
        scavItem = scav_hunt()
        return 'Find a ' + scavItem

    if p_message == '!!ice-q':
        iceQ = ice_breaker()
        return iceQ

    if p_message == '!!triva':

        return
