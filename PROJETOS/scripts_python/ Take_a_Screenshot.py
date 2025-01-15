from PIL import ImageGrab

# Tirar um screenshot
screenshot = ImageGrab.grab()
screenshot.save("screenshot.png")
print("Screenshot salvo como 'screenshot.png'.")
