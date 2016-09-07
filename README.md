# DSpace XMLUI lang utilities
## About
The aim of this project is to assist in translating the XML UI into 
another language, other than english.

It allows you to:
1. Create a new `message_xx.xml` file by combining data from `message.xml` and an older `message_xx.xml` file. The output of this is an xml language file with all messages keys of the latest messages.xml, where all translation from an older messages_xx.xml have been ported over. You are left translating of only the newly added keys, without having to check them one by one.
2. Convert a translation xml file to XLSX format. This allows for editing translation strings in Office, and give the ability to a non-programmer to do the translation.
3. Convert the exported XLSX file back to the native xml file for usage by DSpace.


## Usage
1. Place the python script in the same folder, along with `message.xml`
and an older version of a translation `message_xx.xml`.
2. Edit the python script, and update `incomplete_translation_file`
 accordingly.
3. Execute with `python3 lang-util.py {migrate | export | import}`



###Note
Use `python3 lang-util.py -h` for help.