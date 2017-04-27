import boto3
import __future__
import delete.delete_ec2_resources as delec2
import delete.delete_rds_resources as delrds
import delete.delete_vpc_resources as delvpc
import delete.delete_iam_resources as deliam
import delete.delete_elb_resources as delelb
import data.sessions


if __name__ == "__main__":
    # Define Variables
    sessions = data.sessions.session_list()
    delete_condition = "10."

    # Select Mode
    print "Select Run Mode (1: first / 2: second) : "
    mode = raw_input()
    #print mode

    # Create Session
    for name in sessions:
        session = boto3.Session(
            profile_name=name
        )
        ec2_deletion = delec2.delEC2Resource(session)
        rds_deletion = delrds.delRDSResource(session)
        vpc_deletion = delvpc.delVPCResource(session, delete_condition)
        iam_deletion = deliam.delIAMResource(session)
        elb_deletion = delelb.delELBResourse(session)

        print "start to {}".format(name)

        if mode == "1":
            print "================================"
            print "starting delete ec2 resources"
            ec2_deletion.delete_ec2_instance()
            ec2_deletion.delete_keypairs()

            print "================================"
            print "starting delete RDS resources"
            rds_deletion.delete_rds_instances()

            print "================================"
            print "starting delete IAM resources"
            iam_deletion.detach_iam_policies()

            print "================================"
            print "starting delete ELB resources"
            elb_deletion.delete_elbs()

        elif mode == "2":
            print "================================"
            print "starting delete ec2 resources"
            ec2_deletion.delete_eips()

            print "================================"
            print "starting delete VPC resources"
            vpc_deletion.delete_vpcs()

        else:
            print "Mode Selection is Failed."
            break
