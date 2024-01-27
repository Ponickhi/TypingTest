import curses
from curses import wrapper 
import time
import phraseRandom as rand

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the typing test")
    stdscr.addstr("\npress ENTER to play typing test or press ESC to exit programm anytime")
    stdscr.refresh()
    key = stdscr.getch()

    y = 1
    directory = ""
    
    while True:
        if key == 10:
            stdscr.clear()
            stdscr.addstr("Choose your language and press ENTER to start:")
            stdscr.addstr(y, 0, "      ", curses.color_pair(4))
            stdscr.addstr(1, 6, "English")
            stdscr.addstr(2, 6, "Українська")
            stdscr.addstr(3, 6, "Deutsch")
            stdscr.addstr(4, 6, "Italian")
            stdscr.refresh()

            lang_choice = stdscr.getch()
            
            if lang_choice == 259:
                y -= 1
            elif lang_choice == 258:
                y += 1
            elif lang_choice == 10:
                if y == 1:
                    directory = rand.eng_text()
                    stdscr.clear()
                    stdscr.addstr("You choose eng, press any key to start (except ESC)")
                    stdscr.refresh()
                    stdscr.getkey()
                elif y == 2:
                    directory = rand.ukr_text()
                    stdscr.clear()
                    stdscr.addstr("Ви вибрали укр, нажміть будь яку клавішу (окрім ESC)")
                    stdscr.refresh()
                    stdscr.getkey()
                elif y == 3:
                    directory = rand.ger_text()
                    stdscr.clear()
                    stdscr.addstr("You choose deu, press any key to start (except ESC)")
                    stdscr.refresh()
                    stdscr.getkey()
                elif y == 4:
                    directory = rand.ital_text()
                    stdscr.clear()
                    stdscr.addstr("You choose ital, press any key to start (except ESC)")
                    stdscr.refresh()
                    stdscr.getkey()
                return y, directory
            elif lang_choice == 27:
                break
            else:
                continue

            if y < 1:
                y = 4
            elif y > 4:
                y = 1
        elif key == 27:
            quit()
        else:
            stdscr.clear()
            stdscr.addstr("Please press ENTER or press ESC to exit programm anytime")
            stdscr.refresh()
            key = stdscr.getch()
            continue


def display_text(stdscr, target, current, wpm=0, errors=0):
    stdscr.addstr(target)
    stdscr.addstr(1, 0, f"WPM: {wpm}")
    stdscr.addstr(2, 0, f"Errors: {errors}")

    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)
        if char != correct_char:
            color = curses.color_pair(2)
        stdscr.addstr(0, i, char, color)


def errors_count(stdscr, target, current):
    errors = 0

    for i, char in enumerate(current):
        correct_char = target[i]
        if char != correct_char:
            errors += 1

    return errors

def wpm_test(stdscr, directory, y):
    target_text = directory
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)


    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)

        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm, errors_count(stdscr, target_text, current_text))
        stdscr.refresh()

        compar_text = "".join(current_text)

        if len(compar_text) == len(target_text):
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.get_wch()
            if key == '\x00':
                if y in (1, 3, 4):
                    current_text.append("]")
                elif y == 2:
                    current_text.append("ї")
                continue
            elif key == 530:
                if y in (1, 3, 4):
                  current_text.append("'") 
                elif y == 2:
                    current_text.append("є") 
                continue
        except:
            continue
        
        if ord(key) == 27:
            quit()

        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)



def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_WHITE)

    while True:
        y, directory = start_screen(stdscr)
        wpm_test(stdscr, directory, y)
        stdscr.addstr(3, 0, f"You completed the test")
        stdscr.addstr(4, 0, "Press enter to try again")
        key1 = stdscr.getkey()
        rand.text.clear()

        if ord(key1) == 27:
            break
        else:
            continue


wrapper(main)



#По закінченюю вводу тексту зробити тільки прийом enter, а не будь якої клавіші. Зробити рандомний генератор "речень" з рандомних слів 
