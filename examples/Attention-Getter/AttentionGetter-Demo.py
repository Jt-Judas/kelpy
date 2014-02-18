# -*- coding: utf-8 -*-

"""

	A simple example. One car drives in (irrelevant).
	The task ends when the user clicks the car.
"""

import os, sys
import pygame
from random import randint, choice, sample, shuffle
from time import time

from kelpy.CommandableImageSprite import *
from kelpy.Miscellaneous import *
from kelpy.DisplayQueue import *
from kelpy.OrderedUpdates import *
from kelpy.EventHandler import *
from kelpy.AttentionGetter import *

IMAGE_SCALE = 0.25

MAX_DISPLAY_TIME = 5.0

##############################################
## Set up pygame

screen = initialize_kelpy( dimensions=(800,600) )
spot = Spots(screen)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Run a single trial
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~	

def present_trial(imagepath):
	"""
	This is the main function used to run this demo. It is fed an imagepath and uses this to create a CommandableImageSprite offscreen. This Sprite is later moved onto the screen, where it hangs out until it is clicked.

	"""
	
	
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# Set up the updates, etc. 
	
	images = [ kstimulus('common_objects/fries.png'), kstimulus('common_objects/umbrella.png'), kstimulus('common_objects/lightbulb.png'), kstimulus('common_objects/bicycle.png') ]
	
	# A queue of animation operations
	Q = DisplayQueue()
	
	# Draw a single animation in if you want!
	
	# What order do we draw sprites and things in?
	dos = OrderedUpdates() # Draw and update in this order
	
	start_time = time()
	
	## The standard event loop in kelpy -- this loops infinitely to process interactions
	## and throws events depending on what the user does
	for event in kelpy_standard_event_loop(screen, Q, dos, throw_null_events=True):
		
		gif_attention_getter(screen, spot.center, images)
		
		if( time() - start_time > MAX_DISPLAY_TIME): 
			break
		
		# If the event is a click:
		
	
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Main experiment
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~	

# Set up images:
target_images = [kstimulus("feature_cars/car1_blue_stars.png"),kstimulus("feature_cars/car1_red_circles.png") , kstimulus("feature_cars/car1_red_stars.png"), kstimulus("feature_cars/car2_blue_circles.png")]

# present a number of blocks
for i in range(10):
	
	targetidx = randint(0,len(target_images)-1)
	
	present_trial(target_images[targetidx])
	
	print i, targetidx, filename(target_images[targetidx])
