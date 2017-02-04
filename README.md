# DSpace XMLUI lang utilities
![Screenshot](https://travis-ci.org/evelthon/dspace-xmlui-lang-util.svg?branch=master )

## About
The aim of this project is to assist in translating the XML UI into 
another language, other than english.

## Operations
1. Create a new `message_xx.xml` file by combining data from 
`message.xml` and an older `message_xx.xml` file. The output of this is
 an xml language file with all messages keys of the latest messages.xml,
  where all translation from an older messages_xx.xml have been ported 
  over. You are left translating of only the newly added keys, without 
  having to check them one by one.
2. Convert a translation xml file to XLSX format. This allows for 
editing translation strings in Office, and give the ability to a 
non-programmer to do the translation.
3. Convert the exported XLSX file back to the native xml file for usage
 by DSpace.

##Quick usage
1. Edit the value of `incomplete_translation_file` and set the filename 
of your old translation file.
2. Place the base `message.xml `and the old translation file 
`message_xx.xml` in the same folder as `lang-util.py`.
3. Issue the command `python3 lang-util.py migrate` to generate a new xml 
file where translation strings from the old translation file are migrated
to the latest xml file format.
4. Issue the command `python3 lang-util.py export` to convert your desired
xml file translation to XLSX and open it in a spreadsheet editor.
5. Issue the command `python3 lang-util.py import` to convert your 
previously exported XLSX file back to the DSpace XMLUI xml file.

###Notes
- You can use non-default filename by parsing variables with each command.
Use `python3 lang-util.py {migrate | export | import} -h` to see
available options.
- Use `python3 lang-util.py -h` for help.