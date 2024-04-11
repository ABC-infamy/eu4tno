import os
import csv 

def write_mission(name,x,y,icon_name, tag,required_mission):
    if (required_mission == "none"):
        required_mission = ""
    x = int(x)
    y = int(y)
    directory = os.path.dirname(os.path.realpath(__file__))
    files = os.listdir(directory)
    for file in files:
        if file[0:-4] == tag:
            file_path = (file[0:-4] + ".txt")
            content = f"""
                {name} = {{
                    icon = {icon_name}
                    slot = {x}
                    position = {y}
                    required_missions = {required_mission}
                    provinces_to_highlight = {{  }}
                    trigger = {{
                    }}
                    effect = {{
                    }}
                }}
            """              
            with open("missions/"+file_path, 'a', encoding='utf-8') as file:
                file.write(content)

if __name__ == "__main__":
    directory = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(directory, 'tno_missions.csv')
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            write_mission(*row)