from pygame import QUIT, KEYDOWN, K_PLUS, K_MINUS, MOUSEBUTTONDOWN, MOUSEBUTTONUP, VIDEORESIZE
from data.ui_objects import Animation
from numpy import array


class Events:
    def __init__(self, data):
        self.data = data
        self.scale_queue = []

    def anim_upd(self):
        for i in range(len(self.scale_queue)):
            self.data.dyn_scale, res = self.scale_queue[i].update(array([self.data.dyn_scale]))
            self.data.dyn_scale = self.data.dyn_scale[0]
            if res:
                self.scale_queue.pop(i)

    def update(self, evs):
        self.anim_upd()
        for event in evs:
            if event.type == QUIT:
                self.data.running = False
            elif event.type == KEYDOWN:
                if event.key == K_PLUS:
                    self.scale_queue += [Animation(4.5, 0.3, 0, array([self.data.dyn_scale]), array([self.data.dyn_scale]) * 1.2)]
                elif event.key == K_MINUS:
                    self.scale_queue += [Animation(4.5, 0.3, 0, array([self.data.dyn_scale]), array([self.data.dyn_scale]) / 1.2)]
            elif event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    print("press")
                    # for item in Buttons_sprites:
                    #     if item.rect.collidepoint(event.pos):
                    #         if item.getCellName() in button_kinds and item.getCellName() != 'craft':
                    #             renderabel = button_kinds[button_kinds.index(item.getItemName())]
                    #             item.press()
                    #         elif item.getCellName() == 'craft':
                    #             allCafters[0].addRecipe(str(item.getItemName()))
                    #             item.press()
                    #         elif item.getCellName() != 'craft':
                    #             item.unpress()
                # print(self.data.scale)
            elif event.type == VIDEORESIZE:
                self.data.size = event.size


# import pygame.examples.eventlist
# pygame.examples.eventlist.main()

# # copy paste
# while running:
#
#         if event.type == pygame.MOUSEWHEEL:
#             pos.new_scale(event.dict["y"])
#             if event.dict["y"] > 0:
#                 pos.new_center_pos(pygame.mouse.get_pos())
#             print(pos.SCALE, pos.CENTER_POS)
#             render.draw_set()
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             pos.new_center_pos(pygame.mouse.get_pos())
#             print(pos.SCALE, pos.CENTER_POS)
#             render.draw_set()
#             # Need redraw scene
#
#         if event.type == pygame.USEREVENT + 1:
#             # Update scene every 1000 // FPS millis
#
#             pygame.display.flip()
#
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_F11:
#                 if full_size:
#                     pos.SIZE = width, height = 1920, 1080
#                     screen = pygame.display.set_mode(pos.SIZE, pygame.FULLSCREEN, 32)
#                     full_size = False
#                 else:
#                     pos.SIZE = width, height = standard_width, standard_height
#                     screen = pygame.display.set_mode(size, pygame.RESIZABLE)
#                     full_size = True
#     # print(pygame.time.get_ticks())
#
#     # pygame.draw.rect(screen, (1, 1), (100, 100))
# # pygame.quit()
