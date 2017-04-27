import boto3
import __future__

class delIAMResource:
    def __init__(self, session):
        # Create IAM Object
        self.iam = session.client("iam")
        self.response = "Default Message"


    def detach_iam_policies(self):
        for iam_user in self.iam.list_users()["Users"]:
            user_name = iam_user["UserName"]

            # Detach User Policy
            if user_name != "Administrator":
                # Detach Managed Policy
                for policy in self.iam.list_attached_user_policies(UserName=user_name)["AttachedPolicies"]:
                    policy_arn = policy["PolicyArn"]
                    try:
                        self.response = self.iam.detach_user_policy(
                            UserName=user_name,
                            PolicyArn=policy_arn
                        )
                        print self.response
                        print "IAM Policy {} is detached from {}".format(policy_arn, user_name)
                        return 0
                    except:
                        print "something went wrong with detaching iam policy {}:{}".format(user_name, policy_arn)
                        return 1