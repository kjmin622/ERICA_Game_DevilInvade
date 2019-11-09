import GUI_main
import GUI_game

action = GUI_main.main()

while action != 0 :
    
    if action == 1 :
        done = GUI_game.play_game()



    if(done):
        break
    action = GUI_main.main()
    
