import boto3
import __future__

class delELBResourse:
    def __init__(self, session):
        self.elbs = session.client("elb")
        self.response = "Defailt Message"


    def delete_elbs(self):
        for elb in self.elbs.describe_load_balancers()["LoadBalancerDescriptions"]:
            elb_name = elb["LoadBalancerName"]

            # Delete ELBs
            try:
                self.response = elbs.delete_load_balancer(
                    LoadBalancerName=elb_name
                )
                print responce
                print "ELB {} is deleted".format(elb_name)
                return 0
            except:
                print "something went wrong with deleting ELB instance {}".format(elb_name)
                return 1

