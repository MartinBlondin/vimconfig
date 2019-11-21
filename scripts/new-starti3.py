import i3
import os
import subprocess
from time import sleep
import pyautogui as pag

workspace = {1:  "",
             2:  "",
             3:  "",
             4:  "",
             5:  "",
             6:  "",
             7:  "",
             8:  "",
             9:  "",
             10: ""}
programs = []

def start_program(command, workspace, extra_commands=[]):
    if isinstance(command, str): command = [command]
    programs.append({'process':        subprocess.Popen(command),
                     'workspace':      workspace,
                     'extra_commands': extra_commands})

for i in range(4): start_program('termite', workspace[1])
start_program('termite', workspace[4], ['clear && cowsay -f tux -p "Dont be a dick." | lolcat'])
start_program('termite', workspace[4])
start_program('qutebrowser', workspace[2])
start_program('emacs', workspace[3])
start_program('termite', workspace[5], ['r'])

if os.path.isfile('local_commands_before_startup.py'): subprocess.call(['python3', 'local_commands_before_startup.py'])

for program in programs:
    moved = False
    wids = []
    index = 0
    while not moved:
        try:
            wids = subprocess.check_output(['xdotool', 'search', '--pid', str(program['process'].pid)]).decode('utf-8').split('\n')[:-1]
            index += 1;
            if index == len(wids): index = 0
            try: subprocess.check_output(['i3-msg', f'[id={wids[index]}] move container to workspace {program["workspace"]}'])
            except: continue
            else: moved = True
        except: sleep(0.01)
    for command in program['extra_commands']:
        i3.workspace(str(program['workspace']))
        pag.typewrite(command, 0)
        pag.press('enter')
        sleep(0.02)

i3.workspace(workspace[1])
subprocess.call(['i3-msg', 'move down'])
subprocess.call(['i3-msg', 'focus up'])
subprocess.call(['i3-msg', 'move right'])
subprocess.call(['i3-msg', 'move right'])
pag.typewrite('archey3'); pag.press('enter')
subprocess.call(['i3-msg', 'focus left'])
subprocess.call(['i3-msg', 'move up'])
subprocess.call(['i3-msg', 'move up'])
subprocess.call(['i3-msg', 'resize grow height 20px or 20ppt'])
pag.typewrite('glances'); pag.press('enter')
i3.workspace(workspace[4])
subprocess.call(['i3-msg', 'resize shrink width 30px or 30ppt'])
i3.workspace(workspace[2])

subprocess.call(['setxkbmap', '-option', 'caps:escape'])
subprocess.call(['setxkbmap', '-layout', 'us'])

if os.path.isfile('local_commands_after_startup.py'): subprocess.call(['python3', 'local_commands_after_startup.py'])

for program in programs:
    program['process'].wait()
