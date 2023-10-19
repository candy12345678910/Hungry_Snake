import pygame
import random
import winsound

pygame.init()
pygame.mixer.init()

# pygame.mixer.music.load("PYTHON Programs\Snake_Game\sounds\heheboi.mp3")
# pygame.mixer.music.play()
#Colors
white=(179, 255, 194)
red=(255,0,0)
black=(0,0,0)
warm_red=(255, 78, 59)
yellow=(247, 190, 74)
violet=(76, 50, 168)

#resolution
screen_height=300
screen_width=300


#Game window
gamewindow=pygame.display.set_mode((screen_height,screen_width))

#Caption
pygame.display.set_caption("Hungry Snake")

snake_height=8

#speed
speed=1
clock=pygame.time.Clock()

#Font
font=pygame.font.SysFont(None,20)


#Score Print
def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gamewindow.blit(screen_text,[x,y])

#Snake length function
def plot_snake(gamewindow,color,snk_list,snake_height):
    for x,y in snk_list:
        pygame.draw.rect(gamewindow,color,[x,y,snake_height,snake_height])


#==============================GAME MENU===============================       
def menu():
    gamewindow.fill(white)
    text_screen("Hungry Snake",violet,107,125)
    text_screen("Press [Enter] to play",violet,90,150)
    exit_game=False
    while not exit_game:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    winsound.PlaySound(r"PYTHON Programs\Snake_Game\sounds\bgm.wav",winsound.SND_ASYNC+winsound.SND_LOOP)
                    # winsound.PlaySound(None,0)

                    gameloop()

        pygame.display.update()
        clock.tick(60)
#==============================GAME LOOP===============================
#game loop
def gameloop():
    
    c=0
    #high score
    with open("PYTHON Programs\Snake_Game\highScore.txt","r") as f:
        highscore=int(f.read())

    exit_game=False
    game_over=False

    snake_x=10      #snake position at x
    snake_y=50      #snake position at y

    
    #Food
    food_x=random.randint(20,screen_height-10)
    food_y=random.randint(50,screen_width-10)

    #velocity
    velocity_x=0
    velocity_y=0

    fps=120

    #snake length
    snk_length=1
    snk_list=[]
    
    #score
    score=0

    while not exit_game:
        #game over
        if(game_over):
            gamewindow.fill(warm_red)
            text_screen("Game OVER!",white,110,100)
            text_screen("Press [Enter] to retry",white,90,140)
            text_screen(f"High score {highscore}",white,110,230)
            text_screen("Press [R] to reset highscore",white,70,250)
            
            for event in pygame.event.get():
                #to exit game
                if event.type==pygame.QUIT:
                    exit_game=True
                    
                #to continue game
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        gameloop()

                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_r:
                        with open("PYTHON Programs\Snake_Game\highScore.txt","w") as f:
                            f.write("5")
                        gameloop()


        #game continue
        else:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                
                #Right
                if event.type == pygame.KEYDOWN:
                    if event.key== pygame.K_RIGHT or event.key == pygame.K_d:
                        velocity_x=speed
                        velocity_y=0
                
                #Left
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_LEFT or event.key == pygame.K_a:
                        velocity_x=-speed
                        velocity_y=0

                #Up
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_UP or event.key == pygame.K_w:
                        velocity_y=-speed
                        velocity_x=0
                    
                #Down
                if event.type==pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        velocity_y=speed
                        velocity_x=0

                #Catch food
                if abs(snake_x-food_x)<16 and abs(snake_y-food_y)<16:
                    pygame.mixer.music.load(r"PYTHON Programs\Snake_Game\sounds\bite.mp3")
                    pygame.mixer.music.play()
                    score=score+1
                    if score>highscore:
                        highscore=score
                        if c==0:
                            pygame.mixer.music.load(r"PYTHON Programs\Snake_Game\sounds\nice.mp3")
                            pygame.mixer.music.play()
                            c+=1
                    
                    snk_length+=5
                    food_x=random.randint(10,screen_height-10)
                    food_y=random.randint(50,screen_width-10)


            gamewindow.fill(white)
            pygame.draw.rect(gamewindow,yellow,[0,0,300,30])
            text_screen(f"Score: {str(score)}   High Score: {highscore}",black,10,10)   #Score print
            # pygame.draw.circle(gamewindow,red,(food_x,food_y),4)

            #snake length
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]
            
            #game over condition
            if snake_x==0 or snake_x>screen_width or snake_y==30 or snake_y>screen_height:
                pygame.mixer.music.load(r"PYTHON Programs\Snake_Game\sounds\gameover.mp3")
                pygame.mixer.music.play()
                game_over=True
                with open("PYTHON Programs\Snake_Game\highScore.txt","w") as f:
                    f.write(str(highscore))


            if head in snk_list[:-1]:
                pygame.mixer.music.load(r"PYTHON Programs\Snake_Game\sounds\gameover.mp3")
                pygame.mixer.music.play()
                game_over=True
                with open("PYTHON Programs\Snake_Game\highScore.txt","w") as f:
                    f.write(str(highscore))

            plot_snake(gamewindow,black,snk_list,snake_height)

            pygame.draw.circle(gamewindow,red,(food_x,food_y),4)
            # pygame.draw.rect(gamewindow,black,[snake_x,snake_y,snake_height,snake_width])
        pygame.display.update()
        clock.tick(fps)
        snake_x+=velocity_x
        snake_y+=velocity_y

    pygame.quit()

    quit()

menu()
