# -*- coding: utf-8 -*-

from termcolor import colored

infoStr    = colored('[i]', 'blue')
warningStr = colored('[⚠]', 'yellow')
dangerStr  = colored('[⚠]', 'red')
successStr = colored('[✔]', 'green')

def separator(color, char="="):
    return print(colored(f"{char}" * 70, color))


def initWelcome():
    print(colored('''
 ______     ______     __   __     __  __     __        
/\  == \   /\  __ \   /\ "-.\ \   /\ \_\ \   /\ \       
\ \  __<   \ \  __ \  \ \ \-.  \  \ \____ \  \ \ \____  
 \ \_____\  \ \_\ \_\  \ \_\\\\"\_\  \/\_____\  \ \_____\ 
  \/_____/   \/_/\/_/   \/_/ \/_/   \/_____/   \/_____/ 
                                                         v0.5'''
    , 'magenta'))
    print('Created by: github.com/jesus1554')
    print('Twitter: @jesus_twalter')
    print('\n')
    print('Hey!👋 This is Banyl, an easy-to-use tool to complete all the tags in your music catalog')