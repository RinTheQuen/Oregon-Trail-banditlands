import sys
import pygame
import random

player_hp = 100
enemy_hp = 50
encounter_chance = 0.1
wagon_img = pygame.image.load("wagon.png")
wagon_rect = wagon_img.get_rect()
battle_text = pygame.image.load("battletext.png")
pygame.init()
pygame.display.set_caption("Oregon Trail RPG")
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
speed = 1
in_battle = False
movement_distance = 0


def player_battle():
  global player_hp, enemy_hp
  player_hp = 100
  enemy_hp = 50


def battle_screen():
  global in_battle
  in_battle = True
  screen.blit(battle_text, (0, 0))
  wagon_img = pygame.transform.scale(battle_text, (30, 30))
  pygame.display.flip()
  pygame.display.update()
  print("Entering Battle Mode...")
  while in_battle:
    user_input = input("Choose an action: attack, flee, defend\n")
    if user_input == "attack":
      attack()
      check_battle_end()
    elif user_input == "flee":
      flee()
    elif user_input == "defend":
      defend()
    else:
      print("Invalid action. Choose again.")


def attack():
  global player_hp, enemy_hp
  player_dmg = random.randint(5, 15)
  enemy_dmg = random.randint(3, 10)
  enemy_hp -= player_dmg
  player_hp -= enemy_dmg
  print(f"Player attacks for {player_dmg} damage. Enemy HP: {enemy_hp}")
  print(f"Enemy attacks for {enemy_dmg} damage. Player HP: {player_hp}")


def flee():
  global in_battle
  global movement_distance
  in_battle = False
  movement_distance = 0
  print("Fleeing from battle...")


def defend():
  global player_hp
  player_hp += random.randint(0, 0)
  enemy_dmg = random.randint(1, 6)
  player_hp -= enemy_dmg
  print(f"Player defends and restores health. Player HP: {player_hp}")
  print(f"Enemy attacks for {enemy_dmg} damage. Player HP: {player_hp}")

def check_battle_end():
  global in_battle
  global movement_distance
  if player_hp <= 0:
    print("You were defeated. Game over.")
    in_battle = False
  elif enemy_hp <= 0:
    print("You defeated the enemy. Victory!")
    in_battle = False
    movement_distance = 0
    screen.blit(battle_text, (0, 0))
    wagon_img = pygame.transform.scale(battle_text, (0, 0))
    pygame.display.flip()
    pygame.display.update()
    


while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT] and wagon_rect.left > 0:
    wagon_rect.x -= speed
    movement_distance += speed
  if keys[pygame.K_RIGHT] and wagon_rect.right < 800:
    wagon_rect.x += speed
    movement_distance += speed
  if keys[pygame.K_UP] and wagon_rect.top > 0:
    wagon_rect.y -= speed
    movement_distance += speed
  if keys[pygame.K_DOWN] and wagon_rect.bottom < 570:
    wagon_rect.y += speed
    movement_distance += speed
  if movement_distance >= 300 and not in_battle:
    enemy_hp = random.randint(30, 70)
    print("Random encounter: Bandit appeared!")
    battle_screen()

  screen.fill((0, 0, 0))
  pygame.draw.rect(screen, (0, 0, 0), (0, 0, 800, 600),
                   3)  # Drawing a white border around the screen
  screen.blit(wagon_img, wagon_rect)
  wagon_img = pygame.transform.scale(wagon_img, (30, 30))
  pygame.display.flip()
  pygame.display.update()
  clock.tick(60)
