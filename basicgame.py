
#import library
import pygame
import time
import math


pygame.init() #initialize pygame
screen = pygame.display.set_mode((500,600))
total_secs =0


#color 
GREY = (150,150,150)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255, 0, 0)


#format form
font = pygame.font.SysFont('sans', 30)
font1 = pygame.font.SysFont('sans', 100)


#draw symbol
text_1 = font.render('+', True, BLACK)
text_2 = font.render('-', True, BLACK)
text_3 = font.render('+', True, BLACK)
text_4 = font.render('-', True, BLACK)
text_5 = font.render('Start', True, BLACK)
text_6 = font.render('Reset', True, BLACK)

clock = pygame.time.Clock()

#variable declaration

mins = 0
secs = 0
running = True
start = False
total = 0
sound1 = pygame.mixer.Sound('tick.wav')
sound2 = pygame.mixer.Sound('timeout.wav')

while running:
    screen.fill(GREY)
    
    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    
    #draw button o'clock
    pygame.draw.rect(screen, WHITE, (100,50,50,50))
    pygame.draw.rect(screen, WHITE, (100,200,50,50))
    pygame.draw.rect(screen, WHITE, (200,50,50,50))
    pygame.draw.rect(screen, WHITE, (200,200,50,50))
    pygame.draw.rect(screen, WHITE, (300,50,150,50))
    pygame.draw.rect(screen, WHITE, (300,150,150,50))
    
    screen.blit(text_1, (100,50))
    screen.blit(text_2, (100,200))
    screen.blit(text_3, (200,50))
    screen.blit(text_4, (200,200))
    screen.blit(text_5, (300,50))
    screen.blit(text_6, (300,150))

    

    
    pygame.draw.rect(screen, BLACK, (50, 520, 400,50)) #count time
    pygame.draw.rect(screen, WHITE, (60, 530, 380,30)) #count time
    
    pygame.draw.circle(screen,BLACK,(250,400), 100) #draw circle o'clock
    pygame.draw.circle(screen,WHITE,(250,400), 95)
    pygame.draw.circle(screen,BLACK,(250,400), 5)
    
    #pygame.draw.line(screen,BLACK,(250,400), (250,310))


    
    for event in pygame.event.get():
        #exit if click x
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN: #mouse_left
            if event.button == 1:
                #+minutes
                if(100 < mouse_x <150) and (50 < mouse_y <100):
                    total_secs +=60
                    total = total_secs
                #-minutes
                if(100 < mouse_x <150) and (200 < mouse_y <250):
                    total_secs -=60
                    total = total_secs
                #+secs
                if(200 < mouse_x <250) and (50 < mouse_y <100):
                    total_secs +=1
                    total = total_secs
                #-secs
                if(200 < mouse_x <250) and (200 < mouse_y <250):
                    total_secs -=1
                    total = total_secs
                #start
                if(300 < mouse_x <450) and (50 < mouse_y <200):
                    start = True
                    total = total_secs
                #reset
                if(300 < mouse_x <450) and (150 < mouse_y <200):
                    total_secs = 0
                    
    #setting start
    if start:
        if total_secs >0:
            pygame.mixer.Sound.play(sound1)
            total_secs -= 1
            time.sleep(1)
        else:
            pygame.mixer.Sound.play(sound2)
            start = False
            
                  
    #draw time now  
    mins = total_secs // 60 #logic minutes
    secs = total_secs - (mins * 60)  #logic secs                          
    text_time = font1.render(str(mins) + ':' + str(secs), True, RED) #display time
    screen.blit(text_time,(100, 90)) #draw time 
    
    #setting o'clock (secs)
    x_sec = 250 + 90*math.sin(6*secs*math.pi/180) #sec x
    y_sec = 400 - 90*math.cos(6*secs*math.pi/180) #sec y
    
    pygame.draw.line(screen,BLACK,(250,400), (int(x_sec), int(y_sec)))

    #setting o'clock (minutes)
    x_min = 250 + 50*math.sin(6*mins*math.pi/180) #sec x
    y_min = 400 - 50*math.cos(6*mins*math.pi/180) #sec y
    
    pygame.draw.line(screen,BLACK,(250,400), (int(x_min), int(y_min)))
    #setting o'clock 
    if total != 0:
        pygame.draw.rect(screen,RED, (60,530,int(380*(total_secs/total)),30)) #red timeout
        

                      
    pygame.display.flip()
    
pygame.quit()