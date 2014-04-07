"""
 This script will boot a new server in openstack, register it with chef and execute the chef run list.

"""

#import compute_api_json as caj
#import sys
from pprint import pprint
import argparse
#import json


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Boot a new openstack server and add it to our application.')
    # TODO: We want to get the region, auth endpoint, username and apikey 
    #  from environment variables if not specified via the commandline 
    parser.add_argument('-c', '--creds', nargs=2, dest='creds', required=True,
                       help='Please enter username and APIkey for your account')
    parser.add_argument('-e', '--endpoint', nargs=1, dest='endpoint', required=True,
                        help='Please enter the auth endpoint.')
    parser.add_argument('-r', '--region', nargs=1, dest='region', required=True,
                        help='Please enter the region.')
    parser.add_argument('-s', '--server_name', nargs=1, dest='server_name', required=True,
                        help='Please enter a name for the new server.')
    parser.add_argument('-f', '--flavor', nargs=1, dest='flavor', required=True,
                        help='Flavor must be specified.')
    parser.add_argument('-i', '--image', nargs=1, dest='image', required=True,
                        help='Server image must be specified.')
    args = parser.parse_args()
    pprint(args)
    # if auth token expired, get another




# BASH command:
# supernova joeracker boot --image 80fbcb55-b206-41f9-9bc2-2dd7aac6c061 --flavor 2 minecraft_test
# root is tmXWmGCo7goz, IP is 192.237.181.66;

# Set the rackspace account information

# Start a rackspace server
#supernova joeracker boot --image 80fbcb55-b206-41f9-9bc2-2dd7aac6c061 --flavor 2 minecraft_test

# Get the root password and IP - supposedly this comes from the text output

# Set a DNS A record for the IP

# Upload the cookbook
#knife cookbook upload minecraft_class_server

# Bootstrap the node (register with the chef server and execute runlist)
# knife bootstrap 192.237.181.66 --sudo -x root -P cecilia1 -N "minecraft1" -r "recipe[minecraft_class_server]"
# knife rackspace server create -A joeracker -K 1b8140addf7572b536c7d3d57819e086 -f 2 -I 80fbcb55-b206-41f9-9bc2-2dd7aac6c061 -N m01 -r "recipe[minecraft_class_server]" -S m01

# Execute runlist on the node
#sudo chef-client
