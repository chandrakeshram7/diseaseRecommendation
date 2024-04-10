import os

# Check if AWS_ACCESS_KEY_ID environment variable is set
aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID')
if aws_access_key_id:
    print("AWS_ACCESS_KEY_ID:", aws_access_key_id)
else:
    print("AWS_ACCESS_KEY_ID environment variable is not set.")

# Check if AWS_SECRET_ACCESS_KEY environment variable is set
aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
if aws_secret_access_key:
    print("AWS_SECRET_ACCESS_KEY:", aws_secret_access_key)
else:
    print("AWS_SECRET_ACCESS_KEY environment variable is not set.")

# Check if AWS_DEFAULT_REGION environment variable is set
aws_default_region = os.environ.get('AWS_DEFAULT_REGION')
if aws_default_region:
    print("AWS_DEFAULT_REGION:", aws_default_region)
else:
    print("AWS_DEFAULT_REGION environment variable is not set.")
