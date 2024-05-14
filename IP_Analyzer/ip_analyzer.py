#!/usr/bin/python3
""" AUTHOR: 0xv98
"""

import ipaddress

def ip_func(ip_object):
    """ Setupping The IP Functionality """
    try:
        ip_object = ipaddress.ip_address(ip_object)
        if isinstance(ip_object, ipaddress.IPv4Address):
            """ Checking if ip_object is a valid IPV4 """
            print(f"{ip_object} => is IPV4")
        elif isinstance(ip_object, ipaddress.IPv6Address):
            """ Checking if ip_object is a valid IPV6 """
            print(f"{ip_object} => is IPV6")
        else:
            """ Checking if ip_object is a valid IP Address """
            print(f"{ip_object} => is Not a Valid IP Address !")
    except ValueError as error:
        print(f"Error: {error}")


IP = input("Enter The IP Address : ")
ip_func(IP)
