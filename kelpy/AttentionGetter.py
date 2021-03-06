# -*- coding: utf-8 -*-
import types
import random
import GIFImage
import pygame
from pygame.locals import *
from time import time

"""
	This class is used to play a GIF and a sound to use as an 'attention getter' for infant studies.
"""


#def play_reward_image(screen, g, duration=3.0):
#image = GIFImage.GIFImage(g)
def gif_attention_getter(screen, position, images, sounds=None, keypress=None, stop_music=True, background_color=(255,255,255), duration=4.0):
	"""
		Plays a GIF and sound. If lists of these are given, a random one is chosen. 
		This can stop on a specified keypress or after a fixed duration
		If both are specified, we break on either. 
		
		This function requires a pygame screen object, a positon (x,y), and an array of image filepaths to be used as parameters.
		It optionally can be fed an array of sound filepaths (16 bit signed wav), a maximum duration (default is 4 seconds), a keypress to end the sequence, a boolean for whether to stop the music once the sequence ends (or let it continue into the next sequence), and a background color (Default is set to white). 
	"""
	# convert to lists if not
	if not isinstance(images, types.ListType): images = [images]
	if sounds is not None and not isinstance(sounds, types.ListType): sounds = [sounds]
		
	image = GIFImage.GIFImage(random.choice(images))
	
	if sounds is not None:
		pygame.mixer.music.load(random.choice(sounds))
		pygame.mixer.music.play()
	
	# record the time 
	start_time = time()
	
	# now loop until some exit criterion is met
	while True:
		# exit criteria
		if duration is not None and (time() - start_time) > duration: break
		if keypress is not None and pygame.key.get_pressed()[keypress] == 1: break
			
		# display image
		screen.fill(background_color)
		image.render(screen, (position[0] - image.image.size[0]/2, position[1] - image.image.size[1]/2))
		pygame.display.flip()
		
		
		for event in pygame.event.get():
			if event.type == QUIT: quit()
			if event.type == KEYDOWN and event.key == K_ESCAPE: quit()
		
	if stop_music and sounds is not None:
		pygame.mixer.music.stop()
	
	return (time() - start_time) 
	

