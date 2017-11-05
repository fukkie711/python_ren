animal_list = [
        ("ライオン", 58),
        ("チーター", 110),
        ("シマウマ", 60),
        ("トナカイ", 80),
        ]

faster_list = sorted(
        animal_list,
        key = lambda ani : ani[1],
        reverse = True)

for i in faster_list: print(i)
