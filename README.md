
# ```theoriz3r```

## Starting

Install the [Z3 theorem prover](https://pypi.org/project/z3-solver/) with a command like:

```pip install z3-solver```

Clone this repository. Then go to the ```theories/``` directory. Then execute the file "simple_example.py" as a python script. For example, from nvim, run a command like:

```:! python3 %```

Try commenting out the line that reads 

```not_connected,```

and then executing the file again. The file should change (you may have to reload by calling :e). 


## Dependencies

Tested using

```z3-solver 4.11.2.0```

```Python 3.11.1```

## In ```nvim```

For convenience, maybe make a mapping like:

```nnoremap <SOME KEY COMBO> :set cmdheight=2<CR>:exe '! python3 ' . @%<CR>:set cmdheight=1<CR>```

See ```nvimrc.txt``` for more suggested mappings. Setting folding might also help with large files that have a lot of definitions.

## Commands 

The main commands are:

* DeclareMainType(name). Takes a string and declares a variable with that name. 

* properties(properties_list). Takes a list of strings and creates properties with those names. 

* implies(property1, property2). Takes two properties and asserts that, for any X of the main type, if property1 holds of X then so does property2.

* obj(name, property_list). Takes a string and a list of properties, declares an object of type main type, and asserts that the given properties hold of that object. 

* #!. When a ```theoriz3r``` script is called on itself, the first line that begins with #! will be replaced with some open questions.

* ##def property: text. This declares a text associated with the property. 

* #-- DEF property. When the script is called on itself, it replaces lines starting with #-- DEF giving the definition of the property, if one has been declared. 

It is also possible to declare other types and functions, and to directly assert propositions using Z3's syntax by adding them to some attribute of the main type object. Python can be used to list out propositions to assert. 

## License

Copyright 2023 Tsvi Benson-Tilsen

Licensed under the GNU General Public License. 

See LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt






