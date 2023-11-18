document.addEventListener("keydown", function(event)) {
    // Check if pressed key is arrow key
    if (event.key.startsWith("Arrow")) {
        event.preventDefault();
    }
});
