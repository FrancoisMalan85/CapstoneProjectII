# Capstone Project II: Programmed by Francois Malan
# This is my first game!
# all the images were created by myself

import pygame
import random

# initialise pygame module
pygame.init()

# screen area
scr_width = 1024
scr_height = 768
screen = pygame.display.set_mode((scr_width, scr_height))

# lane locations
lane = [370, 450, 530, 610]

# loading all the images used in the game
background = pygame.image.load("background.png")
image_height = background.get_height()
image_width = background.get_width()
backgroundXposition = 0
backgroundYposition = 0

finish_line = pygame.image.load("finish_line.png")
f_line_height = finish_line.get_height()
f_line_width = finish_line.get_width()
f_lineXpos = 352
f_lineYpos = 0

player = pygame.image.load("player1.bmp")
player_height = player.get_height()
player_width = player.get_width()
playerXpos = 450
playerYpos = 500

blue_car = pygame.image.load("blue_car.bmp")
blue_height = blue_car.get_height()
blue_width = blue_car.get_width()
blue_car_Xpos = lane[1]
blue_car_Ypos = 0

yellow_car = pygame.image.load("yellow_car.bmp")
yellow_height = yellow_car.get_height()
yellow_width = yellow_car.get_width()
yellow_car_Xpos = lane[0]
yellow_car_Ypos = -1000


purple_car = pygame.image.load("purple_car.bmp")
purple_height = purple_car.get_height()
purple_width = purple_car.get_width()
purple_car_Xpos = lane[3]
purple_car_Ypos = -1200

white_car = pygame.image.load("white_car.bmp")
white_height = white_car.get_height()
white_width = white_car.get_width()
white_car_Xpos = lane[2]
white_car_Ypos = -3200

grey_car = pygame.image.load("grey_car.bmp")
grey_height = grey_car.get_height()
grey_width = grey_car.get_width()
grey_car_Xpos = lane[3]
grey_car_Ypos = -5200

plus5 = pygame.image.load("5.bmp")
plus5_height = plus5.get_height()
plus5_width = plus5.get_width()
plus5_Xpos = lane[0]
plus5_Ypos = -1500

plus10 = pygame.image.load("10.bmp")
plus10_height = plus10.get_height()
plus10_width = plus10.get_width()
plus10_Xpos = lane[1]
plus10_Ypos = -2500

plus15 = pygame.image.load("15.bmp")
plus15_height = plus15.get_height()
plus15_width = plus15.get_width()
plus15_Xpos = lane[2]
plus15_Ypos = -4000

plus20 = pygame.image.load("20.bmp")
plus20_height = plus20.get_height()
plus20_width = plus20.get_width()
plus20_Xpos = lane[3]
plus20_Ypos = -6500

go = pygame.image.load("go.png")
go_height = go.get_height()
go_width = go.get_width()
go_Xpos = 455
go_Ypos = 384

you_win = pygame.image.load("you_win.png")
win_height = you_win.get_height()
win_width = you_win.get_width()
win_Xpos = 405
win_Ypos = 200

# all the variables used in the game
length_of_road = 20  # half the number of times the background goes by
distance = 0
speed = 1  # starting speed (rolling start)
count = 0
count2 = 0
score = 0
# boolean variables
accelerate = False
brake = False
turn_left = False
turn_right = False
plus5_collide = False
plus10_collide = False
plus15_collide = False
plus20_collide = False

# game loop
# screen fill not used because screen is filled with background image
while 1:
    # clock is used to keep the refresh rate smooth
    clock = pygame.time.Clock()
    clock.tick(60)
    # using a time delay slows the game down to decrease the effectiveness of the variables
    pygame.time.wait(10)

    distance += speed  # the 'speed' is added to 'distance' variable at every loop so to 'move forward'
    # this if statement loops the background image until 'count' = 'length_of_road'
    if count < length_of_road:
        screen.blit(background, (backgroundXposition, backgroundYposition + distance))
        screen.blit(background, (backgroundXposition, (backgroundYposition - scr_height) + distance))

        # this if statement resets the drive variable to cause the loop
        if distance > scr_height:
            distance = distance - scr_height
            count += 1

    # the finish line appears 1 count before the end of the road
    if count == (length_of_road - 1):
        screen.blit(finish_line, (f_lineXpos, f_lineYpos))
        f_lineYpos += speed

    # player 1
    screen.blit(player, (playerXpos, playerYpos))

    # other cars (enemy objects)
    screen.blit(blue_car, (blue_car_Xpos, blue_car_Ypos))
    screen.blit(yellow_car, (yellow_car_Xpos, yellow_car_Ypos))
    screen.blit(purple_car, (purple_car_Xpos, purple_car_Ypos))
    screen.blit(white_car, (white_car_Xpos, white_car_Ypos))
    screen.blit(grey_car, (grey_car_Xpos, grey_car_Ypos))

    # prizes
    screen.blit(plus5, (plus5_Xpos, plus5_Ypos))
    screen.blit(plus10, (plus10_Xpos, plus10_Ypos))
    screen.blit(plus15, (plus15_Xpos, plus15_Ypos))
    screen.blit(plus20, (plus20_Xpos, plus20_Ypos))

    # Go! message
    count2 += 1  # for every loop 1 is added to the variable 'count2' for 'Go!' message
    if count2 <= 20:  # 'Go!' message appears for 20 loops or counts
        screen.blit(go, (go_Xpos, go_Ypos))

    # You win! message
    if playerYpos <= f_lineYpos:  # if player reaches the finish line 'You win!' message will appear
        screen.blit(you_win, (win_Xpos, win_Ypos))

    # to update the screen
    pygame.display.flip()

    # if player quits, the program ends
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    # controls
    # if these buttons are pressed in then their respective variables are set to True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                accelerate = True
            if event.key == pygame.K_DOWN:
                brake = True
            if event.key == pygame.K_LEFT:
                turn_left = True
            if event.key == pygame.K_RIGHT:
                turn_right = True

    # if these buttons are released then their respective variables are set back to False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                accelerate = False
            if event.key == pygame.K_DOWN:
                brake = False
            if event.key == pygame.K_LEFT:
                turn_left = False
            if event.key == pygame.K_RIGHT:
                turn_right = False

    # after the events are checked and values stored, these if statements control how the player moves
    if accelerate:
        if speed < 20:  # this is the speed limit of the player. speed will only increase if it's below this value
            speed += 2
        # this if statement moves the player up the screen while accelerating to add to the effect
        if playerYpos > 400:
            playerYpos -= 2
    else:  # if the up arrow is released (accelerate is False) then the car slows down to a cruising speed
        if speed > 15:  # cruising speed
            speed -= 1
            playerYpos += 2

    if brake:
        if speed > 0:  # car will continue to slow down until it comes to a stop
            speed -= 1
            if playerYpos < 500:
                playerYpos += 2  # this gives the car the effect of deceleration

    if turn_left:
        if playerXpos > 330:  # this value is the side of the road. it keeps the player from driving into the field
            playerXpos -= int(speed/3)  # the faster you go the more sensitive the steering
        else:
            if speed > 1:
                speed -= 2  # for when you drive on the left of the road the car will slow down and fall back
                playerYpos += 3

    if turn_right:
        if playerXpos < 650:  # this value is the side of the road. it keeps the player from driving into the field
            playerXpos += int(speed/3)  # the faster you go the more sensitive the steering
        else:
            if speed > 1:
                speed -= 2  # for when you drive on the right of the road the car will slow down and fall back
                playerYpos += 3

    # Bounding boxes that surround each image on the screen so the images and interact with each other
    player_box = pygame.Rect(player.get_rect())
    player_box.top = playerYpos
    player_box.left = playerXpos

    blue_box = pygame.Rect(blue_car.get_rect())
    blue_box.top = blue_car_Ypos
    blue_box.left = blue_car_Xpos

    yellow_box = pygame.Rect(yellow_car.get_rect())
    yellow_box.top = yellow_car_Ypos
    yellow_box.left = yellow_car_Xpos

    purple_box = pygame.Rect(blue_car.get_rect())
    purple_box.top = purple_car_Ypos
    purple_box.left = purple_car_Xpos

    white_box = pygame.Rect(white_car.get_rect())
    white_box.top = white_car_Ypos
    white_box.left = white_car_Xpos

    grey_box = pygame.Rect(grey_car.get_rect())
    grey_box.top = grey_car_Ypos
    grey_box.left = grey_car_Xpos

    plus5_box = pygame.Rect(plus5.get_rect())
    plus5_box.top = plus5_Ypos
    plus5_box.left = plus5_Xpos

    plus10_box = pygame.Rect(plus10.get_rect())
    plus10_box.top = plus10_Ypos
    plus10_box.left = plus10_Xpos

    plus15_box = pygame.Rect(plus15.get_rect())
    plus15_box.top = plus15_Ypos
    plus15_box.left = plus15_Xpos

    plus20_box = pygame.Rect(plus20.get_rect())
    plus20_box.top = plus20_Ypos
    plus20_box.left = plus20_Xpos

    finish_box = pygame.Rect(finish_line.get_rect())
    finish_box.top = f_lineYpos - player_height
    finish_box.left = f_lineXpos

    # test for a collision with another car
    if player_box.colliderect(blue_box) or player_box.colliderect(purple_box) or player_box.colliderect(white_box) or player_box.colliderect(grey_box) or player_box.colliderect(yellow_box):
        print(f"You crashed! Your score is {score}")  # display the score the player accumulated up until their accident
        pygame.quit()
        exit(0)

    # test for a collision between the bounding boxes of the player and the finish line
    if player_box.colliderect(finish_box):
        print(f"You win! Your score is {score}")  # display the score the player accumulated throughout the game
        pygame.quit()
        exit(0)

    # test for collision between the player and any of the prizes
    # if True then the boolean is set to True the appropriate score will be added to 'score' variable
    if player_box.colliderect(plus5_box):
        plus5_collide = True
        score += 5
    if player_box.colliderect(plus10_box):
        plus10_collide = True
        score += 10
    if player_box.colliderect(plus15_box):
        plus15_collide = True
        score += 15
    if player_box.colliderect(plus20_box):
        plus20_collide = True
        score += 20

    # the prize's reaction when the player collides with the prize. (Thought it would look fun)
    # '+5' and '+10' will fly up and to the left of the screen
    # '+15' and '+20' will fly up and to the right of the screen
    if plus5_collide is True:
        plus5_Xpos -= 35
        plus5_Ypos -= 34
    if plus10_collide is True:
        plus10_Xpos -= 35
        plus10_Ypos -= 38
    if plus15_collide is True:
        plus15_Xpos += 35
        plus15_Ypos -= 38
    if plus20_collide is True:
        plus20_Xpos += 35
        plus20_Ypos -= 34

    # this alters the Y position and lane position of the other cars and prizes once they've disappeared off the screen so they can all reappear again.

    # random variables:
    random_left = random.randint(0, 1)  # randomly chooses the left two lanes
    random_right = random.randint(2, 3)  # randomly chooses the right two lanes
    random_prize = random.randint(0, 3)  # randomly chooses any lane

    if blue_car_Ypos > scr_height:
        blue_car_Ypos = -800
        blue_car_Xpos = lane[random_left]  # randomly selects between the first two indices of the lane list

    if yellow_car_Ypos > scr_height:
        yellow_car_Ypos = -2500
        if random_left == 0:  # if the blue car is in the first lane, then the yellow car should be in the second lane
            yellow_car_Xpos = lane[1]
        else:
            yellow_car_Xpos = lane[0]

    if purple_car_Ypos > scr_height:
        purple_car_Ypos = -2000
        purple_car_Xpos = lane[random_right]  # randomly selects between the third and fourth index of the lane list

    if white_car_Ypos > scr_height + 1200:
        white_car_Ypos = -4000
        if random_right == 2:  # if the purple car is in the third lane, then the white car should be in the fourth lane
            white_car_Xpos = lane[3]
        else:
            white_car_Xpos = lane[2]

    if grey_car_Ypos > scr_height + 700:
        grey_car_Ypos = -3000
        grey_car_Xpos = lane[random_right]  # the grey car will be in the same lane as the purple car

    # these if statements check for three conditions:
    # if the prize has moved off the screen or if the player has missed it
    # and that there's 5 counts left before the end of the road.
    if (plus5_Xpos < 0 or plus5_Ypos > scr_height) and count < (length_of_road - 5):
        plus5_collide = False
        plus5_Xpos = lane[random_prize]
        plus5_Ypos = -1100
    if (plus10_Xpos < 0 or plus10_Ypos > scr_height) and count < (length_of_road - 5):
        plus10_collide = False
        plus10_Xpos = lane[random_prize]
        plus10_Ypos = -1800
    if (plus15_Xpos > scr_width or plus15_Ypos > scr_height) and count < (length_of_road - 5):
        plus15_collide = False
        plus15_Xpos = lane[random_prize]
        plus15_Ypos = -2100
    if (plus20_Xpos > scr_width or plus20_Ypos > scr_height) and count < (length_of_road - 5):
        plus20_collide = False
        plus20_Xpos = lane[random_prize]
        plus20_Ypos = -1500

    # speeds of the other cars
    # 'speed' is added to each of these variables so they appear unaffected by the players speed
    blue_car_Ypos += speed - 5
    yellow_car_Ypos += speed - 4
    purple_car_Ypos += speed + 8
    if white_car_Ypos > purple_car_Ypos - 200:  # this is to regulate the white car's speed
        white_car_Ypos += speed + 8
    elif white_car_Ypos > grey_car_Ypos - 200:
        white_car_Ypos += speed + 9
    else:
        white_car_Ypos += speed + 12
    if grey_car_Ypos > purple_car_Ypos - 200:  # this is to regulate the grey car's speed
        grey_car_Ypos += speed + 8
    else:
        grey_car_Ypos += speed + 9

    # the prize's speed matches the speed of the road (the prize is stationary relative to the road)
    plus5_Ypos += speed
    plus10_Ypos += speed
    plus15_Ypos += speed
    plus20_Ypos += speed
