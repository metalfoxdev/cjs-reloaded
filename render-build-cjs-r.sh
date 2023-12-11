NEW_BASE_URL="https://cjs-r.onrender.com"

sed -i "s|baseURL = \".*\"|baseURL = \"$NEW_BASE_URL\"|" config.toml

python3 gen_games.py '1'
hugo --gc --minify
