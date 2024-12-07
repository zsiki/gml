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
try:
    xmlschema_doc = etree.parse(argv[1])
except etree.XMLSyntaxError:
    print(f"{argv[1]} invalid or missing schema file")
    exit(2)
xmlschema = etree.XMLSchema(xmlschema_doc)
for xml in argv[2:]:
    etree.clear_error_log()
    print("-"*60)
    try:
        doc = etree.parse(xml)
    except (OSError, etree.XMLSyntaxError):
        print(f"{xml} invalid or missing XML/GML file")
        continue
        
    valid = xmlschema.validate(doc)
    if not valid:
        print(xmlschema.error_log.last_error)
    else:
        print(f"{xml} is VALID")
