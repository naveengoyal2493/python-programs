import socket

def convert_ip_to_valid_ip_address(ip_address:str):
    ip_nums = ip_address.split(".")
    if '/' in ip_nums[3]:
        num, slash_notation = ip_nums[3].split('/')
        valid_ip = f"{int(ip_nums[0])}.{int(ip_nums[1])}.{int(ip_nums[2])}.{int(num)}/{int(slash_notation)}"
    else:
        valid_ip = f"{int(ip_nums[0])}.{int(ip_nums[1])}.{int(ip_nums[2])}.{int(ip_nums[3])}"
    return valid_ip

# print(convert_ip_to_valid_ip_address("01.02.00003.04"))


def is_string_int_val(numeric_string):
    """Returns boolean based on if the given string value is a valid numeric"""
    if not numeric_string and numeric_string != 0:
        return False

    try:
        int(numeric_string)
    except ValueError:
        return False
    # If we reached this far then the int must be good
    return True

# nums = ['a', 'b']
# print(list(filter(is_string_int_val, nums)))

def is_valid_ip_address(ip_address:str):
    slash_notation = None
    if '/' in ip_address:
        ip_address, slash_notation = ip_address.split('/')
        if (not is_string_int_val(slash_notation)) or int(slash_notation) < 0 or int(slash_notation) > 32:
            return False
    try:
        socket.inet_aton(ip_address)
        return True
    except:
        return False

def convert_ip_to_valid_int_nums_ip(address:str):
    slash_notation = None
    if '/' in address:
        address, slash_notation = address.split('/')
    address_nums = address.split(".")
    valid_address = f"{int(address_nums[0])}.{int(address_nums[1])}.{int(address_nums[2])}.{int(address_nums[3])}"
    if slash_notation:
        valid_address += f"/{slash_notation}"
    return valid_address


print(convert_ip_to_valid_int_nums_ip('1.01.00255.256/32'))