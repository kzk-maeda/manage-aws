import boto3
import __future__

class delVPCResource:
    def __init__(self,session,delete_condition):
        # Create EC2 Object as EC2
        self.ec2 = session.resource("ec2")
        self.response = "Default Message"
        self.delete_condition = delete_condition


    def delete_subnets(self):
        # List Subnets
        for subnet in self.ec2.subnets.all():
            subnet_id = subnet.id
            subnet_cidr = subnet.cidr_block

            if subnet_cidr.startswith(self.delete_condition):
                try:
                    self.response = subnet.delete()
                    print self.response
                    print "Subnet {}:{} is deleted".format(subnet_id, subnet_cidr)
                except:
                    print "something went wrong with deleting subnet {} {}".format(subnet_id,subnet_cidr)


    def delete_route_tables(self,vpc_id):
        for table in self.ec2.route_tables.all():
            table_vpcid = table.vpc_id
            if table_vpcid == vpc_id:
                try:
                    self.response = table.delete()
                    print self.response
                    print "Route Table {} is deleted".format(table.id)
                except:
                    print "something went wrong with deleting route table {}".format(table.id)


    def delete_igws(self,vpc_id):
        for igw in self.ec2.internet_gateways.all():
            igw_id = igw.id
            attached_vpc = igw.attachments[0]["VpcId"]
            if attached_vpc == vpc_id:
                try:
                    self.response = igw.detach_from_vpc(VpcId = vpc_id)
                    print self.response
                    self.response = igw.delete()
                    print "IGW {} is deleted".format(igw_id)
                    return 0
                except:
                    print "something went wrong with deleting igw {}".format(igw_id)
                    return 1


    def delete_sgs(self,vpc_id):
        for sg in self.ec2.security_groups.all():
            sg_id = sg.id
            sg_vpcid = sg.vpc_id
            if sg_vpcid == vpc_id:
                try:
                    self.response = sg.delete()
                    print self.response
                    print "SecurityGroup {} is deleted".format(sg_id)
                    return 0
                except:
                    print "something went wrong with deleting security group {}".format(sg_id)
                    return 1


    def detach_dhcp_options(self,vpc_id):
        dhcp = self.ec2.Vpc(vpc_id).dhcp_options
        dhcp_id = dhcp.id
        try:
            self.response = self.ec2.Vpc(vpc_id).associate_dhcp_options(
                DhcpOptionsId='default'
            )
            print self.response
            print "DHCP Option {} is detached".format(dhcp_id)
            return 0
        except:
            print "something went wrong with detaching DHCP Option {}".format(dhcp_id)
            return 1


    def delete_vpcs(self):
        for vpc in self.ec2.vpcs.all():
            vpc_id = vpc.id
            vpc_cidr = vpc.cidr_block

            if vpc_cidr.startswith(self.delete_condition):
                # Delete Subnets
                self.delete_subnets()

                # Delete Route Tables
                self.delete_route_tables(vpc_id)

                # Delete Internet Gateways
                self.delete_igws(vpc_id)

                # Delete Security Group
                self.delete_sgs(vpc_id)

                # Delete DHCP Options
                self.detach_dhcp_options(vpc_id)

                # Delete VPCs
                try:
                    self.response = vpc.delete()
                    print self.response
                    print "VPC {}:{} is deleted".format(vpc_id, vpc_cidr)
                    return 0
                except:
                    print "something went wrong with deleting VPC {} {}".format(vpc_id, vpc_cidr)
                    return 1