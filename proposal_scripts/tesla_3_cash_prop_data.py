from all_proposal_standard_info import *
def tesla_3_cash_prop_data():  

    proposal_info = {}
    proposal_info['long_prop_log_number'] = sheet['P8'].value
    proposal_info['short_prop_log_number'] = sheet['P9'].value
    proposal_info['backup_package'] = sheet['P10'].value
    proposal_info['battery_system_controller'] = sheet['P11'].value
    proposal_info['battery_name'] = sheet['P12'].value
    proposal_info['duration_battery_only'] = sheet['P13'].value
    proposal_info['duration_plus_pv'] = sheet['P14'].value
    proposal_info['battery_kwh'] = sheet['P15'].value
    proposal_info['battery_kw'] = sheet['P16'].value
    proposal_info['total_cost_pre_discount'] = "${:,.0f}".format(round(sheet['P17'].value))
    proposal_info['promo_discount'] = "${:,.0f}".format(round(sheet['P19'].value))
    proposal_info['cash_down_payment'] = "${:,.0f}".format(round(sheet['P20'].value))
    proposal_info['total_sys_cost'] = "${:,.0f}".format(round(sheet['P21'].value))
    proposal_info['tax_credit'] = "${:,.0f}".format(round(sheet['P22'].value))
    proposal_info['net_sys_cost'] = "${:,.0f}".format(round(sheet['P23'].value))
    #rebate info
    if rebate_sheet['C8'].value == 1:
        proposal_info['rebate_text'] = sheet['A18'].value
        proposal_info['rebate_amount'] = "${:,.0f}".format(round(sheet['P18'].value))
    else:
        proposal_info['rebate_text'] = " "
        proposal_info['rebate_amount'] = " "
    #json info
    proposal_info['json_for_proposal_log'] = sheet['P24'].value

    return proposal_info
