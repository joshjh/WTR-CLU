__author__ = 'josh'

''' Runner for allowance database matching, called by USR_analyse'''

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