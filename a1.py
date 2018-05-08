import re

def extract_basename(path):
  """Extracts basename of a given path. Should Work with any OS Path on any OS"""
  basename = re.search(r'[^\\/]+(?=[\\/]?$)', path)
  if basename:
    return basename.group(0)


paths = ['a/b/c/', 'a/b/c', '\\a\\b\\c', '\\a\\b\\c\\', 'a\\b\\c',
         'a/b/../../a/b/c/', 'a/b/../../a/b/c']

print [extract_basename(path) for path in paths]
# ['c', 'c', 'c', 'c', 'c', 'c', 'c']


extra_paths = ['C:\\', 'alone', '/a/space in filename', 'C:\\multi\nline']

print [extract_basename(path) for path in extra_paths]
