from datetime import datetime
from debug import class_info
# import pygame, sys
# from settings import *
# from level import Level
# class Game:
# 	def __init__(self):

# 		# general setup
# 		pygame.init()
# 		self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
# 		pygame.display.set_caption('Unforgiven Crussade')
# 		self.clock = pygame.time.Clock()

# 		self.level = Level()

# 		# sound 
# 		main_sound = pygame.mixer.Sound('../audio/main.ogg')
# 		main_sound.set_volume(0.5)
# 		main_sound.play(loops = -1)

# 	def run(self):

        # while True:
            # for event in pygame.event.get():
            # 	if event.type == pygame.QUIT:
            # 		pygame.quit()
            # 		sys.exit()
        # 		if event.type == pygame.KEYDOWN:
        # 			if event.key == pygame.K_m:
        # 				self.level.toggle_menu()

            # self.screen.fill(WATER_COLOR)
            # self.level.run()
            # pygame.display.update()
        # self.clock.tick(FPS)


  
if __name__ == '__main__':
    import os
    from pynput import keyboard
    from api.HAPI import Hex, HexField, AXES, Position


    CHARS = {
        'empty': '.',
        'player': '#',
    }
    DEBUG = {}

    # game objects
    class Hex(Hex):
        def __str__(self) -> str:
            if self.position == Game.player.position:
                return CHARS['player']
            return CHARS['empty']



    class Player:
        def __init__(self, start_position:Position) -> None:
            self.position = start_position
            self.pressed_buttons = set()
            self.move_delay = 0.5
            self.last_move = datetime.now()


        def move(self, direction:Position) -> None:
            if not direction: return
            if (datetime.now() - self.last_move).total_seconds() <= self.move_delay: return
            self.last_move = datetime.now()
            self.position += direction
            if not Game.field.is_point_on_field(self.position):
                if   direction == [+1,+0]: self.position.x = max(self.position.y - Game.field.size // 2, 0)
                elif direction == [+1,+1]: self.position.x, self.position.y = Game.field.size - self.position.y, Game.field.size - self.position.x
                elif direction == [+0,+1]: self.position.y = max(self.position.x - Game.field.size // 2, 0)
                elif direction == [-1,-0]: self.position.x = min(self.position.y + Game.field.size // 2, Game.field.size-1)
                elif direction == [-1,-1]: self.position.x, self.position.y = Game.field.size-2 - self.position.y, Game.field.size-2 - self.position.x
                elif direction == [-0,-1]: self.position.y = min(self.position.x + Game.field.size // 2, Game.field.size-1)




    class Game:
        # attributes
        is_running:bool = False
        field:HexField = None
        player:Player = None


        @staticmethod
        def stop():
            # is_running
            Game.is_running = False
            # field
            del Game.field
            # player
            Game.player = None


        @staticmethod
        def start():
            # attributes
            ## is_running
            Game.is_running = True
            ## field
            Game.field = HexField(9, Hex)
            Game.field.setup_repr(separator = ' ', offfield = '', bounds = ['|','|'])
            ## player
            Game.player = Player(Position(*Game.field.center))
            
            # input listener
            def on_press(key):
                try: key = key.char
                except: key = key.name  
                Game.player.pressed_buttons.add(key)
            def on_release(key):
                try: key = key.char
                except: key = key.name  
                Game.player.pressed_buttons.remove(key)
            listener = keyboard.Listener(on_press=on_press, on_release=on_release)
            listener.start()

            # run
            Game.main()


        @staticmethod
        def player_handler(player:Player):
            if 'esc' in player.pressed_buttons:
                Game.is_running = False
            # move
            if 's' not in player.pressed_buttons:
                move_direction = Position(0, 0)
                if 'a' in player.pressed_buttons: move_direction = -AXES['x']
                if 'd' in player.pressed_buttons: move_direction =  AXES['x']

                if 'q' in player.pressed_buttons: move_direction = -AXES['y']
                if 'c' in player.pressed_buttons: move_direction =  AXES['y']

                if 'w' in player.pressed_buttons: move_direction = -AXES['z']
                if 'x' in player.pressed_buttons: move_direction =  AXES['z']

                player.move(move_direction)


        old_visual = None
        @staticmethod
        def visual_update():
            new_visual = ''
            new_visual += str(Game.field) + '\n'
            new_visual += '\n'.join([f'{k}: {v}' for k, v in DEBUG.items()])
            if new_visual == Game.old_visual: return
            Game.old_visual = new_visual
            os.system('cls' if os.name=='nt' else 'clear')
            print(new_visual)
            

        @staticmethod
        def main():
            while Game.is_running:
                Game.player_handler(Game.player)
                Game.visual_update()


    # run
    Game.start()










    # from objects.fractions import FractionTheUnforgiven
    # from objects.sectors import TestSector
    

    # player_fracion = FractionTheUnforgiven()
    # ship1 = FractionTheUnforgiven.units[2]([1,2])
    # ship2 = FractionTheUnforgiven.units[2]([1,1])

    


    # values = [" ","░","▒","▓","█"]
    # field = TestSector()
    # print(field.size)
    # field.gen(seed=1)
    # print(field)
    # for coords in field.get_all_coords():
    #     print(field.__getitem__(*coords))
