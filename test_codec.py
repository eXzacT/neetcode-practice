from codec import *
from test_data import arrays_strings


def test_codec_validity():
    """ Class Codec correctly encodes and decodes (31/10/2023) """

    for array in arrays_strings:

        original_string = array['array']
        encoder = Codec()
        encoded_string = encoder.encode(original_string)
        decoded_string = encoder.decode(encoded_string)

        assert original_string == decoded_string, f"Decoded string {decoded_string} does not equal expected {original_string}"
