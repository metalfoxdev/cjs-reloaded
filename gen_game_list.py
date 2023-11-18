"""
Title: gen_game_list
Description: Generates a list of games in MD format based on the GLISTNAME files in the gfiles folder
Author: github.com/metalfoxdev
"""
import os

md_data = []
md_out = ""
game_count = 0

print("Scanning games...")

for _dir in os.listdir(os.path.join("static", "gfiles")):
    try:
        f = open(os.path.join("static", "gfiles", _dir, "GLISTNAME"), "r")
        if os.path.isfile(os.path.join("content", _dir + ".md")):
            md_data.append("[" + f.readline().strip() + "](" + "/" + _dir + ")")
            game_count += 1
        else:
            print("WARNING: .md file not found for '" + _dir + "'")
            exit(1)
    except FileNotFoundError:
        print("WARNING: GLISTNAME not found in the '" + _dir + "' directory")
        exit(1)

md_data = sorted(md_data)
for x in range(len(md_data)):
    if md_out == "":
        md_out = md_data[x]
    else:
        md_out += "\n\n" + md_data[x]

print("Writing glist.md to content...")
f = open(os.path.join("content", "glist.md"), "w")
f.write("# Game List\n## There are currently " + str(game_count) + " games.\n\n" + md_out)
f.close()
print("glist.md generation complete, " + str(game_count) + " games loaded.")
