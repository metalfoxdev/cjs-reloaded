# Contributing Games to our Games repo

1. Find a game (the folder normally consists of HTML and JS files)
2. Test the game by opening a terminal inside your game folder, making sure you have python3 installed, run ```python3 -m http.server 8000``` and open ```localhost:8000``` in a web browser, make sure the game functions as expected.
3. Go to our games repo by [clicking here.](https://github.com/metalfoxdev/cjs-garchive)
4. Fork the repo and add your game folder to it.
5. Give the game folder a shortened name, for example, Madalin Stunt Cars 2 would be called msc2.
6. Create two files inside your game folder called ```GLISTNAME``` and ```GDESC``` with no file extension.
7. Put the full name of your game inside the ```GLISTNAME``` file, for example, "Madalin Stunt Cars 2" and put the description of your game (controls etc.) inside the ```GDESC``` file.
9. Make sure the main html file is called ```index.html```, if it is not then rename it to ```index.html```
10. Send a pull request and your game will be tested then added.
