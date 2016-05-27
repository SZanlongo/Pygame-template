from src.Scenes.TitleScene import *


# run_game is based on Blake O'Hare's tutorial: "PyGame Basics Tutorial" at:
# http://www.nerdparadise.com/tech/python/pygame/basics/
def run_game(width, height, fps, caption, starting_scene):
    pygame.init()
    screen = pygame.display.set_mode((width, height))  # Window dimensions
    pygame.display.set_caption(caption)  # Window title
    clock = pygame.time.Clock()

    active_scene = starting_scene

    # Input handling
    while active_scene != None:
        pressed_keys = pygame.key.get_pressed()
        mpos = pygame.mouse.get_pos()

        # Event filtering
        filtered_events = []
        for event in pygame.event.get():  # User actions
            # Check for quit attempt
            quit_attempt = False
            if event.type == pygame.QUIT:
                quit_attempt = True
            elif event.type == pygame.KEYDOWN:
                alt_pressed = pressed_keys[pygame.K_LALT] or \
                              pressed_keys[pygame.K_RALT]
                if event.key == pygame.K_ESCAPE:
                    quit_attempt = True
                elif event.key == pygame.K_F4 and alt_pressed:
                    quit_attempt = True

            if quit_attempt:
                active_scene.Terminate()
            else:
                filtered_events.append(event)

        # Scene handling
        active_scene.ProcessInput(filtered_events, pressed_keys, mpos)
        active_scene.Update()
        active_scene.Render(screen)

        active_scene = active_scene.next

        # Render and advance clock
        pygame.display.flip()
        clock.tick(fps)  # Set FPS
