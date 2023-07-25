def badge_maker(name):
    return f"Hello, my name is {name}."


def batch_badge_creator(names):
    return [f"Hello, my name is {name}." for name in names]

def assign_rooms(names):
    return [f"Hello, {name}! You'll be assigned to room {idName+1}!" for idName, name in enumerate(names)]
    return None

def printer(names):
    list = [*batch_badge_creator(names), *assign_rooms(names)]
    for message in list:
        print(message)
