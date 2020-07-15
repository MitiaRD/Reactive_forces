# inputs: forces, distances, distances of reactive forces
def inputs():
    # user inputs force in KG which is transformed into Newtons
    force = int(input('Input force in Kg: ')) * 10
    # user inputs a ratio (input as 2 digits separated by a coma: e.g 2, 1) to evaluate where the force is placed on the beam relative to the contact points
    ratio = input(
        'Input two numbers to represent ratio of distance to support: ').split(', ')
    ratio = [int(x) for x in ratio]
    
    reaction_b = calculate_reaction_force_pb(force, ratio)
    reaction_a = calculate_reaction_force_pa(force, reaction_b)

    print("The reaction force in point A was: " +
          str(reaction_a) + ' Newtons')
    print("The reaction force in point B was: ",
          str(reaction_b) + ' Newtons')
    end_or_repeat()


def calculate_reaction_force_pb(force, ratio):
    # calculating force at point A left of force applied, taking clockwise moment to be positive
    reaction_b = (force * ratio[0]) / (ratio[1]+ratio[0])
    return reaction_b


def calculate_reaction_force_pa(force, reaction_b):
    # set the force applied in the centre of the beam for simplicity
    reaction_a = force - reaction_b
    return reaction_a


def end_or_repeat():
    # user decides to repeat or end program
    v = input('Do you want to try again y/n? ')
    if v == 'Y' or v == 'y':
        inputs()
    else:
        exit()


inputs()
