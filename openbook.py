__author__ = 'josh'
""" Opens a excel workbook and indexes the respective rows """
import xlrd

class SP:
     def __init__(self, last_name, position):
         self.whois = (last_name, position)

     def setvalues(self, values):
         for attr in values:
             setattr(self, attr, values[attr])

class AP:
     def __init__(self, NAME, Service_No):
         self.whois = (NAME, Service_No)

     def setvalues(self, values):
         for attr in values:
             setattr(self, attr, values[attr])

def openbook(workbook, sheet_type='USR'):
    """
    opens the workbook and creates class SP.  Returns SP with all attributes for each line in the Excel Sheet
    """
    openedbook = xlrd.open_workbook(workbook)
    if sheet_type == 'USR':
        sheet = openedbook.sheet_by_name('Full USR')
    elif sheet_type == 'ALW':
        sheet = openedbook.sheet_by_name('Faslane')
    elif sheet_type == 'LVE':
        sheet = openedbook.sheet_by_name('Absence Details')
    header = sheet.row_values(0)
    for index in range(len(header)):

        if sheet_type == 'ALW':
            header[index] = header[index].replace(' ', '_')
            header[index] = header[index].replace('(', '_')
            header[index] = header[index].replace(')', '_')
            header[index] = header[index].replace('__', '_')
            # print (header[index])

        else:
            header[index] = header[index].replace(' ', '_')

    unit = []
    if sheet_type == 'USR':
        for x in range(1, sheet.nrows):
            sp_dictionary = dict(zip(header, sheet.row_values(x)))
            SP_object = SP(sp_dictionary['Last_Name'], sp_dictionary['Position'])
            SP_object.setvalues(sp_dictionary)
            unit.append(SP_object)
    elif sheet_type == 'ALW':
        for x in range(1, sheet.nrows):
            al_dictionary = dict(zip(header, sheet.row_values(x)))
            AL_object = SP(al_dictionary['NAME'], al_dictionary['Service_No'])
            AL_object.setvalues(al_dictionary)
            unit.append(AL_object)
    elif sheet_type == 'LVE':
        for x in range(1, sheet.nrows):
            lve_dictionary = dict(zip(header, sheet.row_values(x)))
            lve_object = SP(lve_dictionary['Full_Name'], lve_dictionary['Employee_Number'])
            lve_object.setvalues(lve_dictionary)
            unit.append(lve_object)
    return unit




