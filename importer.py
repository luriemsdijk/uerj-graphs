import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from misc import *
from adjList import *

from file import *
from graphInfo import *
from node import *
from queue import *

from pages.buscaCore import *
from pages.page5 import Busca
from pages.page6 import BuscaCompleta
from pages.page9 import EhConexo
from pages.page10 import TemCiclo
from pages.page11 import EhFloresta
from pages.page12 import EhArvore
from pages.page13 import EhArvore as EhArvore2
from pages.page17 import ObterFlorestaGeradora
from pages.page26 import BuscaProfundidadeI
from pages.page27 import BuscaProfundidadeR
from pages.page57 import BuscaLargura
from pages.page62 import DeterminarDistancias
