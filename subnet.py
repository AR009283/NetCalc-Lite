import ipaddress


def subnet_calculator(ip, prefix):

    try:
        network = ipaddress.ip_network(f"{ip}/{prefix}", strict=False)

        # Calculate first and last usable hosts
        if network.prefixlen == 32:
            first_host = network.network_address
            last_host = network.network_address
            usable_hosts = 1

        elif network.prefixlen == 31:
            first_host = network.network_address
            last_host = network.broadcast_address
            usable_hosts = 2

        else:
            first_host = network.network_address + 1
            last_host = network.broadcast_address - 1
            usable_hosts = network.num_addresses - 2

        return {
            "Network Address": str(network.network_address),
            "Broadcast Address": str(network.broadcast_address),
            "Subnet Mask": str(network.netmask),
            "First Host": str(first_host),
            "Last Host": str(last_host),
            "Usable Hosts": usable_hosts
        }

    except ValueError:
        return None