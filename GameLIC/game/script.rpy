define y = Character("You", color="#ff65e5")
define l = Character("Luca", color="#1228cb")
define a = Character("Achille", color="#fe2916")
define e = Character("Elio", color="#1ac260")

label start:
    scene room
    play music "calm.mp3" volume 0.5

    $ luca = 0
    $ achille = 0
    $ elio = 0

    "You are waking up, it's 7am."
    y "Aaah~ What a good day to be alive, the first day of school !
    I can't wait to meet new friends !!"

label dress :
    scene dressing
    y "I should really dress up for this occasion..."
    menu :
        y "I wonder what am I going to wear"
        "My favorite cute goth outfit !":
            $ luca += 1
        "I'll keep it simple and put a sweatshirt and some jeans":
            $ achille += 1
        "I want to wear a nice dress":
            $ elio += 1
        "Ew, What is that...":
            jump deathFromCoat

label deathFromCoat : 
    
    
