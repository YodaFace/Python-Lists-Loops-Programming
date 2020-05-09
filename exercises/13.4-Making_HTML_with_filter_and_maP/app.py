all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

#Your code go here:

def filter_colors():
    ## THIS DIDN'T WORK AND WAS GIVEN BY ALEX
    # if sexy_colors[0]["sexy"] == True:
    # if all_colors[i]["sexy"] == True:
    ## THIS WORKS AND MAKES MORE SENSE.
    filtered_colors = []
    for color in all_colors: 
        if color["sexy"] == True:
            # do something
            filtered_colors.append(color)
    return filtered_colors


def generate_li():
    just_colors = []
    for color in all_colors:
        
        print(color) 
        # just_colors.append(color) 
        # return filtered_colors




print(filter_colors())

generate_li()