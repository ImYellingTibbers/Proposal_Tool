from all_proposal_standard_info import *
def franklin_1_cash_prop_data():  

    proposal_info = {}
    proposal_info['long_prop_log_number'] = sheet['B8'].value
    proposal_info['short_prop_log_number'] = sheet['B9'].value
    proposal_info['backup_package'] = sheet['B10'].value
    proposal_info['battery_system_controller'] = sheet['B11'].value
    proposal_info['battery_name'] = sheet['B12'].value
    proposal_info['duration_battery_only'] = sheet['B13'].value
    proposal_info['duration_plus_pv'] = sheet['B14'].value
    proposal_info['battery_kwh'] = sheet['B15'].value
    proposal_info['battery_kw'] = sheet['B16'].value
    proposal_info['total_cost_pre_discount'] = "${:,.0f}".format(round(sheet['B17'].value))
    proposal_info['promo_discount'] = "${:,.0f}".format(round(sheet['B19'].value))
    proposal_info['cash_down_payment'] = "${:,.0f}".format(round(sheet['B20'].value))
    proposal_info['total_sys_cost'] = "${:,.0f}".format(round(sheet['B21'].value))
    proposal_info['tax_credit'] = "${:,.0f}".format(round(sheet['B22'].value))
    proposal_info['net_sys_cost'] = "${:,.0f}".format(round(sheet['B23'].value))
    #rebate info
    if rebate_sheet['C8'].value == 1:
        proposal_info['rebate_text'] = sheet['A18'].value
        proposal_info['rebate_amount'] = "${:,.0f}".format(round(sheet['B18'].value))
    else:
        proposal_info['rebate_text'] = " "
        proposal_info['rebate_amount'] = " "
    #json info
    proposal_info['json_for_proposal_log'] = sheet['B24'].value

    return proposal_info
