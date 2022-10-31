'''
Various experiments on drawings data
'''


# TODO run 4-pick over all data (all possible 4 picks = 80 c 4)

import json

class KenoAnalysis:
    drawings_data_file = 'data/drawings.json' # Drawings history between games 2098753 and 2163865

    def load_drawings(self):
        """
        Initialize drawings record
        Drawings data should be in format {"gamenum": [num,num,...num]}
        """
        print('Loading 6 month drawings history...')
        f = open(self.drawings_data_file, 'r')
        self.data = json.loads(f.read())
        self.data = {int(k):v for k,v in self.data.items()}
        self.num_games = len(self.data)
        self.first_game_index = min(self.data.keys())
        self.last_game_index = max(self.data.keys())
        print('Loaded.')

    def print_all(self, limit):
        """
        Print dataset up to limit
        :param int limit: number of items to print
        """
        i = 0
        for key,value in self.data.items():
            print(key,value);
            i += 1
            if (i > limit):
                break

    def get_counts(self):
        """
        Return dict of frequencies of drawn numbers 1-80 in dataset
        """
        counts = {k: 0 for k in range(1,81)}
        for game,draws in self.data.items():
            for draw in draws:
                counts[int(draw)] += 1
        return counts

    def old_stuff(self):
        counts = self.get_counts()
        # experiment 1: % chance of 1-80 in next draw given n was in a previous draw
        # use n=1 to start
        # if n=1 present, check next game, increment odds
        count_next_draw = {k: 0 for k in range(1,81)}
        pct_next_draw = {}
        print(type(self.first_game_index))
        # creates mapping from number and percent each number will be drawn the next game
        for n in range(1,81):
            count_next_draw[n] = {}
            for i in range(1,81):
                count_next_draw[n][i] = 0
            for i in range(self.first_game_index, self.last_game_index):
                # if n=1 present, check next game, increment odds
                if (str(n) in self.data[i]):
                    for num in self.data[i+1]:
                        count_next_draw[n][int(num)] += 1

        with open('exp1.json', 'w') as f:
            json.dump(count_next_draw, f)

        '''
        for k,v in count_next_draw.items():
            n_draw_count =
            pct_next_draw[k] = round(float(v) / 16223, 5)
        '''

        # find max and min + pct for each for all keys of count_nexT_draw

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



keno = KenoAnalysis()
keno.load_drawings()
keno.old_stuff()
