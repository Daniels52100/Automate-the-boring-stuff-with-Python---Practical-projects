#! python3
# This program omits Brazillian credit card codes from text on clipboard.

import re, pyperclip
text = pyperclip.paste()

cvcRegex = re.compile(r'''(
    ((cvc?)|(codigo\sde\sverificacao|código\sde\sverificação)(do\scartao|do\scartão)?)   # Código de Verificação do Cartão
    (\s|-|\s-\s|:|:\s)  # espaço
    (\d{3}) # código
)''',re.VERBOSE|re.IGNORECASE)

cardNumberRegex = re.compile(r'''(
    (\d{4}\s*-?\s*){3}
    (\d{4}) # separando o último trecho dos demais para mostrar após a substituição.
)''',re.VERBOSE)

text = cvcRegex.sub(r'\2\6***',text)
text = cardNumberRegex.sub(r'****-****-****-\3', text)
pyperclip.copy(text)
print('Omission complete. New text copied to clipboard.')