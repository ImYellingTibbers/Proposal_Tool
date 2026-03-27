import os

# Run this python script to access the tools needed for the prop tool to work

try:
    import openpyxl
except:
    os.system('python -m pip install openpyxl')
    import openpyxl

try:
    import PyPDF2
except:
    os.system('python -m pip install PyPDF2')
    import PyPDF2

try:
    import reportlab
except:
    os.system('python -m pip install reportlab')
    import reportlab

try:
    import requests
except:
    os.system('python -m pip install requests')
    import requests

print("pip installations completed")
input()