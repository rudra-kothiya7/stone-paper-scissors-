def player(prev_play, opponent_history=[], my_history=[], 
           play_order=[{}], strategy_scores=[0]*4, last_play=[""]):
    
    counter = {'P': 'S', 'R': 'P', 'S': 'R'}
    
    if not prev_play:
        opponent_history.clear()
        my_history.clear()
        play_order[0].clear()
        strategy_scores[:] = [0]*4
        last_play[0] = "R"
        return "R"
    
    opponent_history.append(prev_play)
    my_history.append(last_play[0])
    
    if len(my_history) >= 2:
        prev_my = my_history[-2]
        
        quincy = ["R","R","P","P","S"][len(opponent_history) % 5]
        if prev_play == quincy:
            strategy_scores[0] += 1
        
        if prev_play == counter[prev_my]:
            strategy_scores[1] += 1
        
        recent = my_history[-11:-1]
        most_common = max(set(recent or ['S']), key=(recent or ['S']).count)
        if prev_play == counter[most_common]:
            strategy_scores[2] += 1
        
        last_pair = prev_my + last_play[0]
        play_order[0][last_pair] = play_order[0].get(last_pair, 0) + 1
        
        potential = {prev_my + m: play_order[0].get(prev_my + m, 0) 
                     for m in ['R','P','S']}
        abbey_pred = max(potential, key=potential.get)[-1]
        if prev_play == counter[abbey_pred]:
            strategy_scores[3] += 1
    
    curr = my_history[-1]
    predictions = [
        ["R","R","P","P","S"][(len(opponent_history)+1) % 5],
        counter[curr],
        counter[max(set(my_history[-10:] or ['S']), 
                   key=(my_history[-10:] or ['S']).count)],
        counter[max({curr+m: play_order[0].get(curr+m,0) 
                    for m in ['R','P','S']}, 
                   key=lambda k: play_order[0].get(k,0))[-1]]  # Abbey
    ]
    
    best = strategy_scores.index(max(strategy_scores))
    guess = counter[predictions[best]]
    
    last_play[0] = guess
    return guess