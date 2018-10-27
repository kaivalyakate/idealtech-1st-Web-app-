import random
def _generate_maid_id():
    maid_id = 'T120'
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    maid_id_length = 3
    for y in range(maid_id_length):
        maid_id += characters[random.randint(0, len(characters)-1)]
    return maid_id
