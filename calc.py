'''
Various experiments on drawings data
'''

import json

print('Loading 6 month drawings history...')
f = open('data/drawings.json', 'r')
data = json.loads(f.read())

print('Loaded.')

num_games = len(data)
counts = {}
for i in range(1,81):
    counts[i] = 0
for game,draws in data.items():
    for draw in draws:
        counts[int(draw)] += 1

def print_all(data):
    i = 0
    for key,value in data.items():
        print(key,value);
        if (i > 20):
            break

# experiment 1: % chance of 1-80 in next draw given n was in a previous draw
# use n=1 to start
# if n=1 present, check next game, increment odds



def old_stuff():
    first_game_index = 2098753
    last_game_index = 2163853
    count_next_draw = {}
    pct_next_draw = {}

    for i in range(1,81):
        count_next_draw[i] = 0
    # creates mapping from number and percent each number will be drawn the next game
    for n in range(1,81):
        count_next_draw[n] = {}
        for i in range(1,81):
            count_next_draw[n][i] = 0
        for i in range(first_game_index, last_game_index):
            # if n=1 present, check next game, increment odds
            if (str(n) in data[str(i)]):
                for num in data[str(i+1)]:
                    count_next_draw[n][int(num)] += 1

    with open('exp1.json', 'w') as f:
        json.dump(count_next_draw, f)


'''
for k,v in count_next_draw.items():
    n_draw_count =
    pct_next_draw[k] = round(float(v) / 16223, 5)
    '''

# find max and min + pct for each for all keys of count_nexT_draw

def subsequent_draw_freqs():
    print('Loading ohter file...')
    f = open('exp1.json', 'r')
    count_next_draw = json.loads(f.read())

# for k,v in count_next_draw.items(): # k= 1 through 80, v=drawcounts next game
    for i in range(1,81):
        # find max
        print('if ' + str(i) + ' appears in one game, the most and least likely numbers in the next game are:')
        print(max(count_next_draw[str(i)], key=count_next_draw[str(i)].get))
        print(float(max(count_next_draw[str(i)].values())) / counts[int(i)])
        print(min(count_next_draw[str(i)], key=count_next_draw[str(i)].get))
        print(float(min(count_next_draw[str(i)].values())) / counts[int(i)])



#print(count_next_draw)



# experiment 2: repeat results
# find all games that have happened >1 times

drawings_to_game = {}
for k,v in data.items():
    v.sort(key=int)
    drawings_to_game[str(v)] = k

print(len(drawings_to_game.values()))

# construct search tree, or hash map probably not so difficult

'''
for k,v in data.items():
    print("observing game " + str(k))
    if (drawings_to_game[str(v)] != k):
        print(k)
        print(drawings_to_game[str(v)])
        '''
