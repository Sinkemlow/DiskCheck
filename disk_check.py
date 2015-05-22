from subprocess import check_output
from sys import platform, exit
from socket import gethostname


def get_df():

    os = platform

    if os == 'linux2':
        print "This is a Linux based system."
        df = check_output(['df', '-Ph'])
        df_output = df.split('\n')
        df_output.pop(0)
        df_output.pop()
        return df_output

    elif os == 'darwin':
        print "This is an OSX based system."
        df = check_output(['df', '-PhT', 'hfs'])
        df_output = df.split('\n')
        df_output.pop(0)
        df_output.pop()
        return df_output

    else:
        print "Unable to determine Operating System."
        exit(0)


def disk_check(df_list):

    hostname = gethostname()
    limit = 80

    for line in df_list:
        usage = line.split()[4]
        filesystem = line.split()[5]
        percentage = int(usage.split("%")[0])
    
        if percentage >= limit:
            message = "The %s filesystem on %s is at %s%%" % (filesystem, hostname, percentage)
            print
            print message

        else:
            print "All filesystems are below %s" % limit


def main():
    disk_check(get_df())

main()
