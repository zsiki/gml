# GML

Utilities for GML/XML format

## validator.py

It validates an XML/GML document to a specified xsd schema. It has only command
line interface.

### Usage

validate.py xsd-file gml-file [gml-file ...]

More XML/GML files can be given on the command line. Validation stops on the the
first error.

### Sample

```
./validator.py EING_GML_szabvany_leiras_2.3.xsd minta_gml_kt_251-31_20240403100759_anonim.gml
minta_251_31/minta_gml_kt_251-31_20240403100759_anonim.gml:26:0:ERROR:SCHEMASV:SCHEMAV_ELEMENT_CONTENT: Element '{eing.foldhivatal.hu}HRSZ': This element is not expected. Expected is ( {eing.foldhivatal.hu}FEKVES ).` 
```
