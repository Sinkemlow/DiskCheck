from subprocess import check_output

df = check_output(['df', '-PhT', 'hfs'])
df_output = df.split('\n')
df_output.pop(0)
df_output.pop()


def disk_check(df_list):
    print "----------------------"
    print "Filesystems above 80%:"
    print "----------------------"
    for line in df_list:
        usage = line.split()[4]
        filesystem = line.split()[5]
        percentage = int(usage.split("%")[0])

        if percentage >= 80:
            print "%s is at %s%%" % (filesystem, percentage)


disk_check(df_output)
