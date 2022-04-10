import sys

# there are 68 periods along the top and bottom of this string

bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
....................................................................

"""

def adorn():
    print("=" * 75)
    print("\t    B I T M A P   M E S S A G E")
    print("=" * 75)
    
def get_word():
    adorn()
    print("\n\t Please enter the message to be displayed as a bitmap message.")
    print("\t >>> msg: ", end="")
    msg = input()
    if msg == "":
        sys.exit()
    return msg

def bitmap_message(msg):
    # loop over each line in the bitmap
    for line in bitmap.splitlines():
        # loop over each character
        for i, bit in enumerate(line):
            if bit == " ":
                #print an empty space since there is a blank space in bitmap
                print(" ", end="")
            else:
                # print a character from message the user has entered
                print(msg[i % len(msg)], end="")
        print("\n")
    adorn()

def run():
    msg = get_word()
    bitmap_message(msg)


if __name__ == '__main__':
    run()