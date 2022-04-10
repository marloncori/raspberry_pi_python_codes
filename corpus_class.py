
class Corpus():
    def __init__(self):
        self.user_inputs = ["chatbot", "chatbot.", "chatbot!", "hi", "hi!", "hello", "hello!", "good", "morning", "morning!", "good morning", "good morning!", "hey", "hey!"]
        self.user_questions = ["how", "how\'s", "are", "you", "everything", "how are you", "you?", "how\'s everthing", "what\'s up", "how are you doing"]
        self.possible_greetings = ["Hi, there", "Hello", "Hey, what\'s up?", "Good morning", "welcome here"]
        self.possible_answers = ["i\'m", "I\'m", "fine", "fine,", "nice", "nice,", "great", "great,", "everything", "everything,", "alright", "alright,", "thanks", "thanks.", "thanks!", "I\'m fine. What about you?", "Everything is okay. What about you?", "Alright. What about you?", "Nice, what about you?", "I\'m doing great, thanks. What about you?", "I\'m fine, thanks. What about you?"]
        self.user_reactions = ["I\'m fine, thanks.", "Everything is okay, thanks for asking", "I\'m nice, thank you", "I\'m doing great, thanks", "Everything is alright, thanks"]
        self.possible_comments = ["Great!", "Superb!", "I\'m glad to here that.", "It\'s good you\'re feeling like that.", "Awesome!", "Wonderfull!"] 
    
    def get_input(self):
        return self.user_inputs
    
    def get_question(self):
        return self.user_questions

    def get_greeting(self):
        return self.possible_greetings

    def get_answer(self):
        return self.possible_answers
    
    def get_reaction(self):
        return self.user_rections
    
    def get_comment(self):
        return self.possible_comments
    