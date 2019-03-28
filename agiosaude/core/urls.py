from django.urls import path
from agiosaude.core import views


urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro_main, name='cadastro_main'),
    path('cadastro/parciente/novo/', views.cadastro_par, name='cadastro_par'),
    path('cadastro/medico/novo/', views.cadastro_med, name='cadastro_med'),
    path('atendimento/', views.atendimento_main, name='atendimento_main'),
    path('atendimento/novo/', views.atendimento_nov, name='atendimento_nov'),
    path('consulta/', views.consulta_main, name='consulta_main'),
    path('ambulatorio/', views.ambulatorio_main, name='ambulatorio_main'),
    path('consulta/eduardo_paiva', views.consulta_par, name='consulta_par'),
    path('resgistro/atendimento', views.registro_ate, name='registro_ate'),
    path('resgistro/exame', views.registro_exa, name='registro_exa'),
]