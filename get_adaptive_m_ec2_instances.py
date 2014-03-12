#!/usr/bin/python
import boto.ec2

conn = boto.ec2.connect_to_region("us-east-1")

reservations = conn.get_all_reservations()

#print reservations
for res in reservations:
	for instance in res.instances:
		#print "{0} {1} {2} {3} {4}".format(instance.id,instance.public_dns_name,instance.private_dns_name,instance.ip_address,instance.private_ip_address)
		print "{0}".format(instance.ip_address)
