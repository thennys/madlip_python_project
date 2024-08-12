"""Function that gets the inputs  from the user"""
def get_user_input(word_type: str):
    user_input = input(f"{word_type} ?:  ")
    return user_input

name = get_user_input("Enter your prefered name")
prog_lang1 = get_user_input("Enter the programming language you are counfortable to work with")
company1 = get_user_input("Which company do you currently work with")
prog_lang2 =get_user_input("Enter any programming language that you are willing to work with")
company2 = get_user_input("Which company do you want to work with")


story = f"""
My name is {name}, I am very proficient in writing codes {prog_lang1}.I am currently working in my own company {company1}.

I am doing this just to remind myself about the python fundamentals after a long break to study {prog_lang2}.

i want to be part of the full stck community so I decided to take a crash course on {prog_lang2} so that I can gain the skill to compete in

in joining the full stack developers in {company2}
"""

print(story)