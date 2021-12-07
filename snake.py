import random
import arcade

SCREEN_WIDTH=500
SECREEN_HEIGHT=500
DEFAULT_FONT_SIZE =4 

class snake(arcade.Sprite) :

    def __init__(self,w,h) -> None:
        super().__init__()

        self.color=arcade.color.BLACK
        self.width=10
        self.height=10
        self.body=0
        self.speed=3
        self.r=10
        self.center_x=SCREEN_WIDTH//2 
        self.center_y=SECREEN_HEIGHT//2
        self.change_x = 0
        self.change_y = 0
        self.score = 1
        self.body = []
        self.body.append([self.center_x,self.center_y])       


    def draw(self):
        for index, item in enumerate(self.body):
             arcade.draw_circle_filled(item[0], item[1], self.r, self.color)
         
    #harekat dar x-y
    def move(self):

        for i in range(len(self.body)-1, 0, -1):
            self.body[i][0] = self.body[i-1][0]
            self.body[i][1] = self.body[i-1][1]

        self.center_x += self.speed * self.change_x
        self.center_y += self.speed * self.change_y

        if self.body:
            self.body[0][0] += self.speed * self.change_x
            self.body[0][1] += self.speed * self.change_y
            
    #emtiazdehi
    def eat(self, food):

        if  food == 'apple':
            self.score += 1
            self.body.append([self.body[len(self.body)-1][0], self.body[len(self.body)-1][1]])

        elif food == 'pear':
            self.score += 2
            self.body.append([self.body[len(self.body)-1][0], self.body[len(self.body)-1][1]])
            self.body.append([self.body[len(self.body)-1][0], self.body[len(self.body)-1][1]])

        elif food == 'shit':
            self.score -=1    
            self.body.pop() 
               
#apple
class Apple(arcade.Sprite):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        self.image = 'apple.png'  
        self.apple = arcade.Sprite(self.image, 0.08)    
        self.apple.center_x = random.randint(20, w-20)  
        self.apple.center_y = random.randint(20, h-20)  

    def draw(self):
        self.apple.draw()

#pear
class Pear(arcade.Sprite):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        self.image = 'pear.png'
        self.pear = arcade.Sprite(self.image, 0.05) 
        self.pear.center_x = random.randint(20, w-20)  
        self.pear.center_y = random.randint(20, h-20)

    def draw(self):
        self.pear.draw()

#shit
class Shit(arcade.Sprite):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        self.image = 'shit.png'
        self.shit = arcade.Sprite(self.image, 0.05)     
        self.shit.center_x = random.randint(20, w-20) 
        self.shit.center_y = random.randint(20, h-20)

    def draw(self):
        self.shit.draw()


class game(arcade.Window) : 

    def __init__(self) -> None:
        super().__init__(width=SCREEN_WIDTH,height=SECREEN_HEIGHT,title='snake game',resizable=True)  
        arcade.set_background_color(arcade.color.RICH_LAVENDER)
        
        #object az hame classha
        self.snake = snake(SCREEN_WIDTH, SECREEN_HEIGHT)  
        self.apple = Apple(SCREEN_WIDTH, SECREEN_HEIGHT)  
        self.pear = Pear(SCREEN_WIDTH, SECREEN_HEIGHT)
        self.shit = Shit(SCREEN_WIDTH, SECREEN_HEIGHT)

    #OUTPUT RANGI 
    def on_draw(self): 
        arcade.start_render() 
        self.snake.draw()
        self.snake.draw()
        self.apple.draw()
        self.pear.draw()
        self.shit.draw()

        start_x = 10  
        start_y = SCREEN_WIDTH - 35 
        
        arcade.draw_text('Score : %i'%self.snake.score, start_x , start_y ,arcade.color.BLACK , DEFAULT_FONT_SIZE * 3, width=SCREEN_WIDTH, align='left')
        
        
        if self.snake.score <= 0 or self.snake.center_x<0 or self.snake.center_x>SCREEN_WIDTH or self.snake.center_y<0 or self.snake.center_y>SECREEN_HEIGHT:
            arcade.draw_text('Game Over',SCREEN_WIDTH//2, SECREEN_HEIGHT//2,arcade.color.BLACK, DEFAULT_FONT_SIZE * 3, width=SCREEN_WIDTH, align='left')
            arcade.exit()    

    #taghirat
    def update(self, delta_time: float):

        self.snake.move()

        if arcade.check_for_collision(self.snake, self.apple.apple):
            self.snake.eat('apple')
            self.apple = Apple(SCREEN_WIDTH, SECREEN_HEIGHT)

        if arcade.check_for_collision(self.snake, self.pear.pear):
            self.snake.eat('pear')
            self.pear = Pear(SCREEN_WIDTH, SECREEN_HEIGHT)
    
        if arcade.check_for_collision(self.snake,self.shit.shit):
            self.snake.eat('shit')
            self.sit = Shit(SCREEN_WIDTH, SECREEN_HEIGHT)

    #TAEEN KELIDHAYE BAZI
    def key_release(self, key, modifiers):
        
        if key == arcade.key.LEFT:
            self.snake.change_x = -1
            self.snake.change_y = 0   
        
        elif key == arcade.key.RIGHT:
            self.snake.change_x = 1
            self.snake.change_y = 0

        elif key == arcade.key.UP:
            self.snake.change_x = 0
            self.snake.change_y = 1      
        
        elif key == arcade.key.DOWN:
            self.snake.change_x = 0
            self.snake.change_y = -1
        
        
play_game=game()    
arcade.run() 