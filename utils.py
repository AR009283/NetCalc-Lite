def get_ip_class(ip):
    first_octet = int(ip.split(".")[0])

    if 1 <= first_octet <= 126:
        return "Class A"
    elif 128 <= first_octet <= 191:
        return "Class B"
    elif 192 <= first_octet <= 223:
        return "Class C"
    elif 224 <= first_octet <= 239:
        return "Class D (Multicast)"
    elif 240 <= first_octet <= 255:
        return "Class E (Experimental)"
    else:
        return "Unknown"


def ip_to_binary(ip):
    binary = []

    for octet in ip.split("."):
        binary.append(format(int(octet), "08b"))

    return ".".join(binary)