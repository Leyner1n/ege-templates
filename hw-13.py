from ipaddress import *


# for mask in range(33):
#     net = ip_network(f'118.193.30.139/{mask}', 0)
#     print(net, net.netmask)  # 248


# for mask in range(33):
#     net = ip_network(f'154.201.208.17/{mask}', 0)
#     print(net, net.netmask)  # 224


# for mask in range(33):
#     net = ip_network(f'122.21.49.91/{mask}', 0)
#     print(net, net.netmask)  # 20


# for mask in range(33):
#     net = ip_network(f'173.103.25.118/{mask}', 0)
#     print(net, net.netmask)  # 11


# for mask in range(33):
#     net = ip_network(f'158.116.11.146/{mask}', 0)
#     print(net, net.netmask)  # 7


# for mask in range(33):
#     net = ip_network(f'191.173.145.240/{mask}', 0)
#     print(net, net.num_addresses)


# net = ip_network('0.0.0.0/255.255.240.0', 0)
# print(net.num_addresses - 2)

# for mask in range(33):
#     net1 = ip_network(f'165.112.200.70/{mask}', 0)
#     net2 = ip_network(f'165.112.175.80/{mask}', 0)
#     if net1 == net2:
#         print(net1)  # 17


# for mask in range(33):
#     ip1 = ip_network(f'10.96.180.231/{mask}', 0)
#     ip2 = ip_network(f'10.96.140.118/{mask}', 0)
#     if ip1 != ip2:
#         print(32 - mask)


# net = ip_network(f'192.168.240.0/255.255.255.0', 0)
# counter = 0
#
# for ip in net:
#     a = f'{ip:b}'
#     if a.count('0') == a.count('1'):
#         counter += 1
#
# print(counter)  # 8


# net = ip_network('10.48.96.0/255.255.240.0', 0)
# counter = 0
#
# for ip in net:
#     a = f'{ip:b}'
#     if a.count('1') > a.count('0'):
#         counter += 1
#
# print(counter)  # 13

