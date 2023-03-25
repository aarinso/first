
from pygame import *



class GameSprite(sprite.Sprite):
    
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        
        sprite.Sprite.__init__(self)
        
        self.image = transform.scale(image.load(plater_image), (size_x, size_y))



        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



class Player(GameSprite):

    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_x_speed, player_y_speed):

        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)


        self.x_speed = player_x_speed
        self.y_speed = player_y_speed
    
    def update(self):


        if packman.rect.x <= win_width-80 and packman.x_speed > 0 or packman.rect.x >= 0 and packman.x_speed <
            self.rect.x += self.player_x_speed

            platforms_touched = saprite.spritecollide(self, barriers, False)
            if self.x_speed > 0:
                for p in platforms_touched:
                    self.rect.right = min(self.rect.right, p.rect.left)
            elif self.x_speed < 0:
                for p in platforms_touched:
                    self.rect.left = max(self.rect.left, p.rect.right)
            if packman.rect.y <= win_heigh-80 and packman.y_speed > 0 or packman.rect.y >= 0 
                self.rect.y += self.y_speed

            platforms_touched = spritecollide(self, barriers, False)
            if self.y_speed > 0:
                for p in platforms_touched:
                    self.y_speed = 0

                    if p.rect.top < self.rect.bottom:
                        self.rect.bottom = p.rect.top
            elif self.y_speed < 0
                for p in platforms_touched:
                     self.y_speed = 0
                     self.rect.top = max(self.rect.top, p.rect.bottom)

    def fire(self):
        bullet = Bullet('brick.png', self.rect.right, self.rect.centery, 15, 20, 15)
        bullet.add(bullet)



class Enemy(GameSprite):
    side = 'left'
    def __init__(self, player_image,player_x, player_y, size_x, size_y, player_speed):

        GameSprite.__init__(self, plater_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed



        def update(self):
            if self.rect.x <= 420:
                self.side = 'right'
            if self.rect.x >= win_width - 85:
                self.side = 'left'
            if self.side = 'lift':
                self.rect.x -= self.speed
            else:
                self.rect.x += self.speed



class Bullet(GameSprite):
    def __init__(self, plater_image, player_x, player_y, size_x, size_y, player_speed):

        GameSprite.__init__(self, plater_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed

    def update(self):
        self.rect.x += self.speed

        if self.rect.x > win_width+10:
            self.kill()



win_width = 700
win_heigh = 500 
display.set_caption("Лабиринт")
window = display.set_mode((win_width, win_heigh))
back = (119, 210, 223)

mixer.init()
mixer.music.load('music')
mixer.music.play()


barriers = sprite.Group()



bullets = sprite.Group()



monsters = sprite.Group()



w1 = GameSprite('wood.png' win_width / 2 - win_width / 3, win_heigh / 2, 300, 50)
w2 = GameSprite('wood.png', 370, 100, 500, 400)



barriers.add(w1)
barriers.add(w2)



packman = Player('hero.png', 5, win_heigh - 80, 80, 80, 0, 0)
final_sprite = GameSprite('stone.png', win_width - 85, win_heigh - 100, 80, 80)


monster1 = Enemy('wall.png', win_width - 80, 150, 80, 80, 5)
monster2 = Enemy('wall.png', win_width - 80, 230, 80, 80, 5)

monsters.add(monster1)
monsters.add(monster2)



finish = False

run = True
while run:

    time.delay(50)

    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.type == K_LEFT:
                packman.x.speed = -5
            elif e.key == K_RIGHT:
                packman.x_speed = 5
            elif e.key == K_UP:
                packman.y_speed = -5
            elif e.key == K_DOWN:
                packman.y_speed = 5 
            elif e.key == K_SPACE:
                packman.fire()


        elif e.type == KEYUP:
            if e.key == K_LEFT:
                packman.x_speed = 0
            elif e.key == K_RIGHT:
                packman.x_speed = 0 
            elif e.key == K_UP:
                packman.x_speed = 0
            elif e.key == K_DOWN:
                packman.x_speed = 0



    if not finish:

        window.fill(back)


        packman.update()
        bullets.update()



        packman.reset()



        bullets.draw(window)
        barriers.draw(window)
        final_sprite.reset()


        sprite.groupcollide(monsters, bullets, True, True)
        monsters.update()
        monster.draw(window)
        sprite.groupcollide(bullets, barriers, True, False)



        if sprite.spritecollide(packman, monsters, False):
            finish = True

            img = image.load('way_3.png')
            d = img.get_width() // img.get_haight()
            window.fill((255, 255, 255))
            window.blit(transform.scale(img, (win_heigh * d, win_heigh)), (90, 0))


        if spritecollide_rect(packman, final_sprite):
            finish = True
            img = image.load('way_3.png')
            window.fill((255, 255, 255))
            window.blit(transform.scale(img, (win_width, win_heigh)), (0, 0))
    display.update()







 