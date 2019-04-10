#!/bin/env python3
# -*- coding: utf8 -*-

import rpy2.robjects as robjects
from rpy2.robjects.packages import importr
from os import path, environ, getcwd, chdir

import sys
import subprocess
import click

# Altera para diretório de trabalho
chdir(path.dirname(path.realpath(__file__)))

# Carregar ambiente virtual se disponível.
if path.exists('./venv'):
    activate_this = path.join(getcwd(), './venv/bin/activate_this.py')
    with open(activate_this) as file_:
        exec(file_.read(), dict(__file__ = activate_this))


@click.command(name = 'geocode')
@click.option('--delim', default=',', help = 'delimitador no arquivo CSV gerado (default=,).')
@click.argument('entrada', type=str)
@click.argument('saida', type=str)
def comando(delim, entrada, saida):
    r_base = importr('base')
    #infilename = sys.argv[1]
    #outfilename = sys.argv[2]

    match = '([^" ]+)\\\\s+'
    replace = '\\\\1 '

    w = robjects.r('library(foreign); write.csv(lapply(read.spss("%s"), function(x) trimws(gsub(\'%s\', \'%s\', x, perl=TRUE))), file="%s", quote = TRUE, sep = "%s")' % (entrada, match, replace, saida, delim))


comando()
