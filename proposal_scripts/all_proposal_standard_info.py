import os
import shutil
from pathlib import Path
from openpyxl import load_workbook
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import black
from reportlab.lib.colors import white
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO

###############################################INITIAL-SETUP####################################################
#pip install openpyxl PyPDF2 reportlab requests
#install ttfs for fonts, keep fonts in input folder
################################################################################################################

###############################################VALIDATE#########################################################
#verify version number of excel file
#verify version of pdfs in inputs folder
################################################################################################################

# Version number (**Update this**)
version_number = "v7.5.3"
#prop tool version = 6.1 (use later)

# Path to key folders
base_path = r'C:\\'
proposal_tool_folder = os.path.join(base_path, 'BRS_battery_proposal_tool_' + version_number)
templates_folder = os.path.join(proposal_tool_folder, 'templates_folder')
output_folder = os.path.join(proposal_tool_folder, 'finished_proposals')

# #other folder locations (use later maybe)
# print_to_pdf_folders = {}
# print_to_pdf_folders['enphase_print_to_pdf_folder'] = r'C:\BRS_battery_proposal_tool_v7.4\proposal_scripts\print_to_pdf\enphase'
# print_to_pdf_folders['franklin_print_to_pdf_folder'] = r'C:\BRS_battery_proposal_tool_v7.4\proposal_scripts\print_to_pdf\franklin'
# print_to_pdf_folders['tesla_print_to_pdf_folder'] = r'C:\BRS_battery_proposal_tool_v7.4\proposal_scripts\print_to_pdf\tesla'

# proposal_data_folders = {}
# proposal_data_folders['enphase_proposal_data_folder'] = r'C:\BRS_battery_proposal_tool_v7.4\proposal_scripts\proposal_data\enphase'
# proposal_data_folders['franklin_proposal_data_folder'] = r'C:\BRS_battery_proposal_tool_v7.4\proposal_scripts\proposal_data\franklin'
# proposal_data_folders['tesla_proposal_data_folder'] = r'C:\BRS_battery_proposal_tool_v7.4\proposal_scripts\proposal_data\tesla'

pdfmetrics.registerFont(TTFont('GothamBook', os.path.join(templates_folder, 'GothamBook.ttf')))
pdfmetrics.registerFont(TTFont('Calibri', os.path.join(templates_folder, 'Calibri.ttf')))
pdfmetrics.registerFont(TTFont('HelveticaLt', os.path.join(templates_folder, 'HelveticaLt.ttf')))
pdfmetrics.registerFont(TTFont('HelveticaBold', os.path.join(templates_folder, 'HelveticaBold.ttf')))
custom_size = (14 * 72, 8.5 * 72) #size of the pages in the pdf, 14" by 8.5", multiplied by 72 points per inch. Otherwise words will disappear.

excel_file = None

for file_name in os.listdir(proposal_tool_folder):
    if "MAIN" in file_name.upper() and version_number in file_name:
        excel_file = os.path.join(proposal_tool_folder, file_name)
        break

if excel_file is None:
    print("File not found. Please check your input folder and excel file location are correct")

wb = load_workbook(excel_file, data_only=True)
sheet = wb['PDF Outputs']
rebate_sheet = wb['Rebates']

customer_info = {}
customer_info['customer_id'] = sheet['B1'].value
customer_info['customer_name'] = sheet['B2'].value
customer_info['customer_address_1'] = sheet['B3'].value
customer_info['customer_address_2'] = sheet['B4'].value
customer_info['customer_pv_sys_size'] = sheet['B5'].value

#vvv file_name names vvv

franklin_cash_template = 'FranklinWH Battery Proposal_Cash_v6.1.pdf'
franklin_goodleap_10_template = 'FranklinWH Battery Proposal_GL_v6.1.pdf'
tesla_cash_template = 'Tesla Battery Proposal_Cash_v6.1.pdf'
tesla_goodleap_10_template = 'Tesla Battery Proposal_GL_v6.1.pdf'
