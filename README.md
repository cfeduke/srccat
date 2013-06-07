# srccat(1)

Syntax highlights a source code file and outputs it to the terminal.

## SYNOPSIS

    srccat PATH

## DESCRIPTION

`srccat` composes a command that maps a source file to its programming language and then uses 
[colout](https://github.com/nojhan/colout) (along with [Pygments](http://pygments.org/)) to syntax highlight the
output.

## INSTALLATION


## DEPENDENCIES

`colout`

## CONFIGURATION

To change the Pygments style used for syntax highlighting, create a .srccat file in your $HOME directory with the
name of the style. If no such file is found monokai is used. If an invalid style is used, Pygments uses its default
style.

To get a list of installed styles:

    $ pygmentize -L

## NOTES

The language mapping dictionary is generated from Pygment's lexer mapping.

## SEE ALSO

* [colout](https://github.com/nojhan/colout)
* [pygments-solarized](https://github.com/cfeduke/pygments-solarized)
