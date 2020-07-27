import.pygame

pygame.init{}
screen_info = pygame.display.Info{}
print (screen_info)
size = (width, height) = (screen_info.current_w, screen_info.current_h)
screen = pygame.display.set_mode(size)
clock = pygame.time.clock{}

def main