import pygame
import Pipe
import Bird
import random

NO_OF_BIRDS=500
SPACE_BETWEEN_PIPES=220
FRAMES_PER_PIPE=60
TRAINING_FRAMES=200000
TOTAL_FRAMES=0
FRAMECOUNT_FOR_PIPES=0
FPS=60
SCORE=0
Test_mode=False

HARRY_MODE=False

PLAYER_SIZE=(70, 50)
SCREEN_SIZE=(800, 800)
PIPE_SIZE=(100, 700)



# DRAW ALL THE OBJECTS
def draw():
    #DRAW THE BACKGROUND
    WIN.blit(bg, (0, 0))

    #DRAW THE BIRDS ON THE WINDOW IF THE BIRD IS ALIVE
    for bird in birds:

        if bird.alive:
            WIN.blit(player,(bird.x,bird.y))

    #DRAW THE BOTTOM PIPE AND THEN FIND THE POSITION OF TOP PIPE AND DRAW IT
    for i in pipes:

        WIN.blit(PIPE_IMG, (i.x, i.y))

        top_y=(i.y-SPACE_BETWEEN_PIPES)-700

        WIN.blit(ROT_PIPE_IMG, (i.x, top_y))
    #pygame.draw.rect(WIN, (0, 0, 0), [jump_true[1], 600, 10, 10], 2)
    #pygame.draw.rect(WIN, (0, 0, 0), [jump_true[2], 600, 10, 10], 2)
    pygame.display.update()

#RESET THE GAME
def reset():
    global pipes,SCORE, birds, best_bird
    fitness=[]
    sum=1
    SCORE=0

    # CALCULATE THE SUM OF ALL THE SCORES AND THE FITNESS OF EACH BIRD IS THE PERCENTAGE OF THEIR SCORE TO THE TOTAL SUM
    for i in birds:
        sum+=i.score
        if i.score>best_bird.score:
            best_bird=i
    for i in birds:
        i.fitness=i.score/sum
        fitness.append(i.fitness)

    # MAKE A NEW GENERATION OF BIRDS TO GET BETTER OUTPUT

    next_gen_birds=[]

    for i in range(NO_OF_BIRDS):

        #DEPENDING ON THE FITNESS CHOOSE A BIRD
        print (best_bird.score)
        bird = random.choices(birds,fitness,k=1)
        if bird[0].score<best_bird.score:
            bird[0]=best_bird
        # MAKE A NEW BIRD
        new_bird=Bird.bird()


        # TO MAKE A 50 PERCENT CHANCE OF EITHER THE NEW BIRD IS A COPY AND MUTATE OF A PREVIOUS BIRD OR A TOTAL RANDOM BIRD


        new_bird.brain.copy(bird[0].brain)
        new_bird.brain.mutate()

        next_gen_birds.append(new_bird)

    pipes = []
    birds= next_gen_birds

# to count frames and add pipes ever x frames
def add_new_pipe(x):
    if x==FRAMES_PER_PIPE:
        new_pipe = Pipe.pipe()
        pipes.append(new_pipe)
        x=0
    return(x+1)

#CHECK IF THE BIRD IS TOUCHING PIPE AND KILL IT AND RESET IT IF ALL THE BIRDS ARE DEAD
def is_game_over():
    global  total_birds_dead, birds, gen

    #IF THE BIRD TOUCHES THE PIPES BIRD IS DEAD
    for i in pipes:
        for bird in birds:
            # IS PIPE IN THE SAME X VALUES AS THE BIRD??
            #the 100 value came from testing the game and checking when the bird dies
            if (i.x)<=(bird.x + PLAYER_SIZE[0])and  (i.x + 100)>=bird.x:
                topy=(i.y-SPACE_BETWEEN_PIPES)

                # IS THE BIRD IN THE EMPTY SPACE BETWEEN THE PIPES??
                if not (topy < bird.y < (i.y-40)) and bird.alive:

                    bird.alive=False
                    total_birds_dead+=1

    #IF THE NUMBER OF DEAD BIRDS IS EQUAL TO TOTAL NUMBER OF BIRDS RESET THE GAME
    if total_birds_dead==NO_OF_BIRDS:
        gen+=1
        total_birds_dead = 0
        reset()


                        #'''Constants'''





total_birds_dead = 0
gen=0
birds=[]
best_bird=None
pipes=[]

run = True

# MAKE THE PYGAME IMAGE FOR PIPE, BIRD AND BACKGROUND
bg_img=pygame.image.load("background.jpeg")
bg=pygame.transform.scale(bg_img, SCREEN_SIZE)

if HARRY_MODE:
    player_img = pygame.image.load("car.png")
    pipe_img = pygame.image.load("ben.png")

else:
    player_img=pygame.image.load("yellowbird.png")
    pipe_img=pygame.image.load("pipes.png")

player = pygame.transform.scale(player_img, PLAYER_SIZE)
PIPE_IMG=pygame.transform.scale(pipe_img, PIPE_SIZE)
ROT_PIPE_IMG=pygame.transform.rotate(PIPE_IMG,180)




                        #'''Constants Over'''


                    #set the window and the clock for the game

pygame.display.set_caption("Flappy Bird")

# SET THE SCREEN SIZE OF THE WINDOW
WIN=pygame.display.set_mode(SCREEN_SIZE)

# THE CLOCK FOR THE GAME
clock=pygame.time.Clock()

# MAKE A LIST OF BIRDS FOR THE NUMBER OF BIRDS
for i in range(NO_OF_BIRDS):
    birds.append(Bird.bird())

#INITIALLY MAKE THE BEST BIRD AS THE FIRST BIRD AND THEN WE CAN CHANGE IT DEPENDING ON THE SCORE
best_bird=birds[0]






                    #GAME LOGIC

while run:

    clock.tick(FPS)

    #check if the window has been closed by the user
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # If space is pressed make the bird jump
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        for bird in birds:
            bird.jump()
        # ONLY FOR TESTING

        #FOR TESTING USE BELOW CODE
    """
        if pygame.key.get_pressed()[pygame.K_DOWN]:
             new_bird.down()
        if pygame.key.get_pressed()[pygame.K_LEFT]:
             new_bird.left()
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
             new_bird.right()"""
    # move the bird according to the input
    #TRAIN WITH BEST INPUT
    """TOTAL_FRAMES += 1
    if TOTAL_FRAMES>115:
        for bird in birds:
            if TOTAL_FRAMES<TRAINING_FRAMES :

                decision=bird.train(pipes)

                #print(TOTAL_FRAMES)

                print(bird.brain.bias_ih.data, bird.brain.bias_ho.data, bird.brain.weights_ih.data,bird.brain.weights_ho.data)

            else:
                #print(bird.brain.bias_ih.data, bird.brain.bias_ho.data, bird.brain.weights_ih.data,bird.brain.weights_ho.data)
                decision=bird.think(pipes)
            print(decision[0][0],bird.think(pipes)[0][0])
            if decision[0][0]>0.5:
                bird.jump()
            bird.move()"""

    for bird in birds:

        # print(bird.brain.bias_ih.data, bird.brain.bias_ho.data, bird.brain.weights_ih.data,bird.brain.weights_ho.data)
        decision = bird.think(pipes)
        if decision[0][0] > 0.5:
            bird.jump()
        bird.move()
        bird.score+=1

    # move all the pipes to the left and delete the pipes which have left the screen
    for pipe in pipes:
        pipe.move()
        if pipe.x<-100:
            pipes.remove(pipe)
            SCORE+=1
            print(SCORE)
            """for bird in birds:

                print(bird.score)"""

    #add new pipes to the game
    FRAMECOUNT_FOR_PIPES=add_new_pipe(FRAMECOUNT_FOR_PIPES)


    #collision detection

    is_game_over()
    # draw the graphic on the screen
    draw()






