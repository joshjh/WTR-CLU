__author__ = 'josh'

''' Runner for allowance database matching, called by USR_analyse'''
from CLU_FIXED_VALUES import FIX_POSTCODE
from CLU_FIXED_VALUES import POSTCODE_FORMATS
import re

def compare(allow_obj, sp_obj, errors):
    # compare allowance database GYH(M) to USR GYH(M)
    if allow_obj.GYH_T_Mileage_To_Nominated_Address == 'N/A':
        pass

    elif allow_obj.GYH_T_Mileage_To_Nominated_Address != sp_obj.Temp_GYH_Mileage:
        print('found mismatch between allowance DB GYH_T :{} and USR GYH_T {}'.format(allow_obj.GYH_T_Mileage_To_Nominated_Address,
                                                                                       sp_obj.Temp_GYH_Mileage))

    if allow_obj.Live_Onboard != 'YES' and sp_obj.Temp_SLA_Charged != '':
        print('does not have live onboard in ALWDB but Temp SLA is {}'.format(sp_obj.Temp_SLA_Charged))

    if allow_obj.Live_Onboard != 'NO' and sp_obj.Temp_SLA_Charged == '':
        print('does live onboard in ALWDB but Temp SLA is {}'.format(sp_obj.Temp_SLA_Charged))

    postcode_check(allow_obj, errors)

def postcode_check(allow_obj, errors):
    # pull out postcode from the allowance object, then run it through the Python Miles Module against the global postcode
    # PS is postcode pulled from GYH_T_address line in allowance object
    ps = allow_obj.Full_GYH_T_Address
    #this is a bit of a fucking mess at the moment, but should sort to the longest of several re matches,
    # which should be the full post code
    matches = []
    for x in POSTCODE_FORMATS:
        matches.append(re.findall(x, ps.replace(" ", ""))) # STRIP WHITESPACE BEFORE MATCHING

    match = (sorted(matches)[-1])
    print (match)
    ## some writing of postcode for miles to pick up seperately.




