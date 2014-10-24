#-*- coding: utf-8 -*-
'''
@author: giulliano
'''

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from collections import deque
import json
import random
from intelligence.gerador.geradorjogo import GeradorJogo 
from intelligence.analise.analisador import analisador 
from intelligence.pergunta.pergunta import pergunta
from django.views.decorators.cache import never_cache

# import the logging library
import logging
# Get an instance of a logger
logger = logging.getLogger('el-easy')

def home(request):
    return render_to_response('home.html', context_instance=RequestContext(request));


@never_cache
def estoucomsorte(request):
    g = GeradorJogo()
    a = analisador()
    jogo = g.randomico()
    analise = a.analisar_probabilidade_jogo(jogo)
    response_data = {}
    response_data['magic_numbers'] = list(jogo)
    response_data['percent'] = analise
    return HttpResponse(json.dumps(response_data), content_type='application/json')

@never_cache
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

@never_cache
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

@never_cache
def percentual(request):
    response_data = {}
    return HttpResponse(json.dumps(response_data), content_type='application/json')
    
@never_cache
def complete(request):
    response_data = {}
    return HttpResponse(json.dumps(response_data), content_type='application/json')

@never_cache    
def randomico(request):
    return estoucomsorte(request)

@csrf_exempt
@never_cache    
def analise_completa(request):
    a = analisador()
    jogo = deque();
    jogo.append(request.POST["nmr1"])
    jogo.append(request.POST["nmr2"])
    jogo.append(request.POST["nmr3"])
    jogo.append(request.POST["nmr4"])
    jogo.append(request.POST["nmr5"])
    jogo.append(request.POST["nmr6"])
    jogo.append(request.POST["nmr7"])
    jogo.append(request.POST["nmr8"])
    jogo.append(request.POST["nmr9"])
    jogo.append(request.POST["nmr10"]) 
    jogo.append(request.POST["nmr11"])
    jogo.append(request.POST["nmr12"])                                            
    jogo.append(request.POST["nmr13"])
    jogo.append(request.POST["nmr14"])                                            
    jogo.append(request.POST["nmr15"])
    logger.info('Solicitada Analise Completa: ' + str(jogo));
    return HttpResponse(json.dumps({"resultado_analise":a.analise_completa(jogo)}), content_type='application/json')

@csrf_exempt
@never_cache    
def analise_por_tempo(request):
    a = analisador()
    jogo = deque();
    jogo.append(request.POST["nmr1"])
    jogo.append(request.POST["nmr2"])
    jogo.append(request.POST["nmr3"])
    jogo.append(request.POST["nmr4"])
    jogo.append(request.POST["nmr5"])
    jogo.append(request.POST["nmr6"])
    jogo.append(request.POST["nmr7"])
    jogo.append(request.POST["nmr8"])
    jogo.append(request.POST["nmr9"])
    jogo.append(request.POST["nmr10"]) 
    jogo.append(request.POST["nmr11"])
    jogo.append(request.POST["nmr12"])                                            
    jogo.append(request.POST["nmr13"])
    jogo.append(request.POST["nmr14"])                                            
    jogo.append(request.POST["nmr15"])
    logger.info('Solicitada Analise Por Tempo: ' + str(jogo));
    return HttpResponse(json.dumps({"resultado_analise":a.analise_por_tempo(jogo, 2014)}), content_type='application/json')
    
def _500(request):
    return render_to_response('500.html');
def _404(request):
    return render_to_response('404.html');
