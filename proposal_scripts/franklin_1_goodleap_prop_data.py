from all_proposal_standard_info import *
def franklin_1_goodleap_prop_data():  

    proposal_info = {}
    proposal_info['long_prop_log_number'] = sheet['B28'].value
    proposal_info['short_prop_log_number'] = sheet['B29'].value
    proposal_info['backup_package'] = sheet['B30'].value
    proposal_info['battery_system_controller'] = sheet['B31'].value
    proposal_info['battery_name'] = sheet['B32'].value
    proposal_info['duration_battery_only'] = sheet['B33'].value
    proposal_info['duration_plus_pv'] = sheet['B34'].value
    proposal_info['battery_kwh'] = sheet['B35'].value
    proposal_info['battery_kw'] = sheet['B36'].value
    proposal_info['payment_1_18_pay_tax_credit'] = "${:,.0f}".format(round(sheet['B37'].value))
    proposal_info['payment_19_plus_pay_tax_credit'] = "${:,.0f}".format(round(sheet['B38'].value))
    proposal_info['payment_1_18_keep_tax_credit'] = "${:,.0f}".format(round(sheet['B39'].value))
    proposal_info['payment_19_plus_keep_tax_credit'] = "${:,.0f}".format(round(sheet['B40'].value))
    proposal_info['total_cost_pre_discount'] = "${:,.0f}".format(round(sheet['B41'].value))
    proposal_info['promo_discount'] = "${:,.0f}".format(round(sheet['B43'].value))
    proposal_info['cash_down_payment'] = "${:,.0f}".format(round(sheet['B44'].value))
    proposal_info['total_loan_amount'] = "${:,.0f}".format(round(sheet['B45'].value))
    proposal_info['tax_credit'] = "${:,.0f}".format(round(sheet['B46'].value))
    proposal_info['net_sys_cost'] = "${:,.0f}".format(round(sheet['B47'].value))
    proposal_info['apr'] = "{:.2f}%".format(sheet['B48'].value * 100)
    proposal_info['loan_term'] = sheet['B49'].value
    proposal_info['payment_by_month_18'] = "${:,.0f}".format(round(sheet['B50'].value))
    #rebate info
    if rebate_sheet['C8'].value == 1:
        proposal_info['rebate_text'] = sheet['A42'].value
        proposal_info['rebate_amount'] = "${:,.0f}".format(round(sheet['B42'].value))
    else:
        proposal_info['rebate_text'] = " "
        proposal_info['rebate_amount'] = " "
    #json info
    proposal_info['json_for_proposal_log'] = sheet['B51'].value

    return proposal_info
