# inputs: forces, distances, distances of reactive forces
def inputs():
    force = int(input('Input force in Kg: ')) * 10
    ratio = input(
        'Input two numbers to represent ratio of distance to support: ').split(', ')
    ratio = [int(x) for x in ratio]

    reaction = calculate_reaction_force_pa(force, ratio)

    print("The reaction force in point A was: " +
          str(calculate_reaction_force_pa(force, ratio)) + ' Newtons')
    print("The reaction force in point B was: ",
          str(calculate_reaction_force_pb(force, ratio)) + ' Newtons')

    end_or_repeat()


def calculate_reaction_force_pb(force, ratio):
    # calculating force at point A left of force applied, taking clockwise action to be positive
    rfpb = (force * ratio[0]) / (ratio[1]+ratio[0])
    return rfpb


def calculate_reaction_force_pa(force, ratio):
    # set the force applied in the centre of the beam for simplicity
    rfpb = calculate_reaction_force_pb(force, ratio)

    rfpa = force - rfpb
    return rfpa


def end_or_repeat():
    v = input('Do you want to try again y/n? ')
    if v == 'Y' or v == 'y':
        inputs()
    else:
        exit()


inputs()
