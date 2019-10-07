# JSON Files Differences

In this simple project, I created a Python script that compares two JSON files and shows their differences.

The script compares each JSON object, It doesn't compare file lines.

### How to use:

```
#> python json_diffs.py examples\file01.json examples\file02.json
The values in object ID are different: SGML != SL
The values in object GlossTerm are different: Standard Generalized Markup Language != Standard Generalized Language
The values in object Abbrev are different: ISO 8879:1986 != ISO 8559:1986
The values in object GlossSeeAlso are different: ['GML', 'XML'] != ['JSO', 'XML']
The data is different
```
