#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lxml import etree


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


if __name__ == "__main__":
    XmluiParser()