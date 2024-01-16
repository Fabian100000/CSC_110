'''
Fabian Campos 
CSC 110
Programming Project 1 
This program recreates the Mad Libs game.
'''

def create_story(person_one, person_two, pet_name, animal, place, 
                 adjective, verb, adverb):
    '''
    This function prints a Mad Libs narrative using 8 arguments.
    Args:
        person_one: The name of the first person in the story.
        person_two: The name of the second person in the story.
        pet_name: The name of the pet in the story.
        animal: The animal in the story.
        place: The name of the place in the story.
        adjective: An adjective used to describe the pet in the story.
        verb: A verb describing the action the pet performed in the story.
        adverb: An adverb modifying the verb "went"
    Returns:
        Prints the Mad Libs story to the console.
    '''

    # print statement

    story = (
        person_one + " and " + person_two + " were best friends.\nOne day " + 
        person_one + " and " + person_two + 
        " decided to go on a\nvacation to " + place + 
        ". However, they didn't know\nwhat to do with their " + 
        adjective + " pet " + animal + " named " + pet_name + ".\n" + 
        pet_name + " had been causing problems, due to constant " + 
        verb + "ing.\n" + person_one + 
        " found a sitter for their pet, and " + adverb + " went on the trip."
    )

    return story












    





















