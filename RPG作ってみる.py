import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#親オブジェクト
class Character:
  def __init__(self, name, hp):
    self.name = name
    self.hp = hp

  def is_alive(self):
    return self.hp > 0
  
  def take_damage(self, amount):
    self.hp -= amount
    print(f'{self.name} は {amount} ダメージを受けた！ 残りHP: {max(0, self.hp)}')

  def heal(self, amount):
    self.hp += amount
    print(f'{self.name}は{amount}回復した！ 現在のHP: {max(0, self.hp)}')

#子オブジェクト１
class Hero(Character):
  def __init__(self, name, hp):
    super().__init__(name, hp)
    self.level = 1
    self.exp = 0
    self.next_exp = 10 #レベルアップに必要な経験値

  def attack(self, enemy):
    damage = random.randint(5, 15) + self.level #レベル補正あり
    print(f'{self.name}の攻撃！')
    enemy.take_damage(damage)

  def gain_exp(self, amount):
    self.exp += amount
    print(f'{self.name}は{amount}経験値を得た！（現在: {self.exp}/{self.next_exp}）')
    if self.exp >= self.next_exp:
      self.level_up()
  def level_up(self):
    self.level += 1
    self.exp -= self.next_exp
    self.next_exp += 10
    self.hp += 10
    print(f"★レベルアップ！{self.name} は Lv.{self.level} になった！HPが10増えた！")

  def show_status(self):
    print(f"\n🌟【{self.name} ステータス】🌟")
    print(f"レベル: {self.level}")
    print(f"HP: {self.hp}")
    print(f"経験値: {self.exp}/{self.next_exp}")

class Enemy(Character):
  def attack(self, hero):
    damage = random.randint(3, 12)
    print(f'{self.name}の攻撃！')
    hero.take_damage(damage)

#ゲームスタート
hero = Hero("勇者", 50)

# 敵のリストを作る
enemy_list = [
    Enemy("スライム", 30),
    Enemy("ゴブリン", 40),
    Enemy("オーク", 60),
    Enemy("ドラゴン", 100)  # ボス
]

# 最初の敵を設定
enemy = enemy_list.pop(0)

running = True
print(f"\n【{enemy.name}に遭遇した！】")

while running:
  messages = []
  
  clear_screen()  # ★ターンの最初に画面クリア！
  #勇者のターン
  hero.show_status()  # ←ターンごとにステータス表示
  print("\n【Your Turn: コマンドを選択してください】")
  print("[1] 攻撃する")
  print("[2] 回復する")
  print("[3] にげる")
  action = input("> ").strip()
  if action == "1":
    hero.attack(enemy)
    if not enemy.is_alive():
      print(f"{enemy.name}は倒れた")
      hero.gain_exp(10)

      if enemy_list:  # まだ敵が残ってたら次に進む
        enemy = enemy_list.pop(0)
        print(f"\n⚔️ 新しい敵「{enemy.name}」が現れた！")
      else:
        print("\n🎉 全ての敵を倒した！ゲームクリア！🎉")
        break    
  elif action == "2":
    hero.heal(random.randint(3, 15))
  elif action == "3":
    print("勇者は逃げ出した！")
    break
  else:
    print("無効な入力です")
  #敵のターン
  print("\n【Enemy's Turn】")
  action = random.randint(1, 2)
  if action == 1:
    enemy.attack(hero)
  elif action == 2:
    enemy.heal(random.randint(3, 15))
  if not hero.is_alive():
    print(f"{hero.name}は倒れた...")
    print("【ゲームオーバー...】")
    running = False