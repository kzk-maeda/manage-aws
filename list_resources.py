import json
import boto3
import __future__
import data.sessions

sessions = data.sessions.session_list()

for session_tg in sessions:

    # Create Session with non-default profile
    session = boto3.Session(
        profile_name = session_tg
    )

    # Print AWS Account
    print "========================="
    print "List from {}".format(session_tg)

    # List EC2 Instance IDs
    ec2 = session.resource('ec2')
    for i in ec2.instances.all():
        print(i.instance_id)

    # List IAM Users
    iam = session.resource('iam')
    for i in iam.users.all():
        print(i.user_name)

    # List RDS Instances
    rds = session.client('rds')
    i = 0
    for instance in rds.describe_db_instances()['DBInstances']:
        print(
            rds.describe_db_instances()['DBInstances'][i]['DBInstanceIdentifier']
        )
        i += 1

    # List VPCs
    # To call VPC, use ec2 resource
    for i in ec2.vpcs.all():
        print(
            i.id,
            i.is_default,
            i.cidr_block
        )

    # List Subnets
    for i in ec2.subnets.all():
        print(
            i.id,
            i.vpc_id,
            i.cidr_block
        )