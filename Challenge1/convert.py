import binascii


def hexTo64(hexString):
    hexString = hexString.decode("hex")
    return binascii.b2a_base64(hexString)


if __name__ == "__main__":
    hexString = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    b64String = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
    print (hexTo64(hexString) == b64String) 
    print hexTo64(hexString)
