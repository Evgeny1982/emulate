import uinput
import time
import random

# Возможные номиналы и масти
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['S', 'H', 'D', 'C']  # Spades, Hearts, Diamonds, Clubs

# Маппинг символов на клавиши
char_map = {
    '2': uinput.KEY_2,
    '3': uinput.KEY_3,
    '4': uinput.KEY_4,
    '5': uinput.KEY_5,
    '6': uinput.KEY_6,
    '7': uinput.KEY_7,
    '8': uinput.KEY_8,
    '9': uinput.KEY_9,
    '0': uinput.KEY_0,
    'J': uinput.KEY_J,
    'Q': uinput.KEY_Q,
    'K': uinput.KEY_K,
    'A': uinput.KEY_A,
    'S': uinput.KEY_S,
    'H': uinput.KEY_H,
    'D': uinput.KEY_D,
    'C': uinput.KEY_C,
}

# Собираем все нужные события клавиш
events = list(set(char_map.values()) | {uinput.KEY_ENTER})

def type_card(device, card_str):
    for ch in card_str:
        key = char_map.get(ch)
        if key:
            device.emit_click(key)
            time.sleep(0.05)
    device.emit_click(uinput.KEY_ENTER)

# Основной цикл
with uinput.Device(events) as device:
    print("🟢 Эмулятор сканера запущен.")
    while True:
        rank = random.choice(ranks)
        suit = random.choice(suits)
        card = f"{rank}{suit}"
        print(f"📤 Отправлена карта: {card}")
        type_card(device, card)
        time.sleep(3)
