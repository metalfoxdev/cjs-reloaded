# Put your Render domain in this variable
NEW_BASE_URL="https://tassomai.onrender.com"

sed -i "s|baseURL = \".*\"|baseURL = \"$NEW_BASE_URL\"|" config.toml

python3 gen_games.py 1
hugo --gc --minify

