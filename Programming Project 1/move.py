'''
Fabian Campos
CSC 110 
Programming Project 1 
This program recreates the Mad Libs game.
'''

def create_story(person_one, street_name, person_two, object_name, 
                 vehicle, adjective):
    '''
    This function prints a mad libs story using 6 arguments.
    Args:
        person_one: The name of the first person in the story.
        street_name: The name of the street in the story.
        person_two: The name of the second person in the story.
        object_name: The object in the story.
        vehicle: The vehicle in the story.
        adjective: An adjective describing the vehicle.
    Returns:
        Prints the Mad Libs story to the console.
    '''

    # print statement

    story = (
        person_one + 
        " decided to move from their apartment on 5th\nto a condo on " + 
        street_name + "." + " They called their friend " + person_two + 
        "\nfor help. However, they could not fit " + object_name + 
        " into\nthe moving truck, so they had to rent a " + adjective + 
        " " + vehicle + "\nin order to move it!"
    )

    return story


















































