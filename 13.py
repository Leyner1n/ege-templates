from ipaddress import *


# ПЕРЕВОД МАСКИИ СЕТИ В ДВОИЧНУЮ
# print('.'.join(f'{x:>08b}' for x in [255, 255, 254, 0]))


# for mask in range(33):
#     net = ip_network(f'111.81.208.27/{mask}', 0)
#     print(net, net.netmask)  # 192

# 111.81.192.0/18 255.255.192.0
# 111.81.192.0/19 255.255.224.0


# for mask in range(33):
#     net = ip_network(f'148.195.140.28/{mask}', 0)
#     print(net)  # 22


# for mask in range(33):
#     net = ip_network(f'241.185.253.57/{mask}', 0)
#     print(net)  # 9


# counter = 0
# for mask in range(33):
#     net = ip_network(f'76.155.48.2/{mask}', 0)
#     if '76.155.48.0' in str(net):
#         counter += 1
#
# print(counter)  # 11


# for mask in range(33):
#     net1 = ip_network(f'112.117.107.70/{mask}', 0)
#     net2 = ip_network(f'112.117.121.80/{mask}', 0)
#     if net1 == net2:  # они находятся в одной сети
#         print(net2, net2.netmask)  # net1 и net2 "=", ответ: 224


# for mask in range(33):
#     net1 = ip_network(f'157.127.182.76/{mask}', 0)
#     net2 = ip_network(f'157.127.190.80/{mask}', 0)
#     if net1 != net2:
#         print(net1)
#         print(net2)  # 21


# ==================================================================
# задача на подсчет адресов, имея только маску секти

# переводим маску в двоичный код, для того, чтобы узнать количество ip адресов
# print('.'.join(f'{x:>08b}' for x in [255, 255, 254, 0])) # 11111111.11111111.11111110.00000000

# количеством ip адресов будет явл степеь 2-ки на кол-во
# нулей справа, то есть 0.00000000 (9 нулей)

# Значит ответ 2 ** 9(512), (в условии еще 2 адреса не используют)

# ОТВЕТ = 510

# решение кодом
# net = ip_network('0.0.0.0/255.255.254.0')
# print(net.num_addresses - 2)
# ==================================================================


# for mask in range(33):
#     net = ip_network(f'108.133.75.91/{mask}', 0)
#     print(net, net.num_addresses)  # 64

# num_addresses учитывает кол-во адресов


# for mask in range(33):
#     net = ip_network(f'175.122.80.13/{mask}', 0)
#     if net.num_addresses >= 60:
#         print(net)  # 7 вариантов маски


# # прототип с поиском номера пк
# net = ip_network('192.168.156.235/255.255.255.240', 0)
# # print(net)  # узнали адрес сети (192.168.156.224)
#
# ip1 = ip_address('192.168.156.235')
# ip2 = ip_address('192.168.156.224')
#
# print(int(ip1) - int(ip2))  # 11


# # задание для подсчета ip адресов кратных какому-то числу
# counter = 0
# net = ip_network('0.0.0.0/255.255.128.0', 0)
#
# for ip in net:
#     if int(ip) % 4 == 0:
#         counter += 1
#
# print(counter)  # 8192
