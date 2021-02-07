#Programmed by Alvito DiStefano
# Music by Gabriel Pinciotti
# Visuals by Justvin Ames and Bill Engle

# Import necessary libraries, functions etc.
import pygame, os, sys, random, numpy as np
from PIL import Image
from minigame_classes import image_id, button_masher, sorting_game
from sprite_sheet import*

# Initiate player class used to keep track of points
class Gamestats():
	def __init__(self):
		self.points_01 = 0
		self.points_02 = 0
		self.points_03 = 0
		self.running = True

# Define main game function
def rungame():
	# Title screen and explanation
	pygame.init()
	pygame.mouse.set_visible(False)
	pygame.display.set_caption("Valen-Time Trials")
	pygame.mixer.init()
	pygame.mixer.music.load('Val Menu cut.ogg')
	pygame.mixer.music.play(loops=-1)
	clock = pygame.time.Clock()
	screen_size = (1500, 750)
	backscreen = pygame.display.set_mode(screen_size)
	backscreen.fill((0,0,0))
	gamestats = Gamestats()
	end_intro = False
	huh = Spritesheet('huh.png',7,8,5000,5000,1,51)
	main_title = Spritesheet('main_title.png',2,4,2*1500,4*750,1,8)
	timer = 0

	while end_intro == False:
		clock.tick(30)
		for event in pygame.event.get():
		
			if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
				gamestats.running = False
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
				end_intro = True
		
		backscreen.fill((0,0,0))

		# Display team title animation
		if timer < 140:
			huh.draw(backscreen,370,0,timer,3)
		else:
			main_title.draw(backscreen,0,0,timer,3)

		pygame.display.update()
		timer += 1

	# Run the three minigames by calling their functions
	if gamestats.running == True:
		image_id(gamestats)
	if gamestats.running == True:
		button_masher(gamestats)
	if gamestats.running == True:
		sorting_game(gamestats)

	# End game screen
	pygame.init()
	pygame.mouse.set_visible(False)
	pygame.display.set_caption("Valen-Time Trials")
	
	score_sum = pygame.mixer.Sound("score_sum.wav")
	harp = pygame.mixer.Sound("harp.wav")

	clock = pygame.time.Clock()
	screen_size = (1500, 750)
	backscreen = pygame.display.set_mode(screen_size)
	backscreen.fill((76,0,153))
	end_outro = False

	timer = 0
	font = pygame.font.SysFont('comicsans',30)
	score_01 = 0
	score_02 = 0
	score_03 = 0
	total_score = gamestats.points_01 + gamestats.points_02 + gamestats.points_03

	count_speed = 4

	# Tally up points by game and overall score
	while end_outro == False:
		if timer == 30:
			score_sum.play()
		clock.tick(30)
		for event in pygame.event.get():
		
			if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
				gamestats.running = False
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
				end_outro = True

		title = font.render("Final Score" ,1, (255,255,255))
		score_01_text = font.render("Romantic Imagery Score: " + str(score_01) ,1, (255,255,255))
		score_02_text = font.render("Flower Run Score: " + str(score_02) ,1, (255,255,255))
		score_03_text = font.render("Delivery Frenzy Score: " + str(score_03) ,1, (255,255,255))
		total_score_text = font.render("Total Score: " + str(total_score) ,1, (255,255,255))

		backscreen.fill((76,0,153))

		if timer >= 30:
			backscreen.blit(score_01_text,(550,200))
			if score_01 + count_speed < gamestats.points_01:
				score_01 += count_speed
			else:
				score_01 = gamestats.points_01

		if timer >= 50:
			backscreen.blit(score_02_text,(550,250))
			if score_02 + count_speed < gamestats.points_02:
				score_02 += count_speed
			else:
				score_02 = gamestats.points_02

		if timer >= 70:
			backscreen.blit(score_03_text,(550,300))

			if score_03 + count_speed < gamestats.points_03:
				score_03 += count_speed
			else:
				score_03 = gamestats.points_03

		if timer >= 145:
			backscreen.blit(total_score_text, (550,400))

		if timer == 180: #and total_score > 400:
			harp.play()

		pygame.display.update()
		timer += 1

rungame()
