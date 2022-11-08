

# copy paste
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEWHEEL:
            pos.new_scale(event.dict["y"])
            if event.dict["y"] > 0:
                pos.new_center_pos(pygame.mouse.get_pos())
            print(pos.SCALE, pos.CENTER_POS)
            render.draw_set()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos.new_center_pos(pygame.mouse.get_pos())
            print(pos.SCALE, pos.CENTER_POS)
            render.draw_set()
            # Need redraw scene

        if event.type == pygame.USEREVENT + 1:
            # Update scene every 1000 // FPS millis

            pygame.display.flip()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:
                if full_size:
                    pos.SIZE = width, height = 1920, 1080
                    screen = pygame.display.set_mode(pos.SIZE, pygame.FULLSCREEN, 32)
                    full_size = False
                else:
                    pos.SIZE = width, height = standard_width, standard_height
                    screen = pygame.display.set_mode(size, pygame.RESIZABLE)
                    full_size = True
    # print(pygame.time.get_ticks())

    # pygame.draw.rect(screen, (1, 1), (100, 100))
pygame.quit()