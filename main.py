from PIL import Image


# Encryption function
def encrypt_image(image_path, key):
    image = Image.open(image_path)
    encrypted_image = Image.new("RGB", image.size)

    key_index = 0  # Track the current position in the key

    for x in range(image.width):
        for y in range(image.height):
            pixel = image.getpixel((x, y))
            key_value = ord(key[key_index % len(key)])  # Convert letter to numerical value
            encrypted_pixel = tuple(c ^ key_value for c in pixel)
            encrypted_image.putpixel((x, y), encrypted_pixel)

            key_index += 1

    encrypted_image.save("encrypted_image.png")
    print("Image encrypted successfully!")


# Decryption function
def decrypt_image(encrypted_image_path, key):
    encrypted_image = Image.open(encrypted_image_path)
    decrypted_image = Image.new("RGB", encrypted_image.size)

    key_index = 0  # Track the current position in the key

    for x in range(encrypted_image.width):
        for y in range(encrypted_image.height):
            encrypted_pixel = encrypted_image.getpixel((x, y))
            key_value = ord(key[key_index % len(key)])  # Convert letter to numerical value
            decrypted_pixel = tuple(c ^ key_value for c in encrypted_pixel)
            decrypted_image.putpixel((x, y), decrypted_pixel)

            key_index += 1

    decrypted_image.save("decrypted_image.png")
    print("Image decrypted successfully!")


# Example usage
image_path = "C:/Users/91630/Downloads/naruto.jpg"
key = 'SECRETKEY'  # Use letters as the key

encrypt_image(image_path, key)
decrypt_image("encrypted_image.png", key)
