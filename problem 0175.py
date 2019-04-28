'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

You are given a starting state start, a list of transition probabilities for a Markov chain,
 and a number of steps num_steps. Run the Markov chain starting from start 
 for num_steps and compute the number of times we visited each state.

For example, given the starting state a, number of steps 5000, and the following transition probabilities:

[
  ('a', 'a', 0.9),
  ('a', 'b', 0.075),
  ('a', 'c', 0.025),
  ('b', 'a', 0.15),
  ('b', 'b', 0.8),
  ('b', 'c', 0.05),
  ('c', 'a', 0.25),
  ('c', 'b', 0.25),
  ('c', 'c', 0.5)
]

One instance of running this Markov chain might produce { 'a': 3012, 'b': 1656, 'c': 332 }.
'''
import random

state = [
  ('a', 'a', 0.9),
  ('a', 'b', 0.075),
  ('a', 'c', 0.025),
  ('b', 'a', 0.15),
  ('b', 'b', 0.8),
  ('b', 'c', 0.05),
  ('c', 'a', 0.25),
  ('c', 'b', 0.25),
  ('c', 'c', 0.5)
]


def follow_chain_and_count(state,n,start):
    result=dict()
    for x in state:
        if x[0] not in result:
            result[x[0]]=0
    position=start
    for _ in range(n):
        compteur=0
        a=random.uniform(0,1)
        verif=False
        for x in state:
            
            if x[0]==position:
                compteur+=x[2]
            if a<compteur:
                result[x[1]]+=1
                position=x[1]
                verif=True
                break
        if verif==False:
            print('erreur')
            
    return result