# Put your Vercel domain in this variable
NEW_BASE_URL="https://cjs-reloaded.vercel.app"

sed -i "s|baseURL = \".*\"|baseURL = \"$NEW_BASE_URL\"|" config.toml

python3 gen_games.py 1
hugo --gc --minify
