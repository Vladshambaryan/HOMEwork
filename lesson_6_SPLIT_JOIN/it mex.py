# print("Добро пожаловать в мой компьютерный тест!")
#
# go = input("Хотите играть? ")
#
# if go.lower() != "да":
#     exit()
#
# print("Отлично! Начинаем игру :)")
# ball = 0
#
# answer = input("Что означает CPU? ")
# if answer.lower() == "центральный процессор":
#     print('Правильно!')
#     ball += 1
# else:
#     print("Неправильно!")
#
# answer = input("Что означает GPU? ")
# if answer.lower() == "графический процессор":
#     print('Правильно!')
#     ball += 1
# else:
#     print("Неправильно!")
#
# answer = input("Что означает RAM? ")
# if answer.lower() == "оперативная память":
#     print('Правильно!')
#     ball += 1
# else:
#     print("Неправильно!")
#
# answer = input("Что означает PSU? ")
# if answer.lower() == "блок питания":
#     print('Правильно!')
#     ball += 1
# else:
#     print("Неправильно!")
#
# print("Вы правильно ответили на " + str(ball) + " вопроса!")
# print("Ваш результат составляет " + str((ball / 4) * 100) + "%.")

list_a = [1, 2020, 70]
list_b = [2, 4, 7, 2000]
list_c = [3, 70, 7]

for a in list_a:
    for b in list_b:
        for c in list_c:
            if a + b + c == 2077:
                print(a, b, c)

                from itertools import product

                list_a = [1, 2020, 70]
                list_b = [2, 4, 7, 2000]
                list_c = [3, 70, 7]

                for a, b, c in product(list_a, list_b, list_c):
                    if a + b + c == 2077:
                        print(a, b, c)
                # 70 2000 7


# import sqlite3
# conn = sqlite3.connect('example.db')
# cursor = conn.cursor()
# cursor.execute('''CREATE TABLE users
#               (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
# conn.close()


# import pygame
# import random
#
# class RewardsBombs():
#     def __init__(self):
#         pygame.init()
#         self.screen_width = 600
#         self.screen_height = 600
#         self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
#         pygame.display.set_caption("Призы и бомбы")
#         self.clock = pygame.time.Clock()
#         self.green_pos = [self.screen_width // 2, self.screen_height - 30]
#         self.red_positions = []
#         self.red_speed = 2
#         self.score = 0
#         self.font = pygame.font.SysFont("Arial", 24)
#         self.run()
#
#     def run(self):
#         while True:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     pygame.quit()
#                     exit()
#
#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_LEFT:
#                         if self.green_pos[0] - 20 >= 0:
#                             self.green_pos[0] -= 20
#                     elif event.key == pygame.K_RIGHT:
#                         if self.green_pos[0] + 20 <= self.screen_width:
#                             self.green_pos[0] += 20
#                     elif event.key == pygame.K_UP:
#                         if self.green_pos[1] - 20 >= 0:
#                             self.green_pos[1] -= 20
#                     elif event.key == pygame.K_DOWN:
#                         if self.green_pos[1] + 20 <= self.screen_height:
#                             self.green_pos[1] += 20
#
#             # движение красных бомб
#             for i in range(len(self.red_positions)):
#                 self.red_positions[i][1] += self.red_speed
#
#             # создание бомб и призов
#             if random.random() < 0.02:
#                 x = random.randint(0, self.screen_width)
#                 num = random.randint(1, 10)
#                 if num % 2 == 0:
#                     self.red_positions.append([x, 0, False])
#                 else:
#                     self.red_positions.append([x, 0, True])
#
#             # проверка столкновений с игроком
#             for pos in self.red_positions:
#                 if pos[2]:
#                     if abs(pos[0] - self.green_pos[0]) <= 20 and abs(pos[1] - self.green_pos[1]) <= 20:
#                         self.score += 1
#                         self.red_positions.remove(pos)
#                 else:
#                     if (pos[0] - self.green_pos[0]) ** 2 + (pos[1] - self.green_pos[1]) ** 2 < 400:
#                         self.game_over()
#
#             # убираем бомбы за пределами окна
#             self.red_positions = [pos for pos in self.red_positions if pos[1] < self.screen_height]
#             self.screen.fill((0, 0, 0))
#
#             for pos in self.red_positions:
#                 if pos[2]:
#                     pygame.draw.polygon(self.screen, (0, 0, 255), [[pos[0], pos[1]-10], [pos[0]+10, pos[1]+10], [pos[0]-10, pos[1]+10]])
#                 else:
#                     pygame.draw.circle(self.screen, (255, 0, 0), pos[:2], 10)
#
#             pygame.draw.circle(self.screen, (0, 255, 0), self.green_pos, 10)
#
#             self.draw_score()
#             pygame.display.update()
#             self.clock.tick(60)
#
#     def draw_score(self):
#         score_surface = self.font.render(f"Призы: {self.score}", True, (255, 255, 255))
#         self.screen.blit(score_surface, (10, 10))
#
#     def game_over(self):
#         message_surface = self.font.render(f"Игра закончена! Призы: {self.score}", True, (255, 0, 0))
#         self.screen.blit(message_surface, (self.screen_width // 2 - message_surface.get_width() // 2, self.screen_height // 2 - message_surface.get_height() // 2))
#         pygame.display.update()
#         pygame.time.wait(3000)
#         pygame.quit()
#         exit()
#
# if __name__ == "__main__":
#     RewardsBombs()





#
# import pygame
# import random
#
# pygame.init()
# screen_width = 640
# screen_height = 480
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption('Лабиринт')
#
# black = (0,0,0)
# white = (255,255,255)
# red = (255,0,0)
# blue = (0,0,255)
# green = (0,255,0)
#
# # параметры стен и дверей
# line_width = 10
# line_gap = 40
# line_offset = 20
# door_width = 20
# door_gap = 40
# max_openings_per_line = 5
#
# # параметры и стартовая позиция игрока
# player_radius = 10
# player_speed = 5
# player_x = screen_width - 12
# player_y = screen_height - line_offset
#
# # рисуем стены и двери
# lines = []
# for i in range(0, screen_width, line_gap):
#     rect = pygame.Rect(i, 0, line_width, screen_height)
#     num_openings = random.randint(1, max_openings_per_line)
#     if num_openings == 1:
#         # одна дверь посередине стены
#         door_pos = random.randint(line_offset + door_width, screen_height - line_offset - door_width)
#         lines.append(pygame.Rect(i, 0, line_width, door_pos - door_width))
#         lines.append(pygame.Rect(i, door_pos + door_width, line_width, screen_height - door_pos - door_width))
#     else:
#         # несколько дверей
#         opening_positions = [0] + sorted([random.randint(line_offset + door_width, screen_height - line_offset - door_width) for _ in range(num_openings-1)]) + [screen_height]
#         for j in range(num_openings):
#             lines.append(pygame.Rect(i, opening_positions[j], line_width, opening_positions[j+1]-opening_positions[j]-door_width))
#
# clock = pygame.time.Clock()
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()
#
#     # передвижение игрока
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT] and player_x > player_radius:
#         player_x -= player_speed
#     elif keys[pygame.K_RIGHT] and player_x < screen_width - player_radius:
#         player_x += player_speed
#     elif keys[pygame.K_UP] and player_y > player_radius:
#         player_y -= player_speed
#     elif keys[pygame.K_DOWN] and player_y < screen_height - player_radius:
#         player_y += player_speed
#
#     # проверка столкновений игрока со стенами
#     player_rect = pygame.Rect(player_x - player_radius, player_y - player_radius, player_radius * 2, player_radius * 2)
#     for line in lines:
#         if line.colliderect(player_rect):
#             # в случае столкновения возвращаем игрока назад
#             if player_x > line.left and player_x < line.right:
#                 if player_y < line.top:
#                     player_y = line.top - player_radius
#                 else:
#                     player_y = line.bottom + player_radius
#             elif player_y > line.top and player_y < line.bottom:
#                 if player_x < line.left:
#                     player_x = line.left - player_radius
#                 else:
#                     player_x = line.right + player_radius
#     screen.fill(black)
#     for line in lines:
#         pygame.draw.rect(screen, green, line)
#     pygame.draw.circle(screen, red, (player_x, player_y), player_radius)
#     pygame.display.update()
#     clock.tick(60)


# from tkinter import *
# import time
# import random
# import pygame
#
# class Ball():
#
#     def __init__(self, canvas, platform, color):
#         self.canvas = canvas
#         self.platform = platform
#         self.oval = canvas.create_oval(200, 200, 215, 215, fill=color)
#         self.dir = [-3, -2, -1, 1, 2, 3]
#         self.x = random.choice(self.dir)
#         self.y = -1
#         self.touch_bottom = False
#
#     def touch_platform(self, ball_pos):
#         platform_pos = self.canvas.coords(self.platform.rect)
#         if ball_pos[2] >= platform_pos[0] and ball_pos[0] <= platform_pos[2]:
#             if ball_pos[3] >= platform_pos[1] and ball_pos[3] <= platform_pos[3]:
#                 return True
#         return False
#
#     def draw(self):
#         self.canvas.move(self.oval, self.x, self.y)
#         pos = self.canvas.coords(self.oval)
#         if pos[1] <= 0:
#             self.y = 3
#         if pos[3] >= 400:
#             self.touch_bottom = True
#         if self.touch_platform(pos) == True:
#             self.y = -3
#         if pos[0] <= 0:
#             self.x = 3
#         if pos[2] >= 500:
#             self.x = -3
#
# class Platform():
#
#     def __init__(self, canvas, color):
#         self.canvas = canvas
#         self.rect = canvas.create_rectangle(230, 300, 330, 310, fill=color)
#         self.x = 0
#         self.canvas.bind_all('<KeyPress-Left>', self.left)
#         self.canvas.bind_all('<KeyPress-Right>', self.right)
#
#     def left(self, event):
#         self.x = -2
#
#     def right(self, event):
#         self.x = 2
#
#     def draw(self):
#         self.canvas.move(self.rect, self.x, 0)
#         pos=self.canvas.coords(self.rect)
#         if pos[0] <= 0:
#             self.x = 0
#         if pos[2] >= 500:
#             self.x = 0
#
#
#
# window = Tk()
# window.title("Аркада")
# window.resizable(0, 0)
# window.wm_attributes("-topmost", 1)
#
# canvas = Canvas(window, width=500, height=400)
# canvas.pack()
#
# platform = Platform(canvas, 'green')
# ball = Ball(canvas, platform, 'red')
#
# while True:
#     if ball.touch_bottom == False:
#         ball.draw()
#         platform.draw()
#     else:
#         break
#
#     window.update()
#     time.sleep(0.01)
#
# window.mainloop()



import pygame
import time
import random

pygame.init()
colors_dictionary = {
    "white": (255, 255, 255),
    "yellow": (255, 255, 102),
    "black": (0, 0, 0),
    "red": (213, 50, 80),
    "green": (0, 255, 0),
    "blue": (50, 153, 213),
}
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Змейка")
clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def Your_score(score):
    value = score_font.render(
        "Ваш счёт: " + str(score), True, colors_dictionary["white"]
    )
    dis.blit(value, [0, 0])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(
            dis, colors_dictionary["black"], [x[0], x[1], snake_block, snake_block]
        )


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])


def gameLoop():
    game_over = False
    game_close = False
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0
    snake_List = []
    Length_of_snake = 1
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    while not game_over:
        while game_close == True:
            dis.fill(colors_dictionary["blue"])
            message(
                "Вы проиграли!\nНажмите Q для выхода или C для повторной игры",
                colors_dictionary["red"],
            )
            Your_score(Length_of_snake - 1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(colors_dictionary["blue"])
        pygame.draw.rect(
            dis, colors_dictionary["green"], [foodx, foody, snake_block, snake_block]
        )
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
        pygame.display.update()
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
        clock.tick(snake_speed)
    pygame.quit()
    quit()


gameLoop()
