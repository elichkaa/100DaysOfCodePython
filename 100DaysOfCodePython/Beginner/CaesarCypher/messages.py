encrypt = 'encode'
decrypt = 'decode'
no = 'no'

prompt = "Type 'encode' to encrypt, type 'decode' to decrypt: "
unavailable_command = "This command doesn't exist."
word = "Type your message: "
shift = "Type the shift number: "
end = "Type 'yes' if you want to go again. Otherwise type 'no'."


def result(shifted_word, encoded):
    if encoded:
        return f"This is your encoded word {shifted_word}"
    else:
        return f"This is your decoded word {shifted_word}"
