text = input()
# # unique_symbols = set()
#
# # for char in text:
# #     unique_symbols.add(char)
# unique_symbols = sorted(set(text))
#
# # for char in sorted(unique_symbols):
# for char in unique_symbols:
#     print(f"{char}: {text.count(char)} time/s")

[print(f"{el}: {text.count(el)} time/s") for el in sorted(set(text))]