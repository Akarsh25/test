# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 20:27:45 2019

@author: akars
"""

import gym

env = gym.make('CartPole-v0')
env.reset()

for _ in range(1000):
    env.render()
    env.step(env.action_space.sample())
    
env.close()