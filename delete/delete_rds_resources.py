import boto3
import __future__

class delRDSResource:
    def __init__(self,session):
        # Create RDS Object
        self.rds = session.client("rds")
        self.response = "Default Message"

    def delete_rds_instances(self):
        # List RDS Instances
        for instance in self.rds.describe_db_instances()["DBInstances"]:
            instance_identifier = instance["DBInstanceIdentifier"]

            # Delete RDS Instance
            try:
                self.response = self.rds.delete_db_instance(
                    DBInstanceIdentifier=instance_identifier,
                    SkipFinalSnapshot=True
                )
                print self.response
                print "RDS {} is deleted".format(instance_identifier)
                return 0
            except:
                print "something went wrong with deleting rds instance {}".format(instance_identifier)
                return 1


    def delete_subnet_group(self):
        # List Subnet Group
        for sg in self.rds.describe_db_subnet_groups()["DBSubnetGroups"]:
            pass

