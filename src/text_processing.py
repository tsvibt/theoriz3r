import time

G_definition_request_line_start = '#-- DEF '
G_definition_line_start = '##def '
G_discarded_line_start = '#-- '
G_main_command_start = '#!'
G_working_file_name = ''

def WriteQuestions(file):
   global G_working_file_name
   G_working_file_name = '../theories/' + file
   Write(file, Text_Results(Read(file)))

def Text_Results(text):
   if any([line.startswith(G_definition_request_line_start) for line in text.split('\n')]):
      return Text_GiveDefinitions(text)
   else:
      lines = [line for line in text.split('\n') if not line.startswith(G_discarded_line_start)]
      return_lines = []
      operated_yet = False
      most_recent_object_name = None
      for line in lines:
         if 'obj(' in line:
            try:
               most_recent_object_name = line.split("'")[1]
            except:
               most_recent_object_name = line.split('"')[1]
         if operated_yet or not line.startswith(G_main_command_start):
            return_lines.append(line)
         else:
            operated_yet = True
            return_lines.extend(Result(line, most_recent_object_name))
      return '\n'.join(return_lines)

def Text_GiveDefinitions(given_text):
   def LineDefine(line):
      if line.startswith(G_definition_request_line_start):
         definiendum = line[len(G_definition_request_line_start):].split(' ')[0].split(':')[0]
         if definiendum.startswith('not_'):
            definiendum = definiendum[len('not_'):]
         for text in [given_text] + [Read(file) for file in Global_auxiliary_files]:
            for maybe_def_line in text.split('\n'):
               if maybe_def_line.startswith(G_definition_line_start + definiendum):
                  return G_discarded_line_start + ' definition: '  + maybe_def_line[len(G_definition_line_start):]
            
         return G_discarded_line_start + ' no definition found for ' + definiendum
      else:
         return line
   return '\n'.join([LineDefine(line) for line in given_text.split('\n')])


def TimeLine(start_time):
   return [G_discarded_line_start + 'total time taken: ' + str(round(time.time() - start_time, 2))]


def Result(line, most_recent_object_name):
   if line.startswith(G_discarded_line_start):
      return []
   if line.startswith(G_main_command_start):
      start_time = time.time()
      inconsistent,info=PropositionsUnsatisfiable(MainType.all_assertions(),
            unsat_core_get=True, timeout_seconds=20)
      if inconsistent:
         return [line] + [G_discarded_line_start + x for x in ['UNSAT core:']+
         [str(assertion).replace('\n', '') for assertion in info]] + TimeLine(start_time)
      elif info=='timeout':
         return [line, G_discarded_line_start+' timed out trying to satisfy input assertions. maybe the assertions rule out finite models; or maybe they are inconsistent, but for reason z3 does not see. maybe try increasing timeout_seconds, above (in text_processing.py).'] + TimeLine(start_time) 

      initial_check_line = [G_discarded_line_start + 'initial consistency check time: ' + str(round(time.time() - start_time, 2))]
      if 'prop' in line:
         return ([line]  +
             [G_discarded_line_start + x for x in PropertyCombinationQuestions()] +
                 [G_discarded_line_start] + TimeLine(start_time) + initial_check_line)
      else:
         object_questions = Object_ResultLines(globals()[most_recent_object_name])
         if len(object_questions) == 0:
            object_questions = ['no unanswered questions found']
         return ([G_main_command_start + ' ' + most_recent_object_name] + 
               [G_discarded_line_start + x for x in object_questions] +
               [G_discarded_line_start] + TimeLine(start_time) + initial_check_line)
   return [line] 



