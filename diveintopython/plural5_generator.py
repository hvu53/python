import re

def build_match_and_apply_functions(pattern, search, replace):
  def matches_rule(word):
    return re.search(pattern, word)
  def apply_rule(word):
    return re.sub(search, replace, word)
  return (matches_rule, apply_rule)

def rules(rules_filename):
  with open(rules_filename, encoding='utf-8') as f:
    for line in f:
      pattern, search, replace = line.split(None,3)
      yield build_match_and_apply_functions(pattern, search, replace)

def plural(noun, rules_filename='plural4-rules.txt'):
  for matches_rule, apply_rule in rules(rules_filename):
    if matches_rule(noun):
      return apply_rule(noun)
  raise ValueError('no matching rule for {0}'.format(noun))