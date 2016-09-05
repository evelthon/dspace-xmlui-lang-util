#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lxml import etree
from openpyxl import Workbook, load_workbook

source_file = 'messages.xml'
incomplete_translation_file = 'messages_el.xml'
output_file = 'output.xml'


class XmluiParser():
    def __init__(self):
        # Parse the non completed translation file
        doc = etree.parse(incomplete_translation_file)
        di = dict()
        for n in doc.getroot().iterdescendants():
            tmp = n.attrib

            '''
                Empty strings (none) are considered false.

                if string:
                    # String is not empty/has content.
                else:
                    # String is empty/does not have content.
            '''
            if tmp.get('key'):
                di[tmp.get('key')] = n.text
                # print(str(tmp.get('key')) + " --  "  + str(n.text))


        # Parse the new English translation
        dest = etree.parse(source_file)
        root = dest.getroot()

        for key, val in di.items():
            # print(key, val)

            if key:
                code = root.xpath("/catalogue/message[@key='" + key + "']")
                if code:
                    code[0].text = val

        f = open(output_file, 'wb')
        f.write(etree.tostring(root, encoding='UTF-8', pretty_print=True))
        f.close()

class SpreadSheet():
    def __init__(self):
        # count_of_keys = len(di)
        #from openpyxl import Workbook, load_workbook
        print("")


    def exportXLSX(self):


        wb = Workbook()
        ws = wb.active
        # create a dict of the contents of the output XML file

        doc = etree.parse(output_file)
        di = dict()
        for n in doc.getroot().iterdescendants():
            tmp = n.attrib
            if tmp.get('key'):
                di[tmp.get('key')] = n.text
                # print(str(tmp.get('key')) + " --  "  + str(n.text))
        for index, (key, val) in enumerate(di.items()):
            print (index, key, val)
            index=index+1
            colA = "A" + str(index)
            colB = "B" + str(index)

            ws[colA] = key
            ws[colB] = val

        wb.save("export.xlsx")

    def importXLSX(self):
        # content goes here
        print("import")

        wb = load_workbook('export.xlsx')
        sheet = wb.get_sheet_by_name('Sheet')
        print(sheet.max_row)
        num_of_keys = sheet.max_row
        for x in range(1, num_of_keys):
            colA = "A" + str(x)
            colB = "B" + str(x)

            #print(sheet[colA].value + "  " + sheet[colB].value)

if __name__ == "__main__":
    XmluiParser()
    # ss = SpreadSheet()
    # ss.exportXLSX()
    # ss.importXLSX()