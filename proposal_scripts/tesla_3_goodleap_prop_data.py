from all_proposal_standard_info import *
def tesla_3_goodleap_prop_data():  

    proposal_info = {}
    proposal_info['long_prop_log_number'] = sheet['P28'].value
    proposal_info['short_prop_log_number'] = sheet['P29'].value
    proposal_info['backup_package'] = sheet['P30'].value
    proposal_info['battery_system_controller'] = sheet['P31'].value
    proposal_info['battery_name'] = sheet['P32'].value
    proposal_info['duration_battery_only'] = sheet['P33'].value
    proposal_info['duration_plus_pv'] = sheet['P34'].value
    proposal_info['battery_kwh'] = sheet['P35'].value
    proposal_info['battery_kw'] = sheet['P36'].value
    proposal_info['payment_1_18_pay_tax_credit'] = "${:,.0f}".format(round(sheet['P37'].value))
    proposal_info['payment_19_plus_pay_tax_credit'] = "${:,.0f}".format(round(sheet['P38'].value))
    proposal_info['payment_1_18_keep_tax_credit'] = "${:,.0f}".format(round(sheet['P39'].value))
    proposal_info['payment_19_plus_keep_tax_credit'] = "${:,.0f}".format(round(sheet['P40'].value))
    proposal_info['total_cost_pre_discount'] = "${:,.0f}".format(round(sheet['P41'].value))
    proposal_info['promo_discount'] = "${:,.0f}".format(round(sheet['P43'].value))
    proposal_info['cash_down_payment'] = "${:,.0f}".format(round(sheet['P44'].value))
    proposal_info['total_loan_amount'] = "${:,.0f}".format(round(sheet['P45'].value))
    proposal_info['tax_credit'] = "${:,.0f}".format(round(sheet['P46'].value))
    proposal_info['net_sys_cost'] = "${:,.0f}".format(round(sheet['P47'].value))
    proposal_info['apr'] = "{:.2f}%".format(sheet['P48'].value * 100)
    proposal_info['loan_term'] = sheet['P49'].value
    proposal_info['payment_by_month_18'] = "${:,.0f}".format(round(sheet['P50'].value))
    #rebate info
    if rebate_sheet['C8'].value == 1:
        proposal_info['rebate_text'] = sheet['A42'].value
        proposal_info['rebate_amount'] = "${:,.0f}".format(round(sheet['P42'].value))
    else:
        proposal_info['rebate_text'] = " "
        proposal_info['rebate_amount'] = " "
    #json info
    proposal_info['json_for_proposal_log'] = sheet['P51'].value

    return proposal_info
