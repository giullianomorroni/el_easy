#-*- coding: utf-8 -*-
'''
@author: giulliano
'''

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
import json
from intelligence.gerador.geradorjogo import GeradorJogo 
from intelligence.analise.analisador import analisador 

# import the logging library
import logging
# Get an instance of a logger
logger = logging.getLogger('el-easy')

def home(request):
    logger.info('teste log');
    return render_to_response('home.html', context_instance=RequestContext(request));

def estoucomsorte(request):
    g = GeradorJogo()
    a = analisador()
    jogo = g.randomico()
    analise = a.analisar_probabilidade_jogo(jogo)
    response_data = {}
    response_data['magic_numbers'] = list(jogo)
    response_data['percent'] = analise
    return HttpResponse(json.dumps(response_data), content_type='application/json')

#def home_casal(request, apelido):
#    apelido = '#'+apelido
#    assinante = Assinante();
#    casal = assinante.site_casal(apelido)
#    print casal
#    return render_to_response('modelos/arrojado/index.html', {'casal':casal}, context_instance=RequestContext(request));

def _500(request):
    return render_to_response('500.html');
def _404(request):
    return render_to_response('404.html');
