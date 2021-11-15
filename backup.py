#!/usr/bin/python3
import sys
import getopt
import boto3
import os
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('~/')
load_dotenv(dotenv_path=dotenv_path)
AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')

session = boto3.session.Session()

s3 = session.resource(service_name='s3',
                      region_name='us-east-2',
                      aws_access_key_id=AWS_ACCESS_KEY,
                      aws_secret_access_key=AWS_SECRET_KEY)
client = session.client(service_name='s3', region_name='us-east-2', aws_access_key_id=AWS_ACCESS_KEY,
                        aws_secret_access_key=AWS_SECRET_KEY)


def main(argv):
    filename = ''
    bucketname = ''
    try:
        opts, args = getopt.getopt(argv, 'hf:b:', ['filename=', 'bucketname='])
    except getopt.GetoptError:
        print('backup.py -f <filename>')
        sys.exit(1)
    for opt, arg in opts:
        if opt == '-h':
            print('backup.py -f <filename>')
            sys.exit()
        elif opt in ("-f", "--filename"):
            filename = arg
        elif opt in ("-b", "--bucketname"):
            bucketname = arg
    # if the filename passed in has any preceding "/"'s to indicate directory/path
    # take them off and get the filename exactly.
    # if there are no /'s, then it will not affect anything.
    s3_backup_name = filename.split('/')[-1]
    print(f"Sending {filename} to {bucketname} in Amazon S3")
    # upload the file passed in to the bucket passed in to S3 with the
    # name of the file exactly
    s3.meta.client.upload_file(filename, bucketname, s3_backup_name)


if __name__ == "__main__":
    main(sys.argv[1:])
