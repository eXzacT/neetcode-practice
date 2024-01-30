class Codec():

    def encode(self, input_string: list[str]) -> str:
        """ Converting a list of strings into one string, and before each word adding the length and # sign (31/10/2023) """
        encoded_string = ""

        for string in input_string:
            encoded_string += str(len(string)) + "#" + string

        return encoded_string

    def decode(self, encoded_string: str) -> list[str]:
        """ Decoding the encoded string back to original (31/10/2023)
            This is done by going through the string and finding out how long the encoded word is,
            then just adding the slice of the same length into a new array of words
        """

        decoded_string = []
        i = previous_word_end = 0

        while i < len(encoded_string):
            if encoded_string[i] == '#':

                # The slice from previous word ending to '#' sign is representing length of the next string (31/10/2023)
                string_length = int(encoded_string[previous_word_end:i])
                i += 1  # Skip the '#' sign (31/10/2023)

                # Add the string to the array of strings, skip the entire string and remember its end position (31/10/2023)
                decoded_string.append(encoded_string[i:i+string_length])
                i += string_length
                previous_word_end = i

            i += 1

        return decoded_string
