def roll_call_dwarves(dwarves):
    dwarves.sort(key=len)
    i = 0
    for i, dwarf in enumerate(dwarves):
        print(f"{i+1}. {dwarf}")

def summon_captain_planet(p_calls):
    formatted_calls = []
    for p_call in p_calls:
        p_call_title = p_call.title()
        formatted_calls.append(f"{p_call_title}!")
    return(formatted_calls)

def long_planeteer_calls(l_calls):
    return any(len(l_call) > 4 for l_call in l_calls)

def find_the_cheese(snacks):
    cheeses = ["cheddar", "gouda", "camembert"]
    for cheese in cheeses:
        if cheese in snacks:
            return cheese
        else:
            return None
