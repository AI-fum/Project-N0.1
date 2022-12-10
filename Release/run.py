from engine import GameManager
from playsound import playsound
import sys



def __main__():
    arg = sys.argv
    search_type = 'a_star'
    if len(arg) > 1:
        if arg[1] in ['ids', 'a_star', 'bfs', 'dfs', 'ucs']:
            search_type = arg[1]
        else:
            print('\n\nInvalid algorithm!')
            return
    game_manager = GameManager()
    # Finding way
    result, depth, cost = game_manager.start_search(search_type)

    # Printing outputs
    directions = {(1, 0): 'Down', (-1, 0): 'Up', (0, 1): 'Right', (0, -1): 'Left'}
    p1 = game_manager.init_state.robot
    for i in range(len(result)):
        p2 = result[i].robot
        print(directions[(p2[0]-p1[0], p2[1]-p1[1])], end='')
        p1 = result[i].robot
    print('\n moves:', depth)
    print('cost:', cost)
    game_manager.display_states(result)
    #playsound('Shamaizadeh-Bishtar-o-Bishtar.mp3')
    


__main__()
