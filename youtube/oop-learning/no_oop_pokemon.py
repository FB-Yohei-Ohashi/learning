# オブジェクト指向なしで自力で実装

def appearance(my_pokemon, enemy_pokemon):
    print(
        f"{my_pokemon["name"]}があらわれた。{my_pokemon["name"]}のHPは{my_pokemon["hp"]}だ。"
    )
    print(
        f"{enemy_pokemon["name"]}があらわれた。{enemy_pokemon["name"]}のHPは{enemy_pokemon["hp"]}だ。"
    )


def attack(atk_pokemon, def_pokemon):
    if def_pokemon["hp"] - atk_pokemon["atk"][0][1] > 0:
        def_pokemon["hp"] -= atk_pokemon["atk"][0][1]
    else:
        def_pokemon["hp"] = 0

    print(
        f"{atk_pokemon["name"]}のこうげき！{atk_pokemon["atk"][0][0]}！{def_pokemon["name"]}は{atk_pokemon["atk"][0][1]}ダメージをもらった。{def_pokemon["name"]}のHPは{def_pokemon["hp"]}だ。"
    )
    return def_pokemon["hp"]


def check_fainted(hp):
    if hp <= 0:
        return True
    else:
        return False


def main():
    my_pokemon = {"name": "ピカチュウ", "hp": 20, "atk": [["10万ボルト", 10]]}
    enemy_pokemon = {"name": "ヒトカゲ", "hp": 18, "atk": [["ひのこ", 5]]}

    appearance(my_pokemon, enemy_pokemon)

    while True:
        enemy_hp = attack(my_pokemon, enemy_pokemon)
        if check_fainted(enemy_hp):
            print(f"{enemy_pokemon["name"]}はたおれた。{my_pokemon["name"]}のかち！")
            break

        my_hp = attack(enemy_pokemon, my_pokemon)
        if check_fainted(my_hp):
            print(f"{my_pokemon["name"]}はたおれた。{enemy_pokemon["name"]}のかち！")
            break


if __name__ in "__main__":
    main()
