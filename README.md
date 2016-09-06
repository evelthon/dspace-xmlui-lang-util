# DSpace XMLUI lang utilities
## About
The aim of this project is to assist in translating the XML UI into 
another language, other than english.

It allows you to create a new `message_xx.xml` file by combining data
from `message.xml` and an older `message_xx.xml` file.
The output of this is an xml language file with all messages keys of
the latest messages.xml, where all translation from an older 
messages_xx.xml have been ported over. You are left translating of only
 the newly added keys, without having to check them one by one.


## Usage
1. Place the python script in the same folder, along with `message.xml`
and an older version of a translation `message_xx.xml`.
2. Edit the python script, and update `incomplete_translation_file`
 accordingly.
3. Execute with `python lang-util.py`
