import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
#for entering of scores of players
player1=[]
player2=[]
score=[]
ball_hit=[]
count=0
balls_hit_by_1=[]
ball1=0
ball=0
while True:
    run=int(input('enter the runs made'))
    if run>6:
        print('all are out')
        break
    elif run%2==0 and run>1:
        player1.append(run)
        ball1=ball1+1
        balls_hit_by_1.append(ball1)
    elif run%2!=0 and run==1:
        player2.append(run)
        ball2=0
        ball2=ball2+1
        balls_hit_by_2=[]
        balls_hit_by_2.append(ball2)
    elif run==3 or run==5:
        player2.append(run)
        ball2=0
        ball2=ball2+1
        balls_hit_by_2=[]
        balls_hit_by_2.append(ball2)
    else:
        print('enter the the valid run')
    score.append(run)
    ball=ball+1
    ball_hit.append(ball)
def stat_player1():
    plt.scatter(balls_hit_by_1,player1)
    plt.title('statistics of player1')
    plt.xlabel('no.of balls')
    plt.ylabel('no.of runs')
    plt.show()
def stat_player2():
    plt.scatter(balls_hit_by_2,player2)
    plt.title('statistics of player2')
    plt.xlabel('no.of balls')
    plt.ylabel('no.of runs')
    plt.show()
def stat_overall():
    plt.scatter(ball_hit,score)
    plt.title('Overall statistics of the team')
    plt.xlabel('no.of balls took by the team')
    plt.ylabel('no.of runs scored by the team')
    plt.show()
stat_player1()
stat_player2()
stat_overall()
