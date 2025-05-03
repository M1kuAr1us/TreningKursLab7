import keyboard

print("Press the keys (press Backspace to exit): ")

while True:
    key = keyboard.read_event()
    if key.event_type == keyboard.KEY_DOWN:
        print(f"Pressed: {key.name}")

        if key.name == 'backspace':
            print("Exit...")
            break
