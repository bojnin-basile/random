#!/usr/bin/env python
# coding: utf-8

# # Chords in text

inputText = """
    
    [III]
    [II]
    [IV]
    [V]
    [iii]
    [ii]
    [VII::chord]
    [iii][vii][iv][ii][i]
"""
print(inputText)

substitutions = [
    ('[III','[Ⅲ'),
    ('[VII','[Ⅶ'),
    ("[II","[Ⅱ"),
    ('[IV','[Ⅳ'),
    ('[VI','[Ⅵ'),
    ("[I", "[Ⅰ"),
    ('[V','[Ⅴ'),
    ('iii','ⅲ'),
    ('[vii','[ⅶ'),
    ('[ii','[ⅱ'),
    ('[vi','[ⅵ'),
    ('[i','[ⅰ'),
    ('[v','[ⅴ')
     ]

for search, replacement in substitutions:
    outputText=inputText.replace(search, replacement);
    #print('output' + outputText);
    #print('input'+inputText);
    inputText = outputText;
print(inputText)






