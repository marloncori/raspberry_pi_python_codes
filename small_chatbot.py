from corpus_class import Corpus
from time import sleep
import random

###### global variables #####
master = " Master Marlon"
data = Corpus()
#############################

def get_user_data():
    print("\033[1;34m\n::::::: Welcome to Simple ChatBot! :::::::\033[0m")
    sleep(1)
    print(" [ ChatBot has entered the room ] ")
    sleep(0.5)
    user_said = str(input("\n  User:  "))
    return user_said

def put_bot_data(sentence, name):
    for user_input in sentence.split():
        if(user_input.lower() in data.get_input()):
            sleep(0.5)
            print("  Chatbot says: \033[1;35m\'{}, {}\'\033[0m".format(random.choice(data.get_greeting()), name))
        #else:
        #    sleep(0.5)
        #    print("  Chatbot says: \033[1;35m\'{}, come again, please!\'\033[0m".format(name))

    user_says = str(input("\n  User:  "))
    return user_says

def put_bot_data_again(sentence, name):
    for user_input in sentence.split():
        if(user_input.lower() in data.get_question()):
            sleep(0.5)
            print("  Chatbot says: \033[1;35m\'{}\'\033[0m".format(random.choice(data.get_answer())))
            break
        else:
            sleep(0.5)
            print("  Chatbot says: \033[1;35m\'{}, come again, please!\'\033[0m".format(name))
            break
    user_said = str(input("\n  User:  "))
    return user_said 

def put_bot_comment(sentence, name):
    for user_input in sentence.split():
        if(user_input.lower() in data.get_answer()):
            sleep(0.5)
            print("  Chatbot says: \033[1;35m\'{}\'\033[0m".format(random.choice(data.get_comment())))
            break
        else:
            sleep(0.5)
            print("  Chatbot says: \033[1;35m\'{}, come again, please!\'\033[0m".format(name))
            break
    print("\033[1;34m\n:::::: End of Simple ChatBot application ::::::\033[0m")
    
if __name__ == '__main__':
    try:
        words = get_user_data()
        query = put_bot_data(words, master)
        answer = put_bot_data_again(query, master)
        put_bot_comment(answer, master)
        
    except KeyboardInterrupt:
        print("\033[1;32m\n   User has stooped the conversation. Bye-bye!\033[0m")