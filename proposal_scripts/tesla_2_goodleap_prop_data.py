from all_proposal_standard_info import *
def tesla_2_goodleap_prop_data():  

    proposal_info = {}
    proposal_info['long_prop_log_number'] = sheet['O28'].value
    proposal_info['short_prop_log_number'] = sheet['O29'].value
    proposal_info['backup_package'] = sheet['O30'].value
    proposal_info['battery_system_controller'] = sheet['O31'].value
    proposal_info['battery_name'] = sheet['O32'].value
    proposal_info['duration_battery_only'] = sheet['O33'].value
    proposal_info['duration_plus_pv'] = sheet['O34'].value
    proposal_info['battery_kwh'] = sheet['O35'].value
    proposal_info['battery_kw'] = sheet['O36'].value
    proposal_info['payment_1_18_pay_tax_credit'] = "${:,.0f}".format(round(sheet['O37'].value))
    proposal_info['payment_19_plus_pay_tax_credit'] = "${:,.0f}".format(round(sheet['O38'].value))
    proposal_info['payment_1_18_keep_tax_credit'] = "${:,.0f}".format(round(sheet['O39'].value))
    proposal_info['payment_19_plus_keep_tax_credit'] = "${:,.0f}".format(round(sheet['O40'].value))
    proposal_info['total_cost_pre_discount'] = "${:,.0f}".format(round(sheet['O41'].value))
    proposal_info['promo_discount'] = "${:,.0f}".format(round(sheet['O43'].value))
    proposal_info['cash_down_payment'] = "${:,.0f}".format(round(sheet['O44'].value))
    proposal_info['total_loan_amount'] = "${:,.0f}".format(round(sheet['O45'].value))
    proposal_info['tax_credit'] = "${:,.0f}".format(round(sheet['O46'].value))
    proposal_info['net_sys_cost'] = "${:,.0f}".format(round(sheet['O47'].value))
    proposal_info['apr'] = "{:.2f}%".format(sheet['O48'].value * 100)
    proposal_info['loan_term'] = sheet['O49'].value
    proposal_info['payment_by_month_18'] = "${:,.0f}".format(round(sheet['O50'].value))
    #rebate info
    if rebate_sheet['C8'].value == 1:
        proposal_info['rebate_text'] = sheet['A42'].value
        proposal_info['rebate_amount'] = "${:,.0f}".format(round(sheet['O42'].value))
    else:
        proposal_info['rebate_text'] = " "
        proposal_info['rebate_amount'] = " "
    #json info
    proposal_info['json_for_proposal_log'] = sheet['O51'].value

    return proposal_info
