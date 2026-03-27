from all_proposal_standard_info import *
def franklin_2_cash_prop_data():  

    proposal_info = {}
    proposal_info['long_prop_log_number'] = sheet['C8'].value
    proposal_info['short_prop_log_number'] = sheet['C9'].value
    proposal_info['backup_package'] = sheet['C10'].value
    proposal_info['battery_system_controller'] = sheet['C11'].value
    proposal_info['battery_name'] = sheet['C12'].value
    proposal_info['duration_battery_only'] = sheet['C13'].value
    proposal_info['duration_plus_pv'] = sheet['C14'].value
    proposal_info['battery_kwh'] = sheet['C15'].value
    proposal_info['battery_kw'] = sheet['C16'].value
    proposal_info['total_cost_pre_discount'] = "${:,.0f}".format(round(sheet['C17'].value))
    proposal_info['promo_discount'] = "${:,.0f}".format(round(sheet['C19'].value))
    proposal_info['cash_down_payment'] = "${:,.0f}".format(round(sheet['C20'].value))
    proposal_info['total_sys_cost'] = "${:,.0f}".format(round(sheet['C21'].value))
    proposal_info['tax_credit'] = "${:,.0f}".format(round(sheet['C22'].value))
    proposal_info['net_sys_cost'] = "${:,.0f}".format(round(sheet['C23'].value))
    #rebate info
    if rebate_sheet['C8'].value == 1:
        proposal_info['rebate_text'] = sheet['A18'].value
        proposal_info['rebate_amount'] = "${:,.0f}".format(round(sheet['C18'].value))
    else:
        proposal_info['rebate_text'] = " "
        proposal_info['rebate_amount'] = " "
    #json info
    proposal_info['json_for_proposal_log'] = sheet['C24'].value

    return proposal_info
