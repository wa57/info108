#Project Name: BlastOff Game
#Date: 4/28/16
#Programmer Name: Will Ashman
#Project Description: A recursive drawing of a NASA launch

#Gathers number to be counted down from and initiates recursion
def main():
    countDownFrom = int(input("Countdown From: "))
    countDown(countDownFrom)
    input('Press Enter to continue...')

def countDown(n):
    #WA - Checks if the number argument is greater than 0, if it is, it prints the current countdown step
    #     as well as the layer of ASCII art associated with that step, the function then calls itself and passes n - 1 as an argument
    if(n >= 0):
        print(n, rescursiveDrawing(n))
        countDown(n-1)
    else:
        print('And liftoff of the INFO 108 mission to knowledge!')

#WA - ASCII Spaceship Art Retrieved from http://textart.io/art/9p8gZx6lM_CRjh2k5e6jgweF
#WA - ASCII Clouds and Sun Art Retrieved from http://www.chris.com/ascii/joan/www.geocities.com/SoHo/7373/nature.html
#WA - ASCII Stars Retrieved from http://www.ascii-code.com/ascii-art/space/stars.php
#WA - Uses conditional statements to draw a NASA spaceship leaving Earth's atmosphere based on countdown position
def rescursiveDrawing(n):
    if n > 99:
        return " "

    #WA - Begin Space art section
    if n == 99:
        return ' '
    if n == 98:
        return "                 '"
    if n == 97:
        return "            *          ."
    if n == 96:
        return "                   *       '"
    if n == 95:
        return "              *                *"
    if 89 < n <= 94:
        return " "
    if n == 89:
        return "   *   '*"
    if n == 88:
        return "           *"
    if n == 87:
        return "           *"
    if n == 86:
        return "                *"
    if n == 85:
        return "                       *"
    if n == 84:
        return "               *"
    if n == 83:
        return "                     *"
    if 78 < n < 83:
        return " "

    #WA - Earth's atmosphere section
    if n == 78:
        return "               _  _"
    if n == 77:
        return "              ( `   )_"
    if n == 76:
        return "             (    )    `)"
    if n == 75:
        return "           (_   (_ .  _) _)"
    if n == 74:
        return " "
    if n == 73:
        return "                                          _"
    if n == 72:
        return "                                         (  )"
    if n == 71:
        return "          _ .                         ( `  ) . )"
    if n == 70:
        return "        (  _ )_                      (_, _(  ,_)_)"
    if n == 69:
        return "      (_  _(_ ,)"
    if n == 68:
        return "                                                             |"
    if n == 67:
        return "               _  _                                        \ _ /"
    if n == 66:
        return "              ( `   )_                                   -= (_) =-"
    if n == 65:
        return "             (    )    `)                                  /   \\"
    if n == 64:
        return "           (_   (_ .  _) _)                                  |"

    #WA - Empty space filler
    if 50 < n <= 63:
        return ""

    #WA - Spaceship Section
    if n == 50:
        return "         /\\"
    if n == 49:
        return "        |==|"
    if n == 48:
        return "        |  |"
    if n == 47:
        return "        |  |"
    if n == 46:
        return "        |  |"
    if n == 45:
        return "       /____\\"
    if 40 <= n <= 44:
        return "       |    |"

    #WA - Main spaceship body with NASA print
    if n == 39:
        return "       |  N |"
    if n == 38:
        return "       |    |"
    if n == 37:
        return "       |  A |"
    if n == 36:
        return "       |    |"
    if n == 35:
        return "       |  S |"
    if n == 34:
        return "       |    |"
    if n == 33:
        return "       |  A |"
    if 20 <= n <= 32:
        return "       |    |"

    #WA - Tail of spacecraft
    if n == 19:
        return "      /| |  |\\"
    if n == 18:
        return "     / | |  | \\"
    if n == 17:
        return "    /__|_|__|__\\"
    if n == 16:
        return "       /_\/_\\"
    if n == 15:
        return "       ######"
    if n == 14:
        return "      ########"
    if n == 13:
        return "       ######"
    if n == 12:
        return "        ####"
    if n == 11:
        return "        ####"
    if n == 10:
        return "         ##"

    #WA - Trailing smoke/engine flame with extra space due to absent tenths place
    if 5 < n < 10:
        return "          ##"
    if n <= 5:
        return "          #"

main()
