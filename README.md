# EncrypDeprypt
It provides a basic implementation of image encryption and decryption using a simple XOR cipher in Python. It utilizes the Python Imaging Library (PIL) to perform image processing tasks. The code includes two main functions: encrypt_image and decrypt_image.

encrypt_image takes an image file path and a key as input. It opens the image, creates a new image of the same size to store the encrypted pixels, and performs XOR encryption on each pixel using the provided key. The encrypted image is then saved as "encrypted_image.png".

decrypt_image takes the encrypted image file path and the same key as input. It opens the encrypted image, creates a new image of the same size to store the decrypted pixels, and performs XOR decryption on each pixel using the provided key. The decrypted image is then saved as "decrypted_image.png".
