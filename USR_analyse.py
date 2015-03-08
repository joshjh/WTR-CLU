__author__ = 'josh'
import ALW_interpreter
from CLU_FIXED_VALUES import *
""" Analyse a USR object """

def run(SP_object, SP_allow_db, errors):
    __check_fixed_values__(SP_object, errors)
    __check_against_ALW__(SP_object, SP_allow_db, errors)
    __check_acting_local__(SP_object, errors)

def __check_acting_local__(SP_object, errors):
    if SP_object.Acting_Paid_Rank != '':
        print ('SP {} {} is Acting Local {} and should be in Supervisors Log'.format(SP_object.whois, SP_object.Assignment_Number,
                                                                                  SP_object.Acting_Paid_Rank))
def __check_fixed_values__(SP_object, errors):
    SP_object_dict = SP_object.__dict__
    if SP_object.whois == ('TRIUMPH', 'OFFICER OF THE DAY|1560669'):
        pass
    else:
        if SP_object.Temp_Allowance_Location in ('ASSLQU', 'INTRANSIT', 'GBR'):
                print('--- ASSESS {} {} should be in the LANDED LOG'.format(SP_object.whois, SP_object.Assignment_Number))

        for key in SP_object_dict:

            # determine the correct map to use
            if SP_object.Grade in ('OR2|OR Main|01', 'OR4|OR Main|01', 'OR2|OR Main|02', 'OR4|OR Main|02'):
                if key in FIX_VALUES_JR and SP_object_dict[key] != FIX_VALUES_JR[key]:
                    print (key,' for Service Person: ',  SP_object.whois, 'is: ', SP_object_dict[key], 'should be: ',
                           FIX_VALUES_JR[key])

            elif SP_object.Grade in ('OR6|OR Main|01', 'OR7|OR Main|01', 'OR8|OR Main|01', 'OR9|OR Main|01, OR6|OR Main|02',
                                     'OR7|OR Main|02', 'OR8|OR Main|02', 'OR9|OR Main|02'):
                if key in FIX_VALUES_SR:
                    if SP_object_dict[key] != FIX_VALUES_SR[key]:
                        print (key,' for Service Person: ',  SP_object.whois, 'is: ', SP_object_dict[key], 'should be: ',
                               FIX_VALUES_SR[key])
            elif SP_object.Grade in ('OF1|OF Main|01', 'OF2|OF Main|01', 'OF1|OF Main|02', 'OF2|OF Main|02'):
                if key in FIX_VALUES_GRUNTER_JO:
                    if SP_object_dict[key] != FIX_VALUES_GRUNTER_JO[key]:
                        print (key,' for Service Person: ',  SP_object.whois, 'is: ', SP_object_dict[key], 'should be: ',
                               FIX_VALUES_GRUNTER_JO[key])
            else:
                 if key in FIX_VALUES_GRUNTER_SO:
                    if SP_object_dict[key] != FIX_VALUES_GRUNTER_SO[key]:
                        print (key,' for Service Person: ',  SP_object.whois, 'is: ', SP_object_dict[key], 'should be: ',
                               FIX_VALUES_GRUNTER_SO[key])

def __check_against_ALW__(SP_object, SP_allow_db, errors):
    '''
    :param SP_object: service person object
    :return: process of errors against the AP database object
    '''
    # we get one SP at a time, but all the allowance database.  We need to match just one of the allowance database
    # lines for each SP
    caught_flag = 0
    if SP_object.whois == ('TRIUMPH', 'OFFICER OF THE DAY|1560669'):
        pass
    else:
        for x in range(len(SP_allow_db)):
            # cut to 7 chars to allow for -2 service numbers
            if str(SP_allow_db[x].Service_No)[:8] == str(SP_object.Assignment_Number)[:8]:
                print('Matched {} to {} in allowance DB'.format(SP_allow_db[x].Service_No, SP_object.Assignment_Number))
                caught_flag = 1
                ALW_interpreter.compare(SP_allow_db[x], SP_object, errors)

        if caught_flag == 0:
            caught_error = 'ERROR: cannot match ' + str(SP_object.whois) + 'to allowance database entry!'
            errors.held_errors(caught_error)


