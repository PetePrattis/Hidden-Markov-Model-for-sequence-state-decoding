# -*- coding: utf-8 -*-

states = ('a','b')


emission_probability = {
	'a': {'A':0.4, 'G':0.4, 'T':0.1, 'C':0.1},
	'b': {'T':0.3, 'C':0.3, 'A':0.2, 'G':0.2},
}

'''
The sequence of observations. That is, a sequence of one feature vector
produced for each input image of a character.
'''
observations = ('G', 'G', 'C', 'T')


start_probability = { 'a': 0.5,'b': 0.5 }


transition_probability = {
    'a': {'a':0.9, 'b':0.1},
	'b': {'a':0.1, 'b':0.9}
    
}

def viterbi(observations, states, start_probability, transition_probability, emission_probability):
    # The trellis consists of nodes for each possible state at each step in the hidden sequence.
    # Each node has a probability.
    # The edges connecting the nodes are transitions between states.
    trellis = [{}]
    # The current path through the trellis.
    path = {}
    maxx =0
    maxx_state = 'a'
    # Add the probabilities of beginning the sequence with each possible state
    for state in states:
        trellis[0][state] = start_probability[state] * emission_probability[state][observations[0]]
        path[state] = [state]
        if trellis[0][state] > maxx:
            maxx = trellis[0][state]#0.2 a, 0.1 b
            maxx_state = state

    # Add probabilities for each subsequent state transitioning to each state.
    for observations_index in range(1,len(observations)):
        # Add a new path for the added step in the sequence.
        trellis.append({})
        new_path = {}
        # For each possible state,
        for state in states:
            # Find the most probable state of:
            # The previous most probable state's probability *
            # the probability of the previous most probable state transitioning to the predicted state *
            # The probability that the current observation corresponds to the predicted state
            
                
          
            (probability, possible_state) = max(
            [(trellis[observations_index-1][maxx_state] * transition_probability[maxx_state][state] 
            * emission_probability[state][observations[observations_index]],state)])

            print (probability,possible_state)
            # Add the probability of the state occuring at this step of the sequence to the trellis.
            trellis[observations_index][state] = probability
            
            # Add the state to the current path
            new_path[state] = path[possible_state] + [state]

        path = new_path

    # Make a list of the paths that traverse the entire observation sequence and their probabilities,
    # and select the most probable.
    (probability, state) = max([(trellis[len(observations) - 1][state], state) for state in states])
    # The most probable path, and its probability.    
    return (probability, path[state])

print viterbi(observations, states, start_probability, transition_probability, emission_probability)
