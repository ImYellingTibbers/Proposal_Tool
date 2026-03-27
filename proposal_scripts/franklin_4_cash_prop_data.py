from all_proposal_standard_info import *
def franklin_4_cash_prop_data():  

    proposal_info = {}
    proposal_info['long_prop_log_number'] = sheet['E8'].value
    proposal_info['short_prop_log_number'] = sheet['E9'].value
    proposal_info['backup_package'] = sheet['E10'].value
    proposal_info['battery_system_controller'] = sheet['E11'].value
    proposal_info['battery_name'] = sheet['E12'].value
    proposal_info['duration_battery_only'] = sheet['E13'].value
    proposal_info['duration_plus_pv'] = sheet['E14'].value
    proposal_info['battery_kwh'] = sheet['E15'].value
    proposal_info['battery_kw'] = sheet['E16'].value
    proposal_info['total_cost_pre_discount'] = "${:,.0f}".format(round(sheet['E17'].value))
    proposal_info['promo_discount'] = "${:,.0f}".format(round(sheet['E19'].value))
    proposal_info['cash_down_payment'] = "${:,.0f}".format(round(sheet['E20'].value))
    proposal_info['total_sys_cost'] = "${:,.0f}".format(round(sheet['E21'].value))
    proposal_info['tax_credit'] = "${:,.0f}".format(round(sheet['E22'].value))
    proposal_info['net_sys_cost'] = "${:,.0f}".format(round(sheet['E23'].value))
    #rebate info
    if rebate_sheet['C8'].value == 1:
        proposal_info['rebate_text'] = sheet['A18'].value
        proposal_info['rebate_amount'] = "${:,.0f}".format(round(sheet['E18'].value))
    else:
        proposal_info['rebate_text'] = " "
        proposal_info['rebate_amount'] = " "
    #json info
    proposal_info['json_for_proposal_log'] = sheet['E24'].value

    return proposal_info
