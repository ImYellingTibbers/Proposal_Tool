from all_proposal_standard_info import *
def franklin_3_goodleap_prop_data():  

    proposal_info = {}
    proposal_info['long_prop_log_number'] = sheet['D28'].value
    proposal_info['short_prop_log_number'] = sheet['D29'].value
    proposal_info['backup_package'] = sheet['D30'].value
    proposal_info['battery_system_controller'] = sheet['D31'].value
    proposal_info['battery_name'] = sheet['D32'].value
    proposal_info['duration_battery_only'] = sheet['D33'].value
    proposal_info['duration_plus_pv'] = sheet['D34'].value
    proposal_info['battery_kwh'] = sheet['D35'].value
    proposal_info['battery_kw'] = sheet['D36'].value
    proposal_info['payment_1_18_pay_tax_credit'] = "${:,.0f}".format(round(sheet['D37'].value))
    proposal_info['payment_19_plus_pay_tax_credit'] = "${:,.0f}".format(round(sheet['D38'].value))
    proposal_info['payment_1_18_keep_tax_credit'] = "${:,.0f}".format(round(sheet['D39'].value))
    proposal_info['payment_19_plus_keep_tax_credit'] = "${:,.0f}".format(round(sheet['D40'].value))
    proposal_info['total_cost_pre_discount'] = "${:,.0f}".format(round(sheet['D41'].value))
    proposal_info['promo_discount'] = "${:,.0f}".format(round(sheet['D43'].value))
    proposal_info['cash_down_payment'] = "${:,.0f}".format(round(sheet['D44'].value))
    proposal_info['total_loan_amount'] = "${:,.0f}".format(round(sheet['D45'].value))
    proposal_info['tax_credit'] = "${:,.0f}".format(round(sheet['D46'].value))
    proposal_info['net_sys_cost'] = "${:,.0f}".format(round(sheet['D47'].value))
    proposal_info['apr'] = "{:.2f}%".format(sheet['D48'].value * 100)
    proposal_info['loan_term'] = sheet['D49'].value
    proposal_info['payment_by_month_18'] = "${:,.0f}".format(round(sheet['D50'].value))
    #rebate info
    if rebate_sheet['C8'].value == 1:
        proposal_info['rebate_text'] = sheet['A42'].value
        proposal_info['rebate_amount'] = "${:,.0f}".format(round(sheet['D42'].value))
    else:
        proposal_info['rebate_text'] = " "
        proposal_info['rebate_amount'] = " "
    #json info
    proposal_info['json_for_proposal_log'] = sheet['D51'].value

    return proposal_info
