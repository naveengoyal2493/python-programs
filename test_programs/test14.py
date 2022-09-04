def convert_subnet_and_gateway_to_valid_ip(network_config):
    config = network_config['ipam']['Config'][0]
    subnet = config["Subnet"]
    subnet_nums = subnet.split(".")
    gateway = config["Gateway"]
    gateway_nums = gateway.split(".")
    valid_subnet = ''
    valid_gateway = ''

    for i in range(4):
        if i == 2:
            subnet_nums[i] = int(subnet_nums[i])
            gateway_nums[i] = int(gateway_nums[i])
        valid_subnet += subnet_nums[i] + "."
        valid_gateway += valid_gateway[i] + "."

    valid_subnet = f"{subnet_nums[0]}.{subnet_nums[1]}.{int(subnet_nums[2])}.{subnet_nums[3]}"


    valid_gateway = f"{gateway_nums[0]}.{gateway_nums[1]}.{int(gateway_nums[2])}.{gateway_nums[3]}"
    
    config["Subnet"] = valid_subnet
    config["Gateway"] = valid_gateway
    network_config['ipam']['Config'][0] = config
    return network_config
