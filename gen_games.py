"""
Title: gen_game_list
Description: Generates a list of games in MD format based on the GLISTNAME files in the gfiles folder
Author: github.com/metalfoxdev
"""
import os
import sys

md_data = []
md_out = ""
game_count = 0
mode = sys.argv[1].strip()

def sub(fname, slug, desc):
    return '---\ntitle: "' + str(fname) + '"\nslug: ' + str(slug) + "\n---\n\n{{< noscroll >}}\n{{< rawhtml >}}\n" + '<iframe width="720" height="576" name="iframe" src="/cjs-garchive/' + str(slug) + '/index.html"></iframe>\n{{< /rawhtml >}}\n\n[Click here to play fullscreen](/cjs-garchive/' + str(slug) + ")\n\n" + desc

def allowed(file):
    if _dir == ".git":
        return False
    elif _dir == "README.md":
        return False
    else:
        return True

print("Scanning games...")

for _dir in os.listdir(os.path.join("static", "cjs-garchive")):
    if allowed(_dir) == False:
        pass
    else:
        try:
            f = open(os.path.join("static", "cjs-garchive", _dir, "GLISTNAME"), "r")
            if mode == "1":
                md_data.append("[" + f.readline().strip() + "](" + "/" + _dir + ")")
            else:
                md_data.append("[" + f.readline().strip() + "](" + "/cjs-reloaded/" + _dir + ")")
            f = open(os.path.join("static", "cjs-garchive", _dir, "GLISTNAME"), "r")
            f2 = open(os.path.join("static", "cjs-garchive", _dir, "GDESC"))
            md = open(os.path.join("content", _dir + ".md"), "w")
            md.write(sub(f.readline().strip(), _dir, f2.read()))
            md.close()
            f2.close()
            game_count += 1
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
f.close()
f = open(os.path.join("content", "glist.md"), "w")
f.write("# Game List\n## There are currently " + str(game_count) + " games.\n\n" + md_out)
f.close()
print("glist.md generation complete, " + str(game_count) + " games loaded.")
