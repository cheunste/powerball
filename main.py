#import powerball
#from . import powerBall
import powerBall
import argparse
import sys

#def main():
#    pbFile=powerball.getFile()
#    powerball.insertToDB(pbFile)
#    return

def check_arg():
    parser = argparse.ArgumentParser(description='Script to get data from Powerball results')

    parser.add_argument('-u','--update',
                        action='store_true',
                        required=False,
                        default=False,
                        help='update DB')

    parser.add_argument('-c','--create',
                        action='store_true',
                        required=False,
                        default=False,
                        help='create DB')

    if parser.parse_args().update:
        powerBall.updateDB()
    if parser.parse_args().create:
        powerBall.create()

if __name__=="__main__":
    check_arg()
