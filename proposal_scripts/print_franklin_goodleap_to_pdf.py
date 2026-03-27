from all_proposal_standard_info import *

def print_franklin_goodleap_to_pdf(proposal_info, customer_info):
    file_name = franklin_goodleap_10_template
    new_file_name = f"{customer_info['customer_name']} - #{proposal_info['short_prop_log_number']} - {proposal_info['battery_kwh']} - GL.pdf"

    # Create full file paths
    input_file_path = os.path.join(templates_folder, file_name)
    output_file_path = os.path.join(output_folder, new_file_name)

    try:
        # Copy the file to the output folder with the new name
        shutil.copy(input_file_path, output_file_path)

        with open(output_file_path, 'rb') as pdf_file:
            pdf_reader = PdfReader(pdf_file)
            pdf_writer = PdfWriter()

            # Iterate through pages
            for page_num in range(len(pdf_reader.pages)):
                existing_page = pdf_reader.pages[page_num]
                if page_num == 0:  #Page 1
                    packet = BytesIO()
                    can = canvas.Canvas(packet, pagesize=custom_size)
                    # Add content for the first page here
                    can.setFont('HelveticaBold', 16)
                    can.drawString(50, 105, f"{customer_info['customer_name']}")
                    can.setFont('GothamBook', 12)
                    can.drawString(50, 85, f"{customer_info['customer_address_1']}")
                    can.drawString(50, 70, f"{customer_info['customer_address_2']}")
                    can.drawString(10, 10, f"{proposal_info['long_prop_log_number']}")
                    can.save()
                    packet.seek(0)
                    overlay_pdf = PdfReader(packet)
                    existing_page.merge_page(overlay_pdf.pages[0])
                elif page_num == 1:  #Page 2
                    pass
                elif page_num == 2:  #Page 3
                    packet = BytesIO()
                    can = canvas.Canvas(packet, pagesize=custom_size)
                    can.setFont('HelveticaBold', 16)
                    can.drawString(480, 360, f"{proposal_info['backup_package']}")
                    can.setFont('GothamBook', 16)
                    can.drawString(220, 360, f"{proposal_info['battery_system_controller']}")
                    can.drawString(60, 360, f"{proposal_info['battery_name']}")
                    can.drawString(770, 302, f"{proposal_info['duration_battery_only']}")
                    can.drawString(770, 275, f"{proposal_info['duration_plus_pv']}")
                    can.drawString(770, 248, f"{proposal_info['battery_kwh']}")
                    can.drawString(770, 221, f"{proposal_info['battery_kw']}")
                    can.save()
                    packet.seek(0)
                    overlay_pdf = PdfReader(packet)
                    existing_page.merge_page(overlay_pdf.pages[0])
                elif page_num == 3:  #Page 4
                    packet = BytesIO()
                    can = canvas.Canvas(packet, pagesize=custom_size)
                    can.setFont('GothamBook', 24)
                    can.drawString(320, 302, f"{proposal_info['payment_1_18_pay_tax_credit']}")
                    can.drawString(482, 302, f"{proposal_info['payment_19_plus_pay_tax_credit']}")
                    can.drawString(320, 195, f"{proposal_info['payment_1_18_keep_tax_credit']}")
                    can.drawString(482, 195, f"{proposal_info['payment_19_plus_keep_tax_credit']}")
                    can.save()
                    packet.seek(0)
                    overlay_pdf = PdfReader(packet)
                    existing_page.merge_page(overlay_pdf.pages[0])    
                elif page_num == 4:  #Page 5
                    packet = BytesIO()
                    can = canvas.Canvas(packet, pagesize=custom_size)
                    can.setFont('Calibri', 14.04)
                    can.drawString(42, 354, f"{proposal_info['rebate_text']}")
                    can.setFont('GothamBook', 14)
                    can.drawString(325, 377, f"{proposal_info['total_cost_pre_discount']}")
                    can.drawString(325, 355, f"{proposal_info['rebate_amount']}")
                    can.drawString(325, 332, f"{proposal_info['promo_discount']}")
                    can.drawString(325, 309, f"{proposal_info['cash_down_payment']}")
                    can.drawString(325, 287, f"{proposal_info['total_loan_amount']}")
                    can.drawString(325, 241, f"{proposal_info['tax_credit']}")
                    can.drawString(325, 219, f"{proposal_info['net_sys_cost']}")
                    can.drawString(325, 173, f"{proposal_info['apr']}")
                    can.drawString(325, 151, f"{proposal_info['loan_term']} years")
                    can.drawString(325, 129, f"{proposal_info['payment_by_month_18']}")
                    can.drawString(793, 377, f"{proposal_info['battery_kwh']}")
                    can.drawString(793, 355, f"{proposal_info['battery_kw']}")
                    can.drawString(793, 286, f"{customer_info['customer_pv_sys_size']} kW")
                    can.save()
                    packet.seek(0)
                    overlay_pdf = PdfReader(packet)
                    existing_page.merge_page(overlay_pdf.pages[0])
                # Add the modified page to the output PDF
                pdf_writer.add_page(existing_page)
            with open(output_file_path, 'wb') as output_pdf:
                pdf_writer.write(output_pdf)

    except Exception as e:
        print(f"An error occurred: {e}")
