import random
from Color import Colors
import os
import time
from character import *


while (True):
    print("="*80)
    print("\n" + Colors.YELLOW+"welcome to" +
          Colors.GREEN+" 미니게임 !!! \n" + Colors.RESET)
    print("="*80)
    time.sleep(2)
    os.system("clear")

    print("="*80)
    print("")
    character = input(f"{Colors.YELLOW}캐릭터를 생성해 주세요{Colors.RESET} : ")
    print("")

    while (True):
        occupation = input(
            f"{Colors.CYAN}직업 선택 (전사  궁수  마법사){Colors.RESET} : ")
        if occupation == "궁수" or occupation == "전사" or occupation == "마법사":
            break
        else:
            print("선택하진 직업은 존재하지 않습니다. 다시 선택해 주세요 \n")

    if occupation == "전사":
        user = Player(character, 200, 14, occupation, 1, 0, 100)
    elif occupation == "궁수":
        user = Player(character, 160, 18, occupation, 1, 0, 100)
    elif occupation == "마법사":
        user = Player(character, 120, 22, occupation, 1, 0, 100)

    print("")
    monster_name = input(
        f"{Colors.BRIGHT_RED}몬스터 이름을 지정해 주세요{Colors.RESET} : ")
    monster = Monster(monster_name, hp = random.randrange(250, 300), power = random.randrange(12, 16), lavel = 1, alive="True", monster_death_exp = random.randrange(25, 75))
    print("")
    print("="*80)
    time.sleep(2)

    print("")
    print(f"{Colors.BRIGHT_YELLOW}{user.name}{Colors.RESET}의 {Colors.RED}hp{Colors.RESET}는 {Colors.RED}{user.max_hp}{Colors.RESET} 입니다")
    print(f"{Colors.YELLOW}{user.name}{Colors.RESET}의 {Colors.BLUE}mp{Colors.RESET}는 {Colors.BLUE}{user.max_mp}{Colors.RESET} 입니다")
    print(f"{Colors.YELLOW}{user.name}{Colors.RESET}의 {Colors.MAGENTA}power{Colors.RESET}는 {Colors.MAGENTA}{user.power}{Colors.RESET} 입니다")
    print("")
    print(f"{Colors.BRIGHT_RED}{monster.name}{Colors.RESET}의 {Colors.RED}hp{Colors.RESET}는 {Colors.RED}{monster.max_hp}{Colors.RESET} 입니다")
    print(f"{Colors.BRIGHT_RED}{monster.name}{Colors.RESET}의 {Colors.MAGENTA}power{Colors.RESET}는 {Colors.MAGENTA}{monster.power}{Colors.RESET} 입니다")
    print("")
    print("="*80)

    while (True):
        user.skill()
        if monster.alive == True:
            if user.defense_success == True:
                print(
                    f"{Colors.YELLOW}{user.name}{Colors.RESET}의 방어 성공! 추가로 hp와 mp가 회복됩니다")
                monster.show_status()
            else:
                user.attack(monster)
                monster.show_status()
        if user.alive == True:
            if user.defense_success == True:
                print(f"{Colors.BRIGHT_RED}{monster.name}{Colors.RESET}의 공격이 막혔습니다!")
                user.show_status()
                user.defense_success = False
            else:
                monster.attack(user)
                user.show_status()
        print("="*80)
        if monster.alive == False:
            print(f'{Colors.RED}You Died ...{Colors.RESET}')
            print(
                f"현재 {Colors.BRIGHT_YELLOW}{user.gold}gold{Colors.RESET}를 가지고 있습니다")
            print("="*80)
            break
        elif user.alive == False:
            print(f'{Colors.YELLOW}축하합니다 당신은 몬스터를 쓰려트렸습니다 !{Colors.RESET}')
            print(
                f"현재 {Colors.BRIGHT_YELLOW}{user.gold}gold{Colors.RESET}를 가지고 있습니다 \n")
            print(
                f"{Colors.YELLOW}{user.name}{Colors.RESET}의 {Colors.RED}남은 hp는 {user.hp}{Colors.RESET} 입니다")
            print(
                f"{Colors.YELLOW}{user.name}{Colors.RESET}의 {Colors.BLUE}남은 mp는 {user.mp}{Colors.RESET} 입니다")
            print("="*80)
            break

    end = input("재시작 하시겠습니까? (Y/N or Press any key) : ")
    print("="*80)
    if end == "Y" or end == "y":
        continue
    else:
        break
