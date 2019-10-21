# ----------
# Background
# 
# A robotics company named Trax has created a line of small self-driving robots 
# designed to autonomously traverse desert environments in search of undiscovered
# water deposits.
#
# A Traxbot looks like a small tank. Each one is about half a meter long and drives
# on two continuous metal tracks. In order to maneuver itself, a Traxbot can do one
# of two things: it can drive in a straight line or it can turn. So to make a 
# right turn, A Traxbot will drive forward, stop, turn 90 degrees, then continue
# driving straight.
#
# This series of questions involves the recovery of a rogue Traxbot. This bot has 
# gotten lost somewhere in the desert and is now stuck driving in an almost-circle: it has
# been repeatedly driving forward by some step size, stopping, turning a certain 
# amount, and repeating this process... Luckily, the Traxbot is still sending all
# of its sensor data back to headquarters.
#
# In this project, we will start with a simple version of this problem and 
# gradually add complexity. By the end, you will have a fully articulated
# plan for recovering the lost Traxbot.
# 
# ----------
# Part One
#
# Let's start by thinking about circular motion (well, really it's polygon motion
# that is close to circular motion). Assume that Traxbot lives on 
# an (x, y) coordinate plane and (for now) is sending you PERFECTLY ACCURATE sensor 
# measurements. 
#
# With a few measurements you should be able to figure out the step size and the 
# turning angle that Traxbot is moving with.
# With these two pieces of information, you should be able to 
# write a function that can predict Traxbot's next location.
#
# You can use the robot class that is already written to make your life easier. 
# You should re-familiarize yourself with this class, since some of the details
# have changed. 
#
# ----------
# YOUR JOB
#
# Complete the estimate_next_pos function. You will probably want to use
# the OTHER variable to keep track of information about the runaway robot.
#
# ----------
# GRADING
# 
# We will make repeated calls to your estimate_next_pos function. After
# each call, we will compare your estimated position to the robot's true
# position. As soon as you are within 0.01 stepsizes of the true position,
# you will be marked correct and we will tell you how many steps it took
# before your function successfully located the target bot.

# These import steps give you access to libraries which you may (or may
# not) want to use.
from robot import *
from math import *
from matrix import *
import random
import numpy as np

# This is the function you have to write. The argument 'measurement' is a 
# single (x, y) point. This function will have to be called multiple
# times before you have enough information to accurately predict the
# next position. The OTHER variable that your function returns will be 
# passed back to your function the next time it is called. You can use
# this to keep track of important information over time.
def measurement_prob(distance, var = 30):
    error = (exp(- (distance ** 2) / (var) / 2.0) /  
              sqrt(2.0 * pi * (var)))
    return error

def estimate_next_pos(measurement, OTHER = None):
    
    N=5000
    OTHER_was_none = False
    if OTHER is None:
        OTHER_was_none = True
        OTHER = []
        for i in range(N):
            r = robot(random.gauss(2,10), random.gauss(2,10), -3+ random.random()*7, -3+random.random()*7, random.random()*10)
            r.set_noise(6, 6, 0)
            # print(r.x, r.y, r.turning, r.heading, r.distance, r.turning_noise)
            OTHER.append(r)

    print('states: ', OTHER)
    

    # measurement update
    w = []

    for i in range(N):
        w.append(measurement_prob(distance_between(measurement, (OTHER[i].x, OTHER[i].y))))
        
    print('weights: ', w)

    # resampling
    total_w = 0
    for i in range(len(w)):
        total_w += w[i]
    print('total_w: ', total_w)
    normalized_w =[]
    for i in range(len(w)):
        normalized_w.append(w[i]/total_w)
    print('normalized weight: ', normalized_w)
    p3 = np.random.choice(list(range(len(normalized_w,))), N,p=normalized_w,replace=True)

    print('before move: ', p3)

    # motion update (prediction)
    p2 = []
    for i in range(N):
        print('literally before move: ', OTHER[p3[i]].x, OTHER[p3[i]].y, OTHER[p3[i]].turning, OTHER[p3[i]].heading, OTHER[p3[i]].distance, OTHER[p3[i]].turning_noise)
        print('\n')
        # OTHER[p3[i]].move_in_circle()
        r = robot(OTHER[p3[i]].x, OTHER[p3[i]].y, OTHER[p3[i]].heading, OTHER[p3[i]].turning, random.gauss(OTHER[p3[i]].distance, 4))
        # r.set_noise(.6, .6, 0)
        r.move_in_circle()
        # r.move_in_circle()
        print('\n')
        print('literally after move: ', i, r.x, r.y, r.turning, r.heading, r.distance, r.turning_noise)
        print('\n')
        p2.append(r)
    print('after move: ', p2)
    # OTHER=p2


    return get_position(p2), p2
    
def get_position(p):
    x = 0.0
    y = 0.0
    for i in range(len(p)):
        x += p[i].x
        y += p[i].y
    return (x / len(p), y / len(p))


# A helper function you may find useful.
def distance_between(point1, point2):
    """Computes distance between point1 and point2. Points are (x, y) pairs."""
    x1, y1 = point1
    x2, y2 = point2
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# This is here to give you a sense for how we will be running and grading
# your code. Note that the OTHER variable allows you to store any 
# information that you want. 
def demo_grading(estimate_next_pos_fcn, target_bot, OTHER = None):
    localized = False
    distance_tolerance = 0.01 * target_bot.distance
    ctr = 0
    # if you haven't localized the target bot, make a guess about the next
    # position, then we move the bot and compare your guess to the true
    # next position. When you are close enough, we stop checking.
    while not localized and ctr <= 10: 
        ctr += 1
        measurement = target_bot.sense()
        position_guess, OTHER = estimate_next_pos_fcn(measurement, OTHER)
        target_bot.move_in_circle()
        true_position = (target_bot.x, target_bot.y)
        #print('true position: ', true_position, 'position_guess: ', position_guess)
        error = distance_between(position_guess, true_position)
        print('error distance: ', error)

        if error <= distance_tolerance:
            print "You got it right! It took you ", ctr, " steps to localize."
            localized = True
        if ctr == 10:
            print "Sorry, it took you too many steps to localize the target."
    return localized

# This is a demo for what a strategy could look like. This one isn't very good.
def naive_next_pos(measurement, OTHER = None):
    """This strategy records the first reported position of the target and
    assumes that eventually the target bot will eventually return to that 
    position, so it always guesses that the first position will be the next."""
    if not OTHER: # this is the first measurement
        OTHER = measurement
    xy_estimate = OTHER 
    return xy_estimate, OTHER

# This is how we create a target bot. Check the robot.py file to understand
# How the robot class behaves.
test_target = robot(2.1, 4.3, 0.5, 2*pi / 34.0, 1.5)
test_target.set_noise(0.0, 0.0, 0.0)

demo_grading(estimate_next_pos, test_target)

def demo_grading_vis(estimate_next_pos_fcn, target_bot, OTHER = None):
    localized = False
    distance_tolerance = 0.01 * target_bot.distance
    ctr = 0
    # if you haven't localized the target bot, make a guess about the next
    # position, then we move the bot and compare your guess to the true
    # next position. When you are close enough, we stop checking.
    #For Visualization
    import turtle    #You need to run this locally to use the turtle module
    window = turtle.Screen()
    window.bgcolor('white')
    size_multiplier= 25.0  #change Size of animation
    broken_robot = turtle.Turtle()
    broken_robot.shape('turtle')
    broken_robot.color('green')
    broken_robot.resizemode('user')
    broken_robot.shapesize(0.1, 0.1, 0.1)
    measured_broken_robot = turtle.Turtle()
    measured_broken_robot.shape('circle')
    measured_broken_robot.color('red')
    measured_broken_robot.resizemode('user')
    measured_broken_robot.shapesize(0.1, 0.1, 0.1)
    prediction = turtle.Turtle()
    prediction.shape('arrow')
    prediction.color('blue')
    prediction.resizemode('user')
    prediction.shapesize(0.1, 0.1, 0.1)
    prediction.penup()
    broken_robot.penup()
    measured_broken_robot.penup()
    #End of Visualization
    while not localized and ctr <= 30:
        ctr += 1
        measurement = target_bot.sense()
        position_guess, OTHER = estimate_next_pos_fcn(measurement, OTHER)
        target_bot.move_in_circle()
        true_position = (target_bot.x, target_bot.y)
        error = distance_between(position_guess, true_position)
        if error <= distance_tolerance:
            print "You got it right! It took you ", ctr, " steps to localize."
            localized = True
        if ctr == 10:
            print "Sorry, it took you too many steps to localize the target."
        #More Visualization
        measured_broken_robot.setheading(target_bot.heading*180/pi)
        measured_broken_robot.goto(measurement[0]*size_multiplier, measurement[1]*size_multiplier-200)
        measured_broken_robot.stamp()
        broken_robot.setheading(target_bot.heading*180/pi)
        broken_robot.goto(target_bot.x*size_multiplier, target_bot.y*size_multiplier-200)
        broken_robot.stamp()
        prediction.setheading(target_bot.heading*180/pi)
        prediction.goto(position_guess[0]*size_multiplier, position_guess[1]*size_multiplier-200)
        prediction.stamp()
        #End of Visualization
    return localized
    
demo_grading_vis(estimate_next_pos, test_target)