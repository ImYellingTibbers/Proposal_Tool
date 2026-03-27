from all_proposal_standard_info import *
def franklin_4_goodleap_prop_data():  

    proposal_info = {}
    proposal_info['long_prop_log_number'] = sheet['E28'].value
    proposal_info['short_prop_log_number'] = sheet['E29'].value
    proposal_info['backup_package'] = sheet['E30'].value
    proposal_info['battery_system_controller'] = sheet['E31'].value
    proposal_info['battery_name'] = sheet['E32'].value
    proposal_info['duration_battery_only'] = sheet['E33'].value
    proposal_info['duration_plus_pv'] = sheet['E34'].value
    proposal_info['battery_kwh'] = sheet['E35'].value
    proposal_info['battery_kw'] = sheet['E36'].value
    proposal_info['payment_1_18_pay_tax_credit'] = "${:,.0f}".format(round(sheet['E37'].value))
    proposal_info['payment_19_plus_pay_tax_credit'] = "${:,.0f}".format(round(sheet['E38'].value))
    proposal_info['payment_1_18_keep_tax_credit'] = "${:,.0f}".format(round(sheet['E39'].value))
    proposal_info['payment_19_plus_keep_tax_credit'] = "${:,.0f}".format(round(sheet['E40'].value))
    proposal_info['total_cost_pre_discount'] = "${:,.0f}".format(round(sheet['E41'].value))
    proposal_info['promo_discount'] = "${:,.0f}".format(round(sheet['E43'].value))
    proposal_info['cash_down_payment'] = "${:,.0f}".format(round(sheet['E44'].value))
    proposal_info['total_loan_amount'] = "${:,.0f}".format(round(sheet['E45'].value))
    proposal_info['tax_credit'] = "${:,.0f}".format(round(sheet['E46'].value))
    proposal_info['net_sys_cost'] = "${:,.0f}".format(round(sheet['E47'].value))
    proposal_info['apr'] = "{:.2f}%".format(sheet['E48'].value * 100)
    proposal_info['loan_term'] = sheet['E49'].value
    proposal_info['payment_by_month_18'] = "${:,.0f}".format(round(sheet['E50'].value))
    #rebate info
    if rebate_sheet['C8'].value == 1:
        proposal_info['rebate_text'] = sheet['A42'].value
        proposal_info['rebate_amount'] = "${:,.0f}".format(round(sheet['E42'].value))
    else:
        proposal_info['rebate_text'] = " "
        proposal_info['rebate_amount'] = " "
    #json info
    proposal_info['json_for_proposal_log'] = sheet['E51'].value

    return proposal_info
