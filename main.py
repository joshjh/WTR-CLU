""" Writer CLU.  Codefied Likeness Utility for Checks and Controls.  Copywrite Josh
Harney 2015.  Released under the GPL"""

import xlrd
import getopt
import sys
import openbook
import USR_analyse
import error_log

def main(argv):
    # get options from the command line.  -h help. -i input file. -t type of input
    try:
        opts, args = getopt.getopt(argv, 'hi:t:')
        for opt, arg in opts:
            if opt in ('-i'):
                inputfile = arg
            elif opt in ('-t'):
                type = arg

    except getopt.GetoptError:
        print('Usage: -h help -i input file -t USR ALW')
    errors = error_log.held_errors()
    SP_object_list = openbook.openbook('usr.xls', sheet_type='USR')
    SP_allow_db = openbook.openbook('allowdb.xls', sheet_type='ALW')

    for x in range(len(SP_object_list)):
        if SP_object_list[x].Assignment_Number != '':
            print('\nIDENTIFIED ANOMOLIES FOR SP {} {}'.format(SP_object_list[x].whois, str(SP_object_list[x].Assignment_Number)[:8]))
            USR_analyse.run(SP_object_list[x], SP_allow_db, errors)
        else:
            errors.held_errors('SP: ' + SP_object_list[x].whois[0] + ' ' + SP_object_list[x].whois[1] +' is a unarrived entity')

    errors.dump_held_errors()
if __name__ == '__main__':
    main(sys.argv[1:])

