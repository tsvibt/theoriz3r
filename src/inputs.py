

Global_auxiliary_files = []
def DeclareAuxiliaryFile(file):
   file = '../theories/' + file
   globals()['Global_auxiliary_files'].append(file)
   exec(open(file).read())

class Type:
   def __init__(self, name: str):
      self.name = name
      self.z3 = z3.DeclareSort(name)
      self.objects = []
      self.properties = []
      self.assertions = []
      self.function_assertions = []
      self.assertion_names = {}
      globals()[name] = self
      self.hints = {}
   def all_nonfunction_assertions(self):
      return self.assertions + [assertion for object in self.objects for assertion in object.assertions]
   def all_assertions(self):
      return self.all_nonfunction_assertions() + self.function_assertions

def DeclareMainType(name):
   globals()['MainType'] = Type(name)
   Variable('X', MainType)
   Variable('Y', MainType)

def Variable(name, typ):
   globals()[name] = z3.Const(name, typ.z3)

def proposition(proposition):
   MainType.assertions.append(proposition)

def obj(name, properties=[], typ=None):
   Object(name, properties, MainType if typ == None else typ)

class Object:
   def __init__(self, name: str, properties, typ):
      self.name = name
      self.z3 = z3.Const(name, typ.z3)
      self.assertions = [property(self.z3) for property in properties]
      typ.objects.append(self)
      globals()[name] = self

class Property:
   def __init__(self, name: str, typ):
      self.name = name
      self.z3 = z3.Function(name, typ.z3, z3.BoolSort())
      if not name.startswith('aux_'):
         typ.properties.append(self)
      globals()['not_'+name]=lambda object: Not(self.z3(object.z3 if type(object) == Object else object))
      globals()[name] = self
   def __call__(self, object):
      return self.z3(object.z3 if type(object) == Object else object)

def properties(property_name_list):
   [Property(property_name, MainType) for property_name in property_name_list] 
   
# assumped to be of maintype, for the X
def implies(property1, property2):
   if type(property1) == list:
      first_property = lambda object1: And([property(object1) for property in property1])
   else:
      first_property = property1
   MainType.assertions.append(ForAll(X, Implies(first_property(X), property2(X))))

def OR(property1, property2):
   return lambda x: Or(property1(x), property2(x))

def binary_function(name):
   globals()[name] = Function(name, MainType.z3, MainType.z3, MainType.z3)

# if we assert the universal statement, stuff takes forever.
def function_preserves(function, binary_boolean, property):
   function_quantify(lambda x,y: Implies(binary_boolean(property(x),
            property(y)), property(function(x,y))))

def function_quantify(function, arity = 2):
   MainType.function_assertions.extend(PropositionFunction_Propositions(function, arity)) 

#given a lambda for 2 things that produces a proposition.... 
def PropositionFunction_Propositions(function, arity = 2):
   return [function(*objects) for objects in 
            itertools.product([object.z3 for object in MainType.objects], repeat=arity)]

def MutuallyExclusiveExhaustive(properties):
   if type(properties[0]) == type(''):
      properties = [globals()[property_name] for property_name in properties]
   for i, property in enumerate(properties): 
      remainder = properties[:i] + properties[i+1:]
      implies(property, lambda x: And([Not(property2(x)) for property2 in remainder]))
      implies(lambda x: And([Not(property2(x)) for property2 in remainder]), property)


# add other combinations? and, or, biimplication (useful for definitions like "A is B and C", eg cadlag)


