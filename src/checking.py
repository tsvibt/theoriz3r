
import ujson

s=z3.Solver()
def PropositionsUnsatisfiable(propositions, unsat_core_get=False, timeout_seconds=.7):
   s.set(timeout=int(timeout_seconds*1000))
   satisfiability = s.check(propositions)
   if satisfiability == z3.unsat:
      return (True, s.unsat_core() if unsat_core_get else 'unsatisfiable')
   elif satisfiability == z3.sat:
      return (False, 'satisfiable')
   else:
      return (False, 'timeout')

def File_Hintsfile(file):
   return '../cached_hints/HINTS_' + file.split('/')[-1]

def Thunk_HandleHints(thunk_function):
   MainType.assertion_names = {assertion: str(assertion) 
                                 for assertion in MainType.all_assertions()}
   try:
      MainType.hints = ujson.loads(Read(File_Hintsfile(G_working_file_name)))
   except:
      MainType.hints = {}
   try:
      return thunk_function()
   finally:
      Write(File_Hintsfile(G_working_file_name), ujson.dumps(MainType.hints))

def PropositionthunkPropositionID_Known(proposition_thunk, proposition_id):
   if PropositionID_TryHint(proposition_id) == 'success':
      return True
   for proposition in [lambda: Not(proposition_thunk()), proposition_thunk]:
      known, core = PropositionsUnsatisfiable([proposition()] + MainType.all_assertions(), unsat_core_get=True)
      if known:
         CorePropositionID_RegisterHint(core, proposition_id)
         return True
   return False

def CorePropositionID_RegisterHint(core, proposition_id):
   MainType.hints[proposition_id] = [MainType.assertion_names[assertion] 
            for assertion in core if assertion in MainType.assertion_names]

def PropositionID_TryHint(proposition_name):
   if proposition_name not in MainType.hints:
      return 'failure'
   else:
      hint_assertion_preconditions = set(MainType.hints[proposition_name])
      for assertion_name in MainType.assertion_names.values():
         hint_assertion_preconditions.discard(assertion_name)
      if hint_assertion_preconditions == set():
         return 'success'
      else:
         MainType.hints.pop(proposition_name)
#         print('hint failed')
         return 'failure'

def Object_ResultLines(object):
   return Thunk_HandleHints(lambda: Object_OpenQuestions(object))

def Object_OpenQuestions(object):
   return [property.name + '?' for property in MainType.properties if 
         not PropositionthunkPropositionID_Known(lambda:property(object), str(property(object)))
         and not property.name.startswith('aux_')]

def PropertyCombinationQuestions():
   return Thunk_HandleHints(PropertyCombinationQuestionsHints)

def PropertyCombinationQuestionsHints():
   lines = []
   max_lines = 5
   for property_count in range(1,4):
      for properties in itertools.combinations(MainType.properties, property_count):
         for truth_values in itertools.product([True, False], repeat=property_count):
            property_truths = list(zip(properties, truth_values))
            if not PropertyTruths_Known(property_truths):
               lines.append(PropertyTruths_String(property_truths) + '?')
               if len(lines)>=max_lines:
                  return lines
   return lines

def PropertyTruths_Known(property_truths):
   thunk = lambda: Exists(X, And([property(X)==truth for property, truth in property_truths]))
   return PropositionthunkPropositionID_Known(thunk, PropertyTruths_String(property_truths))

# why the fuck does this take forever if property_truths is a zip object rather than a list???????
def PropertyTruths_String(property_truths):
   return ', '.join([('' if truth_value else 'not ') + property.name 
               for property, truth_value in property_truths])

