import random

hands = ["グー", "チョキ", "パー"]
points = 0

print("じゃんけんゲーム！")
running = True
while running:
    
    player = input("出す手を選んでね（グー / チョキ / パー）: ")
    

    if player not in hands:
        print("無効な入力です")
    else:
        computer = random.choice(hands)
        print(f"コンピューターの手: {computer}")

        if player == computer:
            print("あいこ！")
        elif (player == "グー" and computer == "チョキ") or \
             (player == "チョキ" and computer == "パー") or \
             (player == "パー" and computer == "グー"):
            print("あなたの勝ち！")
            points += 1
        else:
            print("あなたの負け！")
            points -= 1
        
       
        print(f"現在のポイント: {points}")
        
        if points >= 2:
            print("ゲーム終了！あなたの勝ち")
            running = False
        elif points <= -2:
            print("ゲーム終了！あなたの負け")
            running = False

        stop = input("続ける？（Yes > enter, No > write no）: ")
        if stop == "no":
            print("ゲームを終了します")
            break