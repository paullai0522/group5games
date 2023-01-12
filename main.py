def on_a_pressed():
    if mySprite.is_hitting_tile(CollisionDirection.BOTTOM):
        mySprite.vy = -130
        scene.camera_shake(3, 500)
        music.jump_up.play()
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    info.change_life_by(-1)
    scene.set_background_image(assets.image("""
        我的影像28
    """))
sprites.on_overlap(SpriteKind.player, SpriteKind.projectile, on_on_overlap)

mySprite: Sprite = None
scene.set_background_color(1)
mySprite = sprites.create(assets.image("""
    我的影像2
"""), SpriteKind.player)
mySprite2 = sprites.create(assets.image("""
    我的影像10
"""), SpriteKind.projectile)
mySprite3 = sprites.create(assets.image("""
    我的影像10
"""), SpriteKind.projectile)
mySprite4 = sprites.create(assets.image("""
    我的影像12
"""), SpriteKind.projectile)
mySprite5 = sprites.create(assets.image("""
    我的影像12
"""), SpriteKind.projectile)
mySprite10 = sprites.create(assets.image("""
    我的影像12
"""), SpriteKind.projectile)
mySprite6 = sprites.create(assets.image("""
    我的影像10
"""), SpriteKind.projectile)
mySprite7 = sprites.create(assets.image("""
    我的影像12
"""), SpriteKind.projectile)
mySprite9 = sprites.create(assets.image("""
    我的影像10
"""), SpriteKind.projectile)
mySprite8 = sprites.create(assets.image("""
    我的影像12
"""), SpriteKind.projectile)
mysprite11 = sprites.create(assets.image("""
    我的影像10
"""), SpriteKind.projectile)
myspite12 = sprites.create(assets.image("""
    我的影像10
"""), SpriteKind.projectile)
mysprite13 = sprites.create(assets.image("""
    我的影像12
"""), SpriteKind.projectile)
mysprite14 = sprites.create(assets.image("""
    我的影像10
"""), SpriteKind.projectile)
mysprite15 = sprites.create(assets.image("""
    我的影像12
"""), SpriteKind.projectile)
mysprite17 = sprites.create(assets.image("""
    我的影像10
"""), SpriteKind.projectile)
mySprite16 = sprites.create(assets.image("""
    我的影像12
"""), SpriteKind.projectile)
mysprite18 = sprites.create(assets.image("""
    我的影像10
"""), SpriteKind.projectile)
mysprite19 = sprites.create(assets.image("""
    我的影像12
"""), SpriteKind.projectile)
mysprite20 = sprites.create(assets.image("""
    我的影像10
"""), SpriteKind.projectile)
mysprite21 = sprites.create(assets.image("""
    我的影像10
"""), SpriteKind.projectile)
mysprite22 = sprites.create(assets.image("""
    我的影像12
"""), SpriteKind.projectile)
mysprite23 = sprites.create(assets.image("""
    我的影像10
"""), SpriteKind.projectile)
mysprite24 = sprites.create(assets.image("""
    我的影像12
"""), SpriteKind.projectile)
mysprite25 = sprites.create(assets.image("""
    我的影像10
"""), SpriteKind.projectile)
scene.camera_follow_sprite(mySprite)
mysprite11.set_position(100, 121)
mySprite.set_position(10, 105)
mySprite2.set_position(1000, 121)
mySprite3.set_position(800, 121)
mySprite4.set_position(1100, 121)
mySprite5.set_position(1525, 121)
mySprite6.set_position(2000, 121)
mySprite7.set_position(900, 121)
mySprite8.set_position(500, 121)
mySprite9.set_position(400, 121)
mySprite10.set_position(300, 121)
mysprite11.set_position(100, 121)
myspite12.set_position(200, 121)
mysprite13.set_position(600, 121)
mysprite14.set_position(700, 121)
mysprite15.set_position(1200, 121)
mySprite16.set_position(1300, 121)
mysprite17.set_position(1400, 121)
mysprite18.set_position(1632, 121)
mysprite19.set_position(1740, 121)
mysprite20.set_position(1851, 121)
mysprite21.set_position(1960, 121)
mysprite22.set_position(2074, 121)
mysprite23.set_position(2228, 121)
mysprite24.set_position(2348, 121)
mysprite25.set_position(2479, 121)
mySprite.ax = 2
mySprite.ay = 200
mySprite.set_velocity(25, 0)
tiles.set_current_tilemap(tilemap("""
    層級2
"""))
info.set_life(1)

def on_on_update():
    if mySprite.is_hitting_tile(CollisionDirection.RIGHT):
        scene.set_background_image(assets.image("""
            我的影像27
        """))
        game.over(True, effects.confetti)
game.on_update(on_on_update)
