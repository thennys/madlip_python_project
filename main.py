"""Function that gets the inputs  from the user"""
def get_user_input(word_type: str):
    user_input = input(f"{word_type} ?:  ")
    return user_input

prog_lang1 = get_user_input("Enter the programming language you are counfortable to work with")
company1 = get_user_input("Which company do you currently work with")
prog_lang2 =get_user_input("Enter any programming language that you are willing to work with")
company2 = get_user_input("Which company do you want to work with")