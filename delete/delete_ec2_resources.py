import boto3
import __future__

class delEC2Resource:
    def __init__(self, session):
        # Create EC2 Object
        self.ec2 = session.resource("ec2")
        self.response = "Default Message"


    def delete_ec2_instance(self):
        # List ec2 Instance
        for instance in self.ec2.instances.all():
            instance_id = instance.instance_id
    
            # Delete Instance
            try:
                self.response = instance.terminate()
                print self.response
                print "EC2 {} is terminated".format(instance_id)
                return 0
            except:
                print "something went wrong with deleting ec2 instance {}".format(instance_id)
                return 1


    def delete_keypairs(self):
        # List Keypairs
        for key in self.ec2.key_pairs.all():
            key_name = key.name

            # Delete Keypair
            try:
                self.response = key.delete()
                print self.response
                print "Keypair {} is deleted".format(key_name)
                return 0
            except:
                print "something went wrong with deleting keypair {}".format(key_name)
                return 1


    def delete_eips(self):
        # List EIPs
        for eip in self.ec2.vpc_addresses.all():
            public_ip = eip.public_ip
            try:
                self.response = eip.release()
                print self.response
                print "EIP {} is released".format(public_ip)
                return 0
            except:
                print "something went wrong with releasing EIP {}".format(public_ip)
                return 1
