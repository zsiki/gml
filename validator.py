#!/usr/bin/env python

""" XML validator

    Check XML/GML documents using XSD schema.

    usage validator.py XSD_schema xml_file [xml_file [...]]
"""
from sys import argv
from lxml import etree

if len(argv) < 3:
    print(f"Usage: {argv[0]} xsd_file xml_file [xml_file ...]")
    exit(1)

# load and prepare schema
xmlschema_doc = etree.parse(argv[1])
xmlschema = etree.XMLSchema(xmlschema_doc)
for xml in argv[2:]:
    etree.clear_error_log()
    print("-"*60)
    doc = etree.parse(xml)
    valid = xmlschema.validate(doc)
    if not valid:
        print(xmlschema.error_log.last_error)
    else:
        print(f"{xml} is VALID")
