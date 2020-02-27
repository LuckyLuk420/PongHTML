import pygame as game

from random import randint, randrange

# ___Constants___
# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
game_color = [white, red, green, blue]

# Window
width = 800
height = 700
fps = 60

# Paddle
paddle_speed = height / 60

# Playing field
top = int(height / 7)
half = [int(width / 2), int(height / 2)]
border = [int(width / 80), int(height / 60), int(width - width / 80), int(height - height / 60)]

field = [[border[0], border[1]],
         [border[2], border[1]],
         [border[2], border[3]],
         [border[0], border[3]]]
line_size = 10

# Init Game
game.init()
running = True
clock = game.time.Clock()

# TODO add Game AI for player 2
TWO_P_MODE = True

# Let's have some fun (No Player Mode)
FUN = True

# Window
game.display.set_caption("Pong /// by Lucky Luk")
win = game.display.set_mode((width, height))


# Create Ball
class Ball(game.sprite.Sprite):
    def __init__(self, size, color=white):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.size = size

        # Set background color transparent
        self.image = game.Surface([size, size])
        self.image.fill(black)
        self.image.set_colorkey(black)
        # Fetch the rectangle of the image
        self.rect = self.image.get_rect()
        # Set the velocity
        self.velocity = [randint(2, 6), randint(-8, 8)]

        # Draw the Ball
        game.draw.rect(self.image, color, [0, 0, size, size])

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self, paddle=(0, 0)):
        if self.rect.x < width / 2:
            self.rect.x = paddle[0] + paddle[1]
        if self.rect.x > width / 2:
            self.rect.x = paddle - self.size
        # self.rect.x -= int(self.velocity[0])
        self.velocity[0] = (randrange(100, 130, 5) / 100) * -self.velocity[0]
        # TODO bounce angle depends on where the ball hits the paddle
        self.velocity[1] = randint(-8, 8)

    def reset(self):
        self.velocity[0] = (self.velocity[0] / abs(self.velocity[0]) * randint(2, 6))
        self.rect.x = int(width / 2)
        self.rect.y = int(height / 2)


# Create Paddle
class Paddle(game.sprite.Sprite):

    def __init__(self, p_width, p_height, color=white):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.width = p_width
        self.height = p_height
        # Set background color transparent
        self.image = game.Surface([self.width, self.height])
        self.image.fill(black)
        self.image.set_colorkey(black)
        # Fetch the rectangle of the image
        self.rect = self.image.get_rect()

        # Draw the Paddle
        game.draw.rect(self.image, color, [0, 0, width, height])

    def up(self, pixel=15):
        self.rect.y -= pixel
        if self.rect.y <= top:
            self.rect.y = top

    def down(self, pixel=15):
        self.rect.y += pixel
        if self.rect.y > border[3] - self.height:
            self.rect.y = border[3] - self.height


# Create AI
class AI:

    def __init__(self, paddle):
        self.paddle = paddle

    def move(self, ai_ball, blind=20):
        velocity = (abs(ai_ball.rect.y - (self.paddle.rect.y + (self.paddle.height / 2)))) / 10
        if ai_ball.rect.y + ai_ball.velocity[1] - blind > self.paddle.rect.y + (self.paddle.height / 2):
            self.paddle.rect.y += velocity
            if self.paddle.rect.y > border[3] - self.paddle.height:
                self.paddle.rect.y = border[3] - self.paddle.height
        elif ai_ball.rect.y - ai_ball.velocity[1] + blind < self.paddle.rect.y + (self.paddle.height / 2):
            self.paddle.rect.y -= velocity
            if self.paddle.rect.y <= top:
                self.paddle.rect.y = top


# Set up Ball
ball = Ball(width / 40, game_color[0])
ball.rect.x = int(width / 2)
ball.rect.y = int(height / 2)
# Set up Paddle for Player 1
player1 = Paddle(width / 40, height / 5, game_color[0])
player1.rect.x = int(width / 12)
player1.rect.y = int(height / 2)
p1_ai = AI(player1)
# Set up Paddle for Player 2
player2 = Paddle(width / 40, height / 5, game_color[0])
player2.rect.x = int(11 * width / 12)
player2.rect.y = int(height / 2)
p2_ai = AI(player2)

# Player scores
score1 = 0
score2 = 0

# List of all Sprites
all_sprites_list = game.sprite.Group()
all_sprites_list.add(player1)
all_sprites_list.add(player2)
all_sprites_list.add(ball)

# TODO add button do change color
# TODO --> maybe add a rainbow mode
# def change_color():
#     game_color.append(game_color[0])
#     game_color.pop(0)


# ___Main Loop___
while running:
    # ___Main event Loop___
    for event in game.event.get():
        if event.type == game.QUIT:
            running = False
        elif event.type == game.KEYDOWN:
            if event.key == game.K_ESCAPE:
                running = False
            if event.key == game.K_p:
                if TWO_P_MODE:
                    TWO_P_MODE = False
                    FUN = False
                else:
                    TWO_P_MODE = True
            if event.key == game.K_f:
                if FUN:
                    FUN = False
                    print("No Fun")
                else:
                    FUN = True
                    print("Fun")
            # if event.key == game.K_c:
            #     change_color()

    # Event handlers
    pressed_key = game.key.get_pressed()
    if TWO_P_MODE and FUN:
        p1_ai.move(ball)
    elif pressed_key[game.K_w]:
        player1.up(int(paddle_speed))
    elif pressed_key[game.K_s]:
        player1.down(int(paddle_speed))
    if TWO_P_MODE:
        p2_ai.move(ball)
    elif pressed_key[game.K_UP]:
        player2.up(int(paddle_speed))
    elif pressed_key[game.K_DOWN]:
        player2.down(int(paddle_speed))

    # ___Logic___
    all_sprites_list.update()

    # Collision between ball and walls
    if ball.rect.x <= border[0]:  # Player 2 scored
        score2 += 1
        ball.reset()
    if ball.rect.x >= border[2] - ball.size:  # Player 1 scored
        score1 += 1
        ball.reset()

    if ball.rect.y <= top or ball.rect.y >= border[3] - ball.size:
        ball.rect.y -= ball.velocity[1]
        ball.velocity[1] = -ball.velocity[1]

    # Collision between ball and paddles
    # FIXME  ___DONE___: ball gets stuck in paddle when hit on the side
    if game.sprite.collide_mask(player1, ball):
        ball.bounce((player1.rect.x, player1.width))
    if game.sprite.collide_mask(ball, player2):
        ball.bounce(player2.rect.x)

    # ___Draw___
    # Grid
    win.fill(black)
    game.draw.line(win, game_color[0], [half[0], border[1]], [half[0], border[3]], line_size)
    game.draw.line(win, game_color[0], [border[0], top], [border[2], top], line_size)
    # Border
    game.draw.line(win, game_color[0], [border[0], border[1] - int(line_size / 2.1)], [border[0], border[3]], line_size)
    game.draw.line(win, game_color[0], [border[0] - int(line_size / 2.1), border[3]], [border[2], border[3]], line_size)
    game.draw.line(win, game_color[0], [border[2], border[3] + int(line_size / 2)], [border[2], border[1]], line_size)
    game.draw.line(win, game_color[0], [border[2] + int(line_size / 2), border[1]], [border[0], border[1]], line_size)
    # game.draw.lines(win, game_color[0], True, field, line_size)  # Field grid with rounded edges

    all_sprites_list.draw(win)

    # Score
    font = game.font.Font(None, 100)
    text = font.render(str(score1), False, game_color[0])
    win.blit(text, (int(width / 4), int(border[1] * 2.5)))
    text = font.render(str(score2), False, game_color[0])
    win.blit(text, (int(3 * width / 4), int(border[1] * 2.5)))

    if TWO_P_MODE:
        font = game.font.Font(None, 74)
        text = font.render("CPU", False, game_color[0])
        win.blit(text, (int(5 * width / 9), int(border[1] * 4.5)))

    # Update window
    game.display.flip()
    clock.tick(fps)

# Terminate the engine
game.quit()
