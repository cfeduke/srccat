# srccat(1)

Syntax highlights a source code file and outputs it to the terminal.

## SYNOPSIS

    srccat PATH

## DESCRIPTION

`srccat` composes a command that maps a source file to its programming language and then uses 
[colout](https://github.com/nojhan/colout) (along with [Pygments](http://pygments.org/)) to syntax highlight the
output.

## INSTALLATION

    $ easy_install srccat

On most Unix platforms you will probably need to run the above command with `sudo`.

## DEPENDENCIES

`colout`

## CONFIGURATION

To change the Pygments style used for syntax highlighting, create a .srccat file in your $HOME directory with the
name of the style in a `Config` section (see example). If no such file is found `monokai` is used. If an invalid style 
is used, Pygments uses its default style.

    [Config]
    style: solarizeddark

To get a list of installed styles:

    $ pygmentize -L

## NOTES

The language mapping dictionary is generated from Pygment's lexer mapping.

## TODO

1. For files without extensions examine the first line for a shebang, if present, determine file type from that
1. Language ambiguation overrides in configuration
1. Language ambiguation overrides on command line
1. Style configuration override on command line
1. Style configuration by language
1. Custom extension to language mapping (probably solves bullets 1 and 2)

## SEE ALSO

* [colout](https://github.com/nojhan/colout)
* [pygments-solarized](https://github.com/cfeduke/pygments-solarized)
