def filter_word(word : str):
  res = ""

  for index, item in enumerate(word):
    if index % 2 == 0:
      res += item

  return res