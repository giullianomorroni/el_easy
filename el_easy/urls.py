from django.conf.urls import patterns, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'el_easy.views.home', name='home'),
    url(r'^estoucomsorte/', 'el_easy.views.estoucomsorte', name='estoucomsorte'),
    url(r'^pastelaria/melhores_repeticoes/', 'el_easy.views.melhores_repeticoes', name='melhores_repeticoes'),
    url(r'^pastelaria/melhores_colunas/', 'el_easy.views.melhores_colunas', name='melhores_colunas'),
    url(r'^pastelaria/percentual/', 'el_easy.views.percentual', name='percentual'),
    url(r'^pastelaria/complete/', 'el_easy.views.complete', name='complete'),
    url(r'^pastelaria/randomico/', 'el_easy.views.randomico', name='randomico'),
    url(r'^analisar/analise_por_tempo/', 'el_easy.views.analise_por_tempo', name='analise_por_tempo'),
    url(r'^analisar/analise_completa/', 'el_easy.views.analise_completa', name='analise_completa'),
    
    # url(r'^blog/', include('blog.urls')),
    #url(r'^admin/', include(admin.site.urls)),
)
