#-*- coding: utf-8 -*-
'''
@author: giulliano
'''

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from collections import deque
import json
import random
from intelligence.gerador.geradorjogo import GeradorJogo 
from intelligence.analise.analisador import analisador 
from intelligence.pergunta.pergunta import pergunta

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

def melhores_repeticoes(request):
    g = GeradorJogo()
    a = analisador()
    p = pergunta();
    jogo = g.randomico_com_melhores_repeticoes(p)
    analise = a.analisar_probabilidade_jogo(jogo)
    response_data = {}

    resultado = deque();
    for j in jogo:
        resultado.append(str(j[0]) +"("+ str(j[1])+" repetições)");
    response_data['magic_numbers'] = list(resultado)
    response_data['percent'] = analise
    return HttpResponse(json.dumps(response_data), content_type='application/json')

def melhores_colunas(request):
    g = GeradorJogo()
    a = analisador()
    p = pergunta();
    coluna = random.randint(1, 5)
    jogo = g.randomico_com_melhores_colunas(p, coluna)
    analise = a.analisar_probabilidade_jogo(jogo)
    response_data = {}
    response_data['magic_numbers'] = list(jogo)
    response_data['percent'] = analise
    return HttpResponse(json.dumps(response_data), content_type='application/json')

def percentual(request):
    response_data = {}
    return HttpResponse(json.dumps(response_data), content_type='application/json')
    
def complete(request):
    response_data = {}
    return HttpResponse(json.dumps(response_data), content_type='application/json')
    
def randomico(request):
    return estoucomsorte(request)

def _500(request):
    return render_to_response('500.html');
def _404(request):
    return render_to_response('404.html');
