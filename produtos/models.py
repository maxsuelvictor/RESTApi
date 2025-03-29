from django.db import models

# Create your models here.


class AudTbMAud(models.Model):
    dta_servidor = models.DateField()
    hor_servidor = models.TimeField()
    arq_auditoria = models.BinaryField()
    id_usuario = models.IntegerField(blank=True, null=True)
    id_empresa = models.IntegerField(blank=True, null=True)
    programa = models.CharField(max_length=30, blank=True, null=True)
    id_aud = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'aud_tb_m_aud'
        db_table_comment = 'Tabela de Auditoria'


class BckProducao060223Itens(models.Model):
    id_item = models.IntegerField(primary_key=True)
    ativo = models.BooleanField()
    cardapio = models.BooleanField()
    descricao = models.CharField(max_length=100)
    fantasia = models.CharField(max_length=30, blank=True, null=True)
    referencia = models.CharField(max_length=100, blank=True, null=True)
    aplicacao = models.CharField(max_length=100, blank=True, null=True)
    id_fornecedor = models.IntegerField()
    id_grupo = models.CharField(max_length=11)
    id_und_compra = models.CharField(max_length=3, blank=True, null=True)
    id_und_venda = models.CharField(max_length=3, blank=True, null=True)
    emb_compra = models.FloatField(blank=True, null=True)
    emb_venda = models.FloatField(blank=True, null=True)
    cod_barra = models.CharField(max_length=50, blank=True, null=True)
    cod_fabrica = models.CharField(max_length=30, blank=True, null=True)
    pes_liquido = models.FloatField(blank=True, null=True)
    pes_bruto = models.FloatField(blank=True, null=True)
    est_minimo = models.FloatField(blank=True, null=True)
    loca_rua = models.CharField(max_length=4, blank=True, null=True)
    loca_prateleira = models.CharField(max_length=4, blank=True, null=True)
    loca_escaninho = models.CharField(max_length=4, blank=True, null=True)
    cubagem = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    tam_largura = models.FloatField(blank=True, null=True)
    tam_comprimento = models.FloatField(blank=True, null=True)
    tam_espessura = models.FloatField(blank=True, null=True)
    densidade = models.IntegerField(blank=True, null=True)
    densidade_2 = models.IntegerField(blank=True, null=True)
    densidade_3 = models.IntegerField(blank=True, null=True)
    tipo = models.IntegerField(blank=True, null=True, db_comment='Campo utilizado no sistema de produþÒo\n0 - Normal\n1 - TAMPO  - Utilizado pela bordadeira\n2 - FAIXA  - Utilizado pela bordadeira \n3 - ESPUMA - Utilizado pelo bloco cilindrico  \n')
    geracao_lote_interno = models.IntegerField(blank=True, null=True, db_comment='Campo utilizado no sistema de produþÒo.\nTodo produto tem que ter o seu lote_interno que Ú gerado pelo sistema, isso Ú devido a rastreabilidade.\nO produto pode ter o seu lote gerado a partir de:  \n\n0 - Nota fiscal de entrada, 1 - EspumaþÒo, 2 - Bordadeira, 3 - InspeþÒo de Itens \n, 4 - NÒo utiliza   ')
    destino_reclamado = models.IntegerField(blank=True, null=True, db_comment='Campo utilizado somente no sistema de produþÒo.\nEste campo serß utilizado pela rotina de Atendimento das reclamaþ§es do cliente: PCP_FM_M_ACR.         \n0 - Nenhum\n1 - Flocagem\n2 - Descarte')
    etiq_classificacao_pro = models.IntegerField(blank=True, null=True, db_comment='Campo utilizado no sistema de produþÒo.\nEste campo foi direcinado para a tabela PCP_TB_C_CLE (ID_CLE)')
    etiq_medidas = models.CharField(max_length=60, blank=True, null=True)
    etiq_madeira = models.CharField(max_length=200, blank=True, null=True)
    etiq_espuma1 = models.CharField(max_length=300, blank=True, null=True)
    etiq_espuma2 = models.CharField(max_length=300, blank=True, null=True)
    etiq_espuma3 = models.CharField(max_length=300, blank=True, null=True)
    etiq_revestimento1 = models.CharField(max_length=300, blank=True, null=True)
    etiq_revestimento2 = models.CharField(max_length=300, blank=True, null=True)
    etiq_revestimento3 = models.CharField(max_length=300, blank=True, null=True)
    etiq_recomendacoes_1 = models.CharField(max_length=80, blank=True, null=True)
    etiq_recomendacoes_2 = models.CharField(max_length=80, blank=True, null=True)
    lote_fabric_obrigatorio = models.IntegerField(blank=True, null=True, db_comment='Este campo Ú utilizado pela tela controle de inspeþÒo e recebimento de produto (EST_FM_M_NFE_S). \nIsso server para dizer se o campo lote do fabricante Ú obrigat¾rio.')
    id_ncm = models.CharField(max_length=10, blank=True, null=True)
    preco_avista = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True, db_comment='Descricao completa, campo utilizado no enBueld.')
    preco_aprazo = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    dta_cadastro = models.DateField(blank=True, null=True)
    etiq_modelo = models.CharField(max_length=70, blank=True, null=True)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    id_familia = models.IntegerField(blank=True, null=True)
    des_completa = models.CharField(max_length=250, blank=True, null=True)
    rt_pricipio_ativo = models.CharField(max_length=400, blank=True, null=True)
    rt_composicao = models.CharField(max_length=400, blank=True, null=True)
    ret_emb_capacidade = models.CharField(max_length=20, blank=True, null=True)
    ret_emb_nao_lavavel = models.IntegerField(blank=True, null=True, db_comment='0 - Contaminada\n1 - NÒo-Contaminada')
    ret_emb_lavaveis = models.IntegerField(blank=True, null=True, db_comment='0 - Plßstico\n1 - Metal\n2 - Vidro')
    cod_onu = models.CharField(max_length=20, blank=True, null=True)
    sgq_critica_laudo_fab = models.BooleanField(blank=True, null=True, db_comment='Este campo serß utilizado pela tela de InspeþÒo de Itens (FAT_FM_M_IQM).')
    tam_observacoes = models.CharField(max_length=150, blank=True, null=True)
    etiq_id_cue = models.IntegerField(blank=True, null=True, db_comment='Refere-se a tabela PCP_TB_C_CUE.')
    preco_avista_ant_reajuste = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    preco_aprazo_ant_reajuste = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    dta_ult_reajuste = models.DateField(blank=True, null=True)
    rt_registro = models.CharField(max_length=25, blank=True, null=True)
    custo_servico = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    id_grupo_prod = models.IntegerField(blank=True, null=True)
    id_item_anterior = models.IntegerField(blank=True, null=True)
    preco_sugerido = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    per_cmv_interno = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    per_cmv_externo = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    etiq_espuma4 = models.CharField(max_length=300, blank=True, null=True)
    etiq_espuma5 = models.CharField(max_length=300, blank=True, null=True)
    etiq_espuma6 = models.CharField(max_length=300, blank=True, null=True)
    etiq_revestimento4 = models.CharField(max_length=300, blank=True, null=True)
    etiq_revestimento5 = models.CharField(max_length=300, blank=True, null=True)
    etiq_revestimento6 = models.CharField(max_length=300, blank=True, null=True)
    etiq_marca = models.CharField(max_length=30, blank=True, null=True)
    sgq_tamanho_ite_epp = models.FloatField(blank=True, null=True, db_comment='Campo utilizado pelo relat¾rio de Entrada de Produto Acabado')
    tipo_servico = models.BooleanField(blank=True, null=True)
    mob_nome_foto = models.CharField(max_length=60, blank=True, null=True)
    pneu_largura = models.CharField(max_length=10, blank=True, null=True)
    pneu_altura = models.CharField(max_length=10, blank=True, null=True)
    pneu_aro = models.CharField(max_length=10, blank=True, null=True)
    id_marca = models.IntegerField(blank=True, null=True)
    sgq_personalizado = models.BooleanField(blank=True, null=True, db_comment='produto utilizado pelo m¾dulo sgq.')
    temp_etiq_medidas = models.CharField(max_length=60, blank=True, null=True)
    cod_item_prod = models.IntegerField(blank=True, null=True, db_comment='c¾digo do item da produþÒo ')
    etiq_tipo_produto = models.IntegerField(blank=True, null=True, db_comment='0 - COLCH├O DE ESPUMA\r\n1 - COLCH├O BOX CONJUGADO\r\n2 - COLCH├O AUXILIAR\r\n3 - COLCH├O MISTO\r\n')
    tam_esp_espessura_1 = models.FloatField(blank=True, null=True)
    tam_esp_espessura_2 = models.FloatField(blank=True, null=True)
    tam_esp_espessura_3 = models.FloatField(blank=True, null=True)
    tam_esp_comprimento_1 = models.FloatField(blank=True, null=True)
    tam_esp_comprimento_2 = models.FloatField(blank=True, null=True)
    tam_esp_comprimento_3 = models.FloatField(blank=True, null=True)
    tam_esp_largura_1 = models.FloatField(blank=True, null=True)
    tam_esp_largura_2 = models.FloatField(blank=True, null=True)
    tam_esp_largura_3 = models.FloatField(blank=True, null=True)
    cubagem_esp_1 = models.FloatField(blank=True, null=True)
    cubagem_esp_2 = models.FloatField(blank=True, null=True)
    cubagem_esp_3 = models.FloatField(blank=True, null=True)
    tipo_produto = models.IntegerField(blank=True, null=True, db_comment='0 - NÒo especificado\r\n1 - Manual do Usußrio')
    tam_esp_espessura_revest_1 = models.FloatField(blank=True, null=True)
    tam_esp_espessura_revest_2 = models.FloatField(blank=True, null=True)
    tam_esp_comp_revest_1 = models.FloatField(blank=True, null=True)
    tam_esp_comp_revest_2 = models.FloatField(blank=True, null=True)
    tam_esp_largura_revest_1 = models.FloatField(blank=True, null=True)
    tam_esp_largura_revest_2 = models.FloatField(blank=True, null=True)
    cubagem_esp_revest_1 = models.FloatField(blank=True, null=True)
    cubagem_esp_revest_2 = models.FloatField(blank=True, null=True)
    densidade_esp_revest_1 = models.FloatField(blank=True, null=True)
    densidade_esp_revest_2 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bck_producao_060223_itens'
        db_table_comment = 'Cadastro de Itens'


class BckProducao180723Itens(models.Model):
    id_item = models.IntegerField(primary_key=True)
    ativo = models.BooleanField()
    cardapio = models.BooleanField()
    descricao = models.CharField(max_length=100)
    fantasia = models.CharField(max_length=30, blank=True, null=True)
    referencia = models.CharField(max_length=100, blank=True, null=True)
    aplicacao = models.CharField(max_length=100, blank=True, null=True)
    id_fornecedor = models.ForeignKey('CadTbCFor', models.DO_NOTHING, db_column='id_fornecedor')
    id_grupo = models.ForeignKey('CadTbCGru', models.DO_NOTHING, db_column='id_grupo')
    id_und_compra = models.ForeignKey('CadTbCUnd', models.DO_NOTHING, db_column='id_und_compra', blank=True, null=True)
    id_und_venda = models.ForeignKey('CadTbCUnd', models.DO_NOTHING, db_column='id_und_venda', related_name='bckproducao180723itens_id_und_venda_set', blank=True, null=True)
    emb_compra = models.FloatField(blank=True, null=True)
    emb_venda = models.FloatField(blank=True, null=True)
    cod_barra = models.CharField(max_length=50, blank=True, null=True)
    cod_fabrica = models.CharField(max_length=30, blank=True, null=True)
    pes_liquido = models.FloatField(blank=True, null=True)
    pes_bruto = models.FloatField(blank=True, null=True)
    est_minimo = models.FloatField(blank=True, null=True)
    loca_rua = models.CharField(max_length=4, blank=True, null=True)
    loca_prateleira = models.CharField(max_length=4, blank=True, null=True)
    loca_escaninho = models.CharField(max_length=4, blank=True, null=True)
    cubagem = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    tam_largura = models.FloatField(blank=True, null=True)
    tam_comprimento = models.FloatField(blank=True, null=True)
    tam_espessura = models.FloatField(blank=True, null=True)
    densidade = models.IntegerField(blank=True, null=True)
    densidade_2 = models.IntegerField(blank=True, null=True)
    densidade_3 = models.IntegerField(blank=True, null=True)
    tipo = models.IntegerField(blank=True, null=True, db_comment='Campo utilizado no sistema de produþÒo\n0 - Normal\n1 - TAMPO  - Utilizado pela bordadeira\n2 - FAIXA  - Utilizado pela bordadeira \n3 - ESPUMA - Utilizado pelo bloco cilindrico  \n')
    geracao_lote_interno = models.IntegerField(blank=True, null=True, db_comment='Campo utilizado no sistema de produþÒo.\nTodo produto tem que ter o seu lote_interno que Ú gerado pelo sistema, isso Ú devido a rastreabilidade.\nO produto pode ter o seu lote gerado a partir de:  \n\n0 - Nota fiscal de entrada, 1 - EspumaþÒo, 2 - Bordadeira, 3 - InspeþÒo de Itens \n, 4 - NÒo utiliza   ')
    destino_reclamado = models.IntegerField(blank=True, null=True, db_comment='Campo utilizado somente no sistema de produþÒo.\nEste campo serß utilizado pela rotina de Atendimento das reclamaþ§es do cliente: PCP_FM_M_ACR.         \n0 - Nenhum\n1 - Flocagem\n2 - Descarte')
    etiq_classificacao_pro = models.IntegerField(blank=True, null=True, db_comment='Campo utilizado no sistema de produþÒo.\nEste campo foi direcinado para a tabela PCP_TB_C_CLE (ID_CLE)')
    etiq_medidas = models.CharField(max_length=60, blank=True, null=True)
    etiq_madeira = models.CharField(max_length=200, blank=True, null=True)
    etiq_espuma1 = models.CharField(max_length=300, blank=True, null=True)
    etiq_espuma2 = models.CharField(max_length=300, blank=True, null=True)
    etiq_espuma3 = models.CharField(max_length=300, blank=True, null=True)
    etiq_revestimento1 = models.CharField(max_length=300, blank=True, null=True)
    etiq_revestimento2 = models.CharField(max_length=300, blank=True, null=True)
    etiq_revestimento3 = models.CharField(max_length=300, blank=True, null=True)
    etiq_recomendacoes_1 = models.CharField(max_length=80, blank=True, null=True)
    etiq_recomendacoes_2 = models.CharField(max_length=80, blank=True, null=True)
    lote_fabric_obrigatorio = models.IntegerField(blank=True, null=True, db_comment='Este campo Ú utilizado pela tela controle de inspeþÒo e recebimento de produto (EST_FM_M_NFE_S). \nIsso server para dizer se o campo lote do fabricante Ú obrigat¾rio.')
    id_ncm = models.ForeignKey('CadTbCNcm', models.DO_NOTHING, db_column='id_ncm', blank=True, null=True)
    preco_avista = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True, db_comment='Descricao completa, campo utilizado no enBueld.')
    preco_aprazo = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    dta_cadastro = models.DateField(blank=True, null=True)
    etiq_modelo = models.CharField(max_length=70, blank=True, null=True)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    id_familia = models.ForeignKey('CadTbCFam', models.DO_NOTHING, db_column='id_familia', blank=True, null=True)
    des_completa = models.CharField(max_length=250, blank=True, null=True)
    rt_pricipio_ativo = models.CharField(max_length=400, blank=True, null=True)
    rt_composicao = models.CharField(max_length=400, blank=True, null=True)
    ret_emb_capacidade = models.CharField(max_length=20, blank=True, null=True)
    ret_emb_nao_lavavel = models.IntegerField(blank=True, null=True, db_comment='0 - Contaminada\n1 - NÒo-Contaminada')
    ret_emb_lavaveis = models.IntegerField(blank=True, null=True, db_comment='0 - Plßstico\n1 - Metal\n2 - Vidro')
    cod_onu = models.CharField(max_length=20, blank=True, null=True)
    sgq_critica_laudo_fab = models.BooleanField(blank=True, null=True, db_comment='Este campo serß utilizado pela tela de InspeþÒo de Itens (FAT_FM_M_IQM).')
    tam_observacoes = models.CharField(max_length=150, blank=True, null=True)
    etiq_id_cue = models.IntegerField(blank=True, null=True, db_comment='Refere-se a tabela PCP_TB_C_CUE.')
    preco_avista_ant_reajuste = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    preco_aprazo_ant_reajuste = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    dta_ult_reajuste = models.DateField(blank=True, null=True)
    rt_registro = models.CharField(max_length=25, blank=True, null=True)
    custo_servico = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    id_grupo_prod = models.ForeignKey('CadTbCGrp', models.DO_NOTHING, db_column='id_grupo_prod', blank=True, null=True)
    id_item_anterior = models.IntegerField(blank=True, null=True)
    preco_sugerido = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    per_cmv_interno = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    per_cmv_externo = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    etiq_espuma4 = models.CharField(max_length=300, blank=True, null=True)
    etiq_espuma5 = models.CharField(max_length=300, blank=True, null=True)
    etiq_espuma6 = models.CharField(max_length=300, blank=True, null=True)
    etiq_revestimento4 = models.CharField(max_length=300, blank=True, null=True)
    etiq_revestimento5 = models.CharField(max_length=300, blank=True, null=True)
    etiq_revestimento6 = models.CharField(max_length=300, blank=True, null=True)
    etiq_marca = models.CharField(max_length=30, blank=True, null=True)
    sgq_tamanho_ite_epp = models.FloatField(blank=True, null=True, db_comment='Campo utilizado pelo relat¾rio de Entrada de Produto Acabado')
    tipo_servico = models.BooleanField(blank=True, null=True)
    mob_nome_foto = models.CharField(max_length=60, blank=True, null=True)
    pneu_largura = models.CharField(max_length=10, blank=True, null=True)
    pneu_altura = models.CharField(max_length=10, blank=True, null=True)
    pneu_aro = models.CharField(max_length=10, blank=True, null=True)
    id_marca = models.IntegerField(blank=True, null=True)
    sgq_personalizado = models.BooleanField(blank=True, null=True, db_comment='produto utilizado pelo m¾dulo sgq.')
    temp_etiq_medidas = models.CharField(max_length=60, blank=True, null=True)
    cod_item_prod = models.IntegerField(blank=True, null=True, db_comment='c¾digo do item da produþÒo ')
    etiq_tipo_produto = models.IntegerField(blank=True, null=True, db_comment='0 - COLCH├O DE ESPUMA\r\n1 - COLCH├O BOX CONJUGADO\r\n2 - COLCH├O AUXILIAR\r\n3 - COLCH├O MISTO\r\n')
    tam_esp_espessura_1 = models.FloatField(blank=True, null=True)
    tam_esp_espessura_2 = models.FloatField(blank=True, null=True)
    tam_esp_espessura_3 = models.FloatField(blank=True, null=True)
    tam_esp_comprimento_1 = models.FloatField(blank=True, null=True)
    tam_esp_comprimento_2 = models.FloatField(blank=True, null=True)
    tam_esp_comprimento_3 = models.FloatField(blank=True, null=True)
    tam_esp_largura_1 = models.FloatField(blank=True, null=True)
    tam_esp_largura_2 = models.FloatField(blank=True, null=True)
    tam_esp_largura_3 = models.FloatField(blank=True, null=True)
    cubagem_esp_1 = models.FloatField(blank=True, null=True)
    cubagem_esp_2 = models.FloatField(blank=True, null=True)
    cubagem_esp_3 = models.FloatField(blank=True, null=True)
    tipo_produto = models.IntegerField(blank=True, null=True, db_comment='0 - NÒo especificado\r\n1 - Manual do Usußrio')
    tam_esp_espessura_revest_1 = models.FloatField(blank=True, null=True)
    tam_esp_espessura_revest_2 = models.FloatField(blank=True, null=True)
    tam_esp_comp_revest_1 = models.FloatField(blank=True, null=True)
    tam_esp_comp_revest_2 = models.FloatField(blank=True, null=True)
    tam_esp_largura_revest_1 = models.FloatField(blank=True, null=True)
    tam_esp_largura_revest_2 = models.FloatField(blank=True, null=True)
    cubagem_esp_revest_1 = models.FloatField(blank=True, null=True)
    cubagem_esp_revest_2 = models.FloatField(blank=True, null=True)
    densidade_esp_revest_1 = models.FloatField(blank=True, null=True)
    densidade_esp_revest_2 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bck_producao_180723_itens'
        db_table_comment = 'Cadastro de Itens'


class BckProducao260921Itens(models.Model):
    id_item = models.IntegerField(primary_key=True)
    ativo = models.BooleanField()
    cardapio = models.BooleanField()
    descricao = models.CharField(max_length=100)
    fantasia = models.CharField(max_length=30, blank=True, null=True)
    referencia = models.CharField(max_length=100, blank=True, null=True)
    aplicacao = models.CharField(max_length=100, blank=True, null=True)
    id_fornecedor = models.IntegerField()
    id_grupo = models.CharField(max_length=11)
    id_und_compra = models.CharField(max_length=3, blank=True, null=True)
    id_und_venda = models.CharField(max_length=3, blank=True, null=True)
    emb_compra = models.FloatField(blank=True, null=True)
    emb_venda = models.FloatField(blank=True, null=True)
    cod_barra = models.CharField(max_length=50, blank=True, null=True)
    cod_fabrica = models.CharField(max_length=30, blank=True, null=True)
    pes_liquido = models.FloatField(blank=True, null=True)
    pes_bruto = models.FloatField(blank=True, null=True)
    est_minimo = models.FloatField(blank=True, null=True)
    loca_rua = models.CharField(max_length=4, blank=True, null=True)
    loca_prateleira = models.CharField(max_length=4, blank=True, null=True)
    loca_escaninho = models.CharField(max_length=4, blank=True, null=True)
    cubagem = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    tam_largura = models.FloatField(blank=True, null=True)
    tam_comprimento = models.FloatField(blank=True, null=True)
    tam_espessura = models.FloatField(blank=True, null=True)
    densidade = models.IntegerField(blank=True, null=True)
    densidade_2 = models.IntegerField(blank=True, null=True)
    densidade_3 = models.IntegerField(blank=True, null=True)
    tipo = models.IntegerField(blank=True, null=True, db_comment='Campo utilizado no sistema de produþÒo\n0 - Normal\n1 - TAMPO  - Utilizado pela bordadeira\n2 - FAIXA  - Utilizado pela bordadeira \n3 - ESPUMA - Utilizado pelo bloco cilindrico  \n')
    geracao_lote_interno = models.IntegerField(blank=True, null=True, db_comment='Campo utilizado no sistema de produþÒo.\nTodo produto tem que ter o seu lote_interno que Ú gerado pelo sistema, isso Ú devido a rastreabilidade.\nO produto pode ter o seu lote gerado a partir de:  \n\n0 - Nota fiscal de entrada, 1 - EspumaþÒo, 2 - Bordadeira, 3 - InspeþÒo de Itens \n, 4 - NÒo utiliza   ')
    destino_reclamado = models.IntegerField(blank=True, null=True, db_comment='Campo utilizado somente no sistema de produþÒo.\nEste campo serß utilizado pela rotina de Atendimento das reclamaþ§es do cliente: PCP_FM_M_ACR.         \n0 - Nenhum\n1 - Flocagem\n2 - Descarte')
    etiq_classificacao_pro = models.IntegerField(blank=True, null=True, db_comment='Campo utilizado no sistema de produþÒo.\nEste campo foi direcinado para a tabela PCP_TB_C_CLE (ID_CLE)')
    etiq_medidas = models.CharField(max_length=60, blank=True, null=True)
    etiq_madeira = models.CharField(max_length=200, blank=True, null=True)
    etiq_espuma1 = models.CharField(max_length=300, blank=True, null=True)
    etiq_espuma2 = models.CharField(max_length=300, blank=True, null=True)
    etiq_espuma3 = models.CharField(max_length=300, blank=True, null=True)
    etiq_revestimento1 = models.CharField(max_length=300, blank=True, null=True)
    etiq_revestimento2 = models.CharField(max_length=300, blank=True, null=True)
    etiq_revestimento3 = models.CharField(max_length=300, blank=True, null=True)
    etiq_recomendacoes_1 = models.CharField(max_length=80, blank=True, null=True)
    etiq_recomendacoes_2 = models.CharField(max_length=80, blank=True, null=True)
    lote_fabric_obrigatorio = models.IntegerField(blank=True, null=True, db_comment='Este campo Ú utilizado pela tela controle de inspeþÒo e recebimento de produto (EST_FM_M_NFE_S). \nIsso server para dizer se o campo lote do fabricante Ú obrigat¾rio.')
    id_ncm = models.CharField(max_length=10, blank=True, null=True)
    preco_avista = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True, db_comment='Descricao completa, campo utilizado no enBueld.')
    preco_aprazo = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    dta_cadastro = models.DateField(blank=True, null=True)
    etiq_modelo = models.CharField(max_length=70, blank=True, null=True)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    id_familia = models.IntegerField(blank=True, null=True)
    des_completa = models.CharField(max_length=250, blank=True, null=True)
    rt_pricipio_ativo = models.CharField(max_length=400, blank=True, null=True)
    rt_composicao = models.CharField(max_length=400, blank=True, null=True)
    ret_emb_capacidade = models.CharField(max_length=20, blank=True, null=True)
    ret_emb_nao_lavavel = models.IntegerField(blank=True, null=True, db_comment='0 - Contaminada\n1 - NÒo-Contaminada')
    ret_emb_lavaveis = models.IntegerField(blank=True, null=True, db_comment='0 - Plßstico\n1 - Metal\n2 - Vidro')
    cod_onu = models.CharField(max_length=20, blank=True, null=True)
    sgq_critica_laudo_fab = models.BooleanField(blank=True, null=True, db_comment='Este campo serß utilizado pela tela de InspeþÒo de Itens (FAT_FM_M_IQM).')
    tam_observacoes = models.CharField(max_length=150, blank=True, null=True)
    etiq_id_cue = models.IntegerField(blank=True, null=True, db_comment='Refere-se a tabela PCP_TB_C_CUE.')
    preco_avista_ant_reajuste = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    preco_aprazo_ant_reajuste = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    dta_ult_reajuste = models.DateField(blank=True, null=True)
    rt_registro = models.CharField(max_length=25, blank=True, null=True)
    custo_servico = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    id_grupo_prod = models.IntegerField(blank=True, null=True)
    id_item_anterior = models.IntegerField(blank=True, null=True)
    preco_sugerido = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    per_cmv_interno = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    per_cmv_externo = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    etiq_espuma4 = models.CharField(max_length=300, blank=True, null=True)
    etiq_espuma5 = models.CharField(max_length=300, blank=True, null=True)
    etiq_espuma6 = models.CharField(max_length=300, blank=True, null=True)
    etiq_revestimento4 = models.CharField(max_length=300, blank=True, null=True)
    etiq_revestimento5 = models.CharField(max_length=300, blank=True, null=True)
    etiq_revestimento6 = models.CharField(max_length=300, blank=True, null=True)
    etiq_marca = models.CharField(max_length=30, blank=True, null=True)
    sgq_tamanho_ite_epp = models.FloatField(blank=True, null=True, db_comment='Campo utilizado pelo relat¾rio de Entrada de Produto Acabado')
    tipo_servico = models.BooleanField(blank=True, null=True)
    mob_nome_foto = models.CharField(max_length=60, blank=True, null=True)
    pneu_largura = models.CharField(max_length=10, blank=True, null=True)
    pneu_altura = models.CharField(max_length=10, blank=True, null=True)
    pneu_aro = models.CharField(max_length=10, blank=True, null=True)
    id_marca = models.IntegerField(blank=True, null=True)
    sgq_personalizado = models.BooleanField(blank=True, null=True, db_comment='produto utilizado pelo m¾dulo sgq.')
    temp_etiq_medidas = models.CharField(max_length=60, blank=True, null=True)
    cod_item_prod = models.IntegerField(blank=True, null=True, db_comment='c¾digo do item da produþÒo ')
    etiq_tipo_produto = models.IntegerField(blank=True, null=True, db_comment='0 - COLCH├O DE ESPUMA\r\n1 - COLCH├O BOX CONJUGADO\r\n2 - COLCH├O AUXILIAR\r\n3 - COLCH├O MISTO\r\n')
    tam_esp_espessura_1 = models.FloatField(blank=True, null=True)
    tam_esp_espessura_2 = models.FloatField(blank=True, null=True)
    tam_esp_espessura_3 = models.FloatField(blank=True, null=True)
    tam_esp_comprimento_1 = models.FloatField(blank=True, null=True)
    tam_esp_comprimento_2 = models.FloatField(blank=True, null=True)
    tam_esp_comprimento_3 = models.FloatField(blank=True, null=True)
    tam_esp_largura_1 = models.FloatField(blank=True, null=True)
    tam_esp_largura_2 = models.FloatField(blank=True, null=True)
    tam_esp_largura_3 = models.FloatField(blank=True, null=True)
    cubagem_esp_1 = models.FloatField(blank=True, null=True)
    cubagem_esp_2 = models.FloatField(blank=True, null=True)
    cubagem_esp_3 = models.FloatField(blank=True, null=True)
    tipo_produto = models.IntegerField(blank=True, null=True, db_comment='0 - NÒo especificado\r\n1 - Manual do Usußrio')

    class Meta:
        managed = False
        db_table = 'bck_producao_260921_itens'
        db_table_comment = 'Cadastro de Itens'


class BckProducao270922Itens(models.Model):
    id_item = models.IntegerField(primary_key=True)
    ativo = models.BooleanField()
    cardapio = models.BooleanField()
    descricao = models.CharField(max_length=100)
    fantasia = models.CharField(max_length=30, blank=True, null=True)
    referencia = models.CharField(max_length=100, blank=True, null=True)
    aplicacao = models.CharField(max_length=100, blank=True, null=True)
    id_fornecedor = models.ForeignKey('CadTbCFor', models.DO_NOTHING, db_column='id_fornecedor')
    id_grupo = models.ForeignKey('CadTbCGru', models.DO_NOTHING, db_column='id_grupo')
    id_und_compra = models.ForeignKey('CadTbCUnd', models.DO_NOTHING, db_column='id_und_compra', blank=True, null=True)
    id_und_venda = models.ForeignKey('CadTbCUnd', models.DO_NOTHING, db_column='id_und_venda', related_name='bckproducao270922itens_id_und_venda_set', blank=True, null=True)
    emb_compra = models.FloatField(blank=True, null=True)
    emb_venda = models.FloatField(blank=True, null=True)
    cod_barra = models.CharField(max_length=50, blank=True, null=True)
    cod_fabrica = models.CharField(max_length=30, blank=True, null=True)
    pes_liquido = models.FloatField(blank=True, null=True)
    pes_bruto = models.FloatField(blank=True, null=True)
    est_minimo = models.FloatField(blank=True, null=True)
    loca_rua = models.CharField(max_length=4, blank=True, null=True)
    loca_prateleira = models.CharField(max_length=4, blank=True, null=True)
    loca_escaninho = models.CharField(max_length=4, blank=True, null=True)
    cubagem = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    tam_largura = models.FloatField(blank=True, null=True)
    tam_comprimento = models.FloatField(blank=True, null=True)
    tam_espessura = models.FloatField(blank=True, null=True)
    densidade = models.IntegerField(blank=True, null=True)
    densidade_2 = models.IntegerField(blank=True, null=True)
    densidade_3 = models.IntegerField(blank=True, null=True)
    tipo = models.IntegerField(blank=True, null=True, db_comment='Campo utilizado no sistema de produþÒo\n0 - Normal\n1 - TAMPO  - Utilizado pela bordadeira\n2 - FAIXA  - Utilizado pela bordadeira \n3 - ESPUMA - Utilizado pelo bloco cilindrico  \n')
    geracao_lote_interno = models.IntegerField(blank=True, null=True, db_comment='Campo utilizado no sistema de produþÒo.\nTodo produto tem que ter o seu lote_interno que Ú gerado pelo sistema, isso Ú devido a rastreabilidade.\nO produto pode ter o seu lote gerado a partir de:  \n\n0 - Nota fiscal de entrada, 1 - EspumaþÒo, 2 - Bordadeira, 3 - InspeþÒo de Itens \n, 4 - NÒo utiliza   ')
    destino_reclamado = models.IntegerField(blank=True, null=True, db_comment='Campo utilizado somente no sistema de produþÒo.\nEste campo serß utilizado pela rotina de Atendimento das reclamaþ§es do cliente: PCP_FM_M_ACR.         \n0 - Nenhum\n1 - Flocagem\n2 - Descarte')
    etiq_classificacao_pro = models.IntegerField(blank=True, null=True, db_comment='Campo utilizado no sistema de produþÒo.\nEste campo foi direcinado para a tabela PCP_TB_C_CLE (ID_CLE)')
    etiq_medidas = models.CharField(max_length=60, blank=True, null=True)
    etiq_madeira = models.CharField(max_length=200, blank=True, null=True)
    etiq_espuma1 = models.CharField(max_length=300, blank=True, null=True)
    etiq_espuma2 = models.CharField(max_length=300, blank=True, null=True)
    etiq_espuma3 = models.CharField(max_length=300, blank=True, null=True)
    etiq_revestimento1 = models.CharField(max_length=300, blank=True, null=True)
    etiq_revestimento2 = models.CharField(max_length=300, blank=True, null=True)
    etiq_revestimento3 = models.CharField(max_length=300, blank=True, null=True)
    etiq_recomendacoes_1 = models.CharField(max_length=80, blank=True, null=True)
    etiq_recomendacoes_2 = models.CharField(max_length=80, blank=True, null=True)
    lote_fabric_obrigatorio = models.IntegerField(blank=True, null=True, db_comment='Este campo Ú utilizado pela tela controle de inspeþÒo e recebimento de produto (EST_FM_M_NFE_S). \nIsso server para dizer se o campo lote do fabricante Ú obrigat¾rio.')
    id_ncm = models.ForeignKey('CadTbCNcm', models.DO_NOTHING, db_column='id_ncm', blank=True, null=True)
    preco_avista = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True, db_comment='Descricao completa, campo utilizado no enBueld.')
    preco_aprazo = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    dta_cadastro = models.DateField(blank=True, null=True)
    etiq_modelo = models.CharField(max_length=70, blank=True, null=True)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    id_familia = models.ForeignKey('CadTbCFam', models.DO_NOTHING, db_column='id_familia', blank=True, null=True)
    des_completa = models.CharField(max_length=250, blank=True, null=True)
    rt_pricipio_ativo = models.CharField(max_length=400, blank=True, null=True)
    rt_composicao = models.CharField(max_length=400, blank=True, null=True)
    ret_emb_capacidade = models.CharField(max_length=20, blank=True, null=True)
    ret_emb_nao_lavavel = models.IntegerField(blank=True, null=True, db_comment='0 - Contaminada\n1 - NÒo-Contaminada')
    ret_emb_lavaveis = models.IntegerField(blank=True, null=True, db_comment='0 - Plßstico\n1 - Metal\n2 - Vidro')
    cod_onu = models.CharField(max_length=20, blank=True, null=True)
    sgq_critica_laudo_fab = models.BooleanField(blank=True, null=True, db_comment='Este campo serß utilizado pela tela de InspeþÒo de Itens (FAT_FM_M_IQM).')
    tam_observacoes = models.CharField(max_length=150, blank=True, null=True)
    etiq_id_cue = models.IntegerField(blank=True, null=True, db_comment='Refere-se a tabela PCP_TB_C_CUE.')
    preco_avista_ant_reajuste = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    preco_aprazo_ant_reajuste = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    dta_ult_reajuste = models.DateField(blank=True, null=True)
    rt_registro = models.CharField(max_length=25, blank=True, null=True)
    custo_servico = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    id_grupo_prod = models.ForeignKey('CadTbCGrp', models.DO_NOTHING, db_column='id_grupo_prod', blank=True, null=True)
    id_item_anterior = models.IntegerField(blank=True, null=True)
    preco_sugerido = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    per_cmv_interno = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    per_cmv_externo = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    etiq_espuma4 = models.CharField(max_length=300, blank=True, null=True)
    etiq_espuma5 = models.CharField(max_length=300, blank=True, null=True)
    etiq_espuma6 = models.CharField(max_length=300, blank=True, null=True)
    etiq_revestimento4 = models.CharField(max_length=300, blank=True, null=True)
    etiq_revestimento5 = models.CharField(max_length=300, blank=True, null=True)
    etiq_revestimento6 = models.CharField(max_length=300, blank=True, null=True)
    etiq_marca = models.CharField(max_length=30, blank=True, null=True)
    sgq_tamanho_ite_epp = models.FloatField(blank=True, null=True, db_comment='Campo utilizado pelo relat¾rio de Entrada de Produto Acabado')
    tipo_servico = models.BooleanField(blank=True, null=True)
    mob_nome_foto = models.CharField(max_length=60, blank=True, null=True)
    pneu_largura = models.CharField(max_length=10, blank=True, null=True)
    pneu_altura = models.CharField(max_length=10, blank=True, null=True)
    pneu_aro = models.CharField(max_length=10, blank=True, null=True)
    id_marca = models.IntegerField(blank=True, null=True)
    sgq_personalizado = models.BooleanField(blank=True, null=True, db_comment='produto utilizado pelo m¾dulo sgq.')
    temp_etiq_medidas = models.CharField(max_length=60, blank=True, null=True)
    cod_item_prod = models.IntegerField(blank=True, null=True, db_comment='c¾digo do item da produþÒo ')
    etiq_tipo_produto = models.IntegerField(blank=True, null=True, db_comment='0 - COLCH├O DE ESPUMA\r\n1 - COLCH├O BOX CONJUGADO\r\n2 - COLCH├O AUXILIAR\r\n3 - COLCH├O MISTO\r\n')
    tam_esp_espessura_1 = models.FloatField(blank=True, null=True)
    tam_esp_espessura_2 = models.FloatField(blank=True, null=True)
    tam_esp_espessura_3 = models.FloatField(blank=True, null=True)
    tam_esp_comprimento_1 = models.FloatField(blank=True, null=True)
    tam_esp_comprimento_2 = models.FloatField(blank=True, null=True)
    tam_esp_comprimento_3 = models.FloatField(blank=True, null=True)
    tam_esp_largura_1 = models.FloatField(blank=True, null=True)
    tam_esp_largura_2 = models.FloatField(blank=True, null=True)
    tam_esp_largura_3 = models.FloatField(blank=True, null=True)
    cubagem_esp_1 = models.FloatField(blank=True, null=True)
    cubagem_esp_2 = models.FloatField(blank=True, null=True)
    cubagem_esp_3 = models.FloatField(blank=True, null=True)
    tipo_produto = models.IntegerField(blank=True, null=True, db_comment='0 - NÒo especificado\r\n1 - Manual do Usußrio')
    tam_esp_espessura_revest_1 = models.FloatField(blank=True, null=True)
    tam_esp_espessura_revest_2 = models.FloatField(blank=True, null=True)
    tam_esp_comp_revest_1 = models.FloatField(blank=True, null=True)
    tam_esp_comp_revest_2 = models.FloatField(blank=True, null=True)
    tam_esp_largura_revest_1 = models.FloatField(blank=True, null=True)
    tam_esp_largura_revest_2 = models.FloatField(blank=True, null=True)
    cubagem_esp_revest_1 = models.FloatField(blank=True, null=True)
    cubagem_esp_revest_2 = models.FloatField(blank=True, null=True)
    densidade_esp_revest_1 = models.FloatField(blank=True, null=True)
    densidade_esp_revest_2 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bck_producao_270922_itens'
        db_table_comment = 'Cadastro de Itens'


class BrCredito(models.Model):
    numcoo = models.IntegerField(primary_key=True)  # The composite primary key (numcoo, dthora) found, that is not supported. The first column is selected.
    dthora = models.DateField()
    serial = models.CharField(max_length=60, blank=True, null=True)
    numloja = models.IntegerField(blank=True, null=True)
    cod_doc = models.CharField(max_length=50, blank=True, null=True)
    cod_operacao = models.CharField(max_length=10, blank=True, null=True)
    parcela = models.CharField(max_length=2, blank=True, null=True)
    valor = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    tipo_pag = models.CharField(max_length=50, blank=True, null=True)
    indice_tp = models.CharField(max_length=10, blank=True, null=True)
    historico = models.CharField(max_length=200, blank=True, null=True)
    desc_comprov = models.CharField(max_length=100, blank=True, null=True)
    cod_comprov = models.IntegerField(blank=True, null=True)
    numecf = models.IntegerField(blank=True, null=True)
    numgnf = models.IntegerField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'br_credito'
        unique_together = (('numcoo', 'dthora'),)


class BrCupomDetalhe(models.Model):
    n_cupom = models.OneToOneField('BrCupomMestre', models.DO_NOTHING, db_column='n_cupom', primary_key=True)  # The composite primary key (n_cupom, cod_produto, n_item, serial_impressora) found, that is not supported. The first column is selected.
    cod_produto = models.CharField(max_length=15)
    n_item = models.IntegerField()
    qtde = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    valor_unitario = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    valor_total = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    desconto = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    acrecimo = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    cancelado = models.CharField(max_length=1, blank=True, null=True)
    serial_impressora = models.CharField(max_length=60)
    n_caixa = models.CharField(max_length=3, blank=True, null=True)
    aliquota = models.CharField(max_length=20, blank=True, null=True)
    unidade = models.CharField(max_length=3, blank=True, null=True)
    numloja = models.CharField(max_length=6, blank=True, null=True)
    flag_aceito = models.CharField(max_length=3, blank=True, null=True)
    flag_sis = models.CharField(max_length=1, blank=True, null=True)
    tanque = models.CharField(max_length=3, blank=True, null=True)
    bomba = models.CharField(max_length=3, blank=True, null=True)
    bico = models.CharField(max_length=3, blank=True, null=True)
    ei = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    ef = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    cod_grade = models.CharField(max_length=20, blank=True, null=True)
    cartao_cliente = models.CharField(max_length=20, blank=True, null=True)
    cartao_autorizador = models.CharField(max_length=20, blank=True, null=True)
    desc_produto = models.CharField(max_length=100, blank=True, null=True)
    numcaixa = models.CharField(max_length=5, blank=True, null=True)
    numterminal = models.CharField(max_length=3, blank=True, null=True)
    bico_posto = models.CharField(max_length=3, blank=True, null=True)
    data_ab = models.DateField(blank=True, null=True)
    hora_ab = models.DateField(blank=True, null=True)
    posicao_ab = models.CharField(max_length=10, blank=True, null=True)
    serial = models.CharField(max_length=100, blank=True, null=True)
    tabela = models.CharField(max_length=20, blank=True, null=True)
    cod_kit = models.CharField(max_length=20, blank=True, null=True)
    cod_vendedor = models.CharField(max_length=20, blank=True, null=True)
    cod_operador = models.CharField(max_length=20, blank=True, null=True)
    pdeccodigo = models.CharField(max_length=4, blank=True, null=True)
    prdcoutroscodigo = models.CharField(max_length=18, blank=True, null=True)
    prvndescontopenota = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    prvnacrescimopenota = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    flag_servico = models.CharField(max_length=1, blank=True, null=True)
    ccusto = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    ncm = models.CharField(max_length=8, blank=True, null=True)
    ex_ipi = models.CharField(max_length=3, blank=True, null=True)
    genero = models.CharField(max_length=2, blank=True, null=True)
    cst_icms = models.CharField(max_length=2, blank=True, null=True)
    origem_icms = models.CharField(max_length=1, blank=True, null=True)
    aliquota_ipi = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    aliquota_pis = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    tipo_item = models.CharField(max_length=2, blank=True, null=True)
    cfop = models.IntegerField(blank=True, null=True)
    desc_unidade = models.CharField(max_length=50, blank=True, null=True)
    stb = models.CharField(max_length=1, blank=True, null=True)
    complemento_item = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'br_cupom_detalhe'
        unique_together = (('n_cupom', 'cod_produto', 'n_item', 'serial_impressora'),)


class BrCupomMestre(models.Model):
    n_cupom = models.IntegerField(primary_key=True)  # The composite primary key (n_cupom, serial_impressora) found, that is not supported. The first column is selected.
    cpf_cnpj = models.CharField(max_length=30, blank=True, null=True)
    descontos = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    acrescimos = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    cancelado = models.CharField(max_length=1, blank=True, null=True)
    total_bruto = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    total_liquido = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    serial_impressora = models.CharField(max_length=60)
    cnpj_empresa = models.CharField(max_length=30, blank=True, null=True)
    ie = models.CharField(max_length=40, blank=True, null=True)
    im = models.CharField(max_length=40, blank=True, null=True)
    tipo_ecf = models.CharField(max_length=10, blank=True, null=True)
    marca = models.CharField(max_length=50, blank=True, null=True)
    modelo = models.CharField(max_length=50, blank=True, null=True)
    data_movimento = models.DateField(blank=True, null=True)
    versao_sb = models.CharField(max_length=10, blank=True, null=True)
    data_sb = models.DateField(blank=True, null=True)
    hora_sb = models.DateField(blank=True, null=True)
    dthora_inclusao = models.DateField(blank=True, null=True)
    naofiscal = models.CharField(max_length=1, blank=True, null=True)
    ccf = models.IntegerField(blank=True, null=True)
    indicadordesconto = models.CharField(max_length=1, blank=True, null=True)
    flag_descontoacrescimo = models.CharField(max_length=1, blank=True, null=True)
    nome_cliente = models.CharField(max_length=40, blank=True, null=True)
    n_caixa = models.CharField(max_length=3, blank=True, null=True)
    numloja = models.CharField(max_length=6, blank=True, null=True)
    flag_aceito = models.CharField(max_length=3, blank=True, null=True)
    flag_sis = models.CharField(max_length=1, blank=True, null=True)
    placa = models.CharField(max_length=20, blank=True, null=True)
    hodometro = models.IntegerField(blank=True, null=True)
    motivo_afericao = models.CharField(max_length=100, blank=True, null=True)
    motorista = models.CharField(max_length=60, blank=True, null=True)
    transportadora = models.CharField(max_length=80, blank=True, null=True)
    cpf_cnpj_transp = models.CharField(max_length=20, blank=True, null=True)
    autorizacao = models.CharField(max_length=20, blank=True, null=True)
    ccusto = models.CharField(max_length=10, blank=True, null=True)
    cliccodigo = models.CharField(max_length=20, blank=True, null=True)
    data_homologacao = models.DateField(blank=True, null=True)
    dthora_fechamento = models.DateField(blank=True, null=True)
    cod_pais = models.IntegerField(blank=True, null=True)
    cod_municipio = models.IntegerField(blank=True, null=True)
    suframa = models.CharField(max_length=9, blank=True, null=True)
    endereco = models.CharField(max_length=60, blank=True, null=True)
    numero = models.CharField(max_length=20, blank=True, null=True)
    complemento = models.CharField(max_length=60, blank=True, null=True)
    bairro = models.CharField(max_length=60, blank=True, null=True)
    ie_cliente = models.CharField(max_length=20, blank=True, null=True)
    uf = models.CharField(max_length=2, blank=True, null=True)
    cidade = models.CharField(max_length=50, blank=True, null=True)
    notafiscal = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'br_cupom_mestre'
        unique_together = (('n_cupom', 'serial_impressora'),)


class BrCupomPagamento(models.Model):
    n_cupom = models.OneToOneField(BrCupomMestre, models.DO_NOTHING, db_column='n_cupom', primary_key=True)  # The composite primary key (n_cupom, cod_forma_pag, serial_impressora, item) found, that is not supported. The first column is selected.
    cod_forma_pag = models.CharField(max_length=10)
    valor = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    serial_impressora = models.CharField(max_length=60)
    descricao = models.CharField(max_length=40, blank=True, null=True)
    vinculado = models.CharField(max_length=1, blank=True, null=True)
    cancelado = models.CharField(max_length=1, blank=True, null=True)
    flag_aceito = models.CharField(max_length=3, blank=True, null=True)
    flag_sis = models.CharField(max_length=1, blank=True, null=True)
    cod_forma_troco1 = models.CharField(max_length=10, blank=True, null=True)
    forma_troco1 = models.CharField(max_length=40, blank=True, null=True)
    cod_forma_troco2 = models.CharField(max_length=10, blank=True, null=True)
    forma_troco2 = models.CharField(max_length=40, blank=True, null=True)
    cod_forma_troco3 = models.CharField(max_length=10, blank=True, null=True)
    forma_troco3 = models.CharField(max_length=40, blank=True, null=True)
    n_doc = models.CharField(max_length=20, blank=True, null=True)
    banco = models.CharField(max_length=5, blank=True, null=True)
    agencia = models.CharField(max_length=10, blank=True, null=True)
    conta = models.CharField(max_length=10, blank=True, null=True)
    vencimento = models.DateField(blank=True, null=True)
    qtd_parcela = models.IntegerField(blank=True, null=True)
    valor_troco1 = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    valor_troco2 = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    valor_troco3 = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    id_cliente = models.CharField(max_length=20, blank=True, null=True)
    nome_cheque = models.CharField(max_length=70, blank=True, null=True)
    cpf_cheque = models.CharField(max_length=20, blank=True, null=True)
    fone_cheque = models.CharField(max_length=25, blank=True, null=True)
    cod_retaguarda = models.CharField(max_length=20, blank=True, null=True)
    item = models.IntegerField()
    strtipotransacaotef = models.CharField(max_length=10, blank=True, null=True)
    cod_bandeira = models.CharField(max_length=20, blank=True, null=True)
    parstrnomeredetef = models.CharField(max_length=50, blank=True, null=True)
    parstrnumidtranstef = models.CharField(max_length=20, blank=True, null=True)
    parstrnsutranstefhost = models.CharField(max_length=20, blank=True, null=True)
    dthoratransacao = models.DateField(blank=True, null=True)
    troco = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'br_cupom_pagamento'
        unique_together = (('n_cupom', 'cod_forma_pag', 'serial_impressora', 'item'),)


class BrEstoque(models.Model):
    data = models.DateField(primary_key=True)  # The composite primary key (data, cod_produto) found, that is not supported. The first column is selected.
    cod_produto = models.CharField(max_length=20)
    qtd = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    preco = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    custo = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    descricao = models.CharField(max_length=200, blank=True, null=True)
    flag_sis = models.CharField(max_length=1, blank=True, null=True)
    flag_aceito = models.CharField(max_length=3, blank=True, null=True)
    hora = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'br_estoque'
        unique_together = (('data', 'cod_produto'),)


class BrItensRz(models.Model):
    serial = models.OneToOneField('BrReducaoz', models.DO_NOTHING, db_column='serial', primary_key=True)  # The composite primary key (serial, data_movimento, tag, descricao, indice) found, that is not supported. The first column is selected.
    data_movimento = models.DateField()
    tag = models.CharField(max_length=50)
    descricao = models.CharField(max_length=60)
    valor = models.CharField(max_length=20, blank=True, null=True)
    indice = models.CharField(max_length=10)
    sequencial = models.CharField(max_length=10, blank=True, null=True)
    aliquota = models.CharField(max_length=10, blank=True, null=True)
    contador = models.CharField(max_length=10, blank=True, null=True)
    tipo = models.CharField(max_length=20, blank=True, null=True)
    sigla = models.CharField(max_length=20, blank=True, null=True)
    flag_sis = models.CharField(max_length=1, blank=True, null=True)
    flag_aceito = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'br_itens_rz'
        unique_together = (('serial', 'data_movimento', 'tag', 'descricao', 'indice'),)


class BrMntBombas(models.Model):
    tanque = models.CharField(max_length=3)
    bico = models.CharField(max_length=3)
    bomba = models.CharField(max_length=3)
    data_sub = models.DateField()
    hora_sub = models.DateField()
    motivo = models.CharField(max_length=200, blank=True, null=True)
    cnpj_sub = models.CharField(max_length=14, blank=True, null=True)
    cpf_sub = models.CharField(max_length=14, blank=True, null=True)
    lacre_anterior = models.CharField(max_length=20, blank=True, null=True)
    lacre_novo = models.CharField(max_length=20, blank=True, null=True)
    ei = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    ef = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    flag_sis = models.CharField(max_length=1, blank=True, null=True)
    flag_aceito = models.CharField(max_length=3, blank=True, null=True)
    codigo = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'br_mnt_bombas'


class BrNaofiscal(models.Model):
    numcoo = models.IntegerField(primary_key=True)  # The composite primary key (numcoo, serial) found, that is not supported. The first column is selected.
    serial = models.CharField(max_length=60)
    numgrg = models.IntegerField(blank=True, null=True)
    numecf = models.IntegerField(blank=True, null=True)
    numgnf = models.IntegerField(blank=True, null=True)
    cer = models.IntegerField(blank=True, null=True)
    indice_pg = models.CharField(max_length=20, blank=True, null=True)
    descricao_pg = models.CharField(max_length=60, blank=True, null=True)
    indice_doc = models.CharField(max_length=10, blank=True, null=True)
    descricao_doc = models.CharField(max_length=100, blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    valor = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    numcdc = models.IntegerField(blank=True, null=True)
    hora = models.DateField(blank=True, null=True)
    flag_sis = models.CharField(max_length=1, blank=True, null=True)
    flag_aceito = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'br_naofiscal'
        unique_together = (('numcoo', 'serial'),)


class BrPedDetalhe(models.Model):
    dtemissao = models.OneToOneField('BrPedMestre', models.DO_NOTHING, db_column='dtemissao', primary_key=True)  # The composite primary key (dtemissao, numero_nota, serie_nota, cod_produto) found, that is not supported. The first column is selected.
    numero_nota = models.CharField(max_length=20)
    serie_nota = models.CharField(max_length=3)
    cod_produto = models.CharField(max_length=14)
    desc_produto = models.CharField(max_length=100, blank=True, null=True)
    preco = models.FloatField(blank=True, null=True)
    quantidade = models.FloatField(blank=True, null=True)
    acrescimo = models.FloatField(blank=True, null=True)
    desconto = models.FloatField(blank=True, null=True)
    total_item = models.FloatField(blank=True, null=True)
    un = models.CharField(max_length=3, blank=True, null=True)
    aliquota = models.CharField(max_length=10, blank=True, null=True)
    flag_sis = models.CharField(max_length=1, blank=True, null=True)
    flag_aceito = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'br_ped_detalhe'
        unique_together = (('dtemissao', 'numero_nota', 'serie_nota', 'cod_produto'),)


class BrPedMestre(models.Model):
    dtemissao = models.DateField(primary_key=True)  # The composite primary key (dtemissao, numero, serie) found, that is not supported. The first column is selected.
    numero = models.CharField(max_length=20)
    serie = models.CharField(max_length=3)
    sub_serie = models.CharField(max_length=3, blank=True, null=True)
    base_icms = models.FloatField(blank=True, null=True)
    val_icms = models.FloatField(blank=True, null=True)
    total_nota = models.FloatField(blank=True, null=True)
    modelo = models.CharField(max_length=6, blank=True, null=True)
    flag_sis = models.CharField(max_length=1, blank=True, null=True)
    flag_aceito = models.CharField(max_length=3, blank=True, null=True)
    flag_servico = models.CharField(max_length=1, blank=True, null=True)
    cpf_cnpj = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'br_ped_mestre'
        unique_together = (('dtemissao', 'numero', 'serie'),)


class BrPrevenda(models.Model):
    numprevenda = models.IntegerField(primary_key=True)  # The composite primary key (numprevenda, tipo) found, that is not supported. The first column is selected.
    data_cad = models.DateField(blank=True, null=True)
    data_emissao = models.DateField(blank=True, null=True)
    vendedor = models.CharField(max_length=20, blank=True, null=True)
    plano = models.CharField(max_length=4, blank=True, null=True)
    id_cliente = models.CharField(max_length=20, blank=True, null=True)
    numloja = models.CharField(max_length=10)
    cancelado = models.CharField(max_length=1, blank=True, null=True)
    n_cupom = models.IntegerField(blank=True, null=True)
    serial = models.CharField(max_length=60, blank=True, null=True)
    contrz = models.IntegerField(blank=True, null=True)
    cpf_cnpj = models.CharField(max_length=20, blank=True, null=True)
    endereco = models.CharField(max_length=80, blank=True, null=True)
    nome = models.CharField(max_length=70, blank=True, null=True)
    bairro = models.CharField(max_length=50, blank=True, null=True)
    cidade = models.CharField(max_length=50, blank=True, null=True)
    cep = models.CharField(max_length=15, blank=True, null=True)
    uf = models.CharField(max_length=2, blank=True, null=True)
    fone1 = models.CharField(max_length=25, blank=True, null=True)
    fone2 = models.CharField(max_length=25, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    desconto = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    acrescimo = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    flag_liberado = models.CharField(max_length=1, blank=True, null=True)
    usuario_lib = models.CharField(max_length=50, blank=True, null=True)
    dthora_lib = models.DateField(blank=True, null=True)
    tipo = models.CharField(max_length=1)
    serialpv = models.CharField(max_length=30, blank=True, null=True)
    flag_aceito = models.CharField(max_length=3, blank=True, null=True)
    flag_sis = models.CharField(max_length=1, blank=True, null=True)
    dav_impresso = models.CharField(max_length=1, blank=True, null=True)
    mesa = models.CharField(max_length=30, blank=True, null=True)
    conferencia = models.CharField(max_length=1, blank=True, null=True)
    caixa_conf = models.IntegerField(blank=True, null=True)
    coo_conf = models.IntegerField(blank=True, null=True)
    cer_conf = models.IntegerField(blank=True, null=True)
    data_abertura = models.DateField(blank=True, null=True)
    placa = models.CharField(max_length=10, blank=True, null=True)
    renavan = models.CharField(max_length=30, blank=True, null=True)
    ano = models.CharField(max_length=10, blank=True, null=True)
    marca = models.CharField(max_length=50, blank=True, null=True)
    modelo = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'br_prevenda'
        unique_together = (('numprevenda', 'tipo'),)


class BrPrevendaDetalhe(models.Model):
    numprevenda = models.IntegerField(primary_key=True)  # The composite primary key (numprevenda, loja, cod_produto, item, tipo) found, that is not supported. The first column is selected.
    loja = models.CharField(max_length=10)
    cod_produto = models.CharField(max_length=20)
    qtd = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    un = models.CharField(max_length=3, blank=True, null=True)
    valor = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    desconto = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    acrescimo = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    total = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    cancelado = models.CharField(max_length=1, blank=True, null=True)
    n_cupom = models.IntegerField(blank=True, null=True)
    serial = models.CharField(max_length=60, blank=True, null=True)
    cod_grade = models.CharField(max_length=20, blank=True, null=True)
    item = models.IntegerField()
    cod_kit = models.CharField(max_length=20, blank=True, null=True)
    cod_vendedor = models.CharField(max_length=20, blank=True, null=True)
    desc_produto = models.CharField(max_length=100, blank=True, null=True)
    aliquota = models.CharField(max_length=10, blank=True, null=True)
    servico = models.CharField(max_length=1, blank=True, null=True)
    serialproduto = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.CharField(max_length=1)
    cod_prod_tcsmart = models.CharField(max_length=30, blank=True, null=True)
    tipo_bloqueado = models.CharField(max_length=1, blank=True, null=True)
    flag_sis = models.CharField(max_length=1, blank=True, null=True)
    flag_aceito = models.CharField(max_length=3, blank=True, null=True)
    mesa_origem = models.CharField(max_length=30, blank=True, null=True)
    numprevenda_origem = models.IntegerField(blank=True, null=True)
    item_origem = models.IntegerField(blank=True, null=True)
    ccusto = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    ncm = models.CharField(max_length=8, blank=True, null=True)
    ex_ipi = models.CharField(max_length=3, blank=True, null=True)
    genero = models.CharField(max_length=2, blank=True, null=True)
    cst_icms = models.CharField(max_length=2, blank=True, null=True)
    origem_icms = models.CharField(max_length=1, blank=True, null=True)
    aliquota_ipi = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    aliquota_pis = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    tipo_item = models.CharField(max_length=2, blank=True, null=True)
    cfop = models.IntegerField(blank=True, null=True)
    desc_unidade = models.CharField(max_length=50, blank=True, null=True)
    stb = models.CharField(max_length=1, blank=True, null=True)
    complemento_item = models.CharField(max_length=100, blank=True, null=True)
    prdcoutroscodigo = models.CharField(max_length=18, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'br_prevenda_detalhe'
        unique_together = (('numprevenda', 'loja', 'cod_produto', 'item', 'tipo'),)


class BrPrevendaPagamento(models.Model):
    cod_retaguarda = models.CharField(primary_key=True, max_length=20)  # The composite primary key (cod_retaguarda, numprevenda, tipo) found, that is not supported. The first column is selected.
    numprevenda = models.IntegerField()
    tipo = models.CharField(max_length=1)
    valor = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'br_prevenda_pagamento'
        unique_together = (('cod_retaguarda', 'numprevenda', 'tipo'),)


class BrReducaoz(models.Model):
    serial = models.CharField(primary_key=True, max_length=60)  # The composite primary key (serial, data_movimento) found, that is not supported. The first column is selected.
    cnpj = models.CharField(max_length=40, blank=True, null=True)
    ie = models.CharField(max_length=40, blank=True, null=True)
    im = models.CharField(max_length=40, blank=True, null=True)
    tipo_ecf = models.CharField(max_length=10, blank=True, null=True)
    marca = models.CharField(max_length=50, blank=True, null=True)
    modelo = models.CharField(max_length=40, blank=True, null=True)
    data_movimento = models.DateField()
    n_caixa = models.CharField(max_length=3, blank=True, null=True)
    versao_sb = models.CharField(max_length=20, blank=True, null=True)
    data_sb = models.DateField(blank=True, null=True)
    hora_sb = models.DateField(blank=True, null=True)
    coo_inicial = models.IntegerField(blank=True, null=True)
    coo_final = models.IntegerField(blank=True, null=True)
    dataemissao = models.DateField(blank=True, null=True)
    flag_sis = models.CharField(max_length=1, blank=True, null=True)
    flag_aceito = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'br_reducaoz'
        unique_together = (('serial', 'data_movimento'),)


class BrSeqId(models.Model):
    tabela = models.CharField(primary_key=True, max_length=50)
    seq_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'br_seq_id'


class CadTbCAlm(models.Model):
    id_almoxarifado = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=50)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    id_obra = models.ForeignKey('CtcTbCObr', models.DO_NOTHING, db_column='id_obra', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_alm'


class CadTbCAus(models.Model):
    id_aus = models.IntegerField(primary_key=True)
    id_empresa = models.IntegerField(blank=True, null=True)
    id_funcionario = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_aus'
        db_table_comment = 'Alterar Acessos do Usußrio'


class CadTbCAusPrg(models.Model):
    id_aus = models.OneToOneField(CadTbCAus, models.DO_NOTHING, db_column='id_aus', primary_key=True)  # The composite primary key (id_aus, id_aus_prg) found, that is not supported. The first column is selected.
    id_perfil_seg = models.IntegerField()
    formulario = models.CharField(max_length=100)
    chave = models.CharField(max_length=200)
    id_empresa = models.IntegerField()
    adicionar = models.BooleanField(blank=True, null=True)
    alterar = models.BooleanField(blank=True, null=True)
    excluir = models.BooleanField(blank=True, null=True)
    consulta = models.BooleanField(blank=True, null=True)
    id_aus_prg = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cad_tb_c_aus_prg'
        unique_together = (('id_aus', 'id_aus_prg'),)
        db_table_comment = 'Alterar Acessos do Usußrio'


class CadTbCCcr(models.Model):
    id_ccr = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=60, blank=True, null=True)
    cnpj = models.CharField(max_length=14, blank=True, null=True)
    fone = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_ccr'
        db_table_comment = 'Cadastro de Credenciadora de CartÒo de CrÚdito'


class CadTbCCcu(models.Model):
    id_ccusto = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=30)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_ccu'
        db_table_comment = 'Cadastro de Centro de Custo'


class CadTbCCfo(models.Model):
    id_cfo = models.CharField(primary_key=True, max_length=5)
    descricao = models.CharField(max_length=400)
    id_classe = models.ForeignKey('CadTbCNat', models.DO_NOTHING, db_column='id_classe')
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    id_cfo_xml = models.CharField(max_length=5, blank=True, null=True)
    desc_nat_operacao_nfe = models.CharField(max_length=60, blank=True, null=True)
    cod_cta = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_cfo'
        db_table_comment = 'Cadastro de Codigo Fiscal de OperaþÒo'


class CadTbCCid(models.Model):
    id_cidade = models.CharField(primary_key=True, max_length=10)
    nome = models.CharField(max_length=60)
    uf = models.CharField(max_length=2)
    cep = models.CharField(max_length=9)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    cod_pais = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_cid'
        db_table_comment = 'Cadastro de Cidades conforme IBGE'


class CadTbCCin(models.Model):
    id_cli_informa = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=50)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_cin'
        db_table_comment = 'Cadastro de Informaþ§es de Clientes'


class CadTbCCli(models.Model):
    id_cliente = models.IntegerField(primary_key=True)
    pessoa = models.IntegerField(db_comment='0-Fisica\n1-Juridica')
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=60)
    end_complemento = models.CharField(max_length=30, blank=True, null=True)
    cep = models.CharField(max_length=9)
    numero = models.CharField(max_length=10)
    tel_fixo = models.CharField(max_length=14, blank=True, null=True)
    tel_movel = models.CharField(max_length=14, blank=True, null=True)
    fax = models.CharField(max_length=14, blank=True, null=True)
    doc_cnpj_cpf = models.CharField(max_length=14)
    doc_ie_identidade = models.CharField(max_length=20)
    doc_ip = models.CharField(max_length=20, blank=True, null=True)
    doc_im = models.CharField(max_length=20, blank=True, null=True)
    bairro = models.CharField(max_length=40)
    id_cidade = models.ForeignKey(CadTbCCid, models.DO_NOTHING, db_column='id_cidade', blank=True, null=True)
    ativo = models.BooleanField()
    email = models.CharField(max_length=60, blank=True, null=True)
    lim_valor = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    lim_saldo = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    sexo = models.IntegerField(blank=True, null=True, db_comment='0 - Feminino,\n1 - Masculino')
    situacao = models.IntegerField(db_comment='0 - Normal,\n1 - Especial,\n2 - CrÚditoEncerrado')
    dta_nascimento = models.DateField(blank=True, null=True)
    dta_cadastro = models.DateField()
    tipo_cliente = models.IntegerField(db_comment='0 - Consumidor,\n1 - Revenda')
    cob_endereco = models.CharField(max_length=50, blank=True, null=True)
    cob_bairro = models.CharField(max_length=40, blank=True, null=True)
    cob_cidade = models.CharField(max_length=40, blank=True, null=True)
    cob_estado = models.CharField(max_length=2, blank=True, null=True)
    cob_cep = models.CharField(max_length=9, blank=True, null=True)
    dta_ult_compra = models.DateField(blank=True, null=True)
    dta_pri_compra = models.DateField(blank=True, null=True)
    filiacao = models.CharField(max_length=100, blank=True, null=True)
    cod_sufrana = models.CharField(max_length=20, blank=True, null=True)
    cod_pais = models.CharField(max_length=5, blank=True, null=True)
    id_perfil_cli = models.ForeignKey('CadTbCPec', models.DO_NOTHING, db_column='id_perfil_cli', blank=True, null=True)
    id_rota = models.ForeignKey('PcpTbCRot', models.DO_NOTHING, db_column='id_rota', blank=True, null=True)
    doc_rg_orgao = models.CharField(max_length=10, blank=True, null=True)
    apelido = models.CharField(max_length=40, blank=True, null=True)
    lim_validade = models.DateField(blank=True, null=True)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    id_regiao = models.ForeignKey('PcpTbCReg', models.DO_NOTHING, db_column='id_regiao', blank=True, null=True)
    contribuinte = models.IntegerField(blank=True, null=True, db_comment='0 - Contribuinte de ICMS\n1 - NÒo Contribuinte de ICMS\n2 - ISENTO')
    id_vendedor = models.ForeignKey('CadTbCFun', models.DO_NOTHING, db_column='id_vendedor', blank=True, null=True)
    dias_prazo_financeiro = models.IntegerField(blank=True, null=True)
    profissao = models.CharField(max_length=50, blank=True, null=True)
    renda = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    id_responsavel = models.ForeignKey('CadTbCFun', models.DO_NOTHING, db_column='id_responsavel', related_name='cadtbccli_id_responsavel_set', blank=True, null=True)
    id_controle_fpg_hrq = models.IntegerField(blank=True, null=True)
    permitir_alterar_dias_tit_ped = models.BooleanField(blank=True, null=True)
    status_vis_mobile = models.BooleanField(blank=True, null=True)
    id_cli_temp_mobile = models.CharField(max_length=30, blank=True, null=True)
    per_comissao = models.FloatField(blank=True, null=True)
    gps_latitude = models.FloatField(blank=True, null=True)
    gps_longitude = models.FloatField(blank=True, null=True)
    substituto_tributario = models.BooleanField(blank=True, null=True)
    desenvolvimento = models.BooleanField(blank=True, null=True)
    dta_inicio_desnv = models.DateField(blank=True, null=True)
    aval_doc_cnpj_cpf = models.CharField(max_length=14, blank=True, null=True)
    aval_nome = models.CharField(max_length=40, blank=True, null=True)
    aval_logradouro = models.CharField(max_length=30, blank=True, null=True)
    aval_nro = models.CharField(max_length=10, blank=True, null=True)
    aval_bairro = models.CharField(max_length=20, blank=True, null=True)
    aval_id_cidade = models.CharField(max_length=10, blank=True, null=True)
    aval_cep = models.CharField(max_length=9, blank=True, null=True)
    aval_fone = models.CharField(max_length=14, blank=True, null=True)
    aval_email = models.CharField(max_length=60, blank=True, null=True)
    nome_proprietario = models.CharField(max_length=50, blank=True, null=True, db_comment='A pedido da Colch§es Glogo')
    doc_cnpj_cpf_proprietario = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_cli'
        db_table_comment = 'Cadastro de Clientes'


class CadTbCCliBco(models.Model):
    id_cliente = models.OneToOneField(CadTbCCli, models.DO_NOTHING, db_column='id_cliente', primary_key=True)  # The composite primary key (id_cliente, id_banco_info) found, that is not supported. The first column is selected.
    id_banco_info = models.IntegerField()
    dta_informacao = models.DateField(blank=True, null=True)
    obs = models.CharField(max_length=2800, blank=True, null=True)
    arquivo = models.BinaryField(blank=True, null=True)
    nome_arquivo = models.CharField(max_length=255, blank=True, null=True)
    id_mkt = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_cli_bco'
        unique_together = (('id_cliente', 'id_banco_info'),)
        db_table_comment = 'Banco de Informaþ§es de Clientes'


class CadTbCCliCrd(models.Model):
    id_cliente = models.OneToOneField(CadTbCCli, models.DO_NOTHING, db_column='id_cliente', primary_key=True)  # The composite primary key (id_cliente, id_forma_pag) found, that is not supported. The first column is selected.
    id_forma_pag = models.ForeignKey('CadTbCFpg', models.DO_NOTHING, db_column='id_forma_pag')
    lim_valor = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    lim_saldo = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_cli_crd'
        unique_together = (('id_cliente', 'id_forma_pag'),)


class CadTbCCliCto(models.Model):
    id_cliente = models.OneToOneField(CadTbCCli, models.DO_NOTHING, db_column='id_cliente', primary_key=True)  # The composite primary key (id_cliente, id_contato) found, that is not supported. The first column is selected.
    id_contato = models.IntegerField()
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=14, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)
    dta_nascimento = models.DateField()
    tipo_contato = models.IntegerField(blank=True, null=True, db_comment='0 - Socio\n1 - Filho\n2 - Conjuge\n3 - Pais\n4 - Outros')

    class Meta:
        managed = False
        db_table = 'cad_tb_c_cli_cto'
        unique_together = (('id_cliente', 'id_contato'),)
        db_table_comment = 'Tabela de Contato de clientes'


class CadTbCCliEml(models.Model):
    id_cliente = models.OneToOneField(CadTbCCli, models.DO_NOTHING, db_column='id_cliente', primary_key=True)  # The composite primary key (id_cliente, email) found, that is not supported. The first column is selected.
    email = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_cli_eml'
        unique_together = (('id_cliente', 'email'),)


class CadTbCCliInf(models.Model):
    id_cliente = models.OneToOneField(CadTbCCli, models.DO_NOTHING, db_column='id_cliente', primary_key=True)  # The composite primary key (id_cliente, id_sequencia) found, that is not supported. The first column is selected.
    id_cli_informa = models.ForeignKey(CadTbCCin, models.DO_NOTHING, db_column='id_cli_informa')
    dta_informacao = models.DateField()
    dta_maior_compra = models.DateField(blank=True, null=True)
    vlr_maior_compra = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_lim_liberado = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    atrasa = models.BooleanField(blank=True, null=True)
    informante = models.CharField(max_length=20, blank=True, null=True)
    obs = models.CharField(max_length=800, blank=True, null=True)
    id_sequencia = models.IntegerField()
    dta_ult_compra = models.DateField(blank=True, null=True)
    vlr_ult_compra = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_cli_inf'
        unique_together = (('id_cliente', 'id_sequencia'),)
        db_table_comment = 'Tabela de Informaþ§es de Clientes'


class CadTbCCliPrd(models.Model):
    id_cliente = models.OneToOneField(CadTbCCli, models.DO_NOTHING, db_column='id_cliente', primary_key=True)  # The composite primary key (id_cliente, id_sequencia) found, that is not supported. The first column is selected.
    id_sequencia = models.IntegerField()
    dias = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cad_tb_c_cli_prd'
        unique_together = (('id_cliente', 'id_sequencia'),)


class CadTbCCliPro(models.Model):
    id_cliente = models.OneToOneField(CadTbCCli, models.DO_NOTHING, db_column='id_cliente', primary_key=True)  # The composite primary key (id_cliente, id_propriedade) found, that is not supported. The first column is selected.
    id_propriedade = models.IntegerField()
    tipo = models.IntegerField()
    nome = models.CharField(max_length=50, blank=True, null=True)
    bairro = models.CharField(max_length=40, blank=True, null=True)
    id_cidade = models.CharField(max_length=10, blank=True, null=True)
    doc_ip = models.CharField(max_length=20, blank=True, null=True)
    doc_incra = models.CharField(max_length=20, blank=True, null=True)
    doc_cnpj = models.CharField(max_length=14, blank=True, null=True)
    doc_ie = models.CharField(max_length=20, blank=True, null=True)
    administrador = models.CharField(max_length=50, blank=True, null=True)
    endereco = models.CharField(max_length=60, blank=True, null=True)
    cep = models.CharField(max_length=9, blank=True, null=True)
    numero = models.CharField(max_length=10, blank=True, null=True)
    id_pro_mob_temp = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_cli_pro'
        unique_together = (('id_cliente', 'id_propriedade'),)


class CadTbCCliProCul(models.Model):
    id_cliente = models.OneToOneField(CadTbCCliPro, models.DO_NOTHING, db_column='id_cliente', primary_key=True)  # The composite primary key (id_cliente, id_propriedade, lote, id_cultura) found, that is not supported. The first column is selected.
    id_propriedade = models.IntegerField()
    lote = models.CharField(max_length=20)
    id_cultura = models.ForeignKey('CadTbCCul', models.DO_NOTHING, db_column='id_cultura')
    idade = models.SmallIntegerField(blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    produtividade = models.FloatField(blank=True, null=True)
    obs = models.CharField(max_length=800, blank=True, null=True)
    variedade = models.CharField(max_length=30, blank=True, null=True)
    producao_estimada = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_cli_pro_cul'
        unique_together = (('id_cliente', 'id_propriedade', 'lote', 'id_cultura'),)


class CadTbCCliRec(models.Model):
    id_cliente = models.OneToOneField(CadTbCCli, models.DO_NOTHING, db_column='id_cliente', primary_key=True)  # The composite primary key (id_cliente, id_reclamacao) found, that is not supported. The first column is selected.
    id_reclamacao = models.IntegerField()
    dta_registro = models.DateField()
    obs = models.CharField(max_length=800, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_cli_rec'
        unique_together = (('id_cliente', 'id_reclamacao'),)
        db_table_comment = 'Tabela de ReclamaþÒo de cliente'


class CadTbCCliRvd(models.Model):
    id_cliente = models.OneToOneField(CadTbCCli, models.DO_NOTHING, db_column='id_cliente', primary_key=True)  # The composite primary key (id_cliente, id_rvd) found, that is not supported. The first column is selected.
    id_rvd = models.ForeignKey('CadTbCRvd', models.DO_NOTHING, db_column='id_rvd')

    class Meta:
        managed = False
        db_table = 'cad_tb_c_cli_rvd'
        unique_together = (('id_cliente', 'id_rvd'),)
        db_table_comment = 'Revendas do Cliente'


class CadTbCCliVei(models.Model):
    id_cliente = models.OneToOneField(CadTbCCli, models.DO_NOTHING, db_column='id_cliente', primary_key=True)  # The composite primary key (id_cliente, id_veiculo) found, that is not supported. The first column is selected.
    id_veiculo = models.ForeignKey('CadTbCVei', models.DO_NOTHING, db_column='id_veiculo')

    class Meta:
        managed = False
        db_table = 'cad_tb_c_cli_vei'
        unique_together = (('id_cliente', 'id_veiculo'),)


class CadTbCCne(models.Model):
    id_cnae = models.CharField(primary_key=True, max_length=14)
    descricao = models.CharField(max_length=300)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_cne'
        db_table_comment = 'Tabela de CNAE'


class CadTbCCor(models.Model):
    id_cor = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=40)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_cor'
        db_table_comment = 'Tabela de Cor.'


class CadTbCCpg(models.Model):
    id_condicao_pag = models.IntegerField(primary_key=True)
    ativo = models.BooleanField()
    descricao = models.CharField(max_length=30)
    tipo_pagamento = models.IntegerField(db_comment='0 - AVista,\n1 - APrazo,\n2 - SemPagamento')
    num_parcelas = models.IntegerField()
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    per_desc = models.FloatField(blank=True, null=True)
    perm_desc_especial = models.BooleanField(blank=True, null=True, db_comment='Campo utilizado no pedido de venda.')
    sgq_texto_cnd_ped = models.BooleanField(blank=True, null=True, db_comment='Se estiver TRUE , o pedido de venda irß abrir o campo para o usußrio digitar o texto a ser impresso no pedido de venda ao invÚs da descriþÒo da condiþÒo de pagamento.')

    class Meta:
        managed = False
        db_table = 'cad_tb_c_cpg'
        db_table_comment = 'Tabela de CondiþÒo de Pagamento'


class CadTbCCtc(models.Model):
    id_conta = models.IntegerField(primary_key=True)
    banco = models.IntegerField(blank=True, null=True)
    agencia = models.CharField(max_length=10, blank=True, null=True)
    cedente_cod = models.CharField(max_length=20, blank=True, null=True)
    cedente_nom = models.CharField(max_length=50, blank=True, null=True)
    cedente_mail = models.CharField(max_length=60, blank=True, null=True)
    nnu_proximo = models.CharField(max_length=20, blank=True, null=True)
    conta_corrente = models.CharField(max_length=20, blank=True, null=True)
    descricao = models.CharField(max_length=40, blank=True, null=True)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    tipo = models.IntegerField(blank=True, null=True, db_comment='0-Caixa, 1-Banco')
    mensagem_1 = models.CharField(max_length=100, blank=True, null=True)
    mensagem_2 = models.CharField(max_length=100, blank=True, null=True)
    cedente_ident = models.CharField(max_length=260, blank=True, null=True)
    layout_remessa = models.CharField(max_length=15, blank=True, null=True)
    tipo_cobranca = models.IntegerField(blank=True, null=True, db_comment='0-Nenhum\n1-Banco Do Brasil\n2-Santander\n3-Caixa Economica\n4-Caixa Sicob\n5-Bradesco\n6-Itau\n7-Banco Mercantil\n8-Sicred\n9-Bancoob\n10-Banrisul,\n11-Banestes,\n12-HSBC\n13-BancoDoNordeste\n14-BRB\n15-BicBanco,\n    cobBradescoSICOOB,\n    cobBancoSafra,\n    cobSafraBradesco,\n    cobBancoCECRED\n')
    caract_titulo = models.IntegerField(blank=True, null=True, db_comment='0-Simples\n1-Vinculada\n2-Caucionada\n3-Descontada\n4-Vendor')
    tipo_carteira = models.IntegerField(blank=True, null=True, db_comment='0-Simples\n1-Registrada')
    resp_emissao = models.IntegerField(blank=True, null=True, db_comment='0-Cliente Emite\n1-Banco Emite\n2-Banco Reemite\n3-Banco Nao Reemite')
    agencia_dig = models.IntegerField(blank=True, null=True)
    conta_corrente_dig = models.IntegerField(blank=True, null=True)
    convenio = models.IntegerField(blank=True, null=True)
    carteira = models.CharField(max_length=4, blank=True, null=True, db_comment='Usado na impressÒo do boleto.')
    msg_local_pagto = models.CharField(max_length=80, blank=True, null=True)
    carteira_variacao = models.CharField(max_length=3, blank=True, null=True)
    cnpj_titular = models.CharField(max_length=14, blank=True, null=True, db_comment='Este campo indica qual Ú o CNPJ titula da conta corrente,  pois para o BANCO DO BRASIL, esse valor Ú importante e a mesma conta corrente pode ser usada por outras filiais. Ex. A conta pode ser utilizada para emissÒo de boleto por N filiais, mas essa conta s¾ tem um ·nico CNPJ.')
    imp_msg_juros_mora = models.BooleanField(blank=True, null=True, db_comment='Utilizado no momento de gerar o boleto.')
    especie_tit = models.CharField(max_length=3, blank=True, null=True, db_comment='EspÚcie do TÝtulo\r\nC¾digo adotado pela FEBRABAN para identificar o tipo de tÝtulo de cobranþa.\r\n\r\nDM - Duplicata Mercantil\r\nDS   - Duplicata de Serviþo\r\nNP  - Nota Promiss¾ria\r\nNS  - Nota de Seguro\r\nRC  - Recibo\r\nND -  Nota de DÚbito\r\nLC  -  Letra de CÔmbio\r\n\r\n\r\n')
    aceite_tit = models.CharField(max_length=1, blank=True, null=True, db_comment='C¾digo adotado pela FEBRABAN para identificar se o tÝtulo de cobranþa foi aceito\r\n(reconhecimento da dÝvida pelo Sacado).\r\n\r\nA - Aceite\r\nN - NÒo aceite')
    qtde_dias_protesto = models.IntegerField(blank=True, null=True)
    perc_multa = models.FloatField(blank=True, null=True)
    protestar_negativar = models.IntegerField(blank=True, null=True, db_comment='0 - Nenhum\r\n1 - Protestar\r\n2 - Negativar')
    sequencia_remessa = models.IntegerField(blank=True, null=True, db_comment='Nro sequencial do arquivo de remessa ref. a posicao 111 a 117 no layout 400')

    class Meta:
        managed = False
        db_table = 'cad_tb_c_ctc'
        db_table_comment = 'Tabela de Conta Corrente'


class CadTbCCul(models.Model):
    id_cultura = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=30, blank=True, null=True)
    ciclo_curto = models.BooleanField(blank=True, null=True, db_comment='Criado devido o sistema MOBILE.')

    class Meta:
        managed = False
        db_table = 'cad_tb_c_cul'


class CadTbCEcf(models.Model):
    ecf_serial_impressora = models.CharField(primary_key=True, max_length=60)
    ecf_marca_impressora = models.CharField(max_length=50, blank=True, null=True)
    ecf_modelo_impressora = models.CharField(max_length=50, blank=True, null=True)
    ecf_caixa = models.CharField(max_length=3, blank=True, null=True)
    serie = models.CharField(max_length=3, blank=True, null=True)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    paf_serial_pv = models.CharField(max_length=30, blank=True, null=True)
    id_empresa = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_ecf'
        db_table_comment = 'Cadastro de Impressora Fiscal'


class CadTbCEcfFpg(models.Model):
    ecf_serial_impressora = models.OneToOneField(CadTbCEcf, models.DO_NOTHING, db_column='ecf_serial_impressora', primary_key=True)  # The composite primary key (ecf_serial_impressora, id_forma_pag) found, that is not supported. The first column is selected.
    id_forma_pag = models.IntegerField()
    id_forma_pag_ecf = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cad_tb_c_ecf_fpg'
        unique_together = (('ecf_serial_impressora', 'id_forma_pag'),)
        db_table_comment = 'Tabela de Formas de Pagamento da ECF\n\nEsta tabela terß a funþÒo de linkar a forma de pagamento do enSoft com a forma de pagamento da ECF.\nCriado por Maxsuel Victor em 20/02/2015'


class CadTbCEqp(models.Model):
    id_equipamento = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=60, blank=True, null=True)
    serial = models.CharField(max_length=30, blank=True, null=True)
    modelo = models.CharField(max_length=30, blank=True, null=True)
    garantia = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_eqp'


class CadTbCFam(models.Model):
    id_familia = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=30, blank=True, null=True)
    faz_corr_preco_perfil = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_fam'
        db_table_comment = 'Cadastro de Familia'


class CadTbCFamEmp(models.Model):
    id_familia = models.OneToOneField(CadTbCFam, models.DO_NOTHING, db_column='id_familia', primary_key=True)  # The composite primary key (id_familia, id_empresa) found, that is not supported. The first column is selected.
    id_empresa = models.ForeignKey('CadTbCPar', models.DO_NOTHING, db_column='id_empresa')
    faz_corr_preco_perfil = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_fam_emp'
        unique_together = (('id_familia', 'id_empresa'),)


class CadTbCFor(models.Model):
    id_fornecedor = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=50)
    fantasia = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)
    end_complemento = models.CharField(max_length=30, blank=True, null=True)
    cep = models.CharField(max_length=9)
    numero = models.CharField(max_length=10)
    cp = models.CharField(max_length=10, blank=True, null=True)
    tel_fixo = models.CharField(max_length=14, blank=True, null=True)
    tel_movel = models.CharField(max_length=14, blank=True, null=True)
    fax = models.CharField(max_length=14, blank=True, null=True)
    doc_cnpj = models.CharField(max_length=14, blank=True, null=True)
    doc_cpf = models.CharField(max_length=11, blank=True, null=True)
    doc_ie = models.CharField(max_length=20, blank=True, null=True)
    doc_im = models.CharField(max_length=20, blank=True, null=True)
    bairro = models.CharField(max_length=40)
    id_cidade = models.ForeignKey(CadTbCCid, models.DO_NOTHING, db_column='id_cidade')
    ativo = models.BooleanField()
    email = models.CharField(max_length=60, blank=True, null=True)
    lim_valor = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    dta_fundacao = models.DateField(blank=True, null=True)
    dta_cadastro = models.DateField()
    senha_cotacao = models.CharField(max_length=30, blank=True, null=True)
    fin_conta = models.IntegerField(blank=True, null=True)
    fin_agencia = models.CharField(max_length=10, blank=True, null=True)
    fin_banco = models.IntegerField(blank=True, null=True)
    fin_favor = models.CharField(max_length=50, blank=True, null=True)
    metodo1_norma_aplicavel = models.CharField(max_length=60, blank=True, null=True)
    metodo1_data_validade = models.DateField(blank=True, null=True)
    metodo2_data_recebimento = models.DateField(blank=True, null=True)
    metodo2_situacao = models.IntegerField(blank=True, null=True)
    metodo2_proc_qualificacao = models.CharField(max_length=80, blank=True, null=True)
    metodo3_metodo = models.IntegerField(blank=True, null=True, db_comment='0 - Amostra\r\n1 - Pesquisa de mercado\r\n2 - IndicaþÒo do fabricante\r\n3 - Curriculum vitae\r\n4 - Auto avaliaþÒo\r\n')
    metodo3_data = models.DateField(blank=True, null=True)
    metodo3_numero_nf = models.CharField(max_length=30, blank=True, null=True)
    transportadora = models.BooleanField()
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    tipo_fornecedor = models.IntegerField(blank=True, null=True)
    cod_pais = models.CharField(max_length=5, blank=True, null=True)
    regime = models.IntegerField(blank=True, null=True, db_comment='0 - Simples Nacional; \r\n1 - Normal - Lucro Presumido\r\n2 - Normal - Lucro Real')
    aval_ctc_perg_01 = models.IntegerField(blank=True, null=True, db_comment='0 - NÒo;  1 - Sim;   2 - NÒo se aplica;')
    aval_ctc_perg_02 = models.IntegerField(blank=True, null=True, db_comment='0 - NÒo;  1 - Sim;   2 - NÒo se aplica;')
    aval_ctc_perg_03 = models.IntegerField(blank=True, null=True, db_comment='0 - NÒo;  1 - Sim;   2 - NÒo se aplica;')
    aval_ctc_perg_04 = models.IntegerField(blank=True, null=True, db_comment='0 - NÒo;  1 - Sim;   2 - NÒo se aplica;')
    metodo2_sit_justificativa = models.CharField(max_length=100, blank=True, null=True, db_comment='Este campo nasceu na necessidade do m¾dulo CTC.')
    metodo3_observacoes = models.CharField(max_length=150, blank=True, null=True, db_comment='Este campo surgiu na necessidade do m¾dulo CTC.')
    contribuinte = models.IntegerField(blank=True, null=True, db_comment='0 - Contribuinte de ICMS\n1 - NÒo Contribuinte de ICMS\n2 - ISENTO')
    dias_entrega = models.IntegerField(blank=True, null=True)
    cod_fab_danfe = models.BooleanField(blank=True, null=True)
    fin_conta_dig = models.CharField(max_length=1, blank=True, null=True)
    id_plano = models.CharField(max_length=11, blank=True, null=True)
    metodo3_dta_auto_avaliacao = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_for'
        db_table_comment = 'Tabela de Cadastro de Fornecedores'


class CadTbCForRep(models.Model):
    id_fornecedor = models.OneToOneField(CadTbCFor, models.DO_NOTHING, db_column='id_fornecedor', primary_key=True)  # The composite primary key (id_fornecedor, id_for_rp) found, that is not supported. The first column is selected.
    id_for_rp = models.IntegerField()
    nome = models.CharField(max_length=60, blank=True, null=True)
    doc_cpf = models.CharField(max_length=11, blank=True, null=True)
    cep = models.CharField(max_length=9, blank=True, null=True)
    endereco = models.CharField(max_length=50, blank=True, null=True)
    numero = models.CharField(max_length=10, blank=True, null=True)
    id_cidade = models.CharField(max_length=10, blank=True, null=True)
    tel_1 = models.CharField(max_length=14, blank=True, null=True)
    tel_2 = models.CharField(max_length=14, blank=True, null=True)
    tel_celular = models.CharField(max_length=14, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)
    obs = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_for_rep'
        unique_together = (('id_fornecedor', 'id_for_rp'),)
        db_table_comment = 'Tabela de Cadstro de Representantes do Fornecedor.'


class CadTbCFpg(models.Model):
    id_forma_pag = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=30)
    doc_impresso = models.IntegerField(db_comment='0 - Nenhum,\r\n1 - Duplicata,\r\n2 - Promissoria,\r\n3 - Cartao,\r\n4 - Boleto,\r\n5 - Dinheiro,\r\n6 - Cheque \r\n7 - Credito, 8 - PIX')
    car_deb_cre = models.IntegerField(db_comment='Se o cartÒo Ú DÚbito ou CrÚdito')
    car_taxa = models.FloatField(blank=True, null=True, db_comment='Taxa de administraþÒo do cartÒo.')
    car_dia_pag = models.IntegerField(blank=True, null=True)
    car_conta = models.IntegerField(blank=True, null=True)
    car_telefone = models.CharField(max_length=13, blank=True, null=True)
    cri_debi_cliente = models.BooleanField()
    ven_id_plano = models.ForeignKey('CadTbCPct', models.DO_NOTHING, db_column='ven_id_plano')
    com_id_plano = models.ForeignKey('CadTbCPct', models.DO_NOTHING, db_column='com_id_plano', related_name='cadtbcfpg_com_id_plano_set')
    pag_id_plano_juros = models.ForeignKey('CadTbCPct', models.DO_NOTHING, db_column='pag_id_plano_juros', related_name='cadtbcfpg_pag_id_plano_juros_set')
    pag_id_plano_desconto = models.ForeignKey('CadTbCPct', models.DO_NOTHING, db_column='pag_id_plano_desconto', related_name='cadtbcfpg_pag_id_plano_desconto_set')
    rec_id_plano_juros = models.ForeignKey('CadTbCPct', models.DO_NOTHING, db_column='rec_id_plano_juros', related_name='cadtbcfpg_rec_id_plano_juros_set')
    rec_id_plano_desconto = models.ForeignKey('CadTbCPct', models.DO_NOTHING, db_column='rec_id_plano_desconto', related_name='cadtbcfpg_rec_id_plano_desconto_set')
    id_ccusto = models.ForeignKey(CadTbCCcu, models.DO_NOTHING, db_column='id_ccusto')
    id_tipo_financeiro = models.ForeignKey('CadTbCTif', models.DO_NOTHING, db_column='id_tipo_financeiro')
    gera_caixa_banco = models.BooleanField()
    tipo_pagamento = models.IntegerField(db_comment='0 - AVista,\n1 - APrazo,\n2 - SemPagamento')
    id_local_titulo = models.ForeignKey('CadTbCLto', models.DO_NOTHING, db_column='id_local_titulo', blank=True, null=True)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    taxa_antecipacao = models.FloatField(blank=True, null=True, db_comment='Campo utilizado pela tela de conciliaþÒo de cartÒo.')
    car_bandeira = models.CharField(max_length=2, blank=True, null=True, db_comment='01- Visa\n02- Mastercard\n03- American Express\n04- Sorocred\n99- Outros ')
    id_ccr = models.ForeignKey(CadTbCCcr, models.DO_NOTHING, db_column='id_ccr', blank=True, null=True)
    rbx_id_tipo_financeiro = models.ForeignKey('CadTbCTif', models.DO_NOTHING, db_column='rbx_id_tipo_financeiro', related_name='cadtbcfpg_rbx_id_tipo_financeiro_set', blank=True, null=True)
    rbx_id_ccusto = models.ForeignKey(CadTbCCcu, models.DO_NOTHING, db_column='rbx_id_ccusto', related_name='cadtbcfpg_rbx_id_ccusto_set', blank=True, null=True)
    rbx_id_plano = models.ForeignKey('CadTbCPct', models.DO_NOTHING, db_column='rbx_id_plano', related_name='cadtbcfpg_rbx_id_plano_set', blank=True, null=True)
    vlr_min_parcela = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True, db_comment='Campo utilizado pelo pedido de venda.')
    ativa_red_parc_car_rec = models.BooleanField(blank=True, null=True)
    aval_duplicata = models.BooleanField(blank=True, null=True)
    dias_vencimento = models.IntegerField(blank=True, null=True)
    qtde_red_parc_car_rec = models.IntegerField(blank=True, null=True)
    utilizado_ped_vnd = models.BooleanField(blank=True, null=True)
    sgq_prestacao_conta = models.BooleanField(blank=True, null=True, db_comment='Este campo Ú utilizado pela consulta do cliente, no botÒo Extrato do cliente. Serve para indicar os tÝtulos que estÒo em aberto, Ú que sÒo para PrestaþÒo de Conta.')
    acresc_dias_em_vencto = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_fpg'
        db_table_comment = 'Tabela de Cadastro de Forma de Pagamento'


class CadTbCFpgTap(models.Model):
    id_forma_pag = models.OneToOneField(CadTbCFpg, models.DO_NOTHING, db_column='id_forma_pag', primary_key=True)  # The composite primary key (id_forma_pag, id_empresa, id_maquineta, qtde_parc_tot) found, that is not supported. The first column is selected.
    qtde_parc_tot = models.IntegerField()
    qtde_parc_ini = models.IntegerField(blank=True, null=True)
    qtde_parc_fin = models.IntegerField(blank=True, null=True)
    taxa = models.FloatField(blank=True, null=True)
    dias_acres_vencto = models.IntegerField(blank=True, null=True, db_comment='Campo utilizado no momento do fechamento do caixa. O sistema irß acrescentar no vencimento do cartÒo a qtde de dias que tem neste campo.')
    id_empresa = models.IntegerField()
    id_maquineta = models.ForeignKey('CadTbCMct', models.DO_NOTHING, db_column='id_maquineta')

    class Meta:
        managed = False
        db_table = 'cad_tb_c_fpg_tap'
        unique_together = (('id_forma_pag', 'id_empresa', 'id_maquineta', 'qtde_parc_tot'),)
        db_table_comment = 'Tabela responsßvel pelas taxas aprazos do cartÒo.'


class CadTbCFun(models.Model):
    id_funcionario = models.IntegerField(primary_key=True)
    ativo = models.BooleanField()
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)
    cep = models.CharField(max_length=9)
    numero = models.CharField(max_length=10)
    tel_fixo = models.CharField(max_length=14, blank=True, null=True)
    tel_movel = models.CharField(max_length=14, blank=True, null=True)
    doc_cpf = models.CharField(max_length=11, blank=True, null=True)
    doc_identidade = models.CharField(max_length=11, blank=True, null=True)
    bairro = models.CharField(max_length=40)
    id_cidade = models.ForeignKey(CadTbCCid, models.DO_NOTHING, db_column='id_cidade')
    estado = models.CharField(max_length=2, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)
    sexo = models.IntegerField()
    dta_nascimento = models.DateField()
    dta_cadastro = models.DateField()
    login = models.CharField(max_length=30, blank=True, null=True)
    senha = models.CharField(max_length=100, blank=True, null=True)
    dta_senha_expira = models.DateField(blank=True, null=True)
    id_perfil_seg = models.ForeignKey('CadTbCPes', models.DO_NOTHING, db_column='id_perfil_seg', blank=True, null=True)
    seg_alt_lim_cli = models.BooleanField(blank=True, null=True)
    seg_alt_sit_cli = models.BooleanField(blank=True, null=True)
    seg_alt_pre_pro = models.BooleanField(blank=True, null=True)
    seg_hab_bot_exc = models.BooleanField(blank=True, null=True)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    seg_vis_ult_cmp_ite = models.BooleanField(blank=True, null=True, db_comment='Este campo serß utilizado pela tela de Pesquisa de Item(F3), que terß a funþÒo de esconder o grid de dados da ·ltima compra do item.')
    seg_apr_rep_cmp_ped = models.BooleanField(blank=True, null=True, db_comment='Permite ao usußrio poder Aprovar/Reprovar pedido de compra.\nImportante:  O sistema s¾ mostrarß essa opþÒo se o m¾dulo SGQ = True;')
    seg_vis_msg_sol_cmp = models.BooleanField(blank=True, null=True, db_comment='Este campo tem a funþÒo de mostrar para o usußrio uma msg com as soliþitaþ§es de compras em aberto.')
    seg_per_canc_orv = models.BooleanField(blank=True, null=True, db_comment='Este campo serß utilizado na tela de Ordem de Serviþo.')
    seg_habilitar_seg = models.BooleanField(blank=True, null=True, db_comment='Caso este campo seja marcado, entÒo o usußrio serß obrigado a preencher os dados para login do sistema no cadastro.')
    seg_redef_senha = models.BooleanField(blank=True, null=True, db_comment='Caso este campo esteja marcado, assim que este funcionßrio fizer o Login, o sistema irß abrir uma tela para que ele redefina a senha de acesso.')
    seg_hab_bot_alt_fun = models.BooleanField(blank=True, null=True, db_comment='Desabilita o botÒo ALTERAR da tela de funcionßrios.')
    seq_vis_msg_ped_exp_fat = models.BooleanField(blank=True, null=True, db_comment='Permite que o usußrio veja os pedidos com prazo de entrega experiado.')
    seg_ctc_apg = models.BooleanField(blank=True, null=True)
    seg_alt_vend_ped = models.BooleanField(blank=True, null=True)
    seq_vis_alert_est_min = models.BooleanField(blank=True, null=True)
    excluir_caixa = models.BooleanField(blank=True, null=True)
    seg_hab_lib_brd = models.BooleanField(blank=True, null=True, db_comment='Utilizado pela tela FIN_FM_M_BRD:\nCaso este campo seja TRUE, o usußrio poderß fazer as operaþ§es de LIBERAR, BAIXAR e CANCELAR;\nCaso FALSE, nÒo terß acesso ao botÒo LIBERAR.')
    seg_vis_custo_csu_ite = models.BooleanField(blank=True, null=True)
    seg_zerar_est = models.BooleanField(blank=True, null=True)
    seg_vis_nota_csu_ite = models.BooleanField(blank=True, null=True)
    id_empresa_mob = models.IntegerField(blank=True, null=True, db_comment='Campo utilizado pelo sistema Mobile.')
    vnd_interno_externo = models.IntegerField(blank=True, null=True, db_comment='0 - Vendedor Interno; 1 - Vendedor Externo')
    tipo = models.IntegerField(blank=True, null=True, db_comment='0 - Funcionßrio 1 - Tercerizado')
    aniversariante_mes = models.BooleanField(blank=True, null=True)
    sgq_reimprime_etq = models.BooleanField(blank=True, null=True, db_comment='Se TRUE o usußrio poderß reimprimir uma etiqueta jß impressa. \r\n')
    mob_alt_preco_ped = models.BooleanField(blank=True, null=True, db_comment='Campo utilizado para informar se o usußrio pode alterar o preþo unitßrio no pedido de venda no aplicativo Produtor Mobile.')
    seg_per_desc_maior = models.BooleanField(blank=True, null=True, db_comment='Permite um desconto geral no pedido de venda, onde irß chamar uma telinha.')
    seg_cancelar_os = models.BooleanField(blank=True, null=True)
    adm_sistema = models.BooleanField(blank=True, null=True)
    per_comissao = models.FloatField(blank=True, null=True)
    seg_alt_cli_ped = models.BooleanField(blank=True, null=True)
    sgq_perm_alt_comissao_ped = models.BooleanField(blank=True, null=True, db_comment='Permitir alterar a comissÒo do representane')
    seg_alterar_local_tit_fin = models.BooleanField(blank=True, null=True)
    seg_vis_aviso_tit_spc_protesto = models.BooleanField(blank=True, null=True)
    sgq_perm_botao_ger_prod = models.BooleanField(blank=True, null=True, db_comment='Permite utilizar o botÒo Gerencia ProduþÒo dos Itens.')
    sgq_perm_atual_contagem = models.BooleanField(blank=True, null=True, db_comment='Irß permitir se o usußrio poderß clicar no botÒo Atualizar Contagem , da tela de Contagem de inventßrio')
    sgq_vis_vlr_tot_carga = models.BooleanField(blank=True, null=True)
    seg_alterar_fpg_tit_fin = models.BooleanField(blank=True, null=True)
    seg_alterar_ped_sit = models.IntegerField(blank=True, null=True, db_comment='0 - NÒo se aplica;\r\n1 - Somente pedido em situaþÒo DIGITADO;\r\n2 - Somente pedido em situaþÒo DIGITADO ou APROVADO;\r\n3 - Somente pedido em situaþÒo DIGITADO, APROVADO ou EM PRODUÃ├O;\r\n')
    sgq_per_comissao = models.FloatField(blank=True, null=True, db_comment='Utilizado no pedido de venda quando usa o sgq.')
    per_alterar_repres = models.BooleanField(blank=True, null=True, db_comment='Se TRUE o usußrio poder alterar o campo REPRESENTANTE na tela de clientes.')
    bus_som_ped_sem_pagtos = models.BooleanField(blank=True, null=True, db_comment='Buscar somente pedidos do tipo = Sem Pagamentos (CAD_TB_C_CPG) na importaþÒo para OPs.')
    sgq_perm_inserir_itens_op = models.BooleanField(blank=True, null=True, db_comment='Permite incluir itens na O.P.')

    class Meta:
        managed = False
        db_table = 'cad_tb_c_fun'
        db_table_comment = 'Tabela de Cadastro de Funcionarios'


class CadTbCFunCpn(models.Model):
    id_funcionario = models.OneToOneField(CadTbCFun, models.DO_NOTHING, db_column='id_funcionario', primary_key=True)  # The composite primary key (id_funcionario, id_condicao_pag) found, that is not supported. The first column is selected.
    id_condicao_pag = models.ForeignKey(CadTbCCpg, models.DO_NOTHING, db_column='id_condicao_pag')

    class Meta:
        managed = False
        db_table = 'cad_tb_c_fun_cpn'
        unique_together = (('id_funcionario', 'id_condicao_pag'),)
        db_table_comment = 'Tabela: CondiþÒo de Pagamento nÒo permitada para o vendedor.'


class CadTbCFunCrg(models.Model):
    id_funcionario = models.OneToOneField(CadTbCFun, models.DO_NOTHING, db_column='id_funcionario', primary_key=True)  # The composite primary key (id_funcionario, id_cargo) found, that is not supported. The first column is selected.
    id_cargo = models.ForeignKey('PcpTbCCrg', models.DO_NOTHING, db_column='id_cargo')

    class Meta:
        managed = False
        db_table = 'cad_tb_c_fun_crg'
        unique_together = (('id_funcionario', 'id_cargo'),)


class CadTbCFunEmp(models.Model):
    id_funcionario = models.OneToOneField(CadTbCFun, models.DO_NOTHING, db_column='id_funcionario', primary_key=True)  # The composite primary key (id_funcionario, id_empresa) found, that is not supported. The first column is selected.
    id_empresa = models.ForeignKey('CadTbCPar', models.DO_NOTHING, db_column='id_empresa')
    permitir_acesso = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_fun_emp'
        unique_together = (('id_funcionario', 'id_empresa'),)


class CadTbCGrp(models.Model):
    id_codigo = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_grp'


class CadTbCGru(models.Model):
    id_grupo = models.CharField(primary_key=True, max_length=11)
    descricao = models.CharField(max_length=30)
    origem_mercadoria = models.CharField(max_length=1, blank=True, null=True, db_comment='0 - Nacional, exceto as indicadas nos c¾digos 3 a 5\n1 - Estrangeira - ImportaþÒo direta, exceto a indicada no c¾digo 6\n2 - Estrangeira - Adquirida no mercado interno, exceto a indicada no c¾digo 7\n3 - Nacional, mercadoria ou bem com Conte·do de ImportaþÒo superior a 40% (quarenta por cento)\n4 - Nacional, cuja produþÒo tenha sido feita em conformidade com os processos produtivos bßsicos. \n5 - Nacional, mercadoria ou bem com Conte·do de ImportaþÒo inferior ou igual a 40% (quarenta por cento)\n6 - Estrangeira - ImportaþÒo direta, sem similar nacional, constante em lista de ResoluþÒo CAMEX.\n7 - Estrangeira - Adquirida no mercado interno, sem similar nacional, constante em lista de ResoluþÒo CAMEX.\n')
    tipo = models.IntegerField(blank=True, null=True, db_comment='0 - Analitico,\n1 - Sintetico')
    nivel = models.IntegerField(blank=True, null=True)
    tipo_item = models.CharField(max_length=2, blank=True, null=True, db_comment='  00 - Mercadoria para Revenda\n  01 - Materia prima\n  02 - Embalagem\n  03 - Produto em processo\n  04 - Produto Acabado\n  05 - subproduto\n  06 - Produto Intermediario\n  07 - Material de Uso e consumo\n  08 - Ativo Imobilizado\n  09 - Serviþos\n  10 - Outros Insumos\n  99 - Outros\n')
    id_tributo = models.ForeignKey('CadTbCTri', models.DO_NOTHING, db_column='id_tributo', blank=True, null=True)
    mva = models.FloatField(blank=True, null=True)
    promo_ativa = models.BooleanField(blank=True, null=True)
    promo_perc = models.FloatField(blank=True, null=True)
    ali_interna_icms = models.FloatField(blank=True, null=True)
    id_st_pis_entrada = models.CharField(max_length=2, blank=True, null=True)
    id_st_cof_entrada = models.CharField(max_length=2, blank=True, null=True)
    id_st_ipi_entrada = models.CharField(max_length=2, blank=True, null=True)
    id_st_pis_saida = models.CharField(max_length=2, blank=True, null=True)
    id_st_cof_saida = models.CharField(max_length=2, blank=True, null=True)
    id_st_ipi_saida = models.CharField(max_length=2, blank=True, null=True)
    desc_ativa = models.BooleanField(blank=True, null=True)
    desc_perc = models.FloatField(blank=True, null=True)
    per_ipi = models.FloatField(blank=True, null=True)
    id_cla = models.IntegerField(blank=True, null=True)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    id_fte_etq = models.IntegerField(blank=True, null=True)
    ser_terceiro = models.BooleanField(blank=True, null=True, db_comment='Serviþo de Terceiro, campo utilizado na modulo de oficina.')
    nome_selo_etq = models.CharField(max_length=100, blank=True, null=True, db_comment="Este campo Ú utilizado pela tela PCP_FM_R_ETQ (impressÒo de etiqueta)\nex:  'selo_0001.png'")
    imprime_selo_etq = models.BooleanField(blank=True, null=True, db_comment='Caso seja TRUE , no momento da impressÒo o sistema irß utilizar o mesmo lay-out de ColchÒo Bordado, mas sem a imagem do selo.')
    imprime_msq_etq = models.BooleanField(blank=True, null=True)
    msg_etq1 = models.CharField(max_length=100, blank=True, null=True)
    msg_etq2 = models.CharField(max_length=100, blank=True, null=True)
    msg_etq3 = models.CharField(max_length=100, blank=True, null=True)
    msg_etq4 = models.CharField(max_length=100, blank=True, null=True)
    msg_etq5 = models.CharField(max_length=100, blank=True, null=True)
    msg_etq6 = models.CharField(max_length=100, blank=True, null=True)
    msg_etq7 = models.CharField(max_length=100, blank=True, null=True)
    ctc_epi = models.BooleanField(blank=True, null=True)
    aliquota_ecf = models.CharField(max_length=20, blank=True, null=True)
    part_perc_fcp = models.FloatField(blank=True, null=True, db_comment='Percentual de fundo de combate a pobreza.')
    fp_per_lucro_ven = models.FloatField(blank=True, null=True, db_comment='Colocar no cadastro de grupo')
    dre_perc_out_ded_ven = models.FloatField(blank=True, null=True)
    dre_perc_ircs = models.FloatField(blank=True, null=True)
    ctr_lot_entr = models.BooleanField(blank=True, null=True)
    imp_etq_simples = models.BooleanField(blank=True, null=True)
    path_etq_simples = models.CharField(max_length=100, blank=True, null=True)
    per_cmv_interno = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    per_cmv_externo = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    sgq_inf_qtde_ite_carg = models.BooleanField(blank=True, null=True, db_comment='Se este campo estiver marcado , quer dizer que o usußrio no momento da conferÛncia de carga poderß informar a Qtde total do item para conferir.')
    mob_nome_foto = models.CharField(max_length=60, blank=True, null=True)
    utiliza_lote = models.BooleanField(blank=True, null=True)
    tipo_produto = models.IntegerField(blank=True, null=True, db_comment='1 - Pneu')
    cod_ntr = models.ForeignKey('CadTbCNtr', models.DO_NOTHING, db_column='cod_ntr', blank=True, null=True, db_comment='Estß ligado a tabela CAD_TB_C_NTR (Natureza da Receita)')
    sgq_verif_cod_barra_ped = models.BooleanField(blank=True, null=True, db_comment='utilizado no momento do pedido de venda para verificar se o produto Ú obrigado a ter o c¾digo de barra (GTIN)')
    sgq_descartar_op_etq_cof = models.BooleanField(blank=True, null=True, db_comment='Para os itens que precisa informar a Qtde de etiquetas que vai sair, esse parÔmetro serve para dizer se o sistema tem que levar em consideraþÒo o saldo disponivel em cima da OP da etiqueta ou nÒo.')
    sgq_bloco_espuma = models.BooleanField(blank=True, null=True, db_comment='Se for TRUE o sistema entenderß que os itens deste grupo serÒo do tipo Bloco de Espuma. ')
    sgq_calc_bloco_produzir = models.BooleanField(blank=True, null=True, db_comment='Indica se faz parte de cßlculo p/gerar a O.P do bloco de espuma')
    id_item_bloco_espuma = models.IntegerField(blank=True, null=True, db_comment='S¾ pode aceitar item que faþa parte de grupo de estoque que Ú do tipo Bloco de Espuma.')
    id_item_bloco_espuma_2 = models.IntegerField(blank=True, null=True)
    id_item_bloco_espuma_3 = models.IntegerField(blank=True, null=True)
    id_item_bloco_espuma_revest_1 = models.IntegerField(blank=True, null=True)
    id_item_bloco_espuma_revest_2 = models.IntegerField(blank=True, null=True)
    rastrea_espumacao = models.BooleanField(blank=True, null=True)
    rastrea_laminacao = models.BooleanField(blank=True, null=True)
    rastrea_bordadeira = models.BooleanField(blank=True, null=True)
    rastrea_corte_costura = models.BooleanField(blank=True, null=True)
    rastrea_colagem_tampo_alfin = models.BooleanField(blank=True, null=True)
    rastrea_colagem_molas = models.BooleanField(blank=True, null=True)
    rastrea_montagem_caixa_box = models.BooleanField(blank=True, null=True)
    exibe_na_impressao_op = models.BooleanField(blank=True, null=True)
    nome_selo_inmetro_etq = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_gru'
        db_table_comment = 'Tabela de Grupo de Produtos'


class CadTbCGruCor(models.Model):
    id_grupo = models.ForeignKey(CadTbCGru, models.DO_NOTHING, db_column='id_grupo')
    id_cor = models.ForeignKey(CadTbCCor, models.DO_NOTHING, db_column='id_cor')

    class Meta:
        managed = False
        db_table = 'cad_tb_c_gru_cor'
        unique_together = (('id_grupo', 'id_cor'),)


class CadTbCGruEmp(models.Model):
    id_grupo = models.OneToOneField(CadTbCGru, models.DO_NOTHING, db_column='id_grupo', primary_key=True)  # The composite primary key (id_grupo, id_empresa) found, that is not supported. The first column is selected.
    id_empresa = models.ForeignKey('CadTbCPar', models.DO_NOTHING, db_column='id_empresa')
    fator_corr_aprazo = models.FloatField(blank=True, null=True)
    fator_corr_avista = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_gru_emp'
        unique_together = (('id_grupo', 'id_empresa'),)


class CadTbCHfg(models.Model):
    id_controle = models.IntegerField(primary_key=True)
    nivel = models.IntegerField()
    id_forma_pag = models.ForeignKey(CadTbCFpg, models.DO_NOTHING, db_column='id_forma_pag')

    class Meta:
        managed = False
        db_table = 'cad_tb_c_hfg'


class CadTbCInf(models.Model):
    id_inf = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=800)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_inf'
        db_table_comment = 'Cadastro de Informaþ§es do Fisco'


class CadTbCIte(models.Model):
    id_item = models.IntegerField(primary_key=True)
    ativo = models.BooleanField()
    cardapio = models.BooleanField()
    descricao = models.CharField(max_length=100)
    fantasia = models.CharField(max_length=30, blank=True, null=True)
    referencia = models.CharField(max_length=100, blank=True, null=True)
    aplicacao = models.CharField(max_length=100, blank=True, null=True)
    id_fornecedor = models.ForeignKey(CadTbCFor, models.DO_NOTHING, db_column='id_fornecedor')
    id_grupo = models.ForeignKey(CadTbCGru, models.DO_NOTHING, db_column='id_grupo')
    id_und_compra = models.ForeignKey('CadTbCUnd', models.DO_NOTHING, db_column='id_und_compra', blank=True, null=True)
    id_und_venda = models.ForeignKey('CadTbCUnd', models.DO_NOTHING, db_column='id_und_venda', related_name='cadtbcite_id_und_venda_set', blank=True, null=True)
    emb_compra = models.FloatField(blank=True, null=True)
    emb_venda = models.FloatField(blank=True, null=True)
    cod_barra = models.CharField(max_length=50, blank=True, null=True)
    cod_fabrica = models.CharField(max_length=30, blank=True, null=True)
    pes_liquido = models.FloatField(blank=True, null=True)
    pes_bruto = models.FloatField(blank=True, null=True)
    est_minimo = models.FloatField(blank=True, null=True)
    loca_rua = models.CharField(max_length=4, blank=True, null=True)
    loca_prateleira = models.CharField(max_length=4, blank=True, null=True)
    loca_escaninho = models.CharField(max_length=4, blank=True, null=True)
    cubagem = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    tam_largura = models.FloatField(blank=True, null=True)
    tam_comprimento = models.FloatField(blank=True, null=True)
    tam_espessura = models.FloatField(blank=True, null=True)
    densidade = models.IntegerField(blank=True, null=True)
    densidade_2 = models.IntegerField(blank=True, null=True)
    densidade_3 = models.IntegerField(blank=True, null=True)
    tipo = models.IntegerField(blank=True, null=True, db_comment='Campo utilizado no sistema de produþÒo\n0 - Normal\n1 - TAMPO  - Utilizado pela bordadeira\n2 - FAIXA  - Utilizado pela bordadeira \n3 - ESPUMA - Utilizado pelo bloco cilindrico  \n')
    geracao_lote_interno = models.IntegerField(blank=True, null=True, db_comment='Campo utilizado no sistema de produþÒo.\nTodo produto tem que ter o seu lote_interno que Ú gerado pelo sistema, isso Ú devido a rastreabilidade.\nO produto pode ter o seu lote gerado a partir de:  \n\n0 - Nota fiscal de entrada, 1 - EspumaþÒo, 2 - Bordadeira, 3 - InspeþÒo de Itens \n, 4 - NÒo utiliza   ')
    destino_reclamado = models.IntegerField(blank=True, null=True, db_comment='Campo utilizado somente no sistema de produþÒo.\nEste campo serß utilizado pela rotina de Atendimento das reclamaþ§es do cliente: PCP_FM_M_ACR.         \n0 - Nenhum\n1 - Flocagem\n2 - Descarte')
    etiq_classificacao_pro = models.IntegerField(blank=True, null=True, db_comment='Campo utilizado no sistema de produþÒo.\nEste campo foi direcinado para a tabela PCP_TB_C_CLE (ID_CLE)')
    etiq_medidas = models.CharField(max_length=60, blank=True, null=True)
    etiq_madeira = models.CharField(max_length=200, blank=True, null=True)
    etiq_espuma1 = models.CharField(max_length=300, blank=True, null=True)
    etiq_espuma2 = models.CharField(max_length=300, blank=True, null=True)
    etiq_espuma3 = models.CharField(max_length=300, blank=True, null=True)
    etiq_revestimento1 = models.CharField(max_length=300, blank=True, null=True)
    etiq_revestimento2 = models.CharField(max_length=300, blank=True, null=True)
    etiq_revestimento3 = models.CharField(max_length=300, blank=True, null=True)
    etiq_recomendacoes_1 = models.CharField(max_length=80, blank=True, null=True)
    etiq_recomendacoes_2 = models.CharField(max_length=80, blank=True, null=True)
    lote_fabric_obrigatorio = models.IntegerField(blank=True, null=True, db_comment='Este campo Ú utilizado pela tela controle de inspeþÒo e recebimento de produto (EST_FM_M_NFE_S). \nIsso server para dizer se o campo lote do fabricante Ú obrigat¾rio.')
    id_ncm = models.ForeignKey('CadTbCNcm', models.DO_NOTHING, db_column='id_ncm', blank=True, null=True)
    preco_avista = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True, db_comment='Descricao completa, campo utilizado no enBueld.')
    preco_aprazo = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    dta_cadastro = models.DateField(blank=True, null=True)
    etiq_modelo = models.CharField(max_length=70, blank=True, null=True)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    id_familia = models.ForeignKey(CadTbCFam, models.DO_NOTHING, db_column='id_familia', blank=True, null=True)
    des_completa = models.CharField(max_length=250, blank=True, null=True)
    rt_pricipio_ativo = models.CharField(max_length=400, blank=True, null=True)
    rt_composicao = models.CharField(max_length=400, blank=True, null=True)
    ret_emb_capacidade = models.CharField(max_length=20, blank=True, null=True)
    ret_emb_nao_lavavel = models.IntegerField(blank=True, null=True, db_comment='0 - Contaminada\n1 - NÒo-Contaminada')
    ret_emb_lavaveis = models.IntegerField(blank=True, null=True, db_comment='0 - Plßstico\n1 - Metal\n2 - Vidro')
    cod_onu = models.CharField(max_length=20, blank=True, null=True)
    sgq_critica_laudo_fab = models.BooleanField(blank=True, null=True, db_comment='Este campo serß utilizado pela tela de InspeþÒo de Itens (FAT_FM_M_IQM).')
    tam_observacoes = models.CharField(max_length=150, blank=True, null=True)
    etiq_id_cue = models.IntegerField(blank=True, null=True, db_comment='Refere-se a tabela PCP_TB_C_CUE.')
    preco_avista_ant_reajuste = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    preco_aprazo_ant_reajuste = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    dta_ult_reajuste = models.DateField(blank=True, null=True)
    rt_registro = models.CharField(max_length=25, blank=True, null=True)
    custo_servico = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    id_grupo_prod = models.ForeignKey(CadTbCGrp, models.DO_NOTHING, db_column='id_grupo_prod', blank=True, null=True)
    id_item_anterior = models.IntegerField(blank=True, null=True)
    preco_sugerido = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    per_cmv_interno = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    per_cmv_externo = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    etiq_espuma4 = models.CharField(max_length=300, blank=True, null=True)
    etiq_espuma5 = models.CharField(max_length=300, blank=True, null=True)
    etiq_espuma6 = models.CharField(max_length=300, blank=True, null=True)
    etiq_revestimento4 = models.CharField(max_length=300, blank=True, null=True)
    etiq_revestimento5 = models.CharField(max_length=300, blank=True, null=True)
    etiq_revestimento6 = models.CharField(max_length=300, blank=True, null=True)
    etiq_marca = models.CharField(max_length=30, blank=True, null=True)
    sgq_tamanho_ite_epp = models.FloatField(blank=True, null=True, db_comment='Campo utilizado pelo relat¾rio de Entrada de Produto Acabado')
    tipo_servico = models.BooleanField(blank=True, null=True)
    mob_nome_foto = models.CharField(max_length=60, blank=True, null=True)
    pneu_largura = models.CharField(max_length=10, blank=True, null=True)
    pneu_altura = models.CharField(max_length=10, blank=True, null=True)
    pneu_aro = models.CharField(max_length=10, blank=True, null=True)
    id_marca = models.IntegerField(blank=True, null=True)
    sgq_personalizado = models.BooleanField(blank=True, null=True, db_comment='produto utilizado pelo m¾dulo sgq.')
    temp_etiq_medidas = models.CharField(max_length=60, blank=True, null=True)
    cod_item_prod = models.IntegerField(blank=True, null=True, db_comment='c¾digo do item da produþÒo ')
    etiq_tipo_produto = models.IntegerField(blank=True, null=True, db_comment='0 - COLCH├O DE ESPUMA\r\n1 - COLCH├O BOX CONJUGADO\r\n2 - COLCH├O AUXILIAR\r\n3 - COLCH├O MISTO\r\n')
    tam_esp_espessura_1 = models.FloatField(blank=True, null=True)
    tam_esp_espessura_2 = models.FloatField(blank=True, null=True)
    tam_esp_espessura_3 = models.FloatField(blank=True, null=True)
    tam_esp_comprimento_1 = models.FloatField(blank=True, null=True)
    tam_esp_comprimento_2 = models.FloatField(blank=True, null=True)
    tam_esp_comprimento_3 = models.FloatField(blank=True, null=True)
    tam_esp_largura_1 = models.FloatField(blank=True, null=True)
    tam_esp_largura_2 = models.FloatField(blank=True, null=True)
    tam_esp_largura_3 = models.FloatField(blank=True, null=True)
    cubagem_esp_1 = models.FloatField(blank=True, null=True)
    cubagem_esp_2 = models.FloatField(blank=True, null=True)
    cubagem_esp_3 = models.FloatField(blank=True, null=True)
    tipo_produto = models.IntegerField(blank=True, null=True, db_comment='0 - Outros\r\n1 - Manual do Usußrio\r\n2 - Espuma\r\n3 - Bobina\r\n4 - ColchÒo de espuma\r\n5 - ColchÒo de molas\r\n6 - Cama Box\r\n7 - Base Box\r\n8 - Travesseiro\r\n9 - Colchonete\r\n10 - Encosto\r\n11 - Maquete\r\n12 - Caixa de madeira\r\n13 - Grampo\r\n14 - Cama Box de Molas')
    tam_esp_espessura_revest_1 = models.FloatField(blank=True, null=True)
    tam_esp_espessura_revest_2 = models.FloatField(blank=True, null=True)
    tam_esp_comp_revest_1 = models.FloatField(blank=True, null=True)
    tam_esp_comp_revest_2 = models.FloatField(blank=True, null=True)
    tam_esp_largura_revest_1 = models.FloatField(blank=True, null=True)
    tam_esp_largura_revest_2 = models.FloatField(blank=True, null=True)
    cubagem_esp_revest_1 = models.FloatField(blank=True, null=True)
    cubagem_esp_revest_2 = models.FloatField(blank=True, null=True)
    densidade_esp_revest_1 = models.FloatField(blank=True, null=True)
    densidade_esp_revest_2 = models.FloatField(blank=True, null=True)
    id_item_caixa = models.IntegerField(blank=True, null=True, db_comment='Aqui deve ser informado o item do tipo (CAIXA) que Ú utilizado para produzir as bases box, cama box')

    class Meta:
        managed = False
        db_table = 'cad_tb_c_ite'
        db_table_comment = 'Cadastro de Itens'


class CadTbCIteApl(models.Model):
    id_item = models.OneToOneField(CadTbCIte, models.DO_NOTHING, db_column='id_item', primary_key=True)  # The composite primary key (id_item, id_veiculo) found, that is not supported. The first column is selected.
    id_veiculo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cad_tb_c_ite_apl'
        unique_together = (('id_item', 'id_veiculo'),)
        db_table_comment = 'APLICACAO\nTABELA UTILIZADA PARA COLOCAR OS VEIUCLOS/MAQUIANS QUE UTILIZAM ESTA PEC.\nTABELA UTILIZADA EM CTC E OFI'


class CadTbCIteCat(models.Model):
    id_item = models.OneToOneField(CadTbCIte, models.DO_NOTHING, db_column='id_item', primary_key=True)  # The composite primary key (id_item, id_cat) found, that is not supported. The first column is selected.
    id_cat = models.ForeignKey('OfiTbCCat', models.DO_NOTHING, db_column='id_cat')
    preco = models.DecimalField(max_digits=18, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_ite_cat'
        unique_together = (('id_item', 'id_cat'),)


class CadTbCIteCoj(models.Model):
    id_item = models.OneToOneField(CadTbCIte, models.DO_NOTHING, db_column='id_item', primary_key=True)  # The composite primary key (id_item, id_item_conjugado) found, that is not supported. The first column is selected.
    id_item_conjugado = models.IntegerField()
    qtde = models.FloatField(blank=True, null=True)
    id_busca_item = models.CharField(max_length=30, blank=True, null=True)
    id_cor = models.IntegerField(blank=True, null=True)
    id_tamanho = models.IntegerField(blank=True, null=True)
    qtde_tempo = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_ite_coj'
        unique_together = (('id_item', 'id_item_conjugado'),)


class CadTbCIteCom(models.Model):
    id_item = models.OneToOneField(CadTbCIte, models.DO_NOTHING, db_column='id_item', primary_key=True)  # The composite primary key (id_item, id_materia_prima) found, that is not supported. The first column is selected.
    id_materia_prima = models.IntegerField()
    qtde = models.FloatField()

    class Meta:
        managed = False
        db_table = 'cad_tb_c_ite_com'
        unique_together = (('id_item', 'id_materia_prima'),)
        db_table_comment = 'Cadastro de Ficha de composiþÒo de produto acabado.'


class CadTbCIteCul(models.Model):
    id_item = models.ForeignKey(CadTbCIte, models.DO_NOTHING, db_column='id_item')
    id_cultura = models.ForeignKey(CadTbCCul, models.DO_NOTHING, db_column='id_cultura')
    obs = models.CharField(max_length=800, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_ite_cul'


class CadTbCIteEsp(models.Model):
    id_item = models.OneToOneField(CadTbCIte, models.DO_NOTHING, db_column='id_item', primary_key=True)  # The composite primary key (id_item, id_especificacao) found, that is not supported. The first column is selected.
    id_especificacao = models.ForeignKey('PcpTbCEsp', models.DO_NOTHING, db_column='id_especificacao')

    class Meta:
        managed = False
        db_table = 'cad_tb_c_ite_esp'
        unique_together = (('id_item', 'id_especificacao'),)
        db_table_comment = 'Tabela de EspecificaþÒo - PCP'


class CadTbCIteLoc(models.Model):
    id_item = models.OneToOneField(CadTbCIte, models.DO_NOTHING, db_column='id_item', primary_key=True)  # The composite primary key (id_item, id_empresa) found, that is not supported. The first column is selected.
    id_empresa = models.ForeignKey('CadTbCPar', models.DO_NOTHING, db_column='id_empresa')
    loca_rua = models.CharField(max_length=20, blank=True, null=True)
    loca_prateleira = models.CharField(max_length=20, blank=True, null=True)
    loca_escaninho = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_ite_loc'
        unique_together = (('id_item', 'id_empresa'),)


class CadTbCItePrc(models.Model):
    id_item = models.OneToOneField(CadTbCIte, models.DO_NOTHING, db_column='id_item', primary_key=True)  # The composite primary key (id_item, id_perfil_cli, id_empresa) found, that is not supported. The first column is selected.
    id_perfil_cli = models.IntegerField()
    preco_avista = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    preco1 = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    preco2 = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    preco3 = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    preco4 = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    id_empresa = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cad_tb_c_ite_prc'
        unique_together = (('id_item', 'id_perfil_cli', 'id_empresa'),)


class CadTbCIteTpr(models.Model):
    id_item = models.OneToOneField(CadTbCIte, models.DO_NOTHING, db_column='id_item', primary_key=True)  # The composite primary key (id_item, id_tpr) found, that is not supported. The first column is selected.
    id_tpr = models.IntegerField()
    preco = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    cod_fabrica = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_ite_tpr'
        unique_together = (('id_item', 'id_tpr'),)
        db_table_comment = 'Tabela de Precos, atender ao sistema enBuild'


class CadTbCIteXml(models.Model):
    id_item = models.OneToOneField(CadTbCIte, models.DO_NOTHING, db_column='id_item', primary_key=True)  # The composite primary key (id_item, id_emitente, id_fabrica) found, that is not supported. The first column is selected.
    id_emitente = models.IntegerField()
    id_fabrica = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_ite_xml'
        unique_together = (('id_item', 'id_emitente', 'id_fabrica'),)


class CadTbCLto(models.Model):
    id_local_titulo = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=30)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    em_protesto = models.BooleanField(blank=True, null=True)
    em_spc = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_lto'
        db_table_comment = 'Tabela de Local de Titulo'


class CadTbCMar(models.Model):
    id_mar = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=60, blank=True, null=True)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_mar'
        db_table_comment = 'Cadastro de Marcas'


class CadTbCMct(models.Model):
    id_maquineta = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=30, blank=True, null=True)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_mct'
        db_table_comment = 'Cadastro de Maquinetas de CartÒo de CrÚdito'


class CadTbCMtv(models.Model):
    id_vendedor = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_vendedor')
    ano = models.IntegerField()
    id_grupo_prod = models.ForeignKey(CadTbCGrp, models.DO_NOTHING, db_column='id_grupo_prod')
    id_mtv = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_mtv'


class CadTbCMtvMes(models.Model):
    id_mtv = models.OneToOneField(CadTbCMtv, models.DO_NOTHING, db_column='id_mtv', primary_key=True)
    qtde_mes_01 = models.FloatField(blank=True, null=True)
    valor_mes_01 = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    qtde_mes_02 = models.FloatField(blank=True, null=True)
    valor_mes_02 = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    qtde_mes_03 = models.FloatField(blank=True, null=True)
    valor_mes_03 = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    qtde_mes_04 = models.FloatField(blank=True, null=True)
    valor_mes_04 = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    qtde_mes_05 = models.FloatField(blank=True, null=True)
    valor_mes_05 = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    qtde_mes_06 = models.FloatField(blank=True, null=True)
    valor_mes_06 = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    qtde_mes_07 = models.FloatField(blank=True, null=True)
    valor_mes_07 = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    qtde_mes_08 = models.FloatField(blank=True, null=True)
    valor_mes_08 = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    qtde_mes_09 = models.FloatField(blank=True, null=True)
    valor_mes_09 = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    qtde_mes_10 = models.FloatField(blank=True, null=True)
    valor_mes_10 = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    qtde_mes_11 = models.FloatField(blank=True, null=True)
    valor_mes_11 = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    qtde_mes_12 = models.FloatField(blank=True, null=True)
    valor_mes_12 = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    qtde_total = models.FloatField(blank=True, null=True)
    valor_total = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_mtv_mes'


class CadTbCMve(models.Model):
    id_mve = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=50, blank=True, null=True)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    id_mar = models.ForeignKey(CadTbCMar, models.DO_NOTHING, db_column='id_mar', blank=True, null=True)
    id_cat = models.ForeignKey('OfiTbCCat', models.DO_NOTHING, db_column='id_cat', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_mve'
        db_table_comment = 'Tabela de Cadastro Modelo de Veiculo'


class CadTbCNat(models.Model):
    id_classe = models.CharField(primary_key=True, max_length=4)
    descricao = models.CharField(max_length=50)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_nat'
        db_table_comment = 'Tabela de Naturezas (Classes)'


class CadTbCNcm(models.Model):
    id_ncm = models.CharField(primary_key=True, max_length=10)
    descricao = models.CharField(max_length=100)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    per_imposto = models.FloatField(blank=True, null=True)
    cest = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_ncm'
        db_table_comment = 'Cadastro de NCM'


class CadTbCNtr(models.Model):
    codigo = models.CharField(primary_key=True, max_length=3)
    descricao = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_ntr'
        db_table_comment = 'Cadastro Natureza da Receita'


class CadTbCPai(models.Model):
    id_pais = models.CharField(primary_key=True, max_length=5)
    descricao = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_pai'
        db_table_comment = 'Cadastro de Pais'


class CadTbCPar(models.Model):
    id_empresa = models.IntegerField(primary_key=True)
    emp_cnpj = models.CharField(max_length=14, blank=True, null=True)
    id_ramo = models.ForeignKey('CadTbCRam', models.DO_NOTHING, db_column='id_ramo')
    emp_razao = models.CharField(max_length=50)
    emp_endereco = models.CharField(max_length=50)
    emp_numero = models.CharField(max_length=10)
    emp_complemento = models.CharField(max_length=30, blank=True, null=True)
    emp_bairro = models.CharField(max_length=40, db_comment='Bairro da Empresa')
    id_cidade = models.ForeignKey(CadTbCCid, models.DO_NOTHING, db_column='id_cidade', blank=True, null=True)
    emp_cep = models.CharField(max_length=9)
    emp_telefone = models.CharField(max_length=14, blank=True, null=True)
    emp_fax = models.CharField(max_length=14, blank=True, null=True)
    emp_email = models.CharField(max_length=60, blank=True, null=True)
    emp_site = models.CharField(max_length=60, blank=True, null=True)
    emp_fantasia = models.CharField(max_length=50, blank=True, null=True)
    emp_im = models.CharField(max_length=20, blank=True, null=True)
    emp_ie = models.CharField(max_length=20, blank=True, null=True)
    emp_suframa = models.CharField(max_length=20, blank=True, null=True)
    emp_numero_junta = models.CharField(max_length=20, blank=True, null=True)
    res_nome = models.CharField(max_length=50)
    res_qualificacao = models.CharField(max_length=10, blank=True, null=True)
    res_cpf = models.CharField(max_length=11, blank=True, null=True)
    res_cep = models.CharField(max_length=9)
    res_endereco = models.CharField(max_length=50)
    res_numero = models.CharField(max_length=10)
    res_complemento = models.CharField(max_length=30, blank=True, null=True)
    res_bairro = models.CharField(max_length=40)
    res_cp = models.CharField(max_length=14, blank=True, null=True)
    res_telefone = models.CharField(max_length=14, blank=True, null=True)
    res_fax = models.CharField(max_length=14, blank=True, null=True)
    res_email = models.CharField(max_length=60, blank=True, null=True)
    cnt_nome = models.CharField(max_length=50)
    cnt_cpf = models.CharField(max_length=11, blank=True, null=True)
    cnt_crc = models.CharField(max_length=10)
    cnt_cnpj = models.CharField(max_length=14, blank=True, null=True)
    cnt_cep = models.CharField(max_length=9)
    cnt_endereco = models.CharField(max_length=50)
    cnt_numero = models.CharField(max_length=10)
    cnt_complemento = models.CharField(max_length=30, blank=True, null=True)
    cnt_bairro = models.CharField(max_length=40)
    cnt_telefone = models.CharField(max_length=14, blank=True, null=True)
    cnt_fax = models.CharField(max_length=14, blank=True, null=True)
    cnt_email = models.CharField(max_length=60, blank=True, null=True)
    cnt_id_cidade = models.CharField(max_length=10, blank=True, null=True)
    cnt_qualificacao = models.CharField(max_length=10, blank=True, null=True)
    cnt_cp = models.CharField(max_length=14, blank=True, null=True)
    res_cidade = models.CharField(max_length=30, blank=True, null=True)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    res_id_cidade = models.CharField(max_length=10, blank=True, null=True)
    banco = models.IntegerField(blank=True, null=True)
    agencia = models.CharField(max_length=10, blank=True, null=True)
    conta_corrente = models.CharField(max_length=20, blank=True, null=True)
    agencia_dig = models.IntegerField(blank=True, null=True)
    conta_corrente_dig = models.IntegerField(blank=True, null=True)
    gps_latitude = models.FloatField(blank=True, null=True)
    gps_longitude = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_par'
        db_table_comment = 'Cadastro de Empresa e seus parametros.'


class CadTbCParBxp(models.Model):
    id_empresa = models.OneToOneField(CadTbCPar, models.DO_NOTHING, db_column='id_empresa', primary_key=True)  # The composite primary key (id_empresa, id_empresa_bxp) found, that is not supported. The first column is selected.
    id_empresa_bxp = models.IntegerField()
    permite_baixar = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_par_bxp'
        unique_together = (('id_empresa', 'id_empresa_bxp'),)
        db_table_comment = 'Empresas permitidas baixar contas a pagar na empresa logada.'


class CadTbCParBxr(models.Model):
    id_empresa = models.OneToOneField(CadTbCPar, models.DO_NOTHING, db_column='id_empresa', primary_key=True)  # The composite primary key (id_empresa, id_empresa_bxr) found, that is not supported. The first column is selected.
    id_empresa_bxr = models.IntegerField()
    permite_baixar = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_par_bxr'
        unique_together = (('id_empresa', 'id_empresa_bxr'),)
        db_table_comment = 'Empresas permitidas baixar contas a receber na empresa logada.'


class CadTbCParCpg(models.Model):
    id_empresa = models.OneToOneField(CadTbCPar, models.DO_NOTHING, db_column='id_empresa', primary_key=True)  # The composite primary key (id_empresa, id_condicao_pag) found, that is not supported. The first column is selected.
    id_condicao_pag = models.ForeignKey(CadTbCCpg, models.DO_NOTHING, db_column='id_condicao_pag')
    per_reajuste = models.FloatField(blank=True, null=True)
    sequencia = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_par_cpg'
        unique_together = (('id_empresa', 'id_condicao_pag'),)
        db_table_comment = 'CondiþÒo de pagamento para hieraquia de preþos (composiþÒo do preþoa a prazo)'


class CadTbCParCtr(models.Model):
    id_empresa = models.OneToOneField(CadTbCPar, models.DO_NOTHING, db_column='id_empresa', primary_key=True)
    ativa_producao = models.BooleanField(blank=True, null=True)
    ped_ativa_titulos = models.BooleanField(blank=True, null=True)
    ped_aceita_est_negativo = models.BooleanField(blank=True, null=True)
    utiliza_almoxarifado = models.BooleanField(blank=True, null=True)
    utiliza_lote_na_entrada = models.BooleanField(blank=True, null=True)
    ativa_cor = models.BooleanField(blank=True, null=True)
    ativa_tamanho = models.BooleanField(blank=True, null=True)
    rcr_inf_pag_credito = models.BooleanField(blank=True, null=True)
    nfe_separa_prod_serv = models.BooleanField(blank=True, null=True, db_comment='Separa produtos de serviþos no momento de geraþÒo da nota fiscal, originando de pedido e Ordem de serviþos.')
    ped_ver_limite = models.BooleanField(blank=True, null=True, db_comment='Verifica se no pedido de venda vai validar limite de credito!')
    faz_corr_preco_perfil = models.BooleanField(blank=True, null=True)
    tax_juros_mensal = models.FloatField(blank=True, null=True)
    per_margem_lucro = models.FloatField(blank=True, null=True, db_comment='mARGEM UTILIZADA NA ENTRADA DE MERCADORIA PARA CALCULO DO PREÃO DE VENDA SUGERIDO.')
    per_desp_fixa = models.FloatField(blank=True, null=True, db_comment='Percentual das despesas administrativa, este campo Ú para compor o lucro liquido na venda.')
    per_cofins_l_real = models.FloatField(blank=True, null=True)
    per_pis_l_real = models.FloatField(blank=True, null=True)
    dia_protesto = models.IntegerField(blank=True, null=True)
    per_ir = models.FloatField(blank=True, null=True)
    per_cssl = models.FloatField(blank=True, null=True)
    per_desconto = models.FloatField(blank=True, null=True)
    vlr_lim_maximo = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    per_iss = models.FloatField(blank=True, null=True)
    ped_cliente_consumidor = models.IntegerField(blank=True, null=True)
    pde_id_forma_pag = models.IntegerField(blank=True, null=True)
    pde_id_fornecedor = models.IntegerField(blank=True, null=True)
    pde_id_ccusto = models.IntegerField(blank=True, null=True)
    pde_id_local_titulo = models.IntegerField(blank=True, null=True)
    pde_id_tipo_financeiro = models.IntegerField(blank=True, null=True)
    eff_finalidade = models.CharField(max_length=1, blank=True, null=True, db_comment='C¾digo da finalidade do arquivo: \n0 - Remessa do arquivo original; \n1 - Remessa do arquivo substituto.')
    eff_perfil = models.CharField(max_length=1, blank=True, null=True, db_comment=' Perfil de apresentaþÒo do arquivo fiscal; \nA û Perfil A; \nB û Perfil B.; \nC û Perfil C')
    eff_atividade = models.CharField(max_length=1, blank=True, null=True, db_comment='Indicador de tipo de atividade: \n0 û Industrial ou equiparado a industrial; \n1 û Outros')
    efc_layout = models.CharField(max_length=3, blank=True, null=True, db_comment='DigitaþÒo Livre')
    efc_tipo_escrituracao = models.CharField(max_length=1, blank=True, null=True, db_comment='0 Original\n1 Retificadora')
    efc_ind_reg_cum = models.CharField(max_length=1, blank=True, null=True, db_comment='1 = Regime de Caixa - escrituraþÒo consolidada.\n2 = Regime de CompetÛncia - EscrituraþÒo Consolidada.\n9 = Regime de CompetÛncia - EscrituraþÒo Detalhada')
    efc_situa_especial = models.CharField(max_length=1, blank=True, null=True, db_comment='0 Aberta\n1 CisÒo\n2 FusÒo\n3 InoperaþÒo\n4 Encerramento')
    efc_ind_nat_pj = models.CharField(max_length=2, blank=True, null=True, db_comment='00 Sociedade Empresaria em Geral\n01 Sociedade Corporativa\n02 Entidade Sujeita ao PIS/Pasep..\n')
    efc_ind_ativ = models.CharField(max_length=1, blank=True, null=True, db_comment='0 Industria\n1 Prestador de Serviþos\n2 Atividade de Comercio\n3 Atividade Financeira\n4 Atividade Imobiliaria\n9 Outros')
    efc_ind_apro_cred = models.CharField(max_length=1, blank=True, null=True, db_comment='1 MÚtodo de ApropriaþÒo Direta\n2 MÚtodo sw Retaio Proporcional')
    efc_cod_tipo_cont = models.CharField(max_length=1, blank=True, null=True, db_comment='1 Aliquota Basica\n2 Aliquota Especifica')
    efc_cod_inc_trib = models.CharField(max_length=1, blank=True, null=True)
    sef_layout = models.CharField(max_length=4, blank=True, null=True, db_comment='DigitaþÒo Livre')
    sef_cod_fin = models.CharField(max_length=1, blank=True, null=True, db_comment='Finalidade \n0 Documento original emitido em arquivo\n1 TranscriþÒo de documentos de emissÒo pr¾pria\n2 TranscriþÒo de documentos emitidos por terceiros\n3 TranscriþÒo de documentos capturados por digitalizaþÒo\n4 TranscriþÒo de documentos emitidos em equipamento especializado\n5 Livros de resultados e obrigaþ§es\n6 Livros e mapas de controle\n7 Guias de informaþ§es econ¶mico-fiscais\n8 Livros da contabilidade\n9 Extratos de documentos')
    sef_cod_ctd = models.CharField(max_length=2, blank=True, null=True, db_comment='Conteudo do Arquivo:\n20 - Lanþamentos de operaþ§es e resultados fiscais\n')
    sef_ind_ed = models.CharField(max_length=1, blank=True, null=True, db_comment='Entrada de dados:\n0- DigitaþÒo de dados\n1- ImportaþÒo de arquivo-texto\n2- AdiþÒo de documentos/arquivo-texto\n3- ExportaþÒo de arquivo-texto')
    sef_ind_arq = models.CharField(max_length=1, blank=True, null=True, db_comment='Documento contido no arquivo:\n5- Livros de resultados e obrigaþ§es')
    sef_prf_iss = models.CharField(max_length=1, blank=True, null=True, db_comment='Indicador de exigibilidade da escrituraþÒo do ISS:\n0- Sim, no modo simplificado de escrituraþÒo do imposto\n2- Sim, no modo integral de escrituraþÒo do regime normal de apuraþÒo do imposto\n9- NÒo obrigado a escriturar')
    sef_prf_icms = models.CharField(max_length=1, blank=True, null=True, db_comment='Indicador de exigibilidade da escrituraþÒo do ICMS:\n0- Sim, no modo simplificado de escrituraþÒo do imposto\n1- Sim, no modo intermedißrio de escrituraþÒo do regime normal de apuraþÒo do imposto\n2- Sim, no modo integral de escrituraþÒo do regime normal de apuraþÒo do imposto\n9- NÒo obrigado a escriturar')
    sef_prf_ridf = models.CharField(max_length=1, blank=True, null=True, db_comment='Indicador de exigibilidade do Registro de ImpressÒo de Documentos Fiscais:\n0- Sim\n1- NÒo')
    sef_prf_rudf = models.CharField(max_length=1, blank=True, null=True, db_comment='Indicador de exigibilidade do Registro de UtilizaþÒo de Documentos Fiscais:\n0- Sim\n1- NÒo')
    sef_prf_lmc = models.CharField(max_length=1, blank=True, null=True, db_comment='Indicador de exigibilidade do Livro de MovimentaþÒo de CombustÝveis:\n0- Sim\n1- NÒo')
    sef_prf_rv = models.CharField(max_length=1, blank=True, null=True, db_comment='Indicador de exigibilidade do Registro de VeÝculos:\n0- Sim\n1- NÒo')
    sef_prf_ri = models.CharField(max_length=1, blank=True, null=True, db_comment='Indicador de exigibilidade do Registro de VeÝculos:\n0- Sim\n1- NÒo')
    sef_ind_ec = models.CharField(max_length=1, blank=True, null=True, db_comment='Indicador de apresentaþÒo da escrituraþÒo contßbil:\n0- Completa registrada em arquivo digital\n1- Completa registrada em papel, microfilme, fichas avulsas, ou fichas/folhas contÝnuas\n2- Simplificada registrada em arquivo digital\n3- Simplificada registrada papel, microfilme, fichas avulsas, ou fichas/folhas contÝnuas\n4- Livro Caixa registrado em arquivo digital\n5- Livro Caixa registrado papel, microfilme, fichas avulsas, ou fichas/folhas contÝnuas\n9- NÒo obrigado a escriturar')
    sef_ind_iss = models.CharField(max_length=1, blank=True, null=True, db_comment='Indicador de operaþ§es sujeitas ao ISS:\n0- Sim\n1- NÒo')
    sef_ind_rt = models.CharField(max_length=1, blank=True, null=True, db_comment='Indicador de operaþ§es sujeitas Ó retenþÒo tributßria do ISS, na condiþÒo de contribuinte-substituÝdo:\n0- Sim\n1- NÒo')
    sef_ind_icms = models.CharField(max_length=1, blank=True, null=True, db_comment='Indicador de operaþ§es sujeitas ao ICMS:\n0- Sim\n1- NÒo')
    sef_ind_st = models.CharField(max_length=1, blank=True, null=True, db_comment='Indicador de operaþ§es sujeitas Ó substituiþÒo tributßria do ICMS, na condiþÒo de contribuinte-substituto:\n0- Sim\n1- NÒo')
    sef_ind_at = models.CharField(max_length=1, blank=True, null=True, db_comment='Indicador de operaþ§es sujeitas Ó antecipaþÒo tributßria do ICMS, nas entradas:\n0- Sim\n1- NÒo')
    sef_ind_ipi = models.CharField(max_length=1, blank=True, null=True, db_comment='Indicador de operaþ§es sujeitas ao IPI:\n0- Sim\n1- NÒo')
    sef_ind_ri = models.CharField(max_length=1, blank=True, null=True, db_comment='Indicador de apresentaþÒo avulsa do Registro de Inventßrio:\n0- Sim\n1- NÒo')
    aliq_interna_icms = models.IntegerField(blank=True, null=True)
    dta_saldo_inicial = models.DateField(blank=True, null=True)
    ano_corrente = models.IntegerField(blank=True, null=True)
    mes_corrente = models.IntegerField(blank=True, null=True)
    id_lme = models.IntegerField(blank=True, null=True)
    tipo_desconto_cmp_ped = models.IntegerField(blank=True, null=True)
    id_alm_padrao = models.IntegerField(blank=True, null=True)
    doc_layout = models.CharField(max_length=4, blank=True, null=True)
    doc_cod_fin = models.CharField(max_length=1, blank=True, null=True)
    doc_cod_ctd = models.CharField(max_length=2, blank=True, null=True)
    doc_ind_ed = models.CharField(max_length=1, blank=True, null=True)
    doc_ind_arq = models.CharField(max_length=1, blank=True, null=True)
    doc_prf_iss = models.CharField(max_length=1, blank=True, null=True)
    doc_prf_icms = models.CharField(max_length=1, blank=True, null=True)
    doc_prf_ridf = models.CharField(max_length=1, blank=True, null=True)
    doc_prf_rudf = models.CharField(max_length=1, blank=True, null=True)
    doc_prf_lmc = models.CharField(max_length=1, blank=True, null=True)
    doc_prf_rv = models.CharField(max_length=1, blank=True, null=True)
    doc_prf_ri = models.CharField(max_length=1, blank=True, null=True)
    doc_ind_ec = models.CharField(max_length=1, blank=True, null=True)
    doc_ind_iss = models.CharField(max_length=1, blank=True, null=True)
    doc_ind_rt = models.CharField(max_length=1, blank=True, null=True)
    doc_ind_icms = models.CharField(max_length=1, blank=True, null=True)
    doc_ind_st = models.CharField(max_length=1, blank=True, null=True)
    doc_ind_at = models.CharField(max_length=1, blank=True, null=True)
    doc_ind_ipi = models.CharField(max_length=1, blank=True, null=True)
    doc_ind_ri = models.CharField(max_length=1, blank=True, null=True)
    per_corr_preco_prazo = models.FloatField(blank=True, null=True)
    cte_tipo_estoque_ent = models.IntegerField(blank=True, null=True)
    cte_tipo_estoque_sai = models.IntegerField(blank=True, null=True)
    dec_forma_pag_credito = models.IntegerField(blank=True, null=True, db_comment='DEC=DEVOLUÃ├O DE CLIENTE')
    pcp_id_item_sob_medida = models.IntegerField(blank=True, null=True)
    pcp_cod_int_fte_etq = models.CharField(max_length=5, blank=True, null=True)
    ped_cliente = models.IntegerField(blank=True, null=True)
    mes_limite = models.IntegerField(blank=True, null=True)
    ped_altera_preco = models.BooleanField(blank=True, null=True)
    msg_email_cotacao = models.CharField(max_length=1, blank=True, null=True)
    avf_media_avaliacao = models.FloatField(blank=True, null=True, db_comment='campo utilizado na avaliþÒo de fornecedor do sistema de contrutora')
    per_desp_var = models.FloatField(blank=True, null=True, db_comment='Campo com influÛncia no cßlculo da rentabilidade lÝquida.')
    orv_id_tipo_mov_estoque = models.IntegerField(blank=True, null=True, db_comment='Campo sera utilizado na ordem de servicos.')
    serie_nf = models.CharField(max_length=3, blank=True, null=True, db_comment='Este campo Ú utilizado no momento de gerar nota fiscal de saÝda e de devoluþÒo')
    rcr_id_tif_deb = models.IntegerField(blank=True, null=True, db_comment='Campo utilizado no momento em que Ú feito uma Nota Fiscal de SaÝda (Venda), quando for utilizado forma de pagamento com DOC_IMPRESSO = 7 (CrÚdito);')
    rcr_id_tif_cre = models.IntegerField(blank=True, null=True, db_comment='Campo utilizado no momento em que Ú feito uma Nota Fiscal de SaÝda (Venda), quando for utilizado forma de pagamento com DOC_IMPRESSO = 7 (CrÚdito); ')
    rcr_id_plano_sef = models.CharField(max_length=11, blank=True, null=True, db_comment='Este campo Ú utilizado quando a Nota Fiscal de Venda utiliza forma de pagamento do tipo CR╔DITO. Ele serß usado no momento das geraþ§es dos registros de movimento de caixa. O plano de conta deve ser SEM FLUXO.')
    cxa_id_plano_suprim = models.CharField(max_length=11, blank=True, null=True, db_comment='Este campo serß utilizado pela rotina de Abertura/Fechamento de Caixa que Ú usado pela tela de Controle de Caixa;')
    cxa_id_tif_suprim = models.IntegerField(blank=True, null=True, db_comment='Este campo serß utilizado pela rotina de Abertura/Fechamento de Caixa que Ú usado pela tela de Controle de Caixa;')
    cxa_id_plano_sangria = models.CharField(max_length=11, blank=True, null=True, db_comment='Este campo serß utilizado pela rotina de Suprimentos / Sangria  que Ú usado pela tela de Controle de Caixa;')
    cxa_id_tif_sangria = models.IntegerField(blank=True, null=True, db_comment='Este campo serß utilizado pela rotina de Suprimentos / Sangria  que Ú usado pela tela de Controle de Caixa;')
    cxa_exp_id_tif_sangria = models.IntegerField(blank=True, null=True, db_comment='Este campo serß utilizado pela rotina de Suprimentos / Sangria  que Ú usado pela tela de Controle de Caixa;')
    cxa_exp_id_plano_sangria = models.CharField(max_length=11, blank=True, null=True, db_comment='Este campo serß utilizado pela rotina de Suprimentos / Sangria  que Ú usado pela tela de Controle de Caixa;')
    rcr_id_condicao_pag = models.IntegerField(blank=True, null=True, db_comment='Este campo serß utilizado pela DevoluþÒo de NF de Cliente.')
    rcr_id_forma_pag = models.IntegerField(blank=True, null=True, db_comment='Este campo serß utilizado pela DevoluþÒo de NF de Cliente.')
    dev_for_id_condicao_pag = models.IntegerField(blank=True, null=True, db_comment='Este campo serß utilizado pela tela de Nota Fiscal de Dev. de Fornecedor.')
    cxa_critica_chq = models.BooleanField(blank=True, null=True, db_comment='Este campo serß utilizado pela tela de Controle de Caixa na parte de Notas (FAT_UN_M_CXA_NFE);')
    fat_seq_termo = models.IntegerField(blank=True, null=True, db_comment='Campo sequÛncia utilizado pela impressÒo do Termo, pelo botÒo GerarNfe da tela de controle de caixa.')
    per_cofins_l_presumido = models.FloatField(blank=True, null=True)
    per_pis_l_presumido = models.FloatField(blank=True, null=True)
    cxa_inf_lote_car_fech = models.BooleanField(blank=True, null=True, db_comment='Caso o valor seja TRUE, no momento do fechamento do caixa o usußrio serß obrigado a informar o nro do lote de cada cartÒo.')
    conc_alt_txa_fixa_car = models.BooleanField(blank=True, null=True, db_comment='Caso seja TRUE, na tela de conciliaþÒo de cartÒo de crÚdito o sistema permitirß que o usußrio altere o valor da Taxa Fixa que vem do cartÒo (car_taxa).')
    nfe_ecf_id_condicao_pag = models.IntegerField(blank=True, null=True, db_comment='Campo utilizado no momento da GeraþÒo de uma NFE partindo de uma ECF.')
    nfe_ecf_tipo_estoque = models.IntegerField(blank=True, null=True, db_comment='Campo utilizado no momento da GeraþÒo de uma NFE partindo de uma ECF.')
    cxa_imprime_etq = models.BooleanField(blank=True, null=True, db_comment='Campo utilizado pela rotina de Controle de Caixa, no botÒo Gerar Nfe.')
    cxa_f11_pedido = models.BooleanField(blank=True, null=True, db_comment='Campo utilizado pela tela FAT_FM_M_CXA_NFE.')
    eff_motivo_inv = models.CharField(max_length=2, blank=True, null=True, db_comment='01 û No final no perÝodo;\n02 û Na mudanþa de forma de tributaþÒo da\nmercadoria (ICMS);\n03 û Na solicitaþÒo da baixa cadastral, paralisaþÒo\ntemporßria e outras situaþ§es;\n04 û Na alteraþÒo de regime de pagamento û condiþÒo\ndo contribuinte;\n05 û Por determinaþÒo dos fiscos.')
    fin_id_maquineta_pad = models.IntegerField(blank=True, null=True)
    orv_id_forma_pag_rcr = models.IntegerField(blank=True, null=True)
    fin_perm_n_maquinetas = models.BooleanField(blank=True, null=True)
    mch_id_tif_dep = models.IntegerField(blank=True, null=True, db_comment='Este campo serß utilizado pela MovimentaþÒo de cheque, no momento da operaþÒo Depositar;')
    mch_id_tif_dev = models.IntegerField(blank=True, null=True, db_comment='Este campo serß utilizado pela MovimentaþÒo de cheque, no momento da operaþÒo Devolver;')
    mch_id_tif_ppr = models.IntegerField(blank=True, null=True, db_comment='Este campo poderß ser utilizado pela MovimentaþÒo de cheque, no momento da operaþÒo Paga parcial ou Resgate, isso vai depender da forma de pagamento escolhida;')
    mch_id_plano_dep = models.CharField(max_length=11, blank=True, null=True, db_comment='Este campo serß utilizado pela MovimentaþÒo de cheque, no momento da operaþÒo Depositar;')
    mch_id_plano_dev = models.CharField(max_length=11, blank=True, null=True, db_comment='Este campo serß utilizado pela MovimentaþÒo de cheque, no momento da operaþÒo Depositar;')
    mch_id_plano_ppr = models.CharField(max_length=11, blank=True, null=True, db_comment='Este campo poderß ser utilizado pela MovimentaþÒo de cheque, no momento da operaþÒo Paga parcial ou Resgate, isso vai depender da forma de pagamento escolhida;')
    mch_id_forma_pag = models.IntegerField(blank=True, null=True, db_comment='Este campo serß utilizado pela Rotina de MovimentaþÒo de cheque, nas operaþ§es:\nDepositar, Pagar parcial e Resgatar.\nO valor deste campo serß gravado no REC_PAG.\nO doc_impresso deste campo deve ser NENHUM.\n')
    orv_id_cargo_mec = models.IntegerField(blank=True, null=True, db_comment='Este campo serß utilizado pelo m¾dulo de oficina. O c¾digo do cargo que for informado aqui, estarß informando para o sistema que todo funcionßrio que tiver cadastro neste c¾digo de cargo serß considerado MEC┬NICO.')
    orv_critica_ite_aber = models.BooleanField(blank=True, null=True, db_comment='Este campo informa para o m¾dulo de oficina que serß obrigado a inserþÒo de Itens na abertura da O.S.')
    orv_critica_ocv_aber = models.BooleanField(blank=True, null=True, db_comment='Este campo informa para o m¾dulo de oficina o seguinte procedimento: Caso o cliente tenha algum orþamento aberto para "aquele veÝculo", no momento da Abertura da O.S a importaþÒo deste orþamento passa a ser obrigat¾rio.')
    ped_envia_carga = models.BooleanField(blank=True, null=True, db_comment='Este campo serß utilizado pela m¾dulo REV.\n Caso seja TRUE, o campo "Envia para carga" no pedido de venda serß exibido.')
    nfe_per_partilha_dest = models.FloatField(blank=True, null=True)
    nfe_per_partilha_orig = models.FloatField(blank=True, null=True)
    nfe_per_icms_saida = models.FloatField(blank=True, null=True)
    sgq_ped_gera_nfs = models.BooleanField(blank=True, null=True, db_comment='Este campo serß utilizado apenas para cliente que usa o m¾dulo SGQ.  Este campo nÒo poderß ser colocado na tela de parÔmetros. ╔ de uso interno da e-north.\n')
    cbx_id_plano = models.CharField(max_length=11, blank=True, null=True, db_comment='Campo utilizado pela rotina de baixa de cart§es de crÚdito;')
    cbx_id_plano_desc_ope = models.CharField(max_length=11, blank=True, null=True, db_comment='Campo utilizado pela rotina de baixa de cart§es de crÚdito;')
    cbx_id_plano_desc_antec = models.CharField(max_length=11, blank=True, null=True, db_comment='Campo utilizado pela rotina de baixa de cart§es de crÚdito;')
    cbx_id_tipo_financeiro = models.IntegerField(blank=True, null=True, db_comment='Campo utilizado pela rotina de baixa de cart§es de crÚdito;')
    cbx_id_tipo_financeiro_desc = models.IntegerField(blank=True, null=True, db_comment='Campo utilizado pela rotina de baixa de cart§es de crÚdito;')
    rbx_ret_id_plano = models.CharField(max_length=11, blank=True, null=True, db_comment='Campo utilizado pela rotina de baixa automßtica de boleto;')
    rbx_ret_id_tipo_financeiro = models.IntegerField(blank=True, null=True, db_comment='Campo utilizado pela rotina de baixa automßtica de boleto;')
    rbx_ret_id_ccu = models.IntegerField(blank=True, null=True, db_comment='Campo utilizado pela rotina de baixa automßtica de boleto;')
    rbx_ret_id_forma_pag = models.IntegerField(blank=True, null=True, db_comment='Campo utilizado pela rotina de baixa automßtica de boleto;')
    sgq_dias_prev_cid_dentro = models.IntegerField(blank=True, null=True, db_comment='campo utilizado somente pelo m¾dulo SGQ.  Ao criar um pedido de venda novo o sistema irß mostrar a previsÒo de entraga. ex:\r\nemissÒo do pedido + a qtde deste campo. Isso, caso o cliente seja da mesma UF.')
    sgq_dias_prev_cid_fora = models.IntegerField(blank=True, null=True, db_comment='campo utilizado somente pelo m¾dulo SGQ.  Ao criar um pedido de venda novo o sistema irß mostrar a previsÒo de entraga. ex:\r\nemissÒo do pedido + a qtde deste campo. Isso, caso o cliente seja da UF diferente.')
    des_ind_ed = models.IntegerField(blank=True, null=True)
    des_cod_fin = models.IntegerField(blank=True, null=True)
    des_ind_arq = models.IntegerField(blank=True, null=True)
    des_ind_iss = models.IntegerField(blank=True, null=True)
    des_ind_ec = models.IntegerField(blank=True, null=True)
    des_ind_rt = models.IntegerField(blank=True, null=True)
    des_ind_icms = models.IntegerField(blank=True, null=True)
    des_ind_st = models.IntegerField(blank=True, null=True)
    des_ind_at = models.IntegerField(blank=True, null=True)
    des_ind_ipi = models.IntegerField(blank=True, null=True)
    des_ind_pi = models.IntegerField(blank=True, null=True)
    des_ind_gef = models.IntegerField(blank=True, null=True)
    des_prf_icms = models.IntegerField(blank=True, null=True)
    des_prf_iss = models.IntegerField(blank=True, null=True)
    des_prf_ridf = models.IntegerField(blank=True, null=True)
    des_prf_rudf = models.IntegerField(blank=True, null=True)
    des_prf_lcm = models.IntegerField(blank=True, null=True)
    des_prf_rv = models.IntegerField(blank=True, null=True)
    des_prf_ri = models.IntegerField(blank=True, null=True)
    sgq_dias_prev_uf_dentro = models.IntegerField(blank=True, null=True)
    sgq_dias_prev_uf_fora = models.IntegerField(blank=True, null=True)
    ecf_id_tipo_mov_estoque = models.IntegerField(blank=True, null=True, db_comment='Campo utilizado pela geraþÒo da NF partindo da tabela BR_CUPOM_MESTRE do GerConWin, no enServer mÚtodo FatGerNfs.')
    ecf_id_condicao_pag = models.IntegerField(blank=True, null=True, db_comment='Campo utilizado pela geraþÒo da NF partindo da tabela BR_CUPOM_MESTRE do GerConWin, no enServer mÚtodo FatGerNfs.')
    mvb_id_fornecedor = models.IntegerField(blank=True, null=True)
    ped_cupom_imp = models.IntegerField(blank=True, null=True, db_comment='1 - ImpressÒo A4\r\n2 - ImpressÒo 40 Colunas')
    rcr_id_tipo_financeiro = models.IntegerField(blank=True, null=True)
    rcr_id_plano = models.CharField(max_length=11, blank=True, null=True)
    perm_bxa_pag_n_emp = models.BooleanField(blank=True, null=True)
    rcr_cri_forma_pag = models.BooleanField(blank=True, null=True)
    fp_per_cust_ven_mens = models.FloatField(blank=True, null=True, db_comment='% do Custo Fixo sobre Venda Mensais')
    fp_per_icms_ven = models.FloatField(blank=True, null=True, db_comment='ICMS sobre Vendas')
    fp_per_simples = models.FloatField(blank=True, null=True, db_comment='Simples')
    fp_per_comissao = models.FloatField(blank=True, null=True, db_comment='Comiss§es')
    fp_per_frete_ven = models.FloatField(blank=True, null=True, db_comment='Fretes s/Vendas')
    fp_per_cust_fin_ven = models.FloatField(blank=True, null=True, db_comment='Custo Financeiro sobre Vendas')
    fp_per_prc_prz_ven_prat = models.FloatField(blank=True, null=True)
    associado_acavasf = models.BooleanField(blank=True, null=True)
    tipo_impressao = models.IntegerField(blank=True, null=True, db_comment='0 - ImpressÒo a Laser;1 - ImpressÒo Matricial')
    ped_corr_preco_prazo = models.BooleanField(blank=True, null=True, db_comment='Habilita fazer correþÒo de calculo do preco do item com base nos dias a prazo e percentual do perfil do cliente ')
    emite_duplicata_aceite = models.BooleanField(blank=True, null=True)
    ped_cli_cns_vnd_max = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    cxa_id_tipo_fin_canc_ant = models.IntegerField(blank=True, null=True, db_comment='Tipo financeiro usado no momento que Ú cancelado uma nota fiscal do dia anterior.')
    cxa_id_plano_canc_ant = models.CharField(max_length=11, blank=True, null=True, db_comment='Plano de Contas usado no momento que Ú cancelado uma nota fiscal do dia anterior.')
    prc_ite_manual = models.BooleanField(blank=True, null=True)
    sgq_opr_id_setor = models.IntegerField(blank=True, null=True, db_comment='Campo utilizado pela tela de Ordem de ProduþÒo (PCP_FM_M_OPR), para quando for necessßrio gerar a SolicitaþÒo de \r\nCompras.')
    pcp_epp_id_tipo_mov_estoque = models.IntegerField(blank=True, null=True, db_comment='Campo utilizado pela tela PCP_FM_M_EPP, para movimentaþÒo do estoque.')
    mal_tipo_estoque_ent = models.IntegerField(blank=True, null=True)
    path_remessa = models.CharField(max_length=200, blank=True, null=True)
    ativa_forma_fpg_hrq = models.BooleanField(blank=True, null=True)
    avf_peso_01 = models.FloatField(blank=True, null=True)
    avf_peso_02 = models.FloatField(blank=True, null=True)
    avf_peso_03 = models.FloatField(blank=True, null=True)
    avf_peso_04 = models.FloatField(blank=True, null=True)
    avf_peso_05 = models.FloatField(blank=True, null=True)
    avf_peso_06 = models.FloatField(blank=True, null=True)
    avf_peso_07 = models.FloatField(blank=True, null=True)
    ativa_ite_conj = models.BooleanField(blank=True, null=True)
    id_tif_deb = models.IntegerField(blank=True, null=True, db_comment='Campo utilizado no momento em que Ú feito uma Nota Fiscal de SaÝda (Venda), quando for utilizado forma de pagamento com DOC_IMPRESSO = 7 (CrÚdito);')
    id_tif_cre = models.IntegerField(blank=True, null=True, db_comment='Campo utilizado no momento em que Ú feito uma Nota Fiscal de SaÝda (Venda), quando for utilizado forma de pagamento com DOC_IMPRESSO = 7 (CrÚdito);')
    ped_utiliza_frete = models.BooleanField(blank=True, null=True)
    utiliza_mecanico = models.BooleanField(blank=True, null=True)
    calc_icm_dispensado = models.BooleanField(blank=True, null=True)
    orv_id_cfo_int_dev_gar = models.CharField(max_length=5, blank=True, null=True, db_comment='CFO utilizado no momento de Fechamento de O.S de Garantia na geraþÒo da nota fiscal de devoluþÒo.')
    orv_id_cfo_ext_dev_gar = models.CharField(max_length=5, blank=True, null=True, db_comment='CFO utilizado no momento de Fechamento de O.S de Garantia na geraþÒo da nota fiscal de devoluþÒo.')
    orv_id_tme_dev_gar = models.IntegerField(blank=True, null=True, db_comment='Tipo de movimento estoque utilizado no momento de Fechamento de O.S de Garantia na geraþÒo da nota fiscal de devoluþÒo.')
    orv_id_tme_dev_cli_gar = models.IntegerField(blank=True, null=True)
    preco_por_filial = models.BooleanField(blank=True, null=True)
    con_id_forma_pag_rec = models.IntegerField(blank=True, null=True)
    con_id_forma_pag_pag = models.IntegerField(blank=True, null=True)
    con_id_local_titulo_rec = models.IntegerField(blank=True, null=True)
    con_id_local_titulo_pag = models.IntegerField(blank=True, null=True)
    con_id_ccusto_pag = models.IntegerField(blank=True, null=True)
    perm_bxa_rec_n_emp = models.BooleanField(blank=True, null=True)
    con_id_tipo_financeiro_rec = models.IntegerField(blank=True, null=True)
    con_id_tipo_financeiro_pag = models.IntegerField(blank=True, null=True)
    ativa_preco_cat_ser = models.BooleanField(blank=True, null=True)
    mob_periodo_ult_vend = models.IntegerField(blank=True, null=True, db_comment='Este campo Ú utilizado pelo aplicativo mobile.\r\nAqui o usußrio inseri a qtde de meses ·ltimo que o cliente comprou. exe:  6 ->   6 ultimos meses de venda.')
    dct_id_tipo_financeiro_cred = models.IntegerField(blank=True, null=True)
    dct_id_tipo_financeiro_desc_taxa = models.IntegerField(blank=True, null=True)
    dct_id_tipo_financeiro_canc = models.IntegerField(blank=True, null=True)
    dct_id_plano_cred = models.CharField(max_length=11, blank=True, null=True)
    dct_id_plano_desc_taxa = models.CharField(max_length=11, blank=True, null=True)
    dct_id_forma_pag = models.IntegerField(blank=True, null=True)
    dct_id_plano_canc = models.CharField(max_length=11, blank=True, null=True)
    ped_id_forma_pag_rcr = models.IntegerField(blank=True, null=True)
    eff_layout = models.IntegerField(blank=True, null=True)
    mob_id_tipo_mov_estoque = models.IntegerField(blank=True, null=True, db_comment='Campo utilizado pelo sistema mobile para poder fazer os pedidos de venda. Este campo s¾ pode aceitar tipo de estoque do tipo venda.')
    perm_bxa_rec_n_tit = models.BooleanField(blank=True, null=True)
    substituir_os = models.BooleanField(blank=True, null=True)
    orv_gera_fin_separado = models.BooleanField(blank=True, null=True, db_comment='Campo utilizado no momento de fechar a O.S. Mesmo que o usußrio escolha notas separada, ele poderß serpara o financeiro ou nÒo.')
    per_desc_especial = models.FloatField(blank=True, null=True, db_comment='Campo utilizado pelo pedido de venda.')
    informar_caixa_nfe = models.BooleanField(blank=True, null=True)
    nfe_id_tipo_financeiro = models.IntegerField(blank=True, null=True)
    hab_vlr_custo_cte = models.BooleanField(blank=True, null=True)
    sgq_tipo_comissao = models.IntegerField(blank=True, null=True, db_comment='0 - Nenhum;1 - Por Pedido de Venda')
    sgq_per_comissao_max = models.FloatField(blank=True, null=True)
    pbx_gravar_obs_tit = models.BooleanField(blank=True, null=True)
    rbx_gravar_obs_tit = models.BooleanField(blank=True, null=True)
    nfce_permite_cheque = models.BooleanField(blank=True, null=True)
    perm_bxa_pag_n_tit = models.BooleanField(blank=True, null=True)
    dta_pag_ret_banco = models.IntegerField(blank=True, null=True, db_comment='0 - Data da Ocorrencia; 1 - Data de CrÚdito')
    frete_fob_total_ped = models.BooleanField(blank=True, null=True)
    sgq_calc_sld_produzir_opr = models.BooleanField(blank=True, null=True, db_comment='Caso seja FALSE, a OPR irß considerar que o saldo a produzir do produto seja a mesma qtde que vem do pedido de venda.')
    calcular_iss_retido = models.BooleanField(blank=True, null=True)
    permitir_alterar_vend_ped = models.BooleanField(blank=True, null=True)
    mob_busca_sld_est = models.BooleanField(blank=True, null=True)
    mob_tipo_preco_cli = models.IntegerField(blank=True, null=True, db_comment='0 - Cßlculo usando a tabela CAD_TB_C_ITE_PC\r\n1 - Cßlculo usando Perfil de Cliente, PermissÒo de CorreþÒo por Perfil  + PermissÒo de correþÒo por FamÝlia')
    mob_tipo_ordem = models.IntegerField(blank=True, null=True)
    preco_por_perfil = models.BooleanField(blank=True, null=True)
    hab_icms_desn_saida = models.BooleanField(blank=True, null=True)
    correcao_prc_por_grupo = models.BooleanField(blank=True, null=True)
    chave_bloqueio = models.CharField(max_length=100, blank=True, null=True)
    status_internet = models.BooleanField(blank=True, null=True)
    id_fun_aviso_debito = models.IntegerField(blank=True, null=True)
    horario_aviso_debito = models.TimeField(blank=True, null=True)
    data_aviso_debito = models.DateField(blank=True, null=True)
    limite_cred_fpg = models.BooleanField(blank=True, null=True)
    filtro_pad_csu_ite = models.IntegerField(blank=True, null=True, db_comment='Servirß para a tela de consulta de itens\n0-C¾digo\n1-DescriþÒo\n2-Cod.Barra\n3-Cod.Fabrica\n4-Loca-Rua\n5-AplicaþÒo\n6-Nome do Fornecedor\n7-Cod.Grupo\n8-DescriþÒo do Grupo\n9-ReferÛncia\n10-NCM\n')
    filtro_pad_psq_ite = models.IntegerField(blank=True, null=True, db_comment='Servirß para tela de pesquisa de itens\n0-C¾digo\n1-DescriþÒo do item\n2-Cod.Barra\n3-Cod.Fabrica\n4-Loca-Rua\n5-AplicaþÒo\n6-Nome do Fornecedor\n7-Cod.Grupo\n8-DescriþÒo do Grupo\n9-ReferÛncia\n10-NCM')
    permitir_saida_est_emp = models.BooleanField(blank=True, null=True)
    tipo_controle_lote = models.IntegerField(blank=True, null=True, db_comment='0 - Por item; 1 - Por grupo')
    cad_cli_simplificado = models.BooleanField(blank=True, null=True)
    cad_vei_simplificado = models.BooleanField(blank=True, null=True)
    enviar_rel_grv = models.BooleanField(blank=True, null=True)
    informar_mec_ped_vnd = models.BooleanField(blank=True, null=True)
    exibir_cond_sem_pag = models.BooleanField(blank=True, null=True)
    ped_utiliza_mecanico = models.BooleanField(blank=True, null=True)
    exibir_obs_ped_nfe_fisco = models.BooleanField(blank=True, null=True)
    permitir_nova_os_cli_placa = models.BooleanField(blank=True, null=True)
    obrig_dados_cheque_ped_vnd = models.BooleanField(blank=True, null=True)
    ped_vnd_tme_padrao = models.IntegerField(blank=True, null=True)
    ativo_ped_vnd_tme_padrao = models.BooleanField(blank=True, null=True)
    gerar_nota_fechamento_os = models.BooleanField(blank=True, null=True)
    alterar_vlr_dup_nota_fat = models.BooleanField(blank=True, null=True)
    n_utilizar_cond_pag_os = models.BooleanField(blank=True, null=True)
    tipo_preco_sem_cond_pag_os = models.IntegerField(blank=True, null=True)
    permitir_alterar_dta_baixa_rbx = models.BooleanField(blank=True, null=True)
    ativar_util_fpg_ped_vnd = models.BooleanField(blank=True, null=True)
    letras_maius_obs_ped = models.BooleanField(blank=True, null=True)
    utilizar_ped_bonificacao = models.BooleanField(blank=True, null=True)
    ped_vnd_bonificacao = models.BooleanField(blank=True, null=True)
    informar_mec_por_item_ped = models.BooleanField(blank=True, null=True)
    informar_mec_por_item_os = models.BooleanField(blank=True, null=True)
    csu_cli_fin_separar_fpg = models.BooleanField(blank=True, null=True)
    sgq_verif_op_ped = models.BooleanField(blank=True, null=True, db_comment='Campo responsßvel de verificar a checagem de nro da O.P no momento de informar o pedido de venda na Ordem de Faturamento.')
    sgq_preenc_vlr_pago_bx_tit = models.BooleanField(blank=True, null=True, db_comment='Se estiver TRUE o sistema irß fazer com que no momento de selcionar o tÝtulo para baixar , o sistema irß preencher o valor pago jß com o valor do tÝtulo.')
    sgq_id_almoxarifado_pad_epp = models.IntegerField(blank=True, null=True, db_comment='C¾digo de almoxarifado padrÒo utilizado para Entrada de Produto acabado.')
    pcp_cpa_id_tipo_mov_estoque = models.IntegerField(blank=True, null=True, db_comment='Campo utilizado pela tela de contagem por entrada de produto acabado')
    pcp_atualiza_fin_base_prod = models.BooleanField(blank=True, null=True, db_comment='Se for TRUE, a tela de GeraþÒo de Nota Fiscal (FIN_FM_M_CXA_NFE), irß pedir o(s) c¾digo(s) do(s) pedido(s) da base da produþÒo que se refere a nota fiscal que serß gerada.')
    pcp_id_empresa_base_prod = models.IntegerField(blank=True, null=True, db_comment='se o campo "pcp_atualiza_fin_base_prod" = true, este campo serß obrigat¾rio o preenchimento.')
    pcp_id_empresa_base_fat = models.IntegerField(blank=True, null=True, db_comment='se o campo "pcp_atualiza_fin_base_prod" = true, este campo serß obrigat¾rio o preenchimento.')
    pcp_rom_ano_corrente = models.IntegerField(blank=True, null=True)
    pcp_atualiza_dta_pedido = models.BooleanField(blank=True, null=True, db_comment='Caso este campo seja TRUE, no momento de gerar as parcelas no pedido de venda, o sistema irß atualizar a data do pedido para a data do dia.')
    pcp_opb_id_tipo_mov_estoque = models.IntegerField(blank=True, null=True, db_comment='Tipo de estoque de saÝda utilizado pela tela de Ordem de ProduþÒo pra gerar as O.Ps de Bloco de Espuma')
    sgq_nome_etq_maquete = models.CharField(max_length=100, blank=True, null=True)
    sgq_fat_orc_id_condicao_pag = models.IntegerField(blank=True, null=True, db_comment='CondiþÒo de pagamento padrÒo para orþamento usado pelo SGQ=TRUE')
    sgq_fat_ped_id_condicao_pag = models.IntegerField(blank=True, null=True, db_comment='CondiþÒo de pagamento padrÒo para pedido de venda usado pelo SGQ=TRUE')
    fat_validade_orc = models.IntegerField(blank=True, null=True, db_comment='Qtde de dias de validade para um orþamento')
    fat_id_tipo_mov_estoque_rep = models.IntegerField(blank=True, null=True, db_comment='Tipo de movimento de estoque para pedido de venda com vendedor externo')

    class Meta:
        managed = False
        db_table = 'cad_tb_c_par_ctr'
        db_table_comment = '-Tabela de Controle dos parametros\r\n\r\nEFF - EFD Fiscal\r\nEFC - EFD Contribuiþ§es'


class CadTbCParEml(models.Model):
    id_empresa = models.OneToOneField(CadTbCPar, models.DO_NOTHING, db_column='id_empresa', primary_key=True)  # The composite primary key (id_empresa, email) found, that is not supported. The first column is selected.
    email = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_par_eml'
        unique_together = (('id_empresa', 'email'),)


class CadTbCParMod(models.Model):
    id_empresa = models.OneToOneField(CadTbCPar, models.DO_NOTHING, db_column='id_empresa', primary_key=True)
    cad = models.BooleanField(db_comment='Cadastros')
    tab = models.BooleanField(blank=True, null=True)
    csu = models.BooleanField(blank=True, null=True)
    cmp = models.BooleanField(db_comment='Compras')
    est = models.BooleanField(db_comment='Estoque')
    fat = models.BooleanField(blank=True, null=True)
    ome = models.BooleanField(db_comment='Oficina Mecanica')
    ota = models.BooleanField(db_comment='Oficina Tratores')
    sgq = models.BooleanField(db_comment='Sistema GestÒo de Qualidade')
    seg = models.BooleanField(blank=True, null=True)
    chave = models.CharField(max_length=100, blank=True, null=True)
    fin = models.BooleanField(blank=True, null=True, db_comment='Financeiro')
    ctc = models.BooleanField(blank=True, null=True)
    rev = models.BooleanField(blank=True, null=True, db_comment='Revenda')
    snf = models.BooleanField(blank=True, null=True)
    car = models.BooleanField(blank=True, null=True)
    oqp = models.BooleanField(blank=True, null=True)
    adf = models.BooleanField(blank=True, null=True)
    tor = models.BooleanField(blank=True, null=True)
    omp = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_par_mod'
        db_table_comment = 'Modulos do Sistema'


class CadTbCParNfe(models.Model):
    id_empresa = models.OneToOneField(CadTbCPar, models.DO_NOTHING, db_column='id_empresa', primary_key=True)
    cert_serie = models.CharField(max_length=400, blank=True, null=True)
    danf_tipo_impressao = models.IntegerField(blank=True, null=True, db_comment='0-SemGeracao\n1-Retrato\n2-Paisagem\n3-Simplificado\n4-NFCe\n5-MsgEletronica\n')
    danf_tipo_emissao = models.IntegerField(blank=True, null=True, db_comment='0-Normal, \n1-Contingencia, \n2-SCAN, \n3-DPEC, \n4-FSDA, \n5-SVCAN, \n6-SVCRS, \n7-VCSP, \n8-OffLine\n')
    ws_estado = models.CharField(max_length=2, blank=True, null=True)
    ws_visualiza_msg = models.CharField(max_length=1, blank=True, null=True)
    situacao_emissor = models.IntegerField(blank=True, null=True, db_comment='1-ProduþÒo\n; 2-HomologaþÒo\n')
    proxy_host = models.CharField(max_length=30, blank=True, null=True)
    proxy_porta = models.IntegerField(blank=True, null=True)
    proxy_usuario = models.CharField(max_length=30, blank=True, null=True)
    proxy_senha = models.CharField(max_length=30, blank=True, null=True)
    email_smtp = models.CharField(max_length=100, blank=True, null=True)
    email_smtp_porta = models.IntegerField(blank=True, null=True)
    email_smtp_seguro = models.CharField(max_length=1, blank=True, null=True)
    email_usuario = models.CharField(max_length=30, blank=True, null=True)
    email_senha = models.CharField(max_length=30, blank=True, null=True)
    email_assunto = models.CharField(max_length=150, blank=True, null=True)
    email_msg = models.CharField(max_length=800, blank=True, null=True)
    contigencia_just = models.CharField(max_length=50, blank=True, null=True)
    contigencia_data = models.DateField(blank=True, null=True)
    path_xml = models.CharField(max_length=200, blank=True, null=True)
    path_logo = models.CharField(max_length=200, blank=True, null=True)
    cert_senha = models.CharField(max_length=30, blank=True, null=True)
    path_status = models.CharField(max_length=200, blank=True, null=True)
    path_carta = models.CharField(max_length=200, blank=True, null=True)
    path_pdf = models.CharField(max_length=200, blank=True, null=True)
    nfe_seq_devolucao = models.BooleanField(blank=True, null=True, db_comment='Este campo serve para informar se a empresa trabalha com outro n·mero de sequÛncia para Notas Fiscais de DevoluþÒo.')
    mdfe_tipo_emissao = models.IntegerField(blank=True, null=True, db_comment='0-normal\n1- contiguecia')
    mdfe_tipo_emitente = models.IntegerField(blank=True, null=True, db_comment='1 - Prestador de serviþo de transporte\n2 - transportador de carga propria')
    nfc_id_token = models.CharField(max_length=8, blank=True, null=True, db_comment='O c¾digo de identificaþÒo (cIdToken) do CSC serß um sequencial numÚrico crescente por empresa (CNPJ base 8 dÝgitos) no Estado.')
    nfc_csc = models.CharField(max_length=36, blank=True, null=True, db_comment='O CSC corresponderß a um conjunto de, no mßximo, 36 caracteres alfanumÚricos, sendo que cada CSC possui associado um c¾digo seq³encial de identificaþÒo (cIdToken) de 6 dÝgitos para facilitar a identificaþÒo do respectivo CSC e validaþÒo do QR Code pelo Fisco quando da realizaþÒo da consulta pelo consumidor.\n')
    email_smtp_ssl = models.BooleanField(blank=True, null=True)
    email_smtp_tls = models.BooleanField(blank=True, null=True)
    cod_lot_rps = models.IntegerField(blank=True, null=True)
    reg_esp_tri = models.IntegerField(blank=True, null=True, db_comment='0 - Nenhum\n1 - MicroempresaMunicipal\n2 - Estimativa\n3 - SociedadeProfissionais\n4 - Cooperativa\n5 - MicroempresarioIndividual\n6 - MicroempresarioEmpresaPP\n7 - LucroReal\n8 - LucroPresumido\n9 - SimplesNacional')
    cod_tri_mcp = models.CharField(max_length=20, blank=True, null=True)
    cod_ite_ser = models.CharField(max_length=5, blank=True, null=True)
    path_xml_outros = models.CharField(max_length=200, blank=True, null=True)
    nfe_permite_salv_xml = models.BooleanField(blank=True, null=True)
    rps_nat_opr = models.CharField(max_length=3, blank=True, null=True)
    rps_prefeitura = models.CharField(max_length=100, blank=True, null=True)
    rps_cod_cnae = models.CharField(max_length=7, blank=True, null=True)
    nfe_separar_xml_mes = models.BooleanField(blank=True, null=True)
    inf_nat_ope_nfe_comp = models.CharField(max_length=100, blank=True, null=True)
    ativar_nat_ope_nfe_comp = models.BooleanField(blank=True, null=True)
    path_logo_prefeitura = models.CharField(max_length=200, blank=True, null=True)
    danfe_cod_item = models.IntegerField(blank=True, null=True, db_comment='0 - Cod. Item; 1 - Cod. Fabrica')
    prot_com_ssllib = models.IntegerField(blank=True, null=True, db_comment='0 - libNone\r\n1 - libOpenSSL\r\n2 - libCapicom\r\n3 - libCapicomDelphiSoap\r\n4 - libWinCrypt\r\n5 - libCustom')
    prot_com_criptlib = models.IntegerField(blank=True, null=True, db_comment='0 - cryNone\r\n1 - cryOpenSSL\r\n2 - cryCapicom\r\n3 - cryWinCrypt')
    prot_com_httplib = models.IntegerField(blank=True, null=True, db_comment='0 - httpNone\r\n1 - httpWinNet\r\n2 - httpWinHttp\r\n3 - httpOpenSSL\r\n4 - httpIndy')
    prot_com_xmlsignlib = models.IntegerField(blank=True, null=True, db_comment='0 - xsNone\r\n1 - xsXmlSec\r\n1 - xsMsXml\r\n2 - xsMsXmlCapicom\r\n3 - xsLibXml2')
    nfe_versao = models.IntegerField(blank=True, null=True, db_comment='0- ve200\r\n1 - ve300\r\n2 - ve310\r\n3 - ve400')
    cert_caminho_pfx = models.CharField(max_length=255, blank=True, null=True)
    cert_senha_pfx = models.CharField(max_length=30, blank=True, null=True)
    nfc_nome_arq_rel = models.CharField(max_length=30, blank=True, null=True, db_comment='Nome do arquivo fast report (*.fr3) para emissÒo da NFCe')

    class Meta:
        managed = False
        db_table = 'cad_tb_c_par_nfe'
        db_table_comment = 'Parametros de Nota Fiscal Eletronica'


class CadTbCParRst(models.Model):
    id_empresa = models.OneToOneField(CadTbCPar, models.DO_NOTHING, db_column='id_empresa', primary_key=True)  # The composite primary key (id_empresa, letra_restricao) found, that is not supported. The first column is selected.
    letra_restricao = models.CharField(max_length=2)
    tipo_restricao = models.IntegerField(blank=True, null=True, db_comment='0 - Nenhum\r\n1 - Bloqueia\r\n2 - Envia para liberaþÒo')
    descricao = models.CharField(max_length=100, blank=True, null=True, db_comment='DescriþÒo da restriþÒo.')

    class Meta:
        managed = False
        db_table = 'cad_tb_c_par_rst'
        unique_together = (('id_empresa', 'letra_restricao'),)
        db_table_comment = 'Tabela de Tipos de RestriþÒo para Vendas'


class CadTbCParSer(models.Model):
    id_empresa = models.OneToOneField(CadTbCPar, models.DO_NOTHING, db_column='id_empresa', primary_key=True)  # The composite primary key (id_empresa, nfe_serie) found, that is not supported. The first column is selected.
    nfe_serie = models.CharField(max_length=1, db_comment='N - Normal ; D - DevoluþÒo')
    nfe_numero = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cad_tb_c_par_ser'
        unique_together = (('id_empresa', 'nfe_serie'),)
        db_table_comment = 'Tabela de Serie de Nota Fiscal'


class CadTbCPcc(models.Model):
    cod_nat_cc = models.CharField(max_length=2, blank=True, null=True)
    ind_cta = models.CharField(max_length=1, blank=True, null=True)
    cod_cta = models.CharField(primary_key=True, max_length=20)
    nome_cta = models.CharField(max_length=60, blank=True, null=True)
    cod_cta_ref = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_pcc'


class CadTbCPct(models.Model):
    id_plano = models.CharField(primary_key=True, max_length=11)
    descricao = models.CharField(max_length=50)
    tipo = models.IntegerField(db_comment='0 - Analitico,\n1 - Sintetico')
    tipo_mov = models.IntegerField(db_comment='0 - Fixa,\n1 - Variavel')
    tipo_desp = models.IntegerField(db_comment='0 - Despesas,\r\n1 - Receitas,\r\n2 - SemFluxo,\r\n3 - Tributos,\r\n4 - Resultado, 5 - Investimento ')
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    estr_dre = models.IntegerField(blank=True, null=True, db_comment='0 - Imposto e Custo sobre Vendas\r\n1 - Despesas Operacionais\r\n2 - Receitas NÒo Operacionais\r\n3 - Provis§es para o Imposto\r\n4 - Nenhum')
    cod_contabil = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_pct'
        db_table_comment = 'Cadastro de Plano de Contas.'


class CadTbCPec(models.Model):
    id_perfil_cli = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=50)
    per_correcao = models.FloatField(blank=True, null=True)
    operacao = models.IntegerField(blank=True, null=True)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    per_correcao_aprazo = models.FloatField(blank=True, null=True)
    per_correcao_financeiro = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_pec'
        db_table_comment = 'Cadastro de Perfil de Cliente'


class CadTbCPecEmp(models.Model):
    id_perfil_cli = models.OneToOneField(CadTbCPec, models.DO_NOTHING, db_column='id_perfil_cli', primary_key=True)  # The composite primary key (id_perfil_cli, id_empresa) found, that is not supported. The first column is selected.
    id_empresa = models.ForeignKey(CadTbCPar, models.DO_NOTHING, db_column='id_empresa')
    per_correcao = models.FloatField(blank=True, null=True)
    per_correcao_aprazo = models.FloatField(blank=True, null=True)
    per_correcao_financeiro = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_pec_emp'
        unique_together = (('id_perfil_cli', 'id_empresa'),)


class CadTbCPes(models.Model):
    id_perfil_seg = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=30)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_pes'
        db_table_comment = 'Cadastro de Perfil de Seguranþa.'


class CadTbCPesMod(models.Model):
    id_perfil_seg = models.OneToOneField(CadTbCPes, models.DO_NOTHING, db_column='id_perfil_seg', primary_key=True)  # The composite primary key (id_perfil_seg, formulario) found, that is not supported. The first column is selected.
    formulario = models.CharField(max_length=100)
    ativo = models.BooleanField()
    chave = models.CharField(max_length=200, blank=True, null=True)
    descricao = models.CharField(max_length=100)
    menu = models.CharField(max_length=100, blank=True, null=True)
    modulo = models.CharField(max_length=3, blank=True, null=True)
    modulo_desc = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_pes_mod'
        unique_together = (('id_perfil_seg', 'formulario'),)
        db_table_comment = 'Cadastro de Perfil de Seguranþa - Formulario'


class CadTbCPrg(models.Model):
    id_prg = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=100)
    nome_programa = models.CharField(max_length=30, blank=True, null=True)
    tipo = models.IntegerField(blank=True, null=True, db_comment='   0 - Formulßrio\n   1 - Relatorios')
    menu_ordem = models.IntegerField(blank=True, null=True)
    modulo = models.IntegerField(blank=True, null=True)
    menu_path = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_prg'
        db_table_comment = 'Cadastro de Programas do enSoft'


class CadTbCRam(models.Model):
    id_ramo = models.IntegerField(primary_key=True)
    id_cnae = models.ForeignKey(CadTbCCne, models.DO_NOTHING, db_column='id_cnae')
    descricao = models.CharField(max_length=50)
    regime_tributario = models.IntegerField(db_comment='0 - SimplesNacional,\n1 - LucroPresumido,\n2 - LucroReal')
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_ram'
        db_table_comment = 'Tabela de Ramo de Atividade'


class CadTbCRvd(models.Model):
    id_rvd = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_rvd'
        db_table_comment = 'Cadastro de Revendas.'


class CadTbCSeq(models.Model):
    id_tabela = models.CharField(primary_key=True, max_length=30)
    sequencia = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cad_tb_c_seq'
        db_table_comment = 'Tabela de Sequencia de Cadastros'


class CadTbCSet(models.Model):
    id_setor = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=50)
    lote_controla = models.BooleanField(blank=True, null=True)
    tipo = models.IntegerField(blank=True, null=True, db_comment='0 - LaminaþÒo\r\n;1 - Bordadeira;2 - Colagem\r\n;3 - Costura;4 - Alfinetagem\r\n;5 - EspumaþÒo;6 - RevisÒo;7 - Outros\r\n8 - Colchoaria')
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_set'
        db_table_comment = 'Cadastro de Setores'


class CadTbCSetTds(models.Model):
    id_setor = models.OneToOneField(CadTbCSet, models.DO_NOTHING, db_column='id_setor', primary_key=True)  # The composite primary key (id_setor, id_tdf) found, that is not supported. The first column is selected.
    id_tdf = models.ForeignKey('CadTbCTdf', models.DO_NOTHING, db_column='id_tdf')

    class Meta:
        managed = False
        db_table = 'cad_tb_c_set_tds'
        unique_together = (('id_setor', 'id_tdf'),)
        db_table_comment = 'Tabela de Tipo de defito por setor '


class CadTbCTam(models.Model):
    id_tamanho = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=40, blank=True, null=True)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_tam'
        db_table_comment = 'Cadastro de Tamanhos'


class CadTbCTdf(models.Model):
    id_tdf = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=50, blank=True, null=True)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_tdf'
        db_table_comment = 'Cadastro de Tipo de Defeito.'


class CadTbCTif(models.Model):
    id_tipo_financeiro = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=30)
    natureza = models.IntegerField(db_comment='0 - Debito\n1 - CrÚdito')
    sigla = models.CharField(max_length=10)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    gera_pag = models.BooleanField(blank=True, null=True)
    cri_exporta = models.BooleanField(blank=True, null=True, db_comment='Ativa exportaþÒo no movimento de caixa/banco.')
    prestacao_conta = models.BooleanField(blank=True, null=True)
    gera_deb_cre = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_tif'
        db_table_comment = 'Cadastro de Tipo Financeiro'


class CadTbCTme(models.Model):
    id_tipo_mov_estoque = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=30)
    tipo_movimento = models.IntegerField(db_comment='0 - Entrada,\n1 - Saida')
    ativo = models.BooleanField()
    esto_critica = models.BooleanField()
    esto_movimenta = models.BooleanField()
    cfo_interno_pf = models.ForeignKey(CadTbCCfo, models.DO_NOTHING, db_column='cfo_interno_pf')
    cfo_interno_pj = models.ForeignKey(CadTbCCfo, models.DO_NOTHING, db_column='cfo_interno_pj', related_name='cadtbctme_cfo_interno_pj_set')
    cfo_externo_pf = models.ForeignKey(CadTbCCfo, models.DO_NOTHING, db_column='cfo_externo_pf', related_name='cadtbctme_cfo_externo_pf_set')
    cfo_externo_pj = models.ForeignKey(CadTbCCfo, models.DO_NOTHING, db_column='cfo_externo_pj', related_name='cadtbctme_cfo_externo_pj_set')
    indicador = models.IntegerField(db_comment='0 - Normal,\n1 - DevoluþÒo,\n2 - Tranferencia')
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    cfo_servico_dentro = models.CharField(max_length=5, blank=True, null=True)
    cfo_servico_fora = models.CharField(max_length=5, blank=True, null=True)
    cfo_interno_icm_s_pf = models.CharField(max_length=5, blank=True, null=True)
    cfo_interno_icm_s_pj = models.CharField(max_length=5, blank=True, null=True)
    cfo_externo_icm_s_pf = models.CharField(max_length=5, blank=True, null=True)
    cfo_externo_icm_s_pj = models.CharField(max_length=5, blank=True, null=True)
    cfo_exterior_pf = models.CharField(max_length=5, blank=True, null=True)
    cfo_exterior_pj = models.CharField(max_length=5, blank=True, null=True)
    bonificacao = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_tme'
        db_table_comment = 'Cadastro de Tipo de Estoque.'


class CadTbCTri(models.Model):
    id_tributo = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=40)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_tri'
        db_table_comment = 'Cadastro de TributaþÒo'


class CadTbCTriReg(models.Model):
    id_tributo = models.OneToOneField(CadTbCTri, models.DO_NOTHING, db_column='id_tributo', primary_key=True)  # The composite primary key (id_tributo, id_tipo_mov_estoque, uf, id_empresa) found, that is not supported. The first column is selected.
    id_tipo_mov_estoque = models.ForeignKey(CadTbCTme, models.DO_NOTHING, db_column='id_tipo_mov_estoque')
    uf = models.CharField(max_length=2)
    cnt_id_st_icm = models.CharField(max_length=3, blank=True, null=True)
    cnt_reducao = models.FloatField()
    cnt_aliquota = models.FloatField()
    nct_id_st_icm = models.CharField(max_length=3, blank=True, null=True)
    nct_reducao = models.FloatField()
    nct_aliquota = models.FloatField()
    id_inf = models.ForeignKey(CadTbCInf, models.DO_NOTHING, db_column='id_inf')
    id_empresa = models.IntegerField()
    cnt_csosn = models.CharField(max_length=3, blank=True, null=True)
    nct_csosn = models.CharField(max_length=3, blank=True, null=True)
    nct_aliquota_ecf = models.CharField(max_length=20, blank=True, null=True, db_comment='Valores possiveis deste campo:\r\nFF, II, NN,  valor inteiro ou decimal.')
    part_per_aliq_dest = models.FloatField(blank=True, null=True)
    part_per_ope_int_isen = models.BooleanField(blank=True, null=True)
    part_per_ope_ext_isen = models.BooleanField(blank=True, null=True)
    part_per_red_dest = models.FloatField(blank=True, null=True)
    dis_aliquota = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_tri_reg'
        unique_together = (('id_tributo', 'id_tipo_mov_estoque', 'uf', 'id_empresa'),)


class CadTbCUnd(models.Model):
    id_unidade = models.CharField(primary_key=True, max_length=3)
    descricao = models.CharField(max_length=30)
    num_decimais = models.IntegerField(blank=True, null=True)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    inf_tempo_ite_coj = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_und'
        db_table_comment = 'Cadastro deUnidade de Medida'


class CadTbCVei(models.Model):
    id_veiculo = models.IntegerField(primary_key=True)
    id_placa = models.CharField(max_length=8, blank=True, null=True)
    descricao = models.CharField(max_length=50, blank=True, null=True)
    id_mve = models.ForeignKey(CadTbCMve, models.DO_NOTHING, db_column='id_mve')
    km_aquisicao = models.FloatField(blank=True, null=True)
    dta_aquisicao = models.DateField(blank=True, null=True)
    km_atual = models.FloatField(blank=True, null=True)
    chassi = models.CharField(max_length=20, blank=True, null=True)
    ano_modelo = models.CharField(max_length=4, blank=True, null=True)
    ano_fabricacao = models.CharField(max_length=4, blank=True, null=True)
    renavam = models.CharField(max_length=20, blank=True, null=True)
    alimentacao = models.IntegerField(blank=True, null=True, db_comment='0-InjeþÒo Eletr¶nica\n1-Carburador\n2-Bomba Injetora')
    combustivel = models.IntegerField(blank=True, null=True, db_comment='0-Gasolina\n1-Alcool\n2-Diesel\n3-Gas Natural\n4-Eletrico\n5-Flex')
    serie = models.CharField(max_length=11, blank=True, null=True)
    motor = models.CharField(max_length=11, blank=True, null=True)
    motor_num = models.CharField(max_length=20, blank=True, null=True)
    rastreado = models.BooleanField()
    tipo = models.IntegerField(db_comment='0-Veiculo\n1-Trator/Implemento')
    status = models.IntegerField(blank=True, null=True)
    id_cor = models.ForeignKey(CadTbCCor, models.DO_NOTHING, db_column='id_cor', blank=True, null=True)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    media_consumo = models.FloatField(blank=True, null=True)
    eqp_terceiro = models.BooleanField(blank=True, null=True)
    tipo_rodado = models.SmallIntegerField(blank=True, null=True, db_comment='0-NÒo Aplicavel, \n1-Truck, \n2-Toco, \n3-Cavalo Mecanico, \n4-VAN, \n5-Utilitario, \n6-Outros')
    tipo_carroceria = models.SmallIntegerField(blank=True, null=True, db_comment='0-NaoAplicavel, \n1-Aberta, \n2-Fechada, \n3-Graneleira, \n4-PortaContainer, \n5-Sider')
    cap_veiculo = models.FloatField(blank=True, null=True, db_comment='Capacidade do veiculo')
    tara = models.FloatField(blank=True, null=True)
    uf_licenciado = models.CharField(max_length=2, blank=True, null=True, db_comment='UF em que veÝculo estß licenciado.')
    id_cliente = models.IntegerField(blank=True, null=True)
    cubagem_carga = models.FloatField(blank=True, null=True)
    placa_reboque = models.CharField(max_length=8, blank=True, null=True, db_comment='Este campo serß preenchido quando o campo TIPO_RODADO for igual a CAVALO MEC┬NICO.')
    tara_reboque = models.FloatField(blank=True, null=True)
    cap_reboque = models.FloatField(blank=True, null=True)
    cubagem_reboque = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_vei'
        db_table_comment = 'Cadastro de Veiculos'


class CadTbCVit(models.Model):
    id_visita = models.IntegerField(primary_key=True)
    id_vendedor = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_vendedor', blank=True, null=True)
    doc_cnpj_cpf = models.CharField(max_length=14, blank=True, null=True)
    id_veiculo = models.IntegerField(blank=True, null=True)
    dta_visita = models.DateField(blank=True, null=True)
    obs = models.CharField(max_length=500, blank=True, null=True)
    recomendacoes = models.CharField(max_length=500, blank=True, null=True)
    id_empresa = models.IntegerField(blank=True, null=True)
    gps_latitude = models.FloatField(blank=True, null=True)
    gps_longitude = models.FloatField(blank=True, null=True)
    hor_ini = models.TimeField(blank=True, null=True)
    hor_fim = models.TimeField(blank=True, null=True)
    semana = models.IntegerField(blank=True, null=True)
    placa = models.CharField(max_length=8, blank=True, null=True)
    id_pedido_mobile = models.IntegerField(blank=True, null=True)
    tipo_mobile = models.IntegerField(blank=True, null=True, db_comment='0 - Visita normal (carro pr¾prio)\n1 - Intervalo\n2 - FinalizaþÒo do Dia\n3 - Visita acompanhada.\n')
    remarcar_vis = models.BooleanField(blank=True, null=True)
    dta_prox_vis = models.DateField(blank=True, null=True)
    semana_prox_vis = models.IntegerField(blank=True, null=True)
    id_cliente = models.IntegerField(blank=True, null=True)
    semana_visitada = models.IntegerField(blank=True, null=True, db_comment='Corresponde a semana real que o vendedor visitou o cliente.')

    class Meta:
        managed = False
        db_table = 'cad_tb_c_vit'


class CadTbCVitFot(models.Model):
    id_visita = models.OneToOneField(CadTbCVit, models.DO_NOTHING, db_column='id_visita', primary_key=True)  # The composite primary key (id_visita, id_vit_fot) found, that is not supported. The first column is selected.
    id_vit_fot = models.IntegerField()
    caminho_foto = models.CharField(max_length=255, blank=True, null=True)
    obs = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_vit_fot'
        unique_together = (('id_visita', 'id_vit_fot'),)


class CadTbCVitKmt(models.Model):
    id_visita = models.OneToOneField(CadTbCVit, models.DO_NOTHING, db_column='id_visita', primary_key=True)  # The composite primary key (id_visita, id_km) found, that is not supported. The first column is selected.
    id_km = models.IntegerField()
    id_veiculo = models.IntegerField()
    km_inicial = models.FloatField(blank=True, null=True)
    km_final = models.FloatField(blank=True, null=True)
    km_inicial_orig = models.FloatField(blank=True, null=True)
    km_final_orig = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tb_c_vit_kmt'
        unique_together = (('id_visita', 'id_km'),)


class CmpTbMCot(models.Model):
    id_cotacao = models.IntegerField(primary_key=True)
    id_empresa = models.ForeignKey(CadTbCPar, models.DO_NOTHING, db_column='id_empresa')
    dta_cotacao = models.DateField()
    obs = models.CharField(max_length=100, blank=True, null=True)
    ip_lancador = models.CharField(max_length=30, blank=True, null=True)
    id_funcionario = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_funcionario')
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    situacao = models.IntegerField(blank=True, null=True)
    aprovada = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cmp_tb_m_cot'
        db_table_comment = 'CotaþÒo de Preþos'


class CmpTbMCotFit(models.Model):
    id_cotacao = models.OneToOneField(CmpTbMCot, models.DO_NOTHING, db_column='id_cotacao', primary_key=True)  # The composite primary key (id_cotacao, id_fornecedor, id_sequencia) found, that is not supported. The first column is selected.
    id_fornecedor = models.IntegerField()
    id_item = models.ForeignKey(CadTbCIte, models.DO_NOTHING, db_column='id_item')
    qtde = models.FloatField()
    vlr_unitario = models.DecimalField(max_digits=18, decimal_places=4)
    per_desconto = models.FloatField(blank=True, null=True)
    vlr_desconto = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_total = models.DecimalField(max_digits=18, decimal_places=4)
    frete = models.IntegerField()
    prazo = models.IntegerField()
    disponibilidade = models.BooleanField()
    aprovado = models.BooleanField()
    id_cor = models.IntegerField(blank=True, null=True)
    id_tamanho = models.IntegerField(blank=True, null=True)
    dta_aprovacao = models.DateField(blank=True, null=True)
    ipi = models.BooleanField(blank=True, null=True)
    id_sequencia = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cmp_tb_m_cot_fit'
        unique_together = (('id_cotacao', 'id_fornecedor', 'id_sequencia'),)
        db_table_comment = 'Cotaþ§es - Itens por Fornecedor'


class CmpTbMCotFitApr(models.Model):
    id_cotacao = models.OneToOneField(CmpTbMCot, models.DO_NOTHING, db_column='id_cotacao', primary_key=True)  # The composite primary key (id_cotacao, id_fornecedor, id_sequencia) found, that is not supported. The first column is selected.
    id_fornecedor = models.IntegerField()
    id_item = models.IntegerField()
    id_pedido = models.IntegerField(blank=True, null=True)
    dta_aprovacao = models.DateField(blank=True, null=True)
    id_responsavel = models.IntegerField(blank=True, null=True)
    id_cor = models.IntegerField(blank=True, null=True)
    id_tamanho = models.IntegerField(blank=True, null=True)
    id_sequencia = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cmp_tb_m_cot_fit_apr'
        unique_together = (('id_cotacao', 'id_fornecedor', 'id_sequencia'),)
        db_table_comment = 'ITEM DA COTAÃ├O APROVADA'


class CmpTbMCotFor(models.Model):
    id_cotacao = models.OneToOneField(CmpTbMCot, models.DO_NOTHING, db_column='id_cotacao', primary_key=True)  # The composite primary key (id_cotacao, id_fornecedor) found, that is not supported. The first column is selected.
    id_fornecedor = models.ForeignKey(CadTbCFor, models.DO_NOTHING, db_column='id_fornecedor')
    dta_lancamento = models.DateField(blank=True, null=True)
    vlr_total = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cmp_tb_m_cot_for'
        unique_together = (('id_cotacao', 'id_fornecedor'),)
        db_table_comment = 'CotaþÒo por Fornecedor'


class CmpTbMCotIte(models.Model):
    id_cotacao = models.OneToOneField(CmpTbMCot, models.DO_NOTHING, db_column='id_cotacao', primary_key=True)  # The composite primary key (id_cotacao, id_sequencia) found, that is not supported. The first column is selected.
    id_item = models.ForeignKey(CadTbCIte, models.DO_NOTHING, db_column='id_item')
    qtde = models.FloatField()
    id_cor = models.IntegerField(blank=True, null=True)
    id_tamanho = models.IntegerField(blank=True, null=True)
    id_busca_item = models.CharField(max_length=30, blank=True, null=True)
    id_sequencia = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cmp_tb_m_cot_ite'
        unique_together = (('id_cotacao', 'id_sequencia'),)
        db_table_comment = 'Cotaþ§es - Itens'


class CmpTbMPed(models.Model):
    id_pedido = models.IntegerField(primary_key=True)
    id_empresa = models.ForeignKey(CadTbCPar, models.DO_NOTHING, db_column='id_empresa')
    id_fornecedor = models.ForeignKey(CadTbCFor, models.DO_NOTHING, db_column='id_fornecedor')
    dta_pedido = models.DateField()
    dta_entrega = models.DateField(db_comment='Data que o fornecedo irß entregar a mercadoria.')
    id_responsavel = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_responsavel', db_comment='Responsßvel pelo pedido de compra.')
    observacao = models.CharField(max_length=300, blank=True, null=True)
    status = models.IntegerField(db_comment='0 - Pendente\n1 - Entregue Parcial\n2 - Entregue Total\n3 - Finalisado')
    vlr_ipi = models.DecimalField(max_digits=18, decimal_places=4)
    vlr_bruto = models.DecimalField(max_digits=18, decimal_places=4)
    vlr_desconto = models.DecimalField(max_digits=18, decimal_places=4)
    vlr_liquido = models.DecimalField(max_digits=18, decimal_places=4)
    condicoes_pagamento = models.CharField(max_length=60, blank=True, null=True)
    vlr_frete = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    id_cotacao = models.IntegerField(blank=True, null=True)
    id_solicitacao = models.IntegerField(blank=True, null=True)
    aprovado = models.BooleanField(blank=True, null=True, db_comment='Este campo terß utilidade caso m¾dulo SGQ = true;')
    id_resp_aprov = models.IntegerField(blank=True, null=True, db_comment='Este campo terß utilidade caso m¾dulo SGQ = true;')
    dta_aprov = models.DateField(blank=True, null=True, db_comment='Este campo terß utilidade caso m¾dulo SGQ = true;')
    hor_aprov = models.TimeField(blank=True, null=True, db_comment='Este campo terß utilidade caso m¾dulo SGQ = true;')
    ind_frete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cmp_tb_m_ped'
        db_table_comment = 'Pedido a Fornecedor'


class CmpTbMPedIqm(models.Model):
    id_pedido = models.OneToOneField(CmpTbMPed, models.DO_NOTHING, db_column='id_pedido', primary_key=True)  # The composite primary key (id_pedido, id_iqm) found, that is not supported. The first column is selected.
    id_iqm = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cmp_tb_m_ped_iqm'
        unique_together = (('id_pedido', 'id_iqm'),)


class CmpTbMPedIqmIte(models.Model):
    id_pedido = models.OneToOneField(CmpTbMPedIqm, models.DO_NOTHING, db_column='id_pedido', primary_key=True)  # The composite primary key (id_pedido, id_iqm, id_sequencia) found, that is not supported. The first column is selected.
    id_iqm = models.IntegerField()
    id_sequencia = models.IntegerField()
    id_item = models.IntegerField()
    qtde = models.FloatField(blank=True, null=True)
    id_cor = models.IntegerField(blank=True, null=True)
    id_tamanho = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cmp_tb_m_ped_iqm_ite'
        unique_together = (('id_pedido', 'id_iqm', 'id_sequencia'),)


class CmpTbMPedIte(models.Model):
    id_pedido = models.OneToOneField(CmpTbMPed, models.DO_NOTHING, db_column='id_pedido', primary_key=True)  # The composite primary key (id_pedido, id_sequencia, id_item) found, that is not supported. The first column is selected.
    id_sequencia = models.IntegerField()
    id_item = models.ForeignKey(CadTbCIte, models.DO_NOTHING, db_column='id_item')
    qtde = models.FloatField()
    vlr_unitario = models.DecimalField(max_digits=18, decimal_places=4)
    per_desconto = models.FloatField()
    vlr_desconto = models.DecimalField(max_digits=18, decimal_places=4)
    per_ipi = models.FloatField(blank=True, null=True)
    vlr_ipi = models.DecimalField(max_digits=18, decimal_places=4)
    vlr_bruto = models.DecimalField(max_digits=18, decimal_places=4)
    vlr_liquido = models.DecimalField(max_digits=18, decimal_places=4)
    qtde_baixada = models.FloatField(blank=True, null=True, db_comment='Este campo Ú utilizado pela nota fiscal de entrada.')
    entre_prazo = models.IntegerField(blank=True, null=True, db_comment='Prazo de entrega (dias).')
    per_frete = models.FloatField()
    vlr_frete = models.DecimalField(max_digits=18, decimal_places=4)
    id_tamanho = models.IntegerField(blank=True, null=True)
    id_cor = models.IntegerField(blank=True, null=True)
    id_busca_item = models.CharField(max_length=30, blank=True, null=True)
    qtde_a_baixar = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cmp_tb_m_ped_ite'
        unique_together = (('id_pedido', 'id_sequencia', 'id_item'),)
        db_table_comment = 'Pedido a Fornecedor - Itens'


class CmpTbMPedNfe(models.Model):
    id_pedido = models.OneToOneField(CmpTbMPed, models.DO_NOTHING, db_column='id_pedido', primary_key=True)  # The composite primary key (id_pedido, id_fiscal) found, that is not supported. The first column is selected.
    id_fiscal = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cmp_tb_m_ped_nfe'
        unique_together = (('id_pedido', 'id_fiscal'),)
        db_table_comment = 'Para ter a possibilidade de ter mias de uma nota fiscal para um pedido.'


class CmpTbMPedNfeIte(models.Model):
    id_pedido = models.OneToOneField(CmpTbMPedNfe, models.DO_NOTHING, db_column='id_pedido', primary_key=True)  # The composite primary key (id_pedido, id_fiscal, id_sequencia) found, that is not supported. The first column is selected.
    id_fiscal = models.IntegerField()
    id_sequencia = models.IntegerField()
    id_item = models.IntegerField()
    qtde = models.FloatField(blank=True, null=True)
    id_cor = models.IntegerField(blank=True, null=True)
    id_tamanho = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cmp_tb_m_ped_nfe_ite'
        unique_together = (('id_pedido', 'id_fiscal', 'id_sequencia'),)


class CmpTbMSol(models.Model):
    id_solicitacao = models.IntegerField(primary_key=True)
    id_empresa = models.ForeignKey(CadTbCPar, models.DO_NOTHING, db_column='id_empresa')
    id_funcionario = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_funcionario')
    id_setor = models.ForeignKey(CadTbCSet, models.DO_NOTHING, db_column='id_setor')
    dta_solicitacao = models.DateField()
    status = models.IntegerField()
    obs = models.CharField(max_length=100, blank=True, null=True)
    motivo = models.CharField(max_length=100, blank=True, null=True)
    id_op = models.IntegerField()
    id_cotacao_imp = models.IntegerField(blank=True, null=True)
    id_pedido_imp = models.IntegerField(blank=True, null=True)
    selecao = models.BooleanField(blank=True, null=True)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    id_opr_req = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cmp_tb_m_sol'
        db_table_comment = 'SolicitaþÒo de Compras'


class CmpTbMSolIte(models.Model):
    id_solicitacao = models.OneToOneField(CmpTbMSol, models.DO_NOTHING, db_column='id_solicitacao', primary_key=True)  # The composite primary key (id_solicitacao, id_sequencia) found, that is not supported. The first column is selected.
    id_item = models.IntegerField()
    qtde = models.FloatField()
    obs = models.CharField(max_length=100, blank=True, null=True)
    id_cor = models.IntegerField(blank=True, null=True)
    id_tamanho = models.IntegerField(blank=True, null=True)
    id_busca_item = models.CharField(max_length=30, blank=True, null=True)
    id_sequencia = models.IntegerField()
    desc_item = models.CharField(max_length=100, blank=True, null=True)
    und_item = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cmp_tb_m_sol_ite'
        unique_together = (('id_solicitacao', 'id_sequencia'),)
        db_table_comment = 'SolicitaþÒo de Compras - Itens'


class CtcTbCEoc(models.Model):
    id_estrutura = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctc_tb_c_eoc'


class CtcTbCEocGru(models.Model):
    id_estrutura = models.OneToOneField(CtcTbCEoc, models.DO_NOTHING, db_column='id_estrutura', primary_key=True)  # The composite primary key (id_estrutura, grupo) found, that is not supported. The first column is selected.
    grupo = models.CharField(max_length=5)
    descricao = models.CharField(max_length=600, blank=True, null=True)
    und = models.CharField(max_length=4, blank=True, null=True)
    classe = models.CharField(max_length=6, blank=True, null=True)
    cod_prpoprio = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctc_tb_c_eoc_gru'
        unique_together = (('id_estrutura', 'grupo'),)


class CtcTbCEpi(models.Model):
    id_epi = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=30, blank=True, null=True)
    id_unidade = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctc_tb_c_epi'
        db_table_comment = 'CADASTRO DE EPI'


class CtcTbCObr(models.Model):
    id_obra = models.IntegerField(primary_key=True)
    id_cliente = models.IntegerField()
    descricao = models.CharField(max_length=50)
    ativo = models.BooleanField()
    endereco = models.CharField(max_length=50)
    id_cidade = models.ForeignKey(CadTbCCid, models.DO_NOTHING, db_column='id_cidade', blank=True, null=True)
    cep = models.CharField(max_length=9, blank=True, null=True)
    tel_fixo = models.CharField(max_length=14, blank=True, null=True)
    fax = models.CharField(max_length=14, blank=True, null=True)
    obs = models.CharField(max_length=800, blank=True, null=True)
    dta_entrega = models.DateField()
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    id_tpr = models.ForeignKey('CtcTbCTpr', models.DO_NOTHING, db_column='id_tpr', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctc_tb_c_obr'
        db_table_comment = 'Cadastro de Obras'


class CtcTbCObrCrg(models.Model):
    id_obra = models.OneToOneField(CtcTbCObr, models.DO_NOTHING, db_column='id_obra', primary_key=True)  # The composite primary key (id_obra, id_obra_crg) found, that is not supported. The first column is selected.
    id_cargo = models.ForeignKey('PcpTbCCrg', models.DO_NOTHING, db_column='id_cargo')
    qtde_func = models.IntegerField()
    valor = models.DecimalField(max_digits=18, decimal_places=2)
    dta_ini_contrato = models.DateField()
    dta_fim_contrato = models.DateField()
    obs = models.CharField(max_length=80, blank=True, null=True)
    id_obra_crg = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ctc_tb_c_obr_crg'
        unique_together = (('id_obra', 'id_obra_crg'),)


class CtcTbCObrEqp(models.Model):
    id_obra = models.OneToOneField(CtcTbCObr, models.DO_NOTHING, db_column='id_obra', primary_key=True)  # The composite primary key (id_obra, id_obra_seq) found, that is not supported. The first column is selected.
    id_obra_seq = models.IntegerField()
    id_meq = models.ForeignKey('PcpTbCMeq', models.DO_NOTHING, db_column='id_meq')
    valor = models.DecimalField(max_digits=18, decimal_places=2)
    dta_ini_contrato = models.DateField()
    dta_fim_contrato = models.DateField()
    obs = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctc_tb_c_obr_eqp'
        unique_together = (('id_obra', 'id_obra_seq'),)


class CtcTbCObrIte(models.Model):
    id_obra = models.OneToOneField(CtcTbCObr, models.DO_NOTHING, db_column='id_obra', primary_key=True)  # The composite primary key (id_obra, id_obra_ite) found, that is not supported. The first column is selected.
    id_obra_ite = models.IntegerField()
    id_item = models.ForeignKey(CadTbCIte, models.DO_NOTHING, db_column='id_item')
    dta_ini_contrato = models.DateField()
    dta_fim_contrato = models.DateField()
    obs = models.CharField(max_length=80, blank=True, null=True)
    valor = models.DecimalField(max_digits=18, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'ctc_tb_c_obr_ite'
        unique_together = (('id_obra', 'id_obra_ite'),)


class CtcTbCOco(models.Model):
    id_ocorrencia = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctc_tb_c_oco'


class CtcTbCTpr(models.Model):
    id_tpr = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctc_tb_c_tpr'
        db_table_comment = 'Cadastro de Tabela de precos'


class CtcTbCTprIte(models.Model):
    id_tpr = models.OneToOneField(CtcTbCTpr, models.DO_NOTHING, db_column='id_tpr', primary_key=True)  # The composite primary key (id_tpr, id_item) found, that is not supported. The first column is selected.
    id_item = models.CharField(max_length=20)
    descricao = models.CharField(max_length=800, blank=True, null=True)
    classe = models.IntegerField(blank=True, null=True, db_comment='0-Material\n1-Mao-de-obra\n')
    unidade = models.CharField(max_length=10, blank=True, null=True)
    preco_unitario = models.DecimalField(max_digits=15, decimal_places=6, blank=True, null=True)
    data_base = models.DateField(blank=True, null=True)
    id_item_interno = models.IntegerField(blank=True, null=True, db_comment='Este campo vai servir para fazer a correspondcia entre o codigo das tabelas tcpo... com o codigo do nosso sistema.')

    class Meta:
        managed = False
        db_table = 'ctc_tb_c_tpr_ite'
        unique_together = (('id_tpr', 'id_item'),)


class CtcTbCTprIteCom(models.Model):
    id_tpr = models.OneToOneField(CtcTbCTprIte, models.DO_NOTHING, db_column='id_tpr', primary_key=True)  # The composite primary key (id_tpr, id_item, id_item_comp) found, that is not supported. The first column is selected.
    id_item = models.CharField(max_length=20)
    id_item_comp = models.CharField(max_length=20)
    qtde = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctc_tb_c_tpr_ite_com'
        unique_together = (('id_tpr', 'id_item', 'id_item_comp'),)


class CtcTbMApg(models.Model):
    id_apg = models.IntegerField(primary_key=True)
    id_empresa = models.ForeignKey(CadTbCPar, models.DO_NOTHING, db_column='id_empresa')
    dia = models.CharField(max_length=2)
    historico = models.CharField(max_length=100)
    vlr_previsto = models.DecimalField(max_digits=18, decimal_places=4)
    id_obra = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctc_tb_m_apg'


class CtcTbMAvf(models.Model):
    id_avf = models.IntegerField(primary_key=True)
    dta_avf = models.DateField(blank=True, null=True)
    id_responsavel = models.IntegerField(blank=True, null=True)
    id_fornecedor = models.IntegerField(blank=True, null=True)
    nom_fornecedor = models.CharField(max_length=50, blank=True, null=True)
    doc_cnpj = models.CharField(max_length=14, blank=True, null=True)
    perg_01 = models.BooleanField(blank=True, null=True)
    perg_02 = models.BooleanField(blank=True, null=True)
    perg_03 = models.BooleanField(blank=True, null=True)
    perg_04 = models.BooleanField(blank=True, null=True)
    criterio_01 = models.FloatField(blank=True, null=True)
    criterio_02 = models.FloatField(blank=True, null=True)
    criterio_03 = models.FloatField(blank=True, null=True)
    criterio_04 = models.FloatField(blank=True, null=True)
    criterio_05 = models.FloatField(blank=True, null=True)
    criterio_06 = models.FloatField(blank=True, null=True)
    criterio_07 = models.FloatField(blank=True, null=True)
    peso_01 = models.FloatField(blank=True, null=True)
    peso_02 = models.FloatField(blank=True, null=True)
    peso_03 = models.FloatField(blank=True, null=True)
    peso_04 = models.FloatField(blank=True, null=True)
    peso_05 = models.FloatField(blank=True, null=True)
    peso_06 = models.FloatField(blank=True, null=True)
    peso_07 = models.FloatField(blank=True, null=True)
    obs = models.CharField(max_length=100, blank=True, null=True)
    media = models.FloatField(blank=True, null=True)
    for_aprovado = models.BooleanField(blank=True, null=True)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctc_tb_m_avf'
        db_table_comment = 'AvalialþÒo de Fornecedor'


class CtcTbMBde(models.Model):
    id_bde = models.IntegerField(primary_key=True)
    id_cliente = models.IntegerField(blank=True, null=True)
    id_obra = models.IntegerField(blank=True, null=True)
    id_meq = models.IntegerField(blank=True, null=True)
    dta_bde = models.DateField(blank=True, null=True)
    id_operador = models.IntegerField(blank=True, null=True)
    vlr_desconto = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_acrescimo = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_servicos = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_comissao = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    hori_inicial = models.FloatField(blank=True, null=True)
    hori_final = models.FloatField(blank=True, null=True)
    vlr_combustivel = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    hori_total = models.FloatField(blank=True, null=True)
    vlr_bruto = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    nro_bde = models.IntegerField(blank=True, null=True)
    qtde_combustivel = models.FloatField(blank=True, null=True)
    obs = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctc_tb_m_bde'
        db_table_comment = 'BOLETIM DIARIO DE EQUIPAMENTO'


class CtcTbMBdeOco(models.Model):
    id_bde = models.OneToOneField(CtcTbMBde, models.DO_NOTHING, db_column='id_bde', primary_key=True)  # The composite primary key (id_bde, id_ocorrencia) found, that is not supported. The first column is selected.
    id_ocorrencia = models.ForeignKey(CtcTbCOco, models.DO_NOTHING, db_column='id_ocorrencia')
    qtde = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctc_tb_m_bde_oco'
        unique_together = (('id_bde', 'id_ocorrencia'),)


class CtcTbMBdeVrf(models.Model):
    id_bde = models.IntegerField(blank=True, null=True)
    id_verificacao = models.IntegerField(blank=True, null=True)
    pad_buz_funciona = models.CharField(max_length=1, blank=True, null=True, db_comment='A buzina estß funcionando?')
    pad_extintor_incendio = models.CharField(max_length=1, blank=True, null=True, db_comment='O extintor de incÛndio estß em condiþ§es de uso?')
    pad_verif_cinto_seguranca = models.CharField(max_length=1, blank=True, null=True, db_comment='Foi verificado o cinto de seguranþa?')
    pad_veic_possui_mac = models.CharField(max_length=1, blank=True, null=True, db_comment='O veÝculo possui macaco?')
    pad_veic_possui_chv_roda = models.CharField(max_length=1, blank=True, null=True, db_comment='O veÝculo possui chave de roda?')
    pad_veic_possui_mao_forca = models.CharField(max_length=1, blank=True, null=True, db_comment='O veÝculo possui mÒo de forþa?')
    pad_veic_possui_triangulo = models.CharField(max_length=1, blank=True, null=True, db_comment='O veÝculo possui triÔngulo de sinalizaþÒo?')
    pad_veic_possui_martelo_mad = models.CharField(max_length=1, blank=True, null=True, db_comment='O veÝculo possui martelo de madeira?')
    pad_sis_freio_funciona = models.CharField(max_length=1, blank=True, null=True, db_comment='Sistema de freio estß funcionando corretamente?')
    pad_ind_pres_oleo_funciona = models.CharField(max_length=1, blank=True, null=True, db_comment='O indicador de pressÒo de ¾leo estß funcionando?')
    pad_drenagem_tanq_filtro = models.CharField(max_length=1, blank=True, null=True, db_comment='Foi feito a drenagem do tanque e do filtro de combustÝvel?')
    pad_verif_pres_calib_pneus = models.CharField(max_length=1, blank=True, null=True, db_comment='Foi verificado a pressÒo de calibragem dos pneus?')
    pad_verif_folga_rol_rosca_fim = models.CharField(max_length=1, blank=True, null=True, db_comment='Foi verificada a folga dos rolamentos da rosca sem fim?')
    pad_feita_dren_baloes_ar = models.CharField(max_length=1, blank=True, null=True, db_comment='Foi feita a drenagem dos bal§es de ar?')
    pad_verif_estado_correias = models.CharField(max_length=1, blank=True, null=True, db_comment='Foi verificado o estado das correias?')
    pad_verif_estado_maq_geral = models.CharField(max_length=1, blank=True, null=True, db_comment='Foi verificado o estado das mangueiras em geral?')
    pad_feita_lubrif_ger_equip = models.CharField(max_length=1, blank=True, null=True, db_comment='Foi feita a lubrificaþÒo geral do equipamento?')
    pad_equip_ise_vaz_hidraulico = models.CharField(max_length=1, blank=True, null=True, db_comment='Equipamento isento de vazamento hidra·lico?')
    pad_verif_nivel_agua_radiador = models.CharField(max_length=1, blank=True, null=True, db_comment='Foi verificado o nivel de ßgua do radiador?')
    pad_verif_nivel_oleo_mot_hid_freio = models.CharField(max_length=1, blank=True, null=True, db_comment='Foram verificados os niveis de ¾leo motor, hidrßulico e freio?')
    pad_verif_conserv_polos_baterias = models.CharField(max_length=1, blank=True, null=True, db_comment='Foi verificado conservaþÒo dos polos das baterias?')
    pad_verif_filtro_ar_cabine = models.CharField(max_length=1, blank=True, null=True, db_comment='Foi verificado o filtro de ar da cabine?')
    pad_verif_instalacao_instrum_eletr = models.CharField(max_length=1, blank=True, null=True, db_comment='Foi verificado a instalaþÒo e instrumentos elÚtricos?')
    pad_verif_estado_vidragem_ger = models.CharField(max_length=1, blank=True, null=True, db_comment='Foi verificado o estado da vidraþaria em geral?')
    pad_verif_doc_equip = models.CharField(max_length=1, blank=True, null=True, db_comment='Foi verificada a documentaþÒo do equipamento?')
    pad_verif_estado_mat_rodante = models.CharField(max_length=1, blank=True, null=True, db_comment='Foi verificado o estado do material rodante?')
    pad_ha_vazamento_oleo_combust = models.CharField(max_length=1, blank=True, null=True, db_comment='Hß vazamento de ¾leo ou combustÝvel?')
    pad_maq_kit_mitigacao = models.CharField(max_length=1, blank=True, null=True, db_comment='A mßquina estß equipada com kit de mitigaþÒo (Pß, bandeja de contenþÒo, lona, p¾ de serra e sacolas plßsticas?)')
    pad_maq_ruid_excess = models.CharField(max_length=1, blank=True, null=True, db_comment='A mßquina apresenta ruÝdos excessivos?')
    pneu_isento_picotamento = models.CharField(max_length=1, blank=True, null=True, db_comment='Pneus isentos de picotamentos?')
    pneu_livre_corte_lateral = models.CharField(max_length=1, blank=True, null=True, db_comment='Pneus livres de cortes na lateral?')
    pneu_banda_rol_isenta_solt = models.CharField(max_length=1, blank=True, null=True, db_comment='Banda de rolagem dos pneus isenta de soltura?')
    imple_p_lubrif_cruz_eixo_conjunto = models.CharField(max_length=1, blank=True, null=True, db_comment='Foram lubrificadas as cruzetas do eixo cardam do conjunto?')
    imple_p_bord_tom_isenta_vazam = models.CharField(max_length=1, blank=True, null=True, db_comment='Borda da tomada de forþa isenta de vazamento?')
    imple_p_verif_niv_oleo_cxa_mult = models.CharField(max_length=1, blank=True, null=True, db_comment='Foi verificado o nÝvel de ¾leo da caixa multiplicadora')
    imple_p_verif_corr_gax_bomba = models.CharField(max_length=1, blank=True, null=True, db_comment='Foi verificado a correia e a gazeta da bomba?')
    imple_p_algum_vaz_tanq_trans_ag = models.CharField(max_length=1, blank=True, null=True, db_comment='Hß algum vazamento_no_tanque de transporte de ßgua?')
    imple_b_verif_niv_oleo_hid_basc = models.CharField(max_length=1, blank=True, null=True, db_comment='Foi verificado o nÝvel do olÚo hidrßulico do basculante?')
    imple_b_sis_hid_isento_vaz = models.CharField(max_length=1, blank=True, null=True, db_comment='Sistema hidrßulico isento de vazamento?')
    imple_b_lub_pin_cilin_cruz_tom = models.CharField(max_length=1, blank=True, null=True, db_comment='Foi feita a lubrificaþÒo dos pinos dos mancais de giro, do cilindro e da cruzeta da tomada de forþa?')
    imple_m_verif_niv_oleo_mot_comp = models.CharField(max_length=1, blank=True, null=True, db_comment='Foi verificado o nÝvel de ¾leo do motor e do compressor?')
    imple_m_drenag_reserv_ar_comp = models.CharField(max_length=1, blank=True, null=True, db_comment='Foi feito a drenagem do reservat¾rio de ar do compressor?')
    imple_m_prop_j_v_c_tub_isento_vaz = models.CharField(max_length=1, blank=True, null=True, db_comment='Propulsora, juntas, vßlvulas, conex§es e tubulaþ§es do compressor isentos de vazamentos?')
    imple_m_lub_ger_grax = models.CharField(max_length=1, blank=True, null=True, db_comment='Foi feita a lubrificaþÒo geral dos graxeiros?')
    imple_m_verif_corr_acopl_sis = models.CharField(max_length=1, blank=True, null=True, db_comment='Foi verificado a correia de acoplamento do sistema?')

    class Meta:
        managed = False
        db_table = 'ctc_tb_m_bde_vrf'
        db_table_comment = '\r\nVeificaþ§es do equipamento informado.'


class CtcTbMCep(models.Model):
    id_cep = models.IntegerField(primary_key=True)
    data = models.DateField(blank=True, null=True)
    id_responsavel = models.IntegerField(blank=True, null=True)
    resp_tecnico = models.CharField(max_length=50, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctc_tb_m_cep'
        db_table_comment = 'CONTROLE DE EPI'


class CtcTbMCepEpi(models.Model):
    id_cep = models.OneToOneField(CtcTbMCep, models.DO_NOTHING, db_column='id_cep', primary_key=True)  # The composite primary key (id_cep, sequencia) found, that is not supported. The first column is selected.
    sequencia = models.IntegerField()
    id_epi = models.ForeignKey(CadTbCIte, models.DO_NOTHING, db_column='id_epi', blank=True, null=True)
    marca = models.CharField(max_length=20, blank=True, null=True)
    modelo = models.CharField(max_length=20, blank=True, null=True)
    ca = models.CharField(max_length=20, blank=True, null=True)
    dta_devolucao = models.DateField(blank=True, null=True)
    dta_entrega = models.DateField(blank=True, null=True)
    qtde = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctc_tb_m_cep_epi'
        unique_together = (('id_cep', 'sequencia'),)


class CtcTbMCfe(models.Model):
    id_cfe = models.IntegerField(primary_key=True)
    data = models.DateField(blank=True, null=True)
    id_funcionario = models.IntegerField(blank=True, null=True)
    vlr_total = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctc_tb_m_cfe'
        db_table_comment = 'CONTROLE DE FERRAMENTAS'


class CtcTbMCfeFer(models.Model):
    id_cfe = models.OneToOneField(CtcTbMCfe, models.DO_NOTHING, db_column='id_cfe', primary_key=True)  # The composite primary key (id_cfe, id_meq) found, that is not supported. The first column is selected.
    id_meq = models.IntegerField()
    qtde = models.FloatField(blank=True, null=True)
    vlr_unitario = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_total = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    dta_devolucao = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctc_tb_m_cfe_fer'
        unique_together = (('id_cfe', 'id_meq'),)


class CtcTbMFac(models.Model):
    id_fac = models.IntegerField(primary_key=True)
    dta_abertura = models.DateField(blank=True, null=True)
    pro_acao = models.IntegerField(blank=True, null=True, db_comment='0-Corretiva\n1-Preventiva\n2-Melhoria')
    pro_origem = models.IntegerField(blank=True, null=True, db_comment='0-Auditoria Interna\n1-Auditoria Externa\n2-Reclamaþ§es de Clientes\n3-Colaboradores\n4-Outros')
    pro_id_responsavel = models.IntegerField(blank=True, null=True)
    pro_descricao = models.CharField(max_length=100, blank=True, null=True)
    pro_data = models.DateField(blank=True, null=True)
    aci_descricao = models.CharField(max_length=100, blank=True, null=True)
    aci_id_responsavel = models.IntegerField(blank=True, null=True)
    aci_data = models.DateField(blank=True, null=True)
    ava_avaliacao = models.IntegerField(blank=True, null=True)
    ava_id_responsavel = models.IntegerField(blank=True, null=True)
    ava_data = models.DateField(blank=True, null=True)
    cap_descricao = models.CharField(max_length=100, blank=True, null=True)
    cap_id_responsavel = models.IntegerField(blank=True, null=True)
    cap_data = models.DateField(blank=True, null=True)
    acp_descricao_01 = models.CharField(max_length=100, blank=True, null=True)
    acp_descricao_02 = models.CharField(max_length=100, blank=True, null=True)
    acp_descricao_03 = models.CharField(max_length=100, blank=True, null=True)
    acp_descricao_04 = models.CharField(max_length=100, blank=True, null=True)
    acp_id_resp_01 = models.IntegerField(blank=True, null=True)
    acp_id_resp_02 = models.IntegerField(blank=True, null=True)
    acp_id_resp_03 = models.IntegerField(blank=True, null=True)
    acp_id_resp_04 = models.IntegerField(blank=True, null=True)
    acp_data_01 = models.DateField(blank=True, null=True)
    acp_data_02 = models.DateField(blank=True, null=True)
    acp_data_03 = models.DateField(blank=True, null=True)
    acp_data_04 = models.DateField(blank=True, null=True)
    mae_descricao = models.CharField(max_length=100, blank=True, null=True)
    aco_perg_01 = models.BooleanField(blank=True, null=True)
    aco_perg_02 = models.BooleanField(blank=True, null=True)
    aco_perg_03 = models.BooleanField(blank=True, null=True)
    aco_perg_04 = models.BooleanField(blank=True, null=True)
    aco_perg_01_prazo = models.IntegerField(blank=True, null=True)
    aco_perg_02_prazo = models.IntegerField(blank=True, null=True)
    aco_perg_03_fac = models.IntegerField(blank=True, null=True)
    aco_perg_04_fac = models.IntegerField(blank=True, null=True)
    aca_descricao = models.CharField(max_length=100, blank=True, null=True)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctc_tb_m_fac'
        db_table_comment = 'AþÒo Corretiva, Preventiva e de Melhorias (FAC)'


class CtcTbMLoc(models.Model):
    id_loc = models.IntegerField(primary_key=True)
    dta_locacao = models.DateField(blank=True, null=True)
    id_obra = models.IntegerField(blank=True, null=True)
    num_contrato = models.IntegerField(blank=True, null=True)
    num_documento = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    vlr_frete = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_desconto = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_total = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    id_fornecedor = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctc_tb_m_loc'
        db_table_comment = 'Controle de LocaþÒo'


class CtcTbMLocMeq(models.Model):
    id_loc = models.OneToOneField(CtcTbMLoc, models.DO_NOTHING, db_column='id_loc', primary_key=True)  # The composite primary key (id_loc, id_veiculo) found, that is not supported. The first column is selected.
    id_veiculo = models.IntegerField()
    vlr_unitario = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    qtde = models.FloatField(blank=True, null=True)
    total = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    dta_inicial = models.DateField(blank=True, null=True)
    dta_final = models.DateField(blank=True, null=True)
    entrega = models.DateField(blank=True, null=True)
    devolucao = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctc_tb_m_loc_meq'
        unique_together = (('id_loc', 'id_veiculo'),)
        db_table_comment = 'Equeipamento Locado'


class CtcTbMOfi(models.Model):
    id_ofi = models.IntegerField(primary_key=True)
    data = models.DateField(blank=True, null=True)
    id_veiculo = models.IntegerField(blank=True, null=True)
    id_fornecedor = models.IntegerField(blank=True, null=True)
    problema = models.CharField(max_length=200, blank=True, null=True)
    observacao = models.CharField(max_length=200, blank=True, null=True)
    id_solicitante = models.IntegerField(blank=True, null=True)
    km_veiculo = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    vlr_total = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctc_tb_m_ofi'
        db_table_comment = 'Oficina - Pecas e servicos gasto em manutenþÒo dos veiculos'


class CtcTbMOfiIte(models.Model):
    id_ofi = models.OneToOneField(CtcTbMOfi, models.DO_NOTHING, db_column='id_ofi', primary_key=True)  # The composite primary key (id_ofi, sequencia) found, that is not supported. The first column is selected.
    sequencia = models.IntegerField()
    descricao = models.CharField(max_length=50, blank=True, null=True)
    qtde = models.FloatField(blank=True, null=True)
    vlr_unitario = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_total = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctc_tb_m_ofi_ite'
        unique_together = (('id_ofi', 'sequencia'),)


class CtcTbMOrc(models.Model):
    id_orc = models.IntegerField(primary_key=True)
    dta_orc = models.DateField(blank=True, null=True)
    id_obra = models.IntegerField(blank=True, null=True)
    obs = models.CharField(max_length=100, blank=True, null=True)
    vlr_total = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    id_estrutura = models.IntegerField(blank=True, null=True)
    id_empresa = models.ForeignKey(CadTbCPar, models.DO_NOTHING, db_column='id_empresa', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctc_tb_m_orc'
        db_table_comment = 'Orþamento de Obras'


class CtcTbMOrcIte(models.Model):
    id_orc = models.OneToOneField(CtcTbMOrc, models.DO_NOTHING, db_column='id_orc', primary_key=True)  # The composite primary key (id_orc, grupo) found, that is not supported. The first column is selected.
    grupo = models.CharField(max_length=5)
    descricao = models.CharField(max_length=600, blank=True, null=True)
    und = models.CharField(max_length=4, blank=True, null=True)
    classe = models.CharField(max_length=6, blank=True, null=True)
    cod_prpoprio = models.CharField(max_length=15, blank=True, null=True)
    qtde = models.FloatField(blank=True, null=True)
    vlr_unitario = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_total = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    qtde_saldo_medicao = models.FloatField(blank=True, null=True)
    vlr_mo = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_mat = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    per_ls = models.FloatField(blank=True, null=True)
    vlr_ls = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    per_bdi = models.FloatField(blank=True, null=True)
    vlr_bdi = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    per_adm = models.FloatField(blank=True, null=True)
    vlr_adm = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    total_taxa = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctc_tb_m_orc_ite'
        unique_together = (('id_orc', 'grupo'),)


class CtcTbMOrcIteCom(models.Model):
    id_orc = models.OneToOneField(CtcTbMOrcIte, models.DO_NOTHING, db_column='id_orc', primary_key=True)  # The composite primary key (id_orc, grupo, id_com) found, that is not supported. The first column is selected.
    grupo = models.CharField(max_length=5)
    id_com = models.IntegerField()
    id_item = models.CharField(max_length=20)
    coeficiente = models.FloatField(blank=True, null=True)
    vlr_unitario = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_total = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctc_tb_m_orc_ite_com'
        unique_together = (('id_orc', 'grupo', 'id_com'),)


class CtcTbMOrcIteMed(models.Model):
    id_orc = models.OneToOneField(CtcTbMOrcIte, models.DO_NOTHING, db_column='id_orc', primary_key=True)  # The composite primary key (id_orc, grupo, id_med) found, that is not supported. The first column is selected.
    grupo = models.CharField(max_length=5)
    id_med = models.IntegerField()
    id_item = models.CharField(max_length=20)
    qtde = models.FloatField(blank=True, null=True)
    dta_medicao = models.DateField(blank=True, null=True)
    id_responsavel = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctc_tb_m_orc_ite_med'
        unique_together = (('id_orc', 'grupo', 'id_med'),)


class CtcTbMPme(models.Model):
    id_pme = models.IntegerField(primary_key=True)
    id_equip = models.CharField(max_length=8, blank=True, null=True)
    tipo_cont = models.CharField(max_length=20, blank=True, null=True)
    modelo = models.CharField(max_length=30, blank=True, null=True)
    ult_manu = models.CharField(max_length=10, blank=True, null=True)
    atual_manu = models.CharField(max_length=10, blank=True, null=True)
    prox_manu = models.CharField(max_length=10, blank=True, null=True)
    tipo_prox_manu = models.CharField(max_length=20, blank=True, null=True)
    per_restante = models.CharField(max_length=10, blank=True, null=True)
    per_excedido = models.CharField(max_length=10, blank=True, null=True)
    local = models.CharField(max_length=50, blank=True, null=True)
    observacao = models.CharField(max_length=200, blank=True, null=True)
    tipo_equip = models.CharField(max_length=1, blank=True, null=True)
    dta_ult_dado = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctc_tb_m_pme'


class CtcTbMPro(models.Model):
    id_item = models.OneToOneField(CadTbCIte, models.DO_NOTHING, db_column='id_item', primary_key=True)  # The composite primary key (id_item, lote) found, that is not supported. The first column is selected.
    lote = models.CharField(max_length=30)
    data = models.DateField(blank=True, null=True)
    descricao = models.CharField(max_length=50, blank=True, null=True)
    arquivo = models.CharField(max_length=255, blank=True, null=True)
    doc_pro = models.BinaryField(blank=True, null=True)
    documento = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctc_tb_m_pro'
        unique_together = (('id_item', 'lote'),)


class CtcTbMSlm(models.Model):
    id_controle = models.IntegerField(primary_key=True)
    data = models.DateField()
    id_responsavel = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_responsavel')
    id_obra = models.IntegerField(blank=True, null=True)
    observacao = models.CharField(max_length=100, blank=True, null=True)
    id_empresa = models.ForeignKey(CadTbCPar, models.DO_NOTHING, db_column='id_empresa')

    class Meta:
        managed = False
        db_table = 'ctc_tb_m_slm'


class CtcTbMSlmIte(models.Model):
    id_controle = models.OneToOneField(CtcTbMSlm, models.DO_NOTHING, db_column='id_controle', primary_key=True)  # The composite primary key (id_controle, id_item) found, that is not supported. The first column is selected.
    id_item = models.ForeignKey(CadTbCIte, models.DO_NOTHING, db_column='id_item')
    qtde = models.FloatField()
    observacao = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctc_tb_m_slm_ite'
        unique_together = (('id_controle', 'id_item'),)


class EstTbMCte(models.Model):
    id_controle = models.IntegerField(primary_key=True)
    dta_contagem = models.DateField()
    id_empresa = models.ForeignKey(CadTbCPar, models.DO_NOTHING, db_column='id_empresa')
    obs = models.CharField(max_length=50, blank=True, null=True)
    cte_tipo = models.IntegerField(db_comment='0-LocalizaþÒo\n1-Itens Movimentados\n2-Livre (qualquer item)')
    localizacao = models.CharField(max_length=30, blank=True, null=True)
    dta_movimento = models.DateField(blank=True, null=True)
    id_almoxarifado = models.IntegerField(blank=True, null=True)
    per_inicial = models.DateField(blank=True, null=True)
    per_final = models.DateField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True, db_comment='0-Aberto\n1-Atualizado')
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    corrigir_custo_medio = models.BooleanField(blank=True, null=True, db_comment='Se este campo for TRUE, o usußrio irß especificar apenas o novo valor de custo mÚdio do item.\r\nO saldo irß permanecer o mesmo.')
    offline = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'est_tb_m_cte'
        db_table_comment = 'Contagem de Estoque'


class EstTbMCteIte(models.Model):
    id_controle = models.OneToOneField(EstTbMCte, models.DO_NOTHING, db_column='id_controle', primary_key=True)  # The composite primary key (id_controle, id_item, id_seq_item) found, that is not supported. The first column is selected.
    id_item = models.ForeignKey(CadTbCIte, models.DO_NOTHING, db_column='id_item')
    id_seq_item = models.IntegerField()
    id_cor = models.IntegerField(blank=True, null=True)
    id_tamanho = models.IntegerField(blank=True, null=True)
    id_busca_item = models.CharField(max_length=30, blank=True, null=True)
    contagem = models.FloatField()
    num_lote = models.CharField(max_length=15, blank=True, null=True)
    diferenca = models.FloatField(blank=True, null=True)
    tipo_diferenca = models.IntegerField(blank=True, null=True, db_comment='0- NÒo houve diferenþa\n1- Esta com sobra\n2-Esta com Falta')
    vlr_custo = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    dta_vencimento = models.DateField(blank=True, null=True)
    saldo_estoque_momento = models.FloatField(blank=True, null=True, db_comment='Ficarß gravado o estoque fÝsico do momento.')

    class Meta:
        managed = False
        db_table = 'est_tb_m_cte_ite'
        unique_together = (('id_controle', 'id_item', 'id_seq_item'),)
        db_table_comment = 'Contagem de Estoque - Itens'


class EstTbMFea(models.Model):
    id_fea = models.IntegerField(primary_key=True)
    id_item = models.ForeignKey(CadTbCIte, models.DO_NOTHING, db_column='id_item')
    id_empresa = models.ForeignKey(CadTbCPar, models.DO_NOTHING, db_column='id_empresa')
    data = models.DateField()
    documento = models.IntegerField()
    id_tipo_mov_estoque = models.ForeignKey(CadTbCTme, models.DO_NOTHING, db_column='id_tipo_mov_estoque')
    id_fiscal = models.IntegerField(blank=True, null=True)
    origem = models.IntegerField(db_comment='0 - Por Nota fiscal de entrada\n1 - Por Nota fiscal de saÝda\n2 - Por Ordem de saÝda\n3 - Por almoxarifado - SaÝda\n4 - Por inventßrio\n5 - Por almoxarifado - Devolucao. 6- Por Pedido de Venda 7 - Por Dev. de NF de Fornecedor  8 - Por Dev. de NF de Cliente  9 - Por abertura de OS')
    id_almoxarifado = models.ForeignKey(CadTbCAlm, models.DO_NOTHING, db_column='id_almoxarifado', blank=True, null=True)
    id_mal = models.IntegerField(blank=True, null=True)
    qtde = models.FloatField()
    per_desconto = models.FloatField()
    per_frete = models.FloatField()
    vlr_desconto = models.DecimalField(max_digits=18, decimal_places=4)
    vlr_frete = models.DecimalField(max_digits=18, decimal_places=4)
    vlr_custo = models.DecimalField(max_digits=18, decimal_places=4)
    vlr_bruto = models.DecimalField(max_digits=18, decimal_places=4)
    vlr_movimento = models.DecimalField(max_digits=18, decimal_places=4)
    id_cor = models.IntegerField(blank=True, null=True)
    id_tamanho = models.IntegerField(blank=True, null=True)
    id_seq_item = models.IntegerField(blank=True, null=True)
    id_pedido = models.IntegerField(blank=True, null=True)
    id_controle = models.IntegerField(blank=True, null=True, db_comment='Campo utilizado para gravar o numero de controle da contagem de estoque.')
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    num_lote = models.CharField(max_length=15, blank=True, null=True)
    id_ordem = models.IntegerField(blank=True, null=True, db_comment='Campo utilizado pela Ordem de Serviþo (Oficina)')
    id_met = models.IntegerField(blank=True, null=True)
    id_ors = models.IntegerField(blank=True, null=True)
    id_epp = models.IntegerField(blank=True, null=True)
    id_coj_ite = models.IntegerField(blank=True, null=True)
    coj_ite_hrq = models.CharField(max_length=50, blank=True, null=True)
    id_seq_coj = models.IntegerField(blank=True, null=True)
    id_ordem_asub = models.IntegerField(blank=True, null=True)
    id_opb = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'est_tb_m_fea'
        db_table_comment = 'Ficha de estqoue analitico'


class EstTbMFes(models.Model):
    id_item = models.OneToOneField(CadTbCIte, models.DO_NOTHING, db_column='id_item', primary_key=True)  # The composite primary key (id_item, id_empresa, id_cor, id_tamanho) found, that is not supported. The first column is selected.
    id_empresa = models.ForeignKey(CadTbCPar, models.DO_NOTHING, db_column='id_empresa')
    id_cor = models.IntegerField()
    id_tamanho = models.IntegerField()
    data_ult_movimento = models.DateField(blank=True, null=True)
    data_ult_inventario = models.DateField(blank=True, null=True)
    qtde_entrada = models.FloatField(blank=True, null=True)
    qtde_saida = models.FloatField(blank=True, null=True)
    saldo_fisico = models.FloatField(blank=True, null=True)
    qtde_ped_compra = models.FloatField(blank=True, null=True)
    qtde_ped_venda = models.FloatField(blank=True, null=True)
    vlr_custo_medio = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_custo_ult_compra = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    data_ult_compra = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'est_tb_m_fes'
        unique_together = (('id_item', 'id_empresa', 'id_cor', 'id_tamanho'),)
        db_table_comment = 'Ficha de estque sintetica.'


class EstTbMFesAlm(models.Model):
    id_item = models.OneToOneField(EstTbMFes, models.DO_NOTHING, db_column='id_item', primary_key=True)  # The composite primary key (id_item, id_empresa, id_cor, id_tamanho, id_almoxarifado) found, that is not supported. The first column is selected.
    id_empresa = models.IntegerField()
    id_cor = models.IntegerField()
    id_tamanho = models.IntegerField()
    id_almoxarifado = models.ForeignKey(CadTbCAlm, models.DO_NOTHING, db_column='id_almoxarifado')
    data_ult_movimento = models.DateField(blank=True, null=True)
    data_ult_inventario = models.DateField(blank=True, null=True)
    qtde_entrada = models.FloatField()
    qtde_saida = models.FloatField()
    saldo_fisico = models.FloatField()

    class Meta:
        managed = False
        db_table = 'est_tb_m_fes_alm'
        unique_together = (('id_item', 'id_empresa', 'id_cor', 'id_tamanho', 'id_almoxarifado'),)
        db_table_comment = 'Ficha de estque sintetica por almoxarifado.'


class EstTbMInv(models.Model):
    dta_inventario = models.DateField(primary_key=True)  # The composite primary key (dta_inventario, id_item, id_empresa, id_cor, id_tamanho) found, that is not supported. The first column is selected.
    id_item = models.ForeignKey(CadTbCIte, models.DO_NOTHING, db_column='id_item')
    id_empresa = models.ForeignKey(CadTbCPar, models.DO_NOTHING, db_column='id_empresa')
    qtde = models.FloatField()
    custo = models.DecimalField(max_digits=18, decimal_places=4)
    id_cor = models.IntegerField()
    id_tamanho = models.IntegerField()
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'est_tb_m_inv'
        unique_together = (('dta_inventario', 'id_item', 'id_empresa', 'id_cor', 'id_tamanho'),)
        db_table_comment = 'Inventario de estqoue'


class EstTbMLot(models.Model):
    id_item = models.IntegerField()
    num_lote = models.CharField(primary_key=True, max_length=15)  # The composite primary key (num_lote, id_item, id_almoxarifado, id_cor, id_tamanho) found, that is not supported. The first column is selected.
    id_empresa = models.IntegerField()
    id_almoxarifado = models.IntegerField()
    qtde_entrada = models.FloatField()
    qtde_saida = models.FloatField()
    qtde_atual = models.FloatField()
    id_fiscal = models.IntegerField()
    id_controle = models.IntegerField(db_comment='Este campo armazena o numero da contagem!')
    id_cor = models.IntegerField()
    id_tamanho = models.IntegerField()
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    dta_vencimento = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'est_tb_m_lot'
        unique_together = (('num_lote', 'id_item', 'id_almoxarifado', 'id_cor', 'id_tamanho'),)
        db_table_comment = 'Tabela de Controle de Lote - PCP\nCONTROLE DE INSUMOS POR LOTE, ESTE TABELA SERA USADA NA ENTRADA E NA SAIDA DO ALMOXARIFADO.'


class EstTbMMal(models.Model):
    id_mal = models.IntegerField(primary_key=True)
    id_empresa = models.ForeignKey(CadTbCPar, models.DO_NOTHING, db_column='id_empresa')
    data = models.DateField()
    id_almoxarifado = models.ForeignKey(CadTbCAlm, models.DO_NOTHING, db_column='id_almoxarifado', blank=True, null=True)
    id_tipo_mov_estoque = models.ForeignKey(CadTbCTme, models.DO_NOTHING, db_column='id_tipo_mov_estoque')
    id_setor = models.ForeignKey(CadTbCSet, models.DO_NOTHING, db_column='id_setor')
    id_responsavel = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_responsavel')
    observacao = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.IntegerField(blank=True, null=True)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    id_almoxarifado_dest = models.IntegerField(blank=True, null=True)
    id_opr = models.ForeignKey('PcpTbMOprReq', models.DO_NOTHING, db_column='id_opr', blank=True, null=True)
    id_opr_req = models.IntegerField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)
    id_ccusto = models.ForeignKey(CadTbCCcu, models.DO_NOTHING, db_column='id_ccusto', blank=True, null=True)
    id_equipamento = models.IntegerField(blank=True, null=True)
    km_atual = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'est_tb_m_mal'
        db_table_comment = 'Movimento de Almoxarifado'


class EstTbMMalIte(models.Model):
    id_mal = models.OneToOneField(EstTbMMal, models.DO_NOTHING, db_column='id_mal', primary_key=True)  # The composite primary key (id_mal, id_sequencia, id_item) found, that is not supported. The first column is selected.
    id_sequencia = models.IntegerField()
    id_item = models.ForeignKey(CadTbCIte, models.DO_NOTHING, db_column='id_item')
    qtde = models.FloatField()
    num_lote = models.CharField(max_length=15, blank=True, null=True)
    observacao = models.CharField(max_length=100, blank=True, null=True)
    id_cor = models.IntegerField(blank=True, null=True)
    id_tamanho = models.IntegerField(blank=True, null=True)
    id_busca_item = models.CharField(max_length=30, blank=True, null=True)
    id_opr = models.IntegerField(blank=True, null=True)
    id_opr_req = models.IntegerField(blank=True, null=True)
    id_opr_req_ite = models.IntegerField(blank=True, null=True)
    vlr_unitario = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_total = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'est_tb_m_mal_ite'
        unique_together = (('id_mal', 'id_sequencia', 'id_item'),)
        db_table_comment = 'Movimento de Almoxarifado - Itens'


class EstTbMMet(models.Model):
    id_met = models.IntegerField(primary_key=True)
    id_empresa = models.ForeignKey(CadTbCPar, models.DO_NOTHING, db_column='id_empresa')
    data = models.DateField()
    id_tipo_mov_estoque = models.ForeignKey(CadTbCTme, models.DO_NOTHING, db_column='id_tipo_mov_estoque')
    id_responsavel = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_responsavel')
    observacao = models.CharField(max_length=100, blank=True, null=True)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'est_tb_m_met'


class EstTbMMetIte(models.Model):
    id_met = models.OneToOneField(EstTbMMet, models.DO_NOTHING, db_column='id_met', primary_key=True)  # The composite primary key (id_met, id_sequencia, id_item) found, that is not supported. The first column is selected.
    id_sequencia = models.IntegerField()
    id_item = models.ForeignKey(CadTbCIte, models.DO_NOTHING, db_column='id_item')
    qtde = models.FloatField()
    observacao = models.CharField(max_length=100, blank=True, null=True)
    id_cor = models.IntegerField(blank=True, null=True)
    id_tamanho = models.IntegerField(blank=True, null=True)
    id_busca_item = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'est_tb_m_met_ite'
        unique_together = (('id_met', 'id_sequencia', 'id_item'),)


class FatTbMEtg(models.Model):
    id_entrega = models.IntegerField(primary_key=True)
    id_pedido = models.IntegerField()
    id_forma_pag = models.IntegerField()
    vlr_pagamento = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    mob_id_entrega = models.IntegerField(blank=True, null=True)
    id_empresa = models.IntegerField(blank=True, null=True)
    id_motorista = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fat_tb_m_etg'


class FatTbMEtgDev(models.Model):
    id_entrega = models.OneToOneField(FatTbMEtg, models.DO_NOTHING, db_column='id_entrega', primary_key=True)  # The composite primary key (id_entrega, id_sequencia) found, that is not supported. The first column is selected.
    id_sequencia = models.IntegerField()
    id_item = models.ForeignKey(CadTbCIte, models.DO_NOTHING, db_column='id_item', blank=True, null=True)
    qtde = models.FloatField(blank=True, null=True)
    motivo = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fat_tb_m_etg_dev'
        unique_together = (('id_entrega', 'id_sequencia'),)


class FatTbMEtgFot(models.Model):
    id_entrega = models.OneToOneField(FatTbMEtg, models.DO_NOTHING, db_column='id_entrega', primary_key=True)  # The composite primary key (id_entrega, id_sequencia) found, that is not supported. The first column is selected.
    caminho_foto = models.CharField(max_length=255)
    id_sequencia = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fat_tb_m_etg_fot'
        unique_together = (('id_entrega', 'id_sequencia'),)


class FatTbMIqm(models.Model):
    id_iqm = models.IntegerField(primary_key=True)
    id_empresa = models.IntegerField(blank=True, null=True)
    id_emitente = models.IntegerField(blank=True, null=True)
    dta_recebimento = models.DateField(blank=True, null=True)
    dta_emissao_nf = models.DateField(blank=True, null=True)
    numero_nf = models.IntegerField(blank=True, null=True)
    serie = models.CharField(max_length=3, blank=True, null=True)
    sub_serie = models.CharField(max_length=3, blank=True, null=True)
    id_pedido_compra = models.IntegerField(blank=True, null=True)
    situacao = models.IntegerField(blank=True, null=True, db_comment='0 - em espera  1 - importado')

    class Meta:
        managed = False
        db_table = 'fat_tb_m_iqm'


class FatTbMIqmIte(models.Model):
    id_sequencia = models.IntegerField()
    id_item = models.ForeignKey(CadTbCIte, models.DO_NOTHING, db_column='id_item')
    nro_lote_fabric_produto = models.CharField(max_length=20, blank=True, null=True, db_comment='Essse nro de lote , serß o nro que vem no laudo.')
    num_lote = models.CharField(max_length=15, blank=True, null=True, db_comment='Esse nro de lote interno Ú igual ao que vem na nota fiscal.')
    cert_data = models.DateField(blank=True, null=True)
    cert_numero = models.CharField(max_length=20, blank=True, null=True)
    id_responsavel = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_responsavel', blank=True, null=True)
    cnd_comercial = models.IntegerField(blank=True, null=True, db_comment='0 - Reprovado\n1 - Aprovado')
    qtd_pc_nf = models.IntegerField(blank=True, null=True, db_comment='Verifica se a quantidade do pedido de compra corresponde a nota fiscal de entrada.\n0 - Reprovado\n1 - Aprovado')
    pres_produto = models.IntegerField(blank=True, null=True, db_comment='PreservaþÒo do produto.\n0 - Reprovado\n1 - Aprovado')
    cert_qualidade = models.IntegerField(blank=True, null=True)
    resultado = models.IntegerField(blank=True, null=True, db_comment='Caso algum campo da parte do recebimento receber "Reprovado", automaticamente este campo ficarß\ncom valor Reprovado.\n0 - Reprovado\n1 - Aprovado')
    demerito = models.IntegerField(blank=True, null=True)
    origem = models.CharField(max_length=200, blank=True, null=True, db_comment='O usußrio irß informar o motivo do problema (NÒo conformidade ).')
    qtd_nc = models.FloatField(blank=True, null=True)
    per_lot_rec = models.FloatField(blank=True, null=True)
    situacao = models.CharField(max_length=800, blank=True, null=True)
    disposicao = models.IntegerField(blank=True, null=True)
    apro_gerente = models.IntegerField(blank=True, null=True, db_comment='Refere-se a tabela de funcionßrios.')
    apro_data = models.DateField(blank=True, null=True)
    exec_por = models.IntegerField(blank=True, null=True, db_comment='Refere-se a tabela de funcionßrios.')
    dta_finalisado = models.DateField(blank=True, null=True)
    plano_acao_forn = models.BooleanField(blank=True, null=True, db_comment='0 - NÒo\n1 - Sim')
    comentarios = models.CharField(max_length=400, blank=True, null=True)
    qualidade = models.IntegerField(blank=True, null=True, db_comment='0 - Reprovado\n1 - Aprovado')
    dta_inspecao = models.DateField(blank=True, null=True)
    especificado = models.CharField(max_length=300, blank=True, null=True)
    encontrado = models.CharField(max_length=300, blank=True, null=True)
    numero_laudo = models.CharField(max_length=30, blank=True, null=True)
    data_certif_qualidade = models.DateField(blank=True, null=True, db_comment='Refere-se ao campo "Data de certificado de qualidade".')
    id_cor = models.IntegerField(blank=True, null=True)
    id_tamanho = models.IntegerField(blank=True, null=True)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    id_iqm = models.OneToOneField(FatTbMIqm, models.DO_NOTHING, db_column='id_iqm', primary_key=True)  # The composite primary key (id_iqm, id_sequencia) found, that is not supported. The first column is selected.
    qtde = models.FloatField(blank=True, null=True)
    id_sequencia_ite_cmp_ped = models.IntegerField(blank=True, null=True)
    id_busca_item = models.CharField(max_length=30, blank=True, null=True)
    observacao = models.CharField(max_length=100, blank=True, null=True)
    manual_tam_letras = models.IntegerField(blank=True, null=True, db_comment='0 - Reprovado\n 1 - Aprovado')
    manual_simb_conserv = models.IntegerField(blank=True, null=True, db_comment='0 - Reprovado\n 1 - Aprovado')
    manual_inform_cadast_cont = models.IntegerField(blank=True, null=True, db_comment='0 - Reprovado\n 1 - Aprovado')
    manual_cobert_garant_e_perda = models.IntegerField(blank=True, null=True, db_comment='0 - Reprovado\n 1 - Aprovado')
    manual_tabela_garantia_biotipo = models.IntegerField(blank=True, null=True, db_comment='0 - Reprovado\n 1 - Aprovado')
    manual_aviso_colchao_baby = models.IntegerField(blank=True, null=True, db_comment='0 - Reprovado\n 1 - Aprovado')
    manual_desenho_esquem_colch = models.IntegerField(blank=True, null=True, db_comment='0 - Reprovado\n 1 - Aprovado')
    manual_aviso_asfixia = models.IntegerField(blank=True, null=True, db_comment='0 - Reprovado\n 1 - Aprovado')

    class Meta:
        managed = False
        db_table = 'fat_tb_m_iqm_ite'
        unique_together = (('id_iqm', 'id_sequencia'),)
        db_table_comment = 'Controle de Recebimento e InsepeþÒo de QuÝmicos'


class FatTbMIqmIteAna(models.Model):
    id_iqm = models.OneToOneField(FatTbMIqmIte, models.DO_NOTHING, db_column='id_iqm', primary_key=True)  # The composite primary key (id_iqm, id_sequencia) found, that is not supported. The first column is selected.
    id_sequencia = models.IntegerField()
    id_item = models.ForeignKey(CadTbCIte, models.DO_NOTHING, db_column='id_item')
    num_plano_acao = models.IntegerField()
    dta_emissao = models.DateField()
    especificado = models.CharField(max_length=300, blank=True, null=True)
    encontrado = models.CharField(max_length=300, blank=True, null=True)
    observacao = models.CharField(max_length=300, blank=True, null=True)
    qtde_nc = models.FloatField(db_comment='Este campo deve ter o mesmo conte·do do campo qtde_nc do produto da tabela EST_TB_M_NFE_S.')
    qtde_total = models.FloatField(db_comment='Este campo terß o mesmo valor do campo qtde do produto da tabela EST_TB_M_NFE_I.')
    perc_nc = models.FloatField(db_comment='Este campo terß o mesmo valor do campo QTDE_NC da tabela FAT_TB_M_NFE_ITE_IQM')
    qtde_devolvida = models.FloatField(db_comment='Este campo, o pr¾prio usußrio irß alimentar e seu valor nunca poderß ser maior que o campo QTDE_TOTAL.')
    id_responsavel = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_responsavel')
    id_setor = models.ForeignKey(CadTbCSet, models.DO_NOTHING, db_column='id_setor')
    causa_do_problema_forn = models.CharField(max_length=300, blank=True, null=True)
    resolucao_problema_forn = models.CharField(max_length=300, blank=True, null=True)
    responsavel_forn = models.CharField(max_length=80, blank=True, null=True)
    cargo_resp_forn = models.CharField(max_length=60, blank=True, null=True)
    data_inf_forn = models.DateField(blank=True, null=True)
    acao_tomada_analise = models.IntegerField(blank=True, null=True, db_comment='A aþÒo tomada pelo fornecedor\nfoi considera?\n\n0 - NÒo\n1 - Sim')
    nao_conform_analise = models.IntegerField(blank=True, null=True, db_comment='A nÒo conformidade Ú reincidente?\n0 - NÒo\n1 - Sim')
    requer_nova_acao_analise = models.IntegerField(blank=True, null=True, db_comment='Requer nova aþÒo?\n0 - NÒo\n1 - Sim')
    comentarios_analise = models.CharField(max_length=300, blank=True, null=True)
    id_resp_analise = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_resp_analise', related_name='fattbmiqmiteana_id_resp_analise_set', blank=True, null=True)
    data_analise = models.DateField(blank=True, null=True)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    situacao_analise = models.IntegerField(blank=True, null=True, db_comment='0-ABERTO\n1-FECHADO')
    id_for_rp = models.IntegerField(blank=True, null=True, db_comment='Este campo busca os representantes do fornecedor que estß informado no IQM.')

    class Meta:
        managed = False
        db_table = 'fat_tb_m_iqm_ite_ana'
        unique_together = (('id_iqm', 'id_sequencia'),)
        db_table_comment = 'Plano de aþÒo do Fornecedor'


class FatTbMMkt(models.Model):
    id_mkt = models.IntegerField(primary_key=True)
    dta_criacao = models.DateField()
    hor_criacao = models.TimeField()
    id_responsavel = models.IntegerField()
    id_rota = models.IntegerField(blank=True, null=True)
    id_empresa = models.IntegerField()
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    id_vis = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fat_tb_m_mkt'
        db_table_comment = 'Tabela de Marketing'


class FatTbMMktCli(models.Model):
    id_mkt = models.OneToOneField(FatTbMMkt, models.DO_NOTHING, db_column='id_mkt', primary_key=True)  # The composite primary key (id_mkt, id_cliente) found, that is not supported. The first column is selected.
    id_cliente = models.ForeignKey(CadTbCCli, models.DO_NOTHING, db_column='id_cliente')
    dta_gravacao = models.DateField(blank=True, null=True)
    hor_gravacao = models.TimeField(blank=True, null=True)
    obs = models.CharField(max_length=300, blank=True, null=True)
    selecao = models.BooleanField(blank=True, null=True)
    id_banco_info = models.IntegerField(blank=True, null=True)
    cliente_contato = models.BooleanField(blank=True, null=True, db_comment='Indica se o cliente entrou em contato com telemarking')
    cliente_avulso = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fat_tb_m_mkt_cli'
        unique_together = (('id_mkt', 'id_cliente'),)
        db_table_comment = 'Tabela de Clientes do Marketing'


class FatTbMMktPed(models.Model):
    id_mkt = models.OneToOneField(FatTbMMkt, models.DO_NOTHING, db_column='id_mkt', primary_key=True)  # The composite primary key (id_mkt, id_pedido) found, that is not supported. The first column is selected.
    id_pedido = models.ForeignKey('FatTbMPed', models.DO_NOTHING, db_column='id_pedido')
    dta_gravacao = models.DateField()
    hor_gravacao = models.TimeField()

    class Meta:
        managed = False
        db_table = 'fat_tb_m_mkt_ped'
        unique_together = (('id_mkt', 'id_pedido'),)
        db_table_comment = 'Tabela Pedidos do Marketing'


class FatTbMNfe(models.Model):
    id_fiscal = models.IntegerField(primary_key=True)
    id_almoxarifado = models.ForeignKey(CadTbCAlm, models.DO_NOTHING, db_column='id_almoxarifado', blank=True, null=True)
    id_pedido_compra = models.IntegerField(blank=True, null=True)
    id_condicao_pag = models.ForeignKey(CadTbCCpg, models.DO_NOTHING, db_column='id_condicao_pag')
    id_empresa = models.ForeignKey(CadTbCPar, models.DO_NOTHING, db_column='id_empresa')
    id_emitente = models.IntegerField()
    id_cfo = models.ForeignKey(CadTbCCfo, models.DO_NOTHING, db_column='id_cfo')
    id_transportadora = models.IntegerField(blank=True, null=True)
    id_vendedor = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_vendedor', blank=True, null=True)
    id_tipo_mov_estoque = models.ForeignKey(CadTbCTme, models.DO_NOTHING, db_column='id_tipo_mov_estoque', blank=True, null=True)
    uf_emitente = models.CharField(max_length=2, blank=True, null=True)
    uf_empresa = models.CharField(max_length=2, blank=True, null=True)
    dta_emissao = models.DateField()
    dta_documento = models.DateField()
    cpf_cnpj = models.CharField(max_length=14, blank=True, null=True)
    numero = models.IntegerField()
    serie = models.CharField(max_length=3)
    sub_serie = models.CharField(max_length=3)
    modelo = models.CharField(max_length=2)
    status = models.IntegerField()
    nfe_ecf = models.IntegerField(db_comment='0-NFE; \r\n1-ECF; 2-NFCe; 3-NFSe')
    ecf_prevenda = models.IntegerField(blank=True, null=True)
    id_fiscal_referenciado = models.IntegerField(blank=True, null=True)
    canc_motivo = models.CharField(max_length=100, blank=True, null=True)
    canc_data = models.DateField(blank=True, null=True)
    peso_liquido = models.FloatField(blank=True, null=True)
    peso_bruto = models.FloatField(blank=True, null=True)
    nfe_chave = models.CharField(max_length=44)
    nfe_obs = models.CharField(max_length=800, blank=True, null=True)
    nfe_protocolo = models.CharField(max_length=50, blank=True, null=True)
    nfe_recibo = models.CharField(max_length=50, blank=True, null=True)
    nfe_canc_protocolo = models.CharField(max_length=50, blank=True, null=True)
    nfe_canc_status = models.CharField(max_length=50, blank=True, null=True)
    nfe_tipo_emissao = models.CharField(max_length=1, blank=True, null=True)
    nfe_tipo_ambiente = models.CharField(max_length=1, blank=True, null=True)
    nfe_finalidade = models.IntegerField(blank=True, null=True, db_comment='0-Normal, \n1-Complementar, \n2-Ajuste, \n3-Devolucao')
    nfe_cod_sit = models.CharField(max_length=2, blank=True, null=True)
    ind_operacao = models.IntegerField(db_comment='0-Entrada,\n1-Saida')
    ind_emitente = models.IntegerField()
    ind_frete = models.IntegerField()
    vlr_mercadoria = models.DecimalField(max_digits=18, decimal_places=4)
    vlr_desconto = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_acrescimo = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_liquido = models.DecimalField(max_digits=18, decimal_places=4)
    icm_n_valor = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    icm_n_base = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    icm_s_valor = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    icm_s_base = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    ipi_base = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    ipi_valor = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    iss_base = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    iss_valor = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    fre_base = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    fre_valor = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    pis_valor = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    pis_valor_st = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    cof_valor = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    cof_valor_st = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_isenta = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_outras = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_seguro = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    tipo_nf = models.CharField(max_length=1, blank=True, null=True)
    ecf_serial_impressora = models.CharField(max_length=60, blank=True, null=True)
    ecf_marca_impressora = models.CharField(max_length=50, blank=True, null=True)
    ecf_modelo_impressora = models.CharField(max_length=50, blank=True, null=True)
    ecf_caixa = models.CharField(max_length=3, blank=True, null=True)
    dta_movimento = models.DateField()
    origem_nf = models.CharField(max_length=1, blank=True, null=True, db_comment='A- Pedido de Venda  B- Estoque  C- Oficina  X- ImportaþÒo XML   G- Gerada de cupom fiscal ;  D - Gerado partindo do Cupom GerConWin')
    faturada = models.BooleanField()
    situacao_inspecao = models.IntegerField(blank=True, null=True)
    id_fiscal_frete = models.IntegerField(blank=True, null=True)
    id_pedido_venda = models.IntegerField(blank=True, null=True)
    vlr_outras_desp = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    fre_custo = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_icm_ser_nao_incide = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    cof_base = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    pis_base = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    posvenda = models.BooleanField()
    id_responsavel = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_responsavel', related_name='fattbmnfe_id_responsavel_set', blank=True, null=True)
    tipo_cte = models.IntegerField(blank=True, null=True)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    path_xml = models.CharField(max_length=200, blank=True, null=True)
    nfref_chave = models.CharField(max_length=44, blank=True, null=True)
    imp_valor = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    tri_valor = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    tra_placa = models.CharField(max_length=8, blank=True, null=True)
    tra_uf = models.CharField(max_length=2, blank=True, null=True)
    tra_rntc = models.CharField(max_length=10, blank=True, null=True)
    tra_qtde_vol = models.FloatField(blank=True, null=True)
    tra_especie = models.CharField(max_length=30, blank=True, null=True)
    tra_marca = models.CharField(max_length=30, blank=True, null=True)
    tra_num_vol = models.CharField(max_length=10, blank=True, null=True)
    id_iqm = models.IntegerField(blank=True, null=True)
    id_abertura = models.IntegerField(blank=True, null=True, db_comment='Campo utitlizado pela tela de faturamento, no momento do caixa(usußrio) Gerar NFe.')
    legenda = models.CharField(max_length=20, blank=True, null=True, db_comment='Este campo Ú utilizado pela tela de Controle de Caixa(faturamento), para especificar a situaþÒo da NF do grid de Notas Fiscal atravÚs de cores.')
    prevenda = models.BooleanField(blank=True, null=True, db_comment='Este campo indicar que essa nota fiscal serß um cupom fical no GerconWin.')
    id_ordem = models.IntegerField(blank=True, null=True, db_comment='Campo referente ao ID_ORDEM  da tabela OFI_TB_M_ORV.')
    venctos_origem = models.CharField(max_length=400, blank=True, null=True, db_comment='Este campo poderß ser utilizado no momento do Cupom Fiscal na tela de Controle de Caixa caso a forma de pagamento no GerConWin seja alterado.')
    canc_usuario = models.IntegerField(blank=True, null=True)
    nro_termo = models.IntegerField(blank=True, null=True, db_comment='Neste campo serß armazenado o nro do Termo impresso pela tela de Controle de Caixa atravÚs do botÒo GerarNfe.')
    ind_nf = models.IntegerField(blank=True, null=True, db_comment='Este campo informa que a Nota Fiscal Ú:\n1 - Nota somente de itens;\n2 - Nota somente de Serviþo;\n3 - Nota com Itens e Serviþos;\n')
    vlr_part_dest = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    vlr_part_orig = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    vlr_icm_desc = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True, db_comment='Desconto de ICMS.\r\n')
    id_ors = models.IntegerField(blank=True, null=True, db_comment='Campo utilizado pelo PCP_FM_M_ORS; (Ordem de Faturamento);')
    vlr_fcp = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    di_estrangeiro = models.CharField(max_length=20, blank=True, null=True)
    id_ccusto = models.IntegerField(blank=True, null=True)
    id_fiscal_ref_comp = models.IntegerField(blank=True, null=True, db_comment='Utilizado para armazenar id_fiscal da nota original a ser complementada')
    dis_icm_dispensado = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    id_ordem_gar = models.IntegerField(blank=True, null=True)
    id_seq_fat_gar = models.IntegerField(blank=True, null=True)
    ped_mod_frete = models.IntegerField(blank=True, null=True, db_comment='0 - Nenhum; 1 - CIF; 2 - FOB ')
    ped_vlr_frete = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    num_rps = models.IntegerField(blank=True, null=True)
    iss_valor_retido = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    qtde_volume = models.FloatField(blank=True, null=True)
    vlr_fcp_ope_int = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True, db_comment='Criado devido a nota Nota tÚcnica: NT_2016_002_v1.42 - Fundo de combate a pobreza para operaþ§es internas ou interestaduais com substituiþÒo tributßria')
    vlr_fcp_st_ope_int = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True, db_comment='Criado devido a nota Nota tÚcnica: NT_2016_002_v1.42 - Fundo de combate a pobreza para operaþ§es internas ou interestaduais com substituiþÒo tributßria')
    vlr_fcp_st_ret_ope_int = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True, db_comment='Criado devido a nota Nota tÚcnica: NT_2016_002_v1.42 - Fundo de combate a pobreza para operaþ§es internas ou interestaduais com substituiþÒo tributßria')
    id_pedido_prod_1 = models.IntegerField(blank=True, null=True, db_comment='Esse campo serß utilizado pela empresa tenha o modulo SGQ = true e o ParÔmetro Atualiza vencimentos no pedido de outra base for igual a True.')
    vlr_liquido_ped_prod_1 = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    id_pedido_prod_2 = models.IntegerField(blank=True, null=True, db_comment='Esse campo serß utilizado pela empresa tenha o modulo SGQ = true e o ParÔmetro Atualiza vencimentos no pedido de outra base for igual a True.')
    vlr_liquido_ped_prod_2 = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    id_pedido_prod_3 = models.IntegerField(blank=True, null=True, db_comment='Esse campo serß utilizado pela empresa tenha o modulo SGQ = true e o ParÔmetro Atualiza vencimentos no pedido de outra base for igual a True.')
    vlr_liquido_ped_prod_3 = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    id_pedido_prod_4 = models.IntegerField(blank=True, null=True, db_comment='Esse campo serß utilizado pela empresa tenha o modulo SGQ = true e o ParÔmetro Atualiza vencimentos no pedido de outra base for igual a True.')
    vlr_liquido_ped_prod_4 = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    id_pedido_prod_5 = models.IntegerField(blank=True, null=True, db_comment='Esse campo serß utilizado pela empresa tenha o modulo SGQ = true e o ParÔmetro Atualiza vencimentos no pedido de outra base for igual a True.')
    vlr_liquido_ped_prod_5 = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fat_tb_m_nfe'


class FatTbMNfeArq(models.Model):
    id_fiscal = models.OneToOneField(FatTbMNfe, models.DO_NOTHING, db_column='id_fiscal', primary_key=True)
    arq_xml = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fat_tb_m_nfe_arq'
        db_table_comment = 'Tabela que guarda arquivo XML das notas fiscais.'


class FatTbMNfeDev(models.Model):
    id_fiscal = models.OneToOneField(FatTbMNfe, models.DO_NOTHING, db_column='id_fiscal', primary_key=True)  # The composite primary key (id_fiscal, id_fiscal_dev) found, that is not supported. The first column is selected.
    id_fiscal_dev = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fat_tb_m_nfe_dev'
        unique_together = (('id_fiscal', 'id_fiscal_dev'),)


class FatTbMNfeDevIte(models.Model):
    id_fiscal = models.OneToOneField(FatTbMNfeDev, models.DO_NOTHING, db_column='id_fiscal', primary_key=True)  # The composite primary key (id_fiscal, id_fiscal_dev, id_sequencia) found, that is not supported. The first column is selected.
    id_item = models.IntegerField()
    qtde = models.FloatField()
    id_cor = models.IntegerField(blank=True, null=True)
    id_tamanho = models.IntegerField(blank=True, null=True)
    id_fiscal_dev = models.IntegerField()
    id_sequencia = models.IntegerField()
    qtde_sld_orig = models.FloatField(blank=True, null=True, db_comment='Neste campo ficarß o saldo da qtde do Item da Nota Fiscal de Origem.')
    id_st_icm = models.CharField(max_length=3, blank=True, null=True)
    origem_mercadoria = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fat_tb_m_nfe_dev_ite'
        unique_together = (('id_fiscal', 'id_fiscal_dev', 'id_sequencia'),)


class FatTbMNfeIte(models.Model):
    id_fiscal = models.OneToOneField(FatTbMNfe, models.DO_NOTHING, db_column='id_fiscal', primary_key=True)  # The composite primary key (id_fiscal, id_sequencia, id_fiscal_dev) found, that is not supported. The first column is selected.
    id_sequencia = models.IntegerField()
    id_item = models.ForeignKey(CadTbCIte, models.DO_NOTHING, db_column='id_item')
    id_inf_fisco = models.IntegerField(blank=True, null=True)
    id_cfo = models.ForeignKey(CadTbCCfo, models.DO_NOTHING, db_column='id_cfo')
    id_st_pis = models.CharField(max_length=2, blank=True, null=True)
    id_st_cof = models.CharField(max_length=2, blank=True, null=True)
    id_st_ipi = models.CharField(max_length=2, blank=True, null=True)
    id_st_icm = models.CharField(max_length=3, blank=True, null=True)
    qtde = models.FloatField()
    qtde_devolvida = models.FloatField(blank=True, null=True)
    vlr_unitario = models.DecimalField(max_digits=18, decimal_places=6)
    vlr_mercadoria = models.DecimalField(max_digits=18, decimal_places=4)
    per_desconto = models.FloatField(blank=True, null=True)
    vlr_desconto = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_custo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    vlr_liquido = models.DecimalField(max_digits=18, decimal_places=4)
    vlr_outras = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_isenta = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    vlr_seguro = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    icm_n_aliquota = models.FloatField(blank=True, null=True)
    icm_per_reducao = models.FloatField(blank=True, null=True)
    icm_n_base = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    icm_n_valor = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    icm_s_base = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    icm_s_valor = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    ipi_base = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    ipi_aliquota = models.FloatField(blank=True, null=True)
    ipi_valor = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    iss_base = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    iss_aliquota = models.FloatField(blank=True, null=True)
    iss_valor = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    fre_base = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    fre_percentual = models.FloatField(blank=True, null=True)
    fre_valor = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    pis_base = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    pis_aliquota = models.FloatField(blank=True, null=True)
    pis_valor = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    cof_base = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    cof_aliquota = models.FloatField(blank=True, null=True)
    cof_valor = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    peso_liquido = models.FloatField(blank=True, null=True)
    peso_bruto = models.FloatField(blank=True, null=True)
    nro_pedido = models.IntegerField(blank=True, null=True)
    cof_valor_st = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    imp_valor = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_icm_ser_nao_incide = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_outras_desp = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    num_lote = models.CharField(max_length=15, blank=True, null=True)
    pis_valor_st = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    icm_n_dif_aliq = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    icm_n_vlr_dif_aliq = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    para_analise_raa = models.IntegerField(blank=True, null=True, db_comment='0 - Falso\n1 - Verdadeiro')
    fre_dif_aliq_icm = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    fre_vlr_dif_icm = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    fre_custo = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    origem_mercadoria = models.CharField(max_length=1)
    icm_s_per_mva = models.FloatField(blank=True, null=True)
    id_cor = models.IntegerField(blank=True, null=True)
    id_tamanho = models.IntegerField(blank=True, null=True)
    id_busca_item = models.CharField(max_length=30, blank=True, null=True)
    id_tributo = models.IntegerField(blank=True, null=True)
    tri_valor = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    tri_indice = models.FloatField(blank=True, null=True)
    icm_s_vlr_mva = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    id_sequencia_ite_cmp_ped = models.IntegerField(blank=True, null=True)
    imp_base_calculo = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    imp_desp_aduana = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    imp_iof = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    di_numero = models.IntegerField(blank=True, null=True)
    di_data = models.DateField(blank=True, null=True)
    di_local_desemb = models.CharField(max_length=60, blank=True, null=True)
    di_uf_desemb = models.CharField(max_length=2, blank=True, null=True)
    di_data_desemb = models.DateField(blank=True, null=True)
    di_exportador = models.CharField(max_length=60, blank=True, null=True)
    di_numero_adicao = models.IntegerField(blank=True, null=True)
    di_seq_adicao = models.IntegerField(blank=True, null=True)
    di_fabricante = models.CharField(max_length=60, blank=True, null=True)
    di_vlr_desconto = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    di_fci = models.CharField(max_length=36, blank=True, null=True)
    id_sequencia_ite_iqm = models.IntegerField(blank=True, null=True)
    id_sequencia_ite_xml = models.IntegerField(blank=True, null=True, db_comment='Este campo Ú utilizado pela tela de ImportaþÒo do XML. Corresponde ao campo "Prod.nItem";')
    vlr_acrescimo = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_unitario_orig = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True, db_comment='Este campo irß armazenar o preþo original (Que Ú calculado pelo sistema).  Assim o sistema saberß se o usußrio alterou o preþo no pedido ao verificar VLR_UNITARIO vs VLR_UNITARIO_ORIG')
    vlr_part_dest = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    vlr_part_orig = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    vlr_icm_desc = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True, db_comment='Desconto de ICMS.')
    part_per_aliq_dest = models.FloatField(blank=True, null=True)
    part_per_part_orig = models.FloatField(blank=True, null=True)
    part_per_part_dest = models.FloatField(blank=True, null=True)
    vlr_fcp = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True, db_comment='Fundo de combate a pobreza.')
    per_fcp = models.FloatField(blank=True, null=True)
    part_per_red_int_dest = models.FloatField(blank=True, null=True, db_comment='Guarda o percentual de reduþÒo de alÝquota interna da partilha de destino.')
    fp_vlr_tot_custo_fix_mens = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True, db_comment='Total dos Custos Fixos Mensais')
    fp_vlr_ven_med_mens = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True, db_comment='Vendas mÚdia mensais')
    fp_per_cust_ven_mens = models.FloatField(blank=True, null=True, db_comment='% do Custo Fixo sobre Venda Mensais')
    fp_per_icms_ven = models.FloatField(blank=True, null=True, db_comment='ICMS sobre Vendas')
    fp_per_simples = models.FloatField(blank=True, null=True, db_comment='Simples')
    fp_per_comissao = models.FloatField(blank=True, null=True, db_comment='Comiss§es')
    fp_per_frete_ven = models.FloatField(blank=True, null=True, db_comment='Fretes s/Vendas')
    fp_per_cust_fin_ven = models.FloatField(blank=True, null=True, db_comment='Custo Financeiro sobre Vendas')
    fp_per_lucro_ven = models.FloatField(blank=True, null=True, db_comment='Lucro Desejado sobre Vendas')
    fp_per_total_incid = models.FloatField(blank=True, null=True, db_comment='% Total das IncidÛncias')
    fp_per_markup_div = models.FloatField(blank=True, null=True, db_comment='MarkUp Divisor')
    fp_per_markup_mult = models.FloatField(blank=True, null=True, db_comment='Markup Multiplicador')
    fp_vlr_prc_ven_calc = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True, db_comment='Preþo de Venda Calculado')
    fp_vlr_prc_ven_prat = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True, db_comment='Preþo de Venda a ser Praticado ')
    fp_calculado = models.BooleanField(blank=True, null=True)
    fp_vlr_prc_prz_ven_prat = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    fp_per_prc_prz_ven_prat = models.FloatField(blank=True, null=True)
    id_fiscal_dev = models.IntegerField()
    dre_perc_out_ded_ven = models.FloatField(blank=True, null=True)
    dre_perc_ircs = models.FloatField(blank=True, null=True)
    dta_vencimento = models.DateField(blank=True, null=True)
    di_draw = models.CharField(max_length=11, blank=True, null=True)
    di_tp_viatransp = models.IntegerField(blank=True, null=True)
    di_tp_intermedio = models.IntegerField(blank=True, null=True)
    dis_aliquota = models.FloatField(blank=True, null=True)
    dis_icm_dispensado = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    per_cmv_interno = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    per_cmv_externo = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    per_cmv = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    motivo_icms_des = models.IntegerField(blank=True, null=True)
    iss_valor_retido = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_base_icms_dest = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    qtde_volume = models.FloatField(blank=True, null=True)
    vlr_fcp_base_uf_dest = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True, db_comment='Nota tÚcnica: NT_2016_002_v1.42 - Criado para gravar a informaþÒo da base do fcp no caso ')
    vlr_fcp_ope_int = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True, db_comment='Criado devido a nota Nota tÚcnica: NT_2016_002_v1.42 - Fundo de combate a pobreza para operaþ§es internas ou interestaduais com substituiþÒo tributßria')
    per_fcp_ope_int = models.FloatField(blank=True, null=True, db_comment='Criado devido a nota Nota tÚcnica: NT_2016_002_v1.42 - Fundo de combate a pobreza para operaþ§es internas ou interestaduais com substituiþÒo tributßria')
    vlr_fcp_base_ope_int = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True, db_comment='Criado devido a nota Nota tÚcnica: NT_2016_002_v1.42 - Fundo de combate a pobreza para operaþ§es internas ou interestaduais com substituiþÒo tributßria')
    vlr_fcp_st_ope_int = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True, db_comment='Criado devido a nota Nota tÚcnica: NT_2016_002_v1.42 - Fundo de combate a pobreza para operaþ§es internas ou interestaduais com substituiþÒo tributßria')
    per_fcp_st_ope_int = models.FloatField(blank=True, null=True, db_comment='Criado devido a nota Nota tÚcnica: NT_2016_002_v1.42 - Fundo de combate a pobreza para operaþ§es internas ou interestaduais com substituiþÒo tributßria')
    vlr_fcp_st_base_ope_int = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True, db_comment='Criado devido a nota Nota tÚcnica: NT_2016_002_v1.42 - Fundo de combate a pobreza para operaþ§es internas ou interestaduais com substituiþÒo tributßria')
    per_st_sup_cons_final_ope_int = models.FloatField(blank=True, null=True, db_comment='Criado devido a nota Nota tÚcnica: NT_2016_002_v1.42 - Fundo de combate a pobreza para operaþ§es internas ou interestaduais com substituiþÒo tributßria\r\nAlÝquota suportada pelo Consumidor Final')
    vlr_fcp_st_ret_ope_int = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True, db_comment='Criado devido a nota Nota tÚcnica: NT_2016_002_v1.42 - Fundo de combate a pobreza para operaþ§es internas ou interestaduais com substituiþÒo tributßria')
    per_fcp_st_ret_ope_int = models.FloatField(blank=True, null=True, db_comment='Criado devido a nota Nota tÚcnica: NT_2016_002_v1.42 - Fundo de combate a pobreza para operaþ§es internas ou interestaduais com substituiþÒo tributßria')
    vlr_fcp_st_ret_base_ope_int = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True, db_comment='Criado devido a nota Nota tÚcnica: NT_2016_002_v1.42 - Fundo de combate a pobreza para operaþ§es internas ou interestaduais com substituiþÒo tributßria')
    pcp_obs_item = models.CharField(max_length=200, blank=True, null=True, db_comment='Utilizado quando a empresa utiliza SGQ.')

    class Meta:
        managed = False
        db_table = 'fat_tb_m_nfe_ite'
        unique_together = (('id_fiscal', 'id_sequencia', 'id_fiscal_dev'),)
        db_table_comment = 'Nota Fiscal - Itens'


class FatTbMNfeNff(models.Model):
    id_fiscal = models.OneToOneField(FatTbMNfe, models.DO_NOTHING, db_column='id_fiscal', primary_key=True)  # The composite primary key (id_fiscal, id_fornecedor, nota_frete) found, that is not supported. The first column is selected.
    id_fornecedor = models.IntegerField()
    nota_frete = models.IntegerField()
    vlr_nota = models.DecimalField(max_digits=18, decimal_places=4)
    vlr_frete = models.DecimalField(max_digits=18, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'fat_tb_m_nfe_nff'
        unique_together = (('id_fiscal', 'id_fornecedor', 'nota_frete'),)


class FatTbMNfeTit(models.Model):
    id_fiscal = models.OneToOneField(FatTbMNfe, models.DO_NOTHING, db_column='id_fiscal', primary_key=True)  # The composite primary key (id_fiscal, id_nfe_tit) found, that is not supported. The first column is selected.
    id_nfe_tit = models.IntegerField()
    id_forma_pag = models.ForeignKey(CadTbCFpg, models.DO_NOTHING, db_column='id_forma_pag')
    num_parcela = models.CharField(max_length=15)
    dias = models.IntegerField()
    dta_vencimento = models.DateField()
    vlr_titulo = models.DecimalField(max_digits=18, decimal_places=4)
    id_plano = models.ForeignKey(CadTbCPct, models.DO_NOTHING, db_column='id_plano', blank=True, null=True)
    id_ccusto = models.ForeignKey(CadTbCCcu, models.DO_NOTHING, db_column='id_ccusto', blank=True, null=True)
    che_banco = models.CharField(max_length=10, blank=True, null=True)
    che_agencia = models.CharField(max_length=10, blank=True, null=True)
    che_conta = models.IntegerField(blank=True, null=True)
    che_numero = models.IntegerField(blank=True, null=True)
    che_emitente = models.CharField(max_length=50, blank=True, null=True)
    historico_pag = models.CharField(max_length=100, blank=True, null=True, db_comment='Caso tenha algum texto neste campo , o sistema irß repassar o texto para o campo HISTORICO do tÝtulo do contas a pagar.')
    id_maquineta = models.ForeignKey(CadTbCMct, models.DO_NOTHING, db_column='id_maquineta', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fat_tb_m_nfe_tit'
        unique_together = (('id_fiscal', 'id_nfe_tit'),)
        db_table_comment = 'Nota Fiscal - Titulos'


class FatTbMOrc(models.Model):
    id_orcamento = models.IntegerField(primary_key=True)
    id_empresa = models.IntegerField()
    id_cliente = models.ForeignKey(CadTbCCli, models.DO_NOTHING, db_column='id_cliente')
    dta_orcamento = models.DateField()
    id_funcionario = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_funcionario')
    dta_entrega = models.DateField()
    dta_validade = models.DateField()
    id_forma_pag = models.ForeignKey(CadTbCFpg, models.DO_NOTHING, db_column='id_forma_pag')
    id_condicao_pag = models.ForeignKey(CadTbCCpg, models.DO_NOTHING, db_column='id_condicao_pag')
    obs = models.CharField(max_length=800, blank=True, null=True)
    status = models.IntegerField()
    id_pedido = models.IntegerField()
    vlr_servicos_bru = models.DecimalField(max_digits=18, decimal_places=4)
    vlr_produtos_bru = models.DecimalField(max_digits=18, decimal_places=4)
    vlr_desconto_pro = models.DecimalField(max_digits=18, decimal_places=4)
    vlr_desconto_ser = models.DecimalField(max_digits=18, decimal_places=4)
    vlr_servicos_liq = models.DecimalField(max_digits=18, decimal_places=4)
    vlr_produtos_liq = models.DecimalField(max_digits=18, decimal_places=4)
    vlr_total = models.DecimalField(max_digits=18, decimal_places=4)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    vlr_bruto = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_desc_basico = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    per_desc_basico = models.FloatField(blank=True, null=True)
    vlr_desc_especial = models.DecimalField(max_digits=53, decimal_places=0, blank=True, null=True)
    per_desc_especial = models.FloatField(blank=True, null=True)
    vlr_desconto = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    per_desconto = models.FloatField(blank=True, null=True)
    vlr_liquido = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_frete = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    separa_prod_serv = models.BooleanField(blank=True, null=True)
    vlr_icm_desn = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fat_tb_m_orc'


class FatTbMOrcIte(models.Model):
    id_orcamento = models.OneToOneField(FatTbMOrc, models.DO_NOTHING, db_column='id_orcamento', primary_key=True)  # The composite primary key (id_orcamento, id_item) found, that is not supported. The first column is selected.
    id_item = models.ForeignKey(CadTbCIte, models.DO_NOTHING, db_column='id_item')
    qtde = models.FloatField()
    vlr_unitario = models.DecimalField(max_digits=18, decimal_places=4)
    vlr_bruto = models.DecimalField(max_digits=18, decimal_places=4)
    vlr_desconto = models.DecimalField(max_digits=18, decimal_places=4)
    per_desconto = models.DecimalField(max_digits=18, decimal_places=4)
    vlr_liquido = models.DecimalField(max_digits=18, decimal_places=4)
    id_seq_item = models.IntegerField()
    id_busca_item = models.CharField(max_length=30, blank=True, null=True)
    id_cor = models.IntegerField(blank=True, null=True)
    id_tamanho = models.IntegerField(blank=True, null=True)
    vlr_unitario_orig = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True, db_comment='Este campo irß armazenar o preþo original (Que Ú calculado pelo sistema).  Assim o sistema saberß se o usußrio alterou o preþo no pedido ao verificar VLR_UNITARIO vs VLR_UNITARIO_ORIG')
    pcp_obs_item = models.CharField(max_length=150, blank=True, null=True)
    per_desc_max = models.FloatField(blank=True, null=True)
    vlr_frete = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    per_desc_basico = models.FloatField(blank=True, null=True)
    vlr_desc_basico = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    per_desc_especial = models.FloatField(blank=True, null=True)
    vlr_desc_especial = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fat_tb_m_orc_ite'
        unique_together = (('id_orcamento', 'id_item'),)


class FatTbMPca(models.Model):
    id_carregamento = models.IntegerField(primary_key=True)
    id_responsavel = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_responsavel')
    dta_carregamento = models.DateField()
    status = models.IntegerField()
    id_motorista = models.ForeignKey('PcpTbCMta', models.DO_NOTHING, db_column='id_motorista', blank=True, null=True)
    placa = models.CharField(max_length=8, blank=True, null=True)
    seq_carreg_anual = models.IntegerField(blank=True, null=True, db_comment='O valor deste campo zera todo vez que se muda de ano.')

    class Meta:
        managed = False
        db_table = 'fat_tb_m_pca'


class FatTbMPcaPed(models.Model):
    id_carregamento = models.OneToOneField(FatTbMPca, models.DO_NOTHING, db_column='id_carregamento', primary_key=True)  # The composite primary key (id_carregamento, id_pedido) found, that is not supported. The first column is selected.
    id_pedido = models.ForeignKey('FatTbMPed', models.DO_NOTHING, db_column='id_pedido')

    class Meta:
        managed = False
        db_table = 'fat_tb_m_pca_ped'
        unique_together = (('id_carregamento', 'id_pedido'),)


class FatTbMPcaPedIte(models.Model):
    id_pedido = models.IntegerField()
    id_sequencia = models.IntegerField()
    id_item = models.IntegerField()
    qtde = models.FloatField()
    id_cor = models.IntegerField()
    id_tamanho = models.IntegerField()
    id_carregamento = models.OneToOneField(FatTbMPcaPed, models.DO_NOTHING, db_column='id_carregamento', primary_key=True)  # The composite primary key (id_carregamento, id_pedido, id_sequencia) found, that is not supported. The first column is selected.
    pcp_obs_item = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fat_tb_m_pca_ped_ite'
        unique_together = (('id_carregamento', 'id_pedido', 'id_sequencia'),)


class FatTbMPed(models.Model):
    id_pedido = models.IntegerField(primary_key=True)
    id_empresa = models.ForeignKey(CadTbCPar, models.DO_NOTHING, db_column='id_empresa')
    dta_pedido = models.DateField()
    id_tipo_mov_estoque = models.ForeignKey(CadTbCTme, models.DO_NOTHING, db_column='id_tipo_mov_estoque')
    id_vendedor = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_vendedor')
    obs = models.CharField(max_length=255, blank=True, null=True)
    vlr_bruto = models.DecimalField(max_digits=18, decimal_places=4)
    vlr_desconto = models.DecimalField(max_digits=18, decimal_places=4)
    per_desconto = models.FloatField()
    vlr_liquido = models.DecimalField(max_digits=18, decimal_places=4)
    hor_pedido = models.DateTimeField(blank=True, null=True)
    id_condicao_pag = models.ForeignKey(CadTbCCpg, models.DO_NOTHING, db_column='id_condicao_pag')
    pcp_obs = models.CharField(max_length=200, blank=True, null=True)
    pcp_id_opr = models.IntegerField(blank=True, null=True)
    situacao = models.IntegerField(db_comment='0 - Em aberto     \n1 - Reprovado   \n2 - Em produþÒo \n3 - Faturado\n4 - Cancelado')
    situacao_aprovacao = models.IntegerField(db_comment='0 - Em espera\n1 - Aprovado\n2 - Reprovado')
    id_atendente = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_atendente', related_name='fattbmped_id_atendente_set', blank=True, null=True)
    id_responsavel = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_responsavel', related_name='fattbmped_id_responsavel_set', blank=True, null=True)
    id_cliente = models.ForeignKey(CadTbCCli, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    tipo_restricao = models.CharField(max_length=100, blank=True, null=True, db_comment='0-Debito\n1-Limite de Credito\n')
    id_almoxarifado = models.IntegerField(blank=True, null=True)
    justificativa = models.CharField(max_length=100, blank=True, null=True)
    id_usuario_lib = models.IntegerField(blank=True, null=True)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    origem = models.IntegerField(blank=True, null=True, db_comment='0-desktop\r\n1-dispositivo movel \r\n2-Pedido Cupom\r\n3-SeparaþÒo de Mercadoria\r\n4-Telemarketing')
    dispositivo = models.CharField(max_length=50, blank=True, null=True, db_comment='Nome do dispositivo, se for desktop, colocar o nome da maquina')
    gps_latitude = models.FloatField(blank=True, null=True)
    gps_longitude = models.FloatField(blank=True, null=True)
    cubagem = models.FloatField(blank=True, null=True, db_comment='Campo utilizado quando o parÔmetro SGQ = True.\nEste campo irß ter o total de cubagem de cada item do pedido.\nCßlculo:\ncubagem do CAD_TB_C_ITE * qtde  do PED_ITE\ndepois SOMA o total de cada item e grava o valor no campo CUBAGEM do FAT_TB_M_PED.\n')
    id_orcamento = models.IntegerField(blank=True, null=True)
    envia_carga = models.BooleanField(blank=True, null=True, db_comment='Este campo irß aparecer na tela se \no campo "ped_envia_carga" do cad_tb_c_par_ctr estiver marcado.   Caso o campo "envia_carga" estiver marcado o sistema irß enviß-lo para a tela de liberaþÒo.')
    dta_prev_entrega = models.DateField(blank=True, null=True)
    id_abertura = models.IntegerField(blank=True, null=True, db_comment='Campo utilizado pela tela (FAT_FM_M_PNF) Pedido Cupom.')
    dias_cpg_prazo = models.IntegerField(blank=True, null=True)
    offline = models.BooleanField(blank=True, null=True)
    conferido = models.BooleanField(blank=True, null=True)
    id_conf = models.IntegerField(blank=True, null=True)
    dta_conf = models.DateField(blank=True, null=True)
    hor_conf = models.TimeField(blank=True, null=True)
    resultado_conf = models.IntegerField(blank=True, null=True, db_comment='0-Total\r\n1-Parcial')
    id_resp_conf = models.IntegerField(blank=True, null=True)
    id_propriedade = models.IntegerField(blank=True, null=True)
    id_mkt = models.ForeignKey(FatTbMMkt, models.DO_NOTHING, db_column='id_mkt', blank=True, null=True)
    vlr_frete = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    mod_frete = models.IntegerField(blank=True, null=True, db_comment='0-CIF;1-FOB')
    can_usuario = models.IntegerField(blank=True, null=True)
    can_data = models.DateField(blank=True, null=True)
    can_motivo = models.CharField(max_length=100, blank=True, null=True, db_comment='Utilizado no momento em que o usußrio cancela o pedido pela tela de Cancelamento de Pedido.')
    can_hora = models.TimeField(blank=True, null=True)
    semana = models.IntegerField(blank=True, null=True, db_comment='Campo utilizado pelo dispositivo movel, usado pelo esquema da visita a produtores.')
    id_pedido_mob = models.IntegerField(blank=True, null=True, db_comment='Neste campo de fato fica gravado o Id pedido do mobile, diferente do ID_PEDIDO_TEMP_MOB.')
    id_motorista = models.ForeignKey('PcpTbCMta', models.DO_NOTHING, db_column='id_motorista', blank=True, null=True)
    id_placa = models.CharField(max_length=8, blank=True, null=True)
    vlr_credito = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    id_pedido_temp_mob = models.IntegerField(blank=True, null=True, db_comment='Utilizado no momento da sincronizaþÒo com o sistema Mobile. Depois o valor deste campo Ú apagado.')
    vlr_desc_especial = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_desc_basico = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    sgq_per_comissao = models.FloatField(blank=True, null=True)
    qtde_volume = models.FloatField(blank=True, null=True)
    vlr_icm_desn = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_desc_produtos = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    per_desc_produtos = models.FloatField(blank=True, null=True)
    vlr_produtos = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_serv_bruto = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_desc_servicos = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    per_desc_servicos = models.FloatField(blank=True, null=True)
    vlr_ser_liquido = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_terceiro = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_desc_terceiro = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    per_desc_terceiro = models.FloatField(blank=True, null=True)
    vlr_terc_liquido = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    ped_gera_fin_separado = models.BooleanField(blank=True, null=True)
    vlr_prod_liquido = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    separa_prod_serv = models.BooleanField(blank=True, null=True)
    vlr_cred_produtos = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_cred_servicos = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    id_pedido_orig = models.IntegerField(blank=True, null=True)
    id_mecanico = models.IntegerField(blank=True, null=True)
    vlr_desc_pos_fat = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True, db_comment='Este campo serve para o financeiro informar o valo do desconto ap¾s o faturamento, pois terß influÛncia na comissÒo do representante')
    sgq_texto_cond_pgto = models.CharField(max_length=80, blank=True, null=True)
    per_desc_basico = models.FloatField(blank=True, null=True, db_comment='Utiliazado para quem utiliza SGQ')
    per_desc_especial = models.FloatField(blank=True, null=True, db_comment='Utiliazado para quem utiliza SGQ')
    dta_liberacao = models.DateField(blank=True, null=True, db_comment='Data que foi feita a liberaþÒo do pedido de venda.')
    pedido_automatico = models.BooleanField(blank=True, null=True, db_comment='Pedido gerado automaticamente a partir de um pedido que tenha o seu item alterado para menos e com a confirmaþÒo do usußrio, para poder ser gerado.')
    pedido_origem_aut = models.IntegerField(blank=True, null=True)
    gerar_pedido_diferenca = models.BooleanField(blank=True, null=True, db_comment='Se for true o sistema irß gerar um novo pedido com a qtde retirada do pedido original')
    id_pedido_gerado = models.IntegerField(blank=True, null=True, db_comment='Neste campo fica guardado o nro do pedido que serß gerado com a diferenþa das quantidades dos itens.')
    per_desconto_fat = models.FloatField(blank=True, null=True, db_comment='Este campo Ú utilizado quando o usußrio deseja dar um desconto para abater no valor total liquido dos itens sem ter que deixar informado o percentual do desconto nos itens.')
    texto_diversos_temp = models.CharField(max_length=255, blank=True, null=True, db_comment='Este campo serß utilizado para diversas utilidades.\r\nexemplo: quando rodar algum suporte.')
    id_func_pri_impressao = models.IntegerField(blank=True, null=True)
    dta_pri_impressao = models.DateField(blank=True, null=True)
    hor_pri_impressao = models.TimeField(blank=True, null=True)
    id_func_seg_impressao = models.IntegerField(blank=True, null=True)
    dta_seg_impressao = models.DateField(blank=True, null=True)
    hor_seg_impressao = models.TimeField(blank=True, null=True)
    id_func_ter_impressao = models.IntegerField(blank=True, null=True)
    dta_ter_impressao = models.DateField(blank=True, null=True)
    hor_ter_impressao = models.TimeField(blank=True, null=True)
    motivo_seg_impressao = models.CharField(max_length=100, blank=True, null=True)
    motivo_ter_impressao = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fat_tb_m_ped'


class FatTbMPedIte(models.Model):
    id_pedido = models.OneToOneField(FatTbMPed, models.DO_NOTHING, db_column='id_pedido', primary_key=True)  # The composite primary key (id_pedido, id_sequencia) found, that is not supported. The first column is selected.
    id_sequencia = models.IntegerField()
    id_item = models.ForeignKey(CadTbCIte, models.DO_NOTHING, db_column='id_item')
    qtde = models.FloatField()
    vlr_unitario = models.DecimalField(max_digits=18, decimal_places=4)
    vlr_bruto = models.DecimalField(max_digits=18, decimal_places=4)
    per_desconto = models.FloatField()
    vlr_desconto = models.DecimalField(max_digits=18, decimal_places=4)
    vlr_liquido = models.DecimalField(max_digits=18, decimal_places=4)
    id_cor = models.IntegerField(blank=True, null=True)
    id_tamanho = models.IntegerField(blank=True, null=True)
    id_busca_item = models.CharField(max_length=30, blank=True, null=True)
    vlr_unitario_orig = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True, db_comment='Este campo irß armazenar o preþo original (Que Ú calculado pelo sistema).  Assim o sistema saberß se o usußrio alterou o preþo no pedido ao verificar VLR_UNITARIO vs VLR_UNITARIO_ORIG')
    per_desc_max = models.FloatField(blank=True, null=True)
    qtde_conferida = models.FloatField(blank=True, null=True)
    pcp_obs_item = models.CharField(max_length=150, blank=True, null=True)
    id_cultura = models.IntegerField(blank=True, null=True)
    vlr_frete = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    qtde_volume = models.FloatField(blank=True, null=True)
    vlr_icm_desn = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    motivo_icms_des = models.IntegerField(blank=True, null=True)
    num_lote = models.CharField(max_length=15, blank=True, null=True)
    id_mecanico = models.IntegerField(blank=True, null=True)
    per_desc_basico = models.FloatField(blank=True, null=True)
    vlr_desc_basico = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    per_desc_especial = models.FloatField(blank=True, null=True)
    vlr_desc_especial = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fat_tb_m_ped_ite'
        unique_together = (('id_pedido', 'id_sequencia'),)


class FatTbMPedTit(models.Model):
    id_pedido = models.OneToOneField(FatTbMPed, models.DO_NOTHING, db_column='id_pedido', primary_key=True)  # The composite primary key (id_pedido, id_titulo) found, that is not supported. The first column is selected.
    id_titulo = models.IntegerField()
    dias = models.IntegerField()
    dta_vencimento = models.DateField()
    vlr_titulo = models.DecimalField(max_digits=18, decimal_places=4)
    che_banco = models.CharField(max_length=10, blank=True, null=True)
    che_agencia = models.CharField(max_length=10, blank=True, null=True)
    che_conta = models.IntegerField(blank=True, null=True)
    che_numero = models.IntegerField(blank=True, null=True)
    che_emitente = models.CharField(max_length=50, blank=True, null=True)
    id_forma_pag = models.ForeignKey(CadTbCFpg, models.DO_NOTHING, db_column='id_forma_pag', blank=True, null=True)
    bol_nosso_numero = models.IntegerField(blank=True, null=True)
    id_maquineta = models.IntegerField(blank=True, null=True, db_comment='Campo utilizado pela tela FAT_FM_M_PNF (Pedido Cupom).')

    class Meta:
        managed = False
        db_table = 'fat_tb_m_ped_tit'
        unique_together = (('id_pedido', 'id_titulo'),)


class FatTbMPedTitSer(models.Model):
    id_pedido = models.OneToOneField(FatTbMPed, models.DO_NOTHING, db_column='id_pedido', primary_key=True)  # The composite primary key (id_pedido, id_titulo) found, that is not supported. The first column is selected.
    id_titulo = models.IntegerField()
    dias = models.IntegerField()
    dta_vencimento = models.DateField()
    vlr_titulo = models.DecimalField(max_digits=18, decimal_places=4)
    che_banco = models.CharField(max_length=10, blank=True, null=True)
    che_agencia = models.CharField(max_length=10, blank=True, null=True)
    che_conta = models.IntegerField(blank=True, null=True)
    che_numero = models.IntegerField(blank=True, null=True)
    che_emitente = models.CharField(max_length=50, blank=True, null=True)
    id_forma_pag = models.ForeignKey(CadTbCFpg, models.DO_NOTHING, db_column='id_forma_pag', blank=True, null=True)
    bol_nosso_numero = models.IntegerField(blank=True, null=True)
    id_maquineta = models.IntegerField(blank=True, null=True, db_comment='Campo utilizado pela tela FAT_FM_M_PNF (Pedido Cupom).')

    class Meta:
        managed = False
        db_table = 'fat_tb_m_ped_tit_ser'
        unique_together = (('id_pedido', 'id_titulo'),)


class FatTbMPex(models.Model):
    id_pedido = models.IntegerField(primary_key=True)
    id_empresa = models.IntegerField()
    dta_pedido = models.DateField()
    id_tipo_mov_estoque = models.IntegerField()
    id_vendedor = models.IntegerField()
    obs = models.CharField(max_length=100, blank=True, null=True)
    vlr_bruto = models.DecimalField(max_digits=18, decimal_places=4)
    vlr_desconto = models.DecimalField(max_digits=18, decimal_places=4)
    per_desconto = models.FloatField()
    vlr_liquido = models.DecimalField(max_digits=18, decimal_places=4)
    hor_pedido = models.DateTimeField(blank=True, null=True)
    id_condicao_pag = models.IntegerField()
    pcp_obs = models.CharField(max_length=100, blank=True, null=True)
    pcp_id_opr = models.IntegerField(blank=True, null=True)
    situacao = models.IntegerField()
    situacao_aprovacao = models.IntegerField()
    id_atendente = models.IntegerField(blank=True, null=True)
    id_responsavel = models.IntegerField(blank=True, null=True)
    id_cliente = models.IntegerField(blank=True, null=True)
    tipo_restricao = models.CharField(max_length=100, blank=True, null=True)
    id_almoxarifado = models.IntegerField(blank=True, null=True)
    justificativa = models.CharField(max_length=100, blank=True, null=True)
    id_usuario_lib = models.IntegerField(blank=True, null=True)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    origem = models.IntegerField(blank=True, null=True)
    dispositivo = models.CharField(max_length=50, blank=True, null=True)
    gps_latitude = models.FloatField(blank=True, null=True)
    gps_longitude = models.FloatField(blank=True, null=True)
    cubagem = models.FloatField(blank=True, null=True)
    id_orcamento = models.IntegerField(blank=True, null=True)
    envia_carga = models.BooleanField(blank=True, null=True)
    dta_prev_entrega = models.DateField(blank=True, null=True)
    id_abertura = models.IntegerField(blank=True, null=True)
    dias_cpg_prazo = models.IntegerField(blank=True, null=True)
    offline = models.BooleanField(blank=True, null=True)
    conferido = models.BooleanField(blank=True, null=True)
    id_conf = models.IntegerField(blank=True, null=True)
    dta_conf = models.DateField(blank=True, null=True)
    hor_conf = models.TimeField(blank=True, null=True)
    resultado_conf = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fat_tb_m_pex'


class FatTbMPos(models.Model):
    id_posvenda = models.IntegerField(primary_key=True)
    id_empresa = models.ForeignKey(CadTbCPar, models.DO_NOTHING, db_column='id_empresa')
    dta_posvenda = models.DateField()
    id_cliente = models.ForeignKey(CadTbCCli, models.DO_NOTHING, db_column='id_cliente')
    id_responsavel = models.IntegerField(blank=True, null=True)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fat_tb_m_pos'
        db_table_comment = 'Pos-Venda'


class FatTbMPosIte(models.Model):
    id_posvenda = models.OneToOneField(FatTbMPos, models.DO_NOTHING, db_column='id_posvenda', primary_key=True)  # The composite primary key (id_posvenda, id_fiscal) found, that is not supported. The first column is selected.
    id_fiscal = models.ForeignKey(FatTbMNfe, models.DO_NOTHING, db_column='id_fiscal')
    reclamacao = models.CharField(max_length=800, blank=True, null=True)
    solucao = models.CharField(max_length=800, blank=True, null=True)
    avaliacao = models.IntegerField(db_comment='1 - Ëtimo; 2 - Bom; 3 - Regular; 4 - Ruim;\n')

    class Meta:
        managed = False
        db_table = 'fat_tb_m_pos_ite'
        unique_together = (('id_posvenda', 'id_fiscal'),)


class FatTbMRom(models.Model):
    id_romaneio = models.IntegerField(primary_key=True)
    id_empresa = models.IntegerField()
    dta_emissao = models.DateField()
    id_responsavel = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_responsavel')
    id_motorista = models.ForeignKey('PcpTbCMta', models.DO_NOTHING, db_column='id_motorista')
    obs_1 = models.CharField(max_length=100, blank=True, null=True)
    obs_2 = models.CharField(max_length=100, blank=True, null=True)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    rntrc = models.CharField(max_length=20, blank=True, null=True)
    chave_mdf = models.CharField(max_length=44, blank=True, null=True)
    und_transporte = models.SmallIntegerField(blank=True, null=True, db_comment='0-RodoTracao, \n1-RodoReboque, \n2-Navio, \n3-Balsa, \n4-Aeronave, \n5-Vagao, \n6-Outros')
    total_notas = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vol_carga = models.FloatField(blank=True, null=True)
    qtde_carga = models.FloatField(blank=True, null=True)
    id_veiculo = models.IntegerField(blank=True, null=True)
    mdf_recibo = models.CharField(max_length=50, blank=True, null=True)
    mdf_protocolo = models.CharField(max_length=50, blank=True, null=True)
    veiculo = models.CharField(max_length=50, blank=True, null=True)
    id_placa = models.CharField(max_length=8, blank=True, null=True)
    id_pca = models.IntegerField(blank=True, null=True, db_comment='Campo utilizado na importaþÒo de carregamento de pedido')
    mdf_numero = models.IntegerField(blank=True, null=True)
    ciot = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True, db_comment='C¾digo Identificador da OperaþÒo de\nTransporte - TambÚm Conhecido como conta frete;')
    tipo = models.IntegerField(blank=True, null=True, db_comment='Campo criado para informar para o MDF se as notas informadas no MANIFESTO sÒo de Clientes ou Fornecedores.\n0 - Clientes\n1 - Fornecedores')
    status = models.IntegerField(blank=True, null=True, db_comment='0 - Em aberto\n1 - Encerrado')
    canc_motivo = models.CharField(max_length=100, blank=True, null=True)
    canc_data = models.DateField(blank=True, null=True)
    canc_usuario = models.IntegerField(blank=True, null=True)
    cancelado = models.BooleanField(blank=True, null=True)
    mdf_encerrado = models.BooleanField(blank=True, null=True)
    dta_hor_ini_viagem = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fat_tb_m_rom'
        db_table_comment = 'Romaneio de Carha'


class FatTbMRomLac(models.Model):
    id_romaneio = models.OneToOneField(FatTbMRom, models.DO_NOTHING, db_column='id_romaneio', primary_key=True)  # The composite primary key (id_romaneio, lacre) found, that is not supported. The first column is selected.
    lacre = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'fat_tb_m_rom_lac'
        unique_together = (('id_romaneio', 'lacre'),)


class FatTbMRomLot(models.Model):
    id_romaneio = models.OneToOneField(FatTbMRom, models.DO_NOTHING, db_column='id_romaneio', primary_key=True)  # The composite primary key (id_romaneio, id_lote_caminhao) found, that is not supported. The first column is selected.
    id_lote_caminhao = models.IntegerField()
    qtde = models.FloatField()
    observacao = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fat_tb_m_rom_lot'
        unique_together = (('id_romaneio', 'id_lote_caminhao'),)


class FatTbMRomNfe(models.Model):
    id_romaneio = models.OneToOneField(FatTbMRom, models.DO_NOTHING, db_column='id_romaneio', primary_key=True)  # The composite primary key (id_romaneio, id_fiscal) found, that is not supported. The first column is selected.
    id_fiscal = models.ForeignKey(FatTbMNfe, models.DO_NOTHING, db_column='id_fiscal')
    id_busca_nfe = models.CharField(max_length=9, blank=True, null=True)
    importada = models.BooleanField(blank=True, null=True, db_comment='Nota fiscal importada por Carregamento.')

    class Meta:
        managed = False
        db_table = 'fat_tb_m_rom_nfe'
        unique_together = (('id_romaneio', 'id_fiscal'),)


class FatTbMRomNfeIte(models.Model):
    id_romaneio = models.OneToOneField(FatTbMRomNfe, models.DO_NOTHING, db_column='id_romaneio', primary_key=True)  # The composite primary key (id_romaneio, id_fiscal, id_sequencia) found, that is not supported. The first column is selected.
    id_fiscal = models.IntegerField()
    id_item = models.IntegerField()
    qtde = models.FloatField()
    id_cor = models.IntegerField(blank=True, null=True)
    id_tamanho = models.IntegerField(blank=True, null=True)
    id_sequencia = models.IntegerField()
    peso_liquido = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fat_tb_m_rom_nfe_ite'
        unique_together = (('id_romaneio', 'id_fiscal', 'id_sequencia'),)


class FatTbMRomPer(models.Model):
    id_romaneio = models.OneToOneField(FatTbMRom, models.DO_NOTHING, db_column='id_romaneio', primary_key=True)  # The composite primary key (id_romaneio, uf) found, that is not supported. The first column is selected.
    uf = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'fat_tb_m_rom_per'
        unique_together = (('id_romaneio', 'uf'),)
        db_table_comment = 'Tabela de Percurso de Estados do Motorista.'


class FatTbMRte(models.Model):
    id_rte = models.IntegerField(primary_key=True)
    id_empresa = models.IntegerField()
    dta_criacao = models.DateField(blank=True, null=True)
    hor_criacao = models.TimeField(blank=True, null=True)
    id_responsavel = models.IntegerField()
    importado = models.BooleanField(blank=True, null=True)
    observacao = models.CharField(max_length=200, blank=True, null=True)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fat_tb_m_rte'


class FatTbMRtePed(models.Model):
    id_rte = models.IntegerField(primary_key=True)  # The composite primary key (id_rte, id_pedido) found, that is not supported. The first column is selected.
    id_pedido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fat_tb_m_rte_ped'
        unique_together = (('id_rte', 'id_pedido'),)


class FatTbMXml(models.Model):
    nota_fiscal = models.IntegerField()
    dta_emissao = models.DateField()
    serie = models.CharField(max_length=3, blank=True, null=True)
    cfop = models.CharField(max_length=5, blank=True, null=True)
    id_tipo_estoque = models.IntegerField(blank=True, null=True)
    id_condicao_pag = models.IntegerField(blank=True, null=True)
    chave = models.CharField(max_length=44)
    vlr_bruto = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_liquido = models.DecimalField(max_digits=18, decimal_places=4)
    cnpj_emitente = models.CharField(max_length=14)
    nome_emitente = models.CharField(max_length=50, blank=True, null=True)
    id_almoxarifado = models.IntegerField(blank=True, null=True)
    vlr_icm_desc = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    id_controle = models.IntegerField(primary_key=True)
    id_empresa = models.ForeignKey(CadTbCPar, models.DO_NOTHING, db_column='id_empresa')
    id_iqm = models.IntegerField(blank=True, null=True)
    id_fiscal = models.IntegerField(blank=True, null=True)
    fre_valor = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_outras = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_desconto = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_outras_desp = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_icms = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_base = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    ipi_valor = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    icm_s_valor = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    nref_chave = models.CharField(max_length=44, blank=True, null=True)
    nfe_finalidade = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fat_tb_m_xml'


class FatTbMXmlIte(models.Model):
    seq = models.IntegerField()
    cod_fabrica = models.CharField(max_length=30, blank=True, null=True)
    id_item = models.IntegerField(blank=True, null=True)
    id_cst_icms = models.CharField(max_length=3, blank=True, null=True)
    id_cfop = models.CharField(max_length=5, blank=True, null=True)
    vlr_bruto = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_liquido = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    desc_item = models.CharField(max_length=50, blank=True, null=True)
    und = models.CharField(max_length=3, blank=True, null=True)
    qtde = models.FloatField(blank=True, null=True)
    vlr_unitario = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_desconto = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    id_cor = models.IntegerField(blank=True, null=True)
    id_tamanho = models.IntegerField(blank=True, null=True)
    num_lote = models.CharField(max_length=15, blank=True, null=True)
    id_controle = models.OneToOneField(FatTbMXml, models.DO_NOTHING, db_column='id_controle', primary_key=True)  # The composite primary key (id_controle, id_sequencia) found, that is not supported. The first column is selected.
    id_sequencia = models.IntegerField()
    id_sequencia_ite_iqm = models.IntegerField(blank=True, null=True)
    id_busca_item = models.CharField(max_length=30, blank=True, null=True)
    icm_n_aliquota = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    icm_per_reducao = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    icm_n_base = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    icm_n_valor = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    icm_s_base = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    icm_s_valor = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_outras_desp = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    ipi_base = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    ipi_aliquota = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    ipi_valor = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    pis_base = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    pis_aliquota = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    pis_valor = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    fre_valor = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    cof_base = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    cof_aliquota = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    cof_valor = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    origem_mercadoria = models.CharField(max_length=1, blank=True, null=True)
    vlr_icm_desc = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_outras = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    motivo_icms_des = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fat_tb_m_xml_ite'
        unique_together = (('id_controle', 'id_sequencia'),)


class FatTbMXmlIteLot(models.Model):
    id_controle = models.OneToOneField(FatTbMXmlIte, models.DO_NOTHING, db_column='id_controle', primary_key=True)  # The composite primary key (id_controle, id_sequencia, num_lote) found, that is not supported. The first column is selected.
    id_sequencia = models.IntegerField()
    num_lote = models.CharField(max_length=15)
    qtde = models.FloatField()
    dta_vencimento = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fat_tb_m_xml_ite_lot'
        unique_together = (('id_controle', 'id_sequencia', 'num_lote'),)


class FatTbMXmlTit(models.Model):
    id_controle = models.OneToOneField(FatTbMXml, models.DO_NOTHING, db_column='id_controle', primary_key=True)  # The composite primary key (id_controle, id_titulo) found, that is not supported. The first column is selected.
    id_forma_pag = models.IntegerField(blank=True, null=True)
    id_titulo = models.IntegerField()
    num_titulo = models.CharField(max_length=20)
    vlr_titulo = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    dta_vencimento = models.DateField(blank=True, null=True)
    id_plano = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fat_tb_m_xml_tit'
        unique_together = (('id_controle', 'id_titulo'),)


class FinTbMBrd(models.Model):
    id_brd = models.IntegerField(primary_key=True)
    id_empresa = models.ForeignKey(CadTbCPar, models.DO_NOTHING, db_column='id_empresa', blank=True, null=True)
    dta_criacao = models.DateField(blank=True, null=True)
    hor_criacao = models.TimeField(blank=True, null=True)
    id_resp_criacao = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_resp_criacao', blank=True, null=True)
    dta_lib = models.DateField(blank=True, null=True)
    hor_lib = models.TimeField(blank=True, null=True)
    id_resp_lib = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_resp_lib', related_name='fintbmbrd_id_resp_lib_set', blank=True, null=True)
    dta_bxa = models.DateField(blank=True, null=True)
    hor_bxa = models.TimeField(blank=True, null=True)
    id_resp_bxa = models.IntegerField(blank=True, null=True)
    vlr_a_pagar = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    id_forma_pag = models.ForeignKey(CadTbCFpg, models.DO_NOTHING, db_column='id_forma_pag', blank=True, null=True)
    id_tipo_financeiro = models.ForeignKey(CadTbCTif, models.DO_NOTHING, db_column='id_tipo_financeiro', blank=True, null=True)
    obs = models.CharField(max_length=200, blank=True, null=True)
    id_conta = models.ForeignKey(CadTbCCtc, models.DO_NOTHING, db_column='id_conta', blank=True, null=True)
    id_abertura = models.ForeignKey('FinTbMCxa', models.DO_NOTHING, db_column='id_abertura', blank=True, null=True)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    liberado = models.BooleanField(blank=True, null=True)
    baixado = models.BooleanField(blank=True, null=True)
    cancelado = models.BooleanField(blank=True, null=True)
    id_resp_canc = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_resp_canc', related_name='fintbmbrd_id_resp_canc_set', blank=True, null=True)
    dta_canc = models.DateField(blank=True, null=True)
    hor_canc = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fin_tb_m_brd'
        db_table_comment = 'Tabela de Border¶'


class FinTbMBrdTit(models.Model):
    id_brd = models.OneToOneField(FinTbMBrd, models.DO_NOTHING, db_column='id_brd', primary_key=True)  # The composite primary key (id_brd, id_titulo) found, that is not supported. The first column is selected.
    id_titulo = models.ForeignKey('FinTbMPag', models.DO_NOTHING, db_column='id_titulo')
    vlr_pagamento = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_juros = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_desconto = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    per_desconto = models.FloatField(blank=True, null=True)
    vlr_a_pagar = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_restante = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    dta_vencimento = models.DateField(blank=True, null=True)
    vlr_titulo = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    num_parcela = models.CharField(max_length=20, blank=True, null=True)
    vlr_multa = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    atraso = models.IntegerField(blank=True, null=True)
    id_conta = models.ForeignKey(CadTbCCtc, models.DO_NOTHING, db_column='id_conta', blank=True, null=True)
    id_plano = models.ForeignKey(CadTbCPct, models.DO_NOTHING, db_column='id_plano', blank=True, null=True)
    id_ccusto = models.ForeignKey(CadTbCCcu, models.DO_NOTHING, db_column='id_ccusto', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fin_tb_m_brd_tit'
        unique_together = (('id_brd', 'id_titulo'),)
        db_table_comment = 'TÝtulos do border¶'


class FinTbMCbx(models.Model):
    id_cbx = models.IntegerField(primary_key=True)
    dta_baixa = models.DateField(blank=True, null=True)
    vlr_bruto = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    vlr_desconto_ope = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    vlr_desconto_antec = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    vlr_liquido = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    observacao = models.CharField(max_length=100, blank=True, null=True)
    id_responsavel = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_responsavel', blank=True, null=True)
    id_forma_pag = models.ForeignKey(CadTbCFpg, models.DO_NOTHING, db_column='id_forma_pag', blank=True, null=True)
    com_bxa_antecipacao = models.BooleanField(blank=True, null=True)
    id_conta = models.ForeignKey(CadTbCCtc, models.DO_NOTHING, db_column='id_conta', blank=True, null=True)
    id_empresa = models.ForeignKey(CadTbCPar, models.DO_NOTHING, db_column='id_empresa', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fin_tb_m_cbx'
        db_table_comment = 'Baixa de Cart§es de CrÚdito'


class FinTbMCbxTit(models.Model):
    id_cbx = models.OneToOneField(FinTbMCbx, models.DO_NOTHING, db_column='id_cbx', primary_key=True)  # The composite primary key (id_cbx, id_titulo) found, that is not supported. The first column is selected.
    id_titulo = models.ForeignKey('FinTbMRec', models.DO_NOTHING, db_column='id_titulo')
    vlr_desconto_ope = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    vlr_desconto_antec = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    vlr_bruto = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    vlr_liquido = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fin_tb_m_cbx_tit'
        unique_together = (('id_cbx', 'id_titulo'),)
        db_table_comment = 'Titulos da baixa de cart§es de crÚdito'


class FinTbMCob(models.Model):
    id_controle = models.IntegerField(primary_key=True)
    dta_cobranca = models.DateField()
    tipo_contato = models.IntegerField(db_comment='0-Telefone\n1-Cobrador\n2-Advogado\n3-E-mail\n4-Carta de cobranþa\n')
    observacao = models.CharField(max_length=800)
    hor_cobranca = models.DateTimeField(blank=True, null=True)
    acordo = models.BooleanField()
    id_funcionario = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_funcionario')
    per_juros_negociado = models.DecimalField(max_digits=18, decimal_places=4)
    id_cliente = models.IntegerField(blank=True, null=True)
    dta_acordo = models.DateField(blank=True, null=True)
    vlr_negociado = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True, db_comment='0-aberto\n1-importado')
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    id_empresa = models.ForeignKey(CadTbCPar, models.DO_NOTHING, db_column='id_empresa')
    nome_contato = models.CharField(max_length=80, blank=True, null=True)
    contato = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fin_tb_m_cob'
        db_table_comment = 'Controle de Cobranþa'


class FinTbMCobTit(models.Model):
    id_controle = models.OneToOneField(FinTbMCob, models.DO_NOTHING, db_column='id_controle', primary_key=True)  # The composite primary key (id_controle, id_titulo) found, that is not supported. The first column is selected.
    id_titulo = models.ForeignKey('FinTbMRec', models.DO_NOTHING, db_column='id_titulo')
    selecao = models.BooleanField(blank=True, null=True)
    dias_atraso = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fin_tb_m_cob_tit'
        unique_together = (('id_controle', 'id_titulo'),)


class FinTbMCon(models.Model):
    id_conciliacao = models.IntegerField(primary_key=True)
    dta_conciliacao = models.DateField(blank=True, null=True)
    id_conta = models.IntegerField(blank=True, null=True)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    id_responsavel = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_responsavel', blank=True, null=True)
    id_empresa = models.ForeignKey(CadTbCPar, models.DO_NOTHING, db_column='id_empresa', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fin_tb_m_con'
        db_table_comment = 'ConsciliaþÒo Bancaria'


class FinTbMConCxb(models.Model):
    id_conciliacao = models.OneToOneField(FinTbMCon, models.DO_NOTHING, db_column='id_conciliacao', primary_key=True)  # The composite primary key (id_conciliacao, id_cxb) found, that is not supported. The first column is selected.
    id_cxb = models.IntegerField()
    debcre = models.IntegerField(blank=True, null=True, db_comment='0 - DÚbito;  1 - CrÚdito;')
    historico = models.CharField(max_length=100, blank=True, null=True, db_comment='Refere-se a tag-> <MEMO> do arquivo .ofx;')
    tipo = models.CharField(max_length=30, blank=True, null=True, db_comment='Refere-se a tag-> <TRNTYPE> do arquivo .ofx;')
    documento = models.CharField(max_length=30, blank=True, null=True, db_comment='Refere-se a tag-> <CHECKNUM> do arquivo .ofx;')
    vlr_lancamento = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True, db_comment='Refere-se a tag-> <TRNAMT> do arquivo .ofx;')
    status = models.CharField(max_length=1, blank=True, null=True, db_comment='F - Fechado (o usußrio fez o relacionamento do registro do arquivo ofx com o movimento do sistema FIN_TB_M_CTA)\nA - Em aberto (o usußrio ainda nÒo fez o relacionamento do registro do arquivo ofx com o movimento do sistema)')
    selecao = models.IntegerField(blank=True, null=True)
    dta_movimento = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fin_tb_m_con_cxb'
        unique_together = (('id_conciliacao', 'id_cxb'),)
        db_table_comment = 'Tabela de extrato do banco, arquivo OFX dos bancos.'


class FinTbMConCxbAux(models.Model):
    id_conciliacao = models.OneToOneField(FinTbMConCxb, models.DO_NOTHING, db_column='id_conciliacao', primary_key=True)  # The composite primary key (id_conciliacao, id_cxb, id_controle) found, that is not supported. The first column is selected.
    id_controle = models.IntegerField()
    id_plano = models.CharField(max_length=11, blank=True, null=True)
    id_conta = models.IntegerField(blank=True, null=True)
    id_tipo_financeiro = models.IntegerField(blank=True, null=True)
    vlr_lancamento = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    id_titulo = models.IntegerField(blank=True, null=True, db_comment='Identificador do titulo no contas a pagar que foi gerado na conciliacao.')
    historico = models.CharField(max_length=100, blank=True, null=True)
    num_doc = models.IntegerField(blank=True, null=True)
    id_cxb = models.IntegerField(db_comment='Este campo faz relaþÒo com a tabela fin_tb_m_con_cxb.')
    dta_movimento = models.DateField(blank=True, null=True)
    tipo = models.IntegerField(blank=True, null=True, db_comment='0 - SugestÒo \n1 - Novo movimento')
    id_tipo_financeiro_transf = models.IntegerField(blank=True, null=True)
    id_emitente = models.IntegerField(blank=True, null=True)
    tipo_titulo = models.IntegerField(blank=True, null=True, db_comment='0 - Movimento CTA; 1 - Contas a Receber;2 - Contas a Pagar')

    class Meta:
        managed = False
        db_table = 'fin_tb_m_con_cxb_aux'
        unique_together = (('id_conciliacao', 'id_cxb', 'id_controle'),)
        db_table_comment = 'Tabela Auxiliar do Arquivo de ConciliaþÒo'


class FinTbMConCxbDet(models.Model):
    id_conciliacao = models.OneToOneField(FinTbMCon, models.DO_NOTHING, db_column='id_conciliacao', primary_key=True)  # The composite primary key (id_conciliacao, id_cxb, id_controle, id_titulo_rec, id_titulo_pag) found, that is not supported. The first column is selected.
    id_controle = models.IntegerField()
    id_plano = models.CharField(max_length=11, blank=True, null=True)
    id_conta = models.IntegerField(blank=True, null=True)
    id_tipo_financeiro = models.ForeignKey(CadTbCTif, models.DO_NOTHING, db_column='id_tipo_financeiro', blank=True, null=True)
    vlr_lancamento = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    id_titulo = models.IntegerField(blank=True, null=True, db_comment='Identificador do titulo no contas a pagar que foi gerado na conciliacao.')
    historico = models.CharField(max_length=100, blank=True, null=True)
    num_doc = models.IntegerField(blank=True, null=True)
    id_cxb = models.IntegerField(db_comment='Este campo faz relaþÒo com a tabela fin_tb_m_con_cxb.')
    dta_mov_cxb = models.DateField(blank=True, null=True)
    mov_gerado = models.BooleanField(blank=True, null=True, db_comment='Se "true", quer dizer que no momento da conciliaþÒo este registro foi criado;\nSe "false", quer dizer que o registro foi importado do FIN_TB_M_CTA.')
    tipo_reg = models.IntegerField(blank=True, null=True, db_comment='0 - Normal;  1- TransferÛncia (Este estatus tem utilizaþÒo no momento de calcular a diferenþa de valores no relacionamento;')
    id_tipo_financeiro_transf = models.ForeignKey(CadTbCTif, models.DO_NOTHING, db_column='id_tipo_financeiro_transf', related_name='fintbmconcxbdet_id_tipo_financeiro_transf_set', blank=True, null=True)
    id_titulo_rec = models.IntegerField()
    id_titulo_pag = models.IntegerField()
    tipo_titulo = models.IntegerField(blank=True, null=True, db_comment='0 - Movimento do CTA; 1 - Contas a Receber; 2 - Contas a Pagar')
    vlr_titulo = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True, db_comment='Campo utilizado para titulos de contas a receber e a pagar')
    vlr_juros = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True, db_comment='Campo utilizado pelo titulos a receber e a pagar')
    id_emitente = models.IntegerField(blank=True, null=True)
    vlr_desconto_ope = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    doc_impresso = models.IntegerField(blank=True, null=True)
    vlr_desconto = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fin_tb_m_con_cxb_det'
        unique_together = (('id_conciliacao', 'id_cxb', 'id_controle', 'id_titulo_rec', 'id_titulo_pag'),)
        db_table_comment = 'Lanþamento Gerado na conciliaþÒo'


class FinTbMCta(models.Model):
    id_controle = models.IntegerField(primary_key=True)
    id_abertura = models.IntegerField()
    id_empresa = models.IntegerField()
    tipo_lancamento = models.IntegerField(db_comment='0-Caixa\n1-Banco')
    dta_lancamento = models.DateField()
    num_doc = models.IntegerField()
    id_plano = models.ForeignKey(CadTbCPct, models.DO_NOTHING, db_column='id_plano')
    deb_cre = models.IntegerField(db_comment='0-Debito\n1-Credito')
    historico = models.CharField(max_length=100)
    vlr_lancamento = models.DecimalField(max_digits=18, decimal_places=4)
    origem = models.IntegerField(db_comment='0-Manual\r\n1-Baixa de Conta a Receber\r\n2-Baixa de Contas a Pagar\r\n3-DevoluþÒo de vendas 4-ConciliaþÒo bancßria  5-Nota Fiscal de SaÝda 6-Nota de CrÚdito  7 - Abertura de caixa  8 - Controle de Caixa;\r\n9 - MovimentaþÒo de cheque;\r\n10 - Baixa de cart§es de crÚdito;\r\n11 - Baixa automßtica de boletos (Rec);\r\n12 - Cancelamento NF dia Anterior; 13 - Baixa por Border¶;14 - Lanþamento do Movimento do Funcionßrio;15 - PrestaþÒo de Contas; 16 - Desconto de Titulos;17 - Nota Fiscal de Entrada')
    id_conta = models.ForeignKey(CadTbCCtc, models.DO_NOTHING, db_column='id_conta', blank=True, null=True)
    id_tipo_financeiro = models.ForeignKey(CadTbCTif, models.DO_NOTHING, db_column='id_tipo_financeiro')
    conc_numero = models.IntegerField(blank=True, null=True)
    conc_tipo_financeiro = models.IntegerField(blank=True, null=True)
    conc_id_plano = models.CharField(max_length=11, blank=True, null=True)
    conc_vlr_lancamento = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    exp_id_controle = models.IntegerField(blank=True, null=True)
    exp_id_tipo_financeiro = models.IntegerField(blank=True, null=True)
    exp_id_plano = models.CharField(max_length=11, blank=True, null=True)
    exp_id_conta = models.IntegerField(blank=True, null=True)
    id_baixa_pbx = models.IntegerField(blank=True, null=True)
    id_baixa_rbx = models.IntegerField(blank=True, null=True)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    dta_movimento = models.DateField(blank=True, null=True)
    conciliado = models.BooleanField(blank=True, null=True)
    id_fiscal = models.IntegerField(blank=True, null=True)
    id_titulo_rec = models.IntegerField(blank=True, null=True)
    id_credito = models.IntegerField(blank=True, null=True)
    id_mch = models.IntegerField(blank=True, null=True, db_comment='Este campo corresponde ao ID_CONTROLE da tabela FIN_TB_M_MCH;')
    id_conciliacao = models.IntegerField(blank=True, null=True, db_comment='Campo utilizado pela Rotina de ConciliaþÒo bancßria;')
    dta_conciliacao = models.DateField(blank=True, null=True)
    id_cbx = models.IntegerField(blank=True, null=True, db_comment='Este campo Ú alimentado pela rotina de FIN_FM_M_CBX.')
    id_obra = models.IntegerField(blank=True, null=True)
    id_titulo_pag = models.IntegerField(blank=True, null=True)
    id_brd = models.IntegerField(blank=True, null=True, db_comment='Refere-se a talela FIN_TB_M_BRD.')
    id_lmf = models.IntegerField(blank=True, null=True, db_comment='C¾digo do Lanþamento de Movimento do Funcionßrio')
    id_prc = models.IntegerField(blank=True, null=True, db_comment='C¾digo de PrestaþÒo de Contas')
    id_prc_det = models.IntegerField(blank=True, null=True, db_comment='C¾digo do registros filhos da prestaþÒo de Contas')
    id_dct_desc = models.IntegerField(blank=True, null=True)
    id_dct_canc = models.IntegerField(blank=True, null=True)
    id_cliente = models.IntegerField(blank=True, null=True)
    pag_cred_cli = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fin_tb_m_cta'
        db_table_comment = 'Controle de Caixa e Banco.'


class FinTbMCxa(models.Model):
    id_abertura = models.IntegerField(primary_key=True)
    dta_abertura = models.DateField()
    id_conta = models.ForeignKey(CadTbCCtc, models.DO_NOTHING, db_column='id_conta')
    id_empresa = models.ForeignKey(CadTbCPar, models.DO_NOTHING, db_column='id_empresa')
    ecf_serial_impressora = models.CharField(max_length=60, blank=True, null=True)
    id_funcionario = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_funcionario')
    status = models.IntegerField()
    dta_fechamento = models.DateField(blank=True, null=True)
    vlr_suprimento = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    hor_fechamento = models.TimeField(blank=True, null=True)
    dta_ult_reabertura = models.DateField(blank=True, null=True)
    hor_ult_reabertura = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fin_tb_m_cxa'
        db_table_comment = 'Controle de Abertura de Caixa'


class FinTbMDct(models.Model):
    id_dct = models.IntegerField(primary_key=True)
    data_operacao = models.DateField()
    data_original = models.DateField()
    id_conta = models.ForeignKey(CadTbCCtc, models.DO_NOTHING, db_column='id_conta', blank=True, null=True)
    id_local_titulo = models.ForeignKey(CadTbCLto, models.DO_NOTHING, db_column='id_local_titulo', blank=True, null=True)
    per_taxa_desc = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_taxa_desc = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    tipo_operacao = models.IntegerField(db_comment='0 - Descontar TÝtulos; 1- Baixar TÝtulos Descontados; 2 - Desfazer Desconto de TÝtulos')
    vlr_total_titulos = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    id_empresa = models.IntegerField()
    id_responsavel = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_responsavel', blank=True, null=True)
    can_motivo = models.CharField(max_length=100, blank=True, null=True)
    cancelado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fin_tb_m_dct'


class FinTbMDctTit(models.Model):
    id_dct = models.OneToOneField(FinTbMDct, models.DO_NOTHING, db_column='id_dct', primary_key=True)  # The composite primary key (id_dct, id_titulo) found, that is not supported. The first column is selected.
    id_titulo = models.ForeignKey('FinTbMRec', models.DO_NOTHING, db_column='id_titulo')
    vlr_cobrado_canc_desc = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_taxa_desc = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fin_tb_m_dct_tit'
        unique_together = (('id_dct', 'id_titulo'),)


class FinTbMLdm(models.Model):
    id_ldm = models.IntegerField(primary_key=True)
    id_conta = models.ForeignKey(CadTbCCtc, models.DO_NOTHING, db_column='id_conta', blank=True, null=True)
    natureza = models.IntegerField()
    id_motorista = models.ForeignKey('PcpTbCMta', models.DO_NOTHING, db_column='id_motorista')
    id_forma_pag = models.ForeignKey(CadTbCFpg, models.DO_NOTHING, db_column='id_forma_pag')
    id_plano = models.ForeignKey(CadTbCPct, models.DO_NOTHING, db_column='id_plano')
    dta_emissao = models.DateField()
    dta_vencimento = models.DateField()
    num_parcela = models.CharField(max_length=20, blank=True, null=True)
    historico = models.CharField(max_length=100, blank=True, null=True)
    vlr_titulo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    mob_id_ldm = models.IntegerField(blank=True, null=True)
    id_empresa = models.IntegerField(blank=True, null=True)
    caminho_foto = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fin_tb_m_ldm'


class FinTbMLmf(models.Model):
    id_lmf = models.IntegerField(primary_key=True)
    id_conta = models.ForeignKey(CadTbCCtc, models.DO_NOTHING, db_column='id_conta')
    id_tipo_financeiro = models.ForeignKey(CadTbCTif, models.DO_NOTHING, db_column='id_tipo_financeiro')
    dta_movimento = models.DateField()
    id_funcionario = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_funcionario')
    historico = models.CharField(max_length=100, blank=True, null=True)
    vlr_movimento = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_saldo = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True, db_comment='0-Aguardando PrestaþÒo;1-PrestaþÒo Parcial;2-Encerrado')
    id_plano = models.ForeignKey(CadTbCPct, models.DO_NOTHING, db_column='id_plano')
    dta_vencimento = models.DateField(blank=True, null=True)
    id_empresa = models.ForeignKey(CadTbCPar, models.DO_NOTHING, db_column='id_empresa')
    vlr_pago = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    id_obra = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fin_tb_m_lmf'


class FinTbMMch(models.Model):
    id_controle = models.IntegerField(primary_key=True)
    dta_movimento = models.DateField(blank=True, null=True)
    id_conta = models.ForeignKey(CadTbCCtc, models.DO_NOTHING, db_column='id_conta', blank=True, null=True)
    informativo = models.CharField(max_length=100, blank=True, null=True, db_comment='Campo utilizado pelo sistema para detalhar a funþÒo da OperaþÒo escolhida pelo o usußrio. O usußrio nÒo manipula este campo.')
    observacoes = models.CharField(max_length=100, blank=True, null=True)
    vlr_movimento = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    hor_movimento = models.TimeField(blank=True, null=True)
    operacao = models.IntegerField(blank=True, null=True, db_comment='1 - Depositar;\r\n2 - Devolver;\r\n3 - Pagar parcial;\r\n4 - Resgatar; 5 - Pgto a terceiros; 6 - Cheque descontado;')
    id_responsavel = models.IntegerField(blank=True, null=True)
    vlr_tot_juros = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_tot_movimento = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True, db_comment='╔ o resultado de vlr_movimento + vlr_tot_movimento;')
    id_condicao_pag = models.ForeignKey(CadTbCCpg, models.DO_NOTHING, db_column='id_condicao_pag', blank=True, null=True)
    id_cliente = models.ForeignKey(CadTbCCli, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True, db_comment='Campo utilizado somente para operaþ§es de Resgate ou Pagto parcial')
    id_abertura = models.IntegerField(blank=True, null=True)
    id_recibo = models.IntegerField(blank=True, null=True, db_comment='Esse campo Ú utilizado para registrar n║ do recibo')
    id_empresa = models.IntegerField()
    vlr_tot_juros_che = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fin_tb_m_mch'
        db_table_comment = 'MOVIMENTO DE CHEQUE'


class FinTbMMchChe(models.Model):
    id_controle = models.OneToOneField(FinTbMMch, models.DO_NOTHING, db_column='id_controle', primary_key=True)  # The composite primary key (id_controle, id_titulo) found, that is not supported. The first column is selected.
    id_titulo = models.ForeignKey('FinTbMRec', models.DO_NOTHING, db_column='id_titulo')
    vlr_pago = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    id_alinea = models.CharField(max_length=2, blank=True, null=True)
    vlr_juros = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fin_tb_m_mch_che'
        unique_together = (('id_controle', 'id_titulo'),)
        db_table_comment = 'CHEQUES DO MOVIMENTO'


class FinTbMMchTit(models.Model):
    id_controle = models.OneToOneField(FinTbMMch, models.DO_NOTHING, db_column='id_controle', primary_key=True)  # The composite primary key (id_controle, id_titulo) found, that is not supported. The first column is selected.
    id_titulo = models.IntegerField()
    id_forma_pag = models.ForeignKey(CadTbCFpg, models.DO_NOTHING, db_column='id_forma_pag', blank=True, null=True)
    dias = models.IntegerField(blank=True, null=True)
    dta_vencimento = models.DateField(blank=True, null=True)
    num_parcela = models.CharField(max_length=15, blank=True, null=True)
    vlr_juros = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_total = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    che_conta = models.IntegerField(blank=True, null=True)
    che_numero = models.IntegerField(blank=True, null=True)
    che_banco = models.CharField(max_length=10, blank=True, null=True)
    che_emitente = models.CharField(max_length=50, blank=True, null=True)
    che_agencia = models.CharField(max_length=10, blank=True, null=True)
    vlr_titulo = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fin_tb_m_mch_tit'
        unique_together = (('id_controle', 'id_titulo'),)
        db_table_comment = 'MovimentaþÒo de Cheque - TÝtulos'


class FinTbMOrc(models.Model):
    id_orc = models.IntegerField(primary_key=True)
    ano = models.IntegerField(blank=True, null=True)
    vlr_orcamento = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    id_empresa = models.ForeignKey(CadTbCPar, models.DO_NOTHING, db_column='id_empresa', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fin_tb_m_orc'
        db_table_comment = 'ORCAMENTO ANUAL'


class FinTbMOrcPlc(models.Model):
    id_orc = models.OneToOneField(FinTbMOrc, models.DO_NOTHING, db_column='id_orc', primary_key=True)  # The composite primary key (id_orc, id_plc) found, that is not supported. The first column is selected.
    id_plc = models.CharField(max_length=11)
    prev_jan = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    prev_fev = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    prev_mar = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    prev_abr = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    prev_mai = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    prev_jun = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    prev_jul = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    prev_ago = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    prev_set = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    prev_out = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    prev_nov = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    prev_dez = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    prev_total = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fin_tb_m_orc_plc'
        unique_together = (('id_orc', 'id_plc'),)
        db_table_comment = 'PLANO DE CONTAS DO ORCAMENTO'


class FinTbMPag(models.Model):
    id_titulo = models.IntegerField(primary_key=True)
    id_empresa = models.ForeignKey(CadTbCPar, models.DO_NOTHING, db_column='id_empresa')
    id_fornecedor = models.ForeignKey(CadTbCFor, models.DO_NOTHING, db_column='id_fornecedor')
    num_parcela = models.CharField(max_length=20, blank=True, null=True)
    dta_emissao = models.DateField()
    historico = models.CharField(max_length=100)
    vlr_parcela = models.DecimalField(max_digits=18, decimal_places=4)
    vlr_original = models.DecimalField(max_digits=18, decimal_places=4)
    dta_vencimento = models.DateField()
    dta_original = models.DateField()
    vlr_saldo = models.DecimalField(max_digits=18, decimal_places=4)
    id_fiscal = models.IntegerField(blank=True, null=True)
    origem = models.IntegerField(db_comment='0-Estoque\r\n  1-Caixa/Banco  2 - Pequenas Despesas  3 - Baixa Contas a Pagar  4 - Movimento Bancßrio 5 - Lancamento Manual 6 - Lanþamento de Movimento do Funcionßrio  7 - PrestaþÒo de Contas 8 - ConciliaþÒo Bancßria')
    id_forma_pag = models.ForeignKey(CadTbCFpg, models.DO_NOTHING, db_column='id_forma_pag')
    pre_conta = models.IntegerField(blank=True, null=True)
    pre_cheque = models.IntegerField(blank=True, null=True)
    pre_banco = models.CharField(max_length=10, blank=True, null=True)
    pre_emitente = models.CharField(max_length=50, blank=True, null=True)
    pre_agencia = models.CharField(max_length=10, blank=True, null=True)
    tipo_lancamento = models.IntegerField(db_comment='0-Manual\n1-Automatico')
    id_local_titulo = models.ForeignKey(CadTbCLto, models.DO_NOTHING, db_column='id_local_titulo')
    id_plano = models.ForeignKey(CadTbCPct, models.DO_NOTHING, db_column='id_plano')
    id_ccusto = models.IntegerField(blank=True, null=True)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    per_juros = models.FloatField(blank=True, null=True)
    per_multa = models.FloatField(blank=True, null=True)
    id_abertura = models.IntegerField(blank=True, null=True, db_comment='Campo utilizado pela telinha de Pequeas Despesas;')
    id_baixa = models.IntegerField(blank=True, null=True)
    id_cta = models.IntegerField(blank=True, null=True, db_comment='Refere-se ao valor copiado do campo "id_controle" da tabela fin_tb_m_cta, por sua vez, Ú gerado pela tela MovimentaþÒo Bancßrio ')
    id_obra = models.IntegerField(blank=True, null=True)
    dta_lancamento = models.DateField(blank=True, null=True)
    id_lmf = models.IntegerField(blank=True, null=True, db_comment='C¾digo de Lanþamento de Movimento Funcionßrio')
    id_prc = models.IntegerField(blank=True, null=True, db_comment='C¾digo de PrestaþÒo de Contas')
    id_prc_det = models.IntegerField(blank=True, null=True, db_comment='C¾digo do registros filhos da prestaþÒo de Contas')
    id_conciliacao = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fin_tb_m_pag'
        db_table_comment = 'Contas a Pagar'


class FinTbMPagPag(models.Model):
    id_titulo = models.OneToOneField(FinTbMPag, models.DO_NOTHING, db_column='id_titulo', primary_key=True)  # The composite primary key (id_titulo, id_baixa) found, that is not supported. The first column is selected.
    id_baixa = models.IntegerField()
    dta_pagamento = models.DateField()
    vlr_pagamento = models.DecimalField(max_digits=18, decimal_places=4)
    per_juros = models.DecimalField(max_digits=18, decimal_places=4)
    vlr_juros = models.DecimalField(max_digits=18, decimal_places=4)
    vlr_desconto = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    historico = models.CharField(max_length=100)
    id_forma_pag = models.ForeignKey(CadTbCFpg, models.DO_NOTHING, db_column='id_forma_pag')
    id_plano = models.ForeignKey(CadTbCPct, models.DO_NOTHING, db_column='id_plano', blank=True, null=True)
    id_plano_juros = models.ForeignKey(CadTbCPct, models.DO_NOTHING, db_column='id_plano_juros', related_name='fintbmpagpag_id_plano_juros_set', blank=True, null=True)
    chp_vlr_anterior = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    id_responsavel = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_responsavel', blank=True, null=True)
    id_ccusto = models.IntegerField(blank=True, null=True)
    id_plano_desconto = models.CharField(max_length=11, blank=True, null=True)
    vlr_multa = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    id_abertura = models.IntegerField(blank=True, null=True)
    com_substituicao = models.BooleanField(blank=True, null=True)
    vlr_cred_utilizado = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    id_empresa_bxa = models.IntegerField(blank=True, null=True, db_comment='Empresa que recebeu o pagamento.')
    id_brd = models.IntegerField(blank=True, null=True, db_comment='Refere-se a talela FIN_TB_M_BRD.')
    id_fiscal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fin_tb_m_pag_pag'
        unique_together = (('id_titulo', 'id_baixa'),)


class FinTbMPbx(models.Model):
    id_baixa = models.IntegerField(primary_key=True)
    id_empresa = models.ForeignKey(CadTbCPar, models.DO_NOTHING, db_column='id_empresa', blank=True, null=True)
    dta_baixa = models.DateField(blank=True, null=True)
    vlr_baixa = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    observacao = models.CharField(max_length=100, blank=True, null=True)
    id_forma_pag = models.ForeignKey(CadTbCFpg, models.DO_NOTHING, db_column='id_forma_pag', blank=True, null=True)
    id_abertura = models.IntegerField(blank=True, null=True)
    vlr_credito_utilizado = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    id_fornecedor = models.ForeignKey(CadTbCFor, models.DO_NOTHING, db_column='id_fornecedor', blank=True, null=True)
    id_conta = models.IntegerField(blank=True, null=True)
    id_tipo_financeiro = models.IntegerField(blank=True, null=True)
    id_responsavel = models.IntegerField(blank=True, null=True)
    dta_lancamento = models.DateField(blank=True, null=True)
    id_plano = models.CharField(max_length=11, blank=True, null=True)
    id_ccusto = models.IntegerField(blank=True, null=True)
    vlr_saldo_credito = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_credito_disponivel = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    id_recibo = models.IntegerField(blank=True, null=True, db_comment='Esse campo Ú utilizado para conter n║ do recibo')
    vlr_a_pagar = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_tot_novo_tit = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fin_tb_m_pbx'
        db_table_comment = 'Baixa de Contas a Pagar.'


class FinTbMPbxCht(models.Model):
    id_baixa = models.IntegerField(primary_key=True)  # The composite primary key (id_baixa, id_titulo) found, that is not supported. The first column is selected.
    id_titulo = models.IntegerField()
    vlr_cheque = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fin_tb_m_pbx_cht'
        unique_together = (('id_baixa', 'id_titulo'),)
        db_table_comment = 'Baixa de Contas a Pagar com Cheques de Terceiros'


class FinTbMPbxGer(models.Model):
    id_baixa = models.OneToOneField(FinTbMPbx, models.DO_NOTHING, db_column='id_baixa', primary_key=True)  # The composite primary key (id_baixa, id_controle) found, that is not supported. The first column is selected.
    id_controle = models.IntegerField()
    vlr_pagamento = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    dta_vencimento = models.DateField(blank=True, null=True)
    che_numero = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fin_tb_m_pbx_ger'
        unique_together = (('id_baixa', 'id_controle'),)


class FinTbMPbxTit(models.Model):
    id_baixa = models.OneToOneField(FinTbMPbx, models.DO_NOTHING, db_column='id_baixa', primary_key=True)  # The composite primary key (id_baixa, id_titulo) found, that is not supported. The first column is selected.
    id_titulo = models.IntegerField()
    vlr_pagamento = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_juros = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_desconto = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_credito_utilizado = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    per_desconto = models.FloatField(blank=True, null=True)
    vlr_a_pagar = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_restante = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    dta_vencimento = models.DateField(blank=True, null=True)
    vlr_titulo = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    num_parcela = models.CharField(max_length=20, blank=True, null=True)
    vlr_multa = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    atraso = models.IntegerField(blank=True, null=True)
    id_conta = models.IntegerField(blank=True, null=True, db_comment='Este campo recebe o valor do ID_CONTA da tabela pai (FIN_TB_M_PBX), internamente.')

    class Meta:
        managed = False
        db_table = 'fin_tb_m_pbx_tit'
        unique_together = (('id_baixa', 'id_titulo'),)


class FinTbMPcr(models.Model):
    id_credito = models.IntegerField(primary_key=True)
    id_empresa = models.IntegerField()
    origem = models.IntegerField(db_comment='1 - Baixa Contas a Pagar; 2 - DevoluþÒo do Fornecedor')
    num_documento = models.CharField(max_length=20)
    vlr_credito = models.DecimalField(max_digits=18, decimal_places=4)
    vlr_saldo = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    dta_credito = models.DateField()
    deb_cre = models.IntegerField()
    id_fornecedor = models.IntegerField()
    historico = models.CharField(max_length=200)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    id_baixa = models.IntegerField(blank=True, null=True)
    id_titulo = models.IntegerField(blank=True, null=True)
    id_fiscal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fin_tb_m_pcr'


class FinTbMPrc(models.Model):
    id_prc = models.IntegerField(primary_key=True)
    id_lmf = models.ForeignKey(FinTbMLmf, models.DO_NOTHING, db_column='id_lmf')
    vlr_total_prc = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    id_empresa = models.ForeignKey(CadTbCPar, models.DO_NOTHING, db_column='id_empresa')
    dta_prestacao = models.DateField()

    class Meta:
        managed = False
        db_table = 'fin_tb_m_prc'


class FinTbMPrcDet(models.Model):
    id_prc = models.OneToOneField(FinTbMPrc, models.DO_NOTHING, db_column='id_prc', primary_key=True)  # The composite primary key (id_prc, id_sequencia) found, that is not supported. The first column is selected.
    id_tipo_financeiro = models.ForeignKey(CadTbCTif, models.DO_NOTHING, db_column='id_tipo_financeiro')
    id_tipo_titulo = models.IntegerField(blank=True, null=True)
    id_plano = models.ForeignKey(CadTbCPct, models.DO_NOTHING, db_column='id_plano', blank=True, null=True)
    id_conta = models.IntegerField(blank=True, null=True)
    vlr_prestacao = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    historico = models.CharField(max_length=60, blank=True, null=True)
    id_tipo_financeiro_cp = models.IntegerField(blank=True, null=True)
    id_sequencia = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fin_tb_m_prc_det'
        unique_together = (('id_prc', 'id_sequencia'),)


class FinTbMRbx(models.Model):
    id_baixa = models.IntegerField(primary_key=True)
    id_empresa = models.ForeignKey(CadTbCPar, models.DO_NOTHING, db_column='id_empresa', blank=True, null=True)
    dta_baixa = models.DateField(blank=True, null=True)
    vlr_baixa = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    observacao = models.CharField(max_length=100, blank=True, null=True)
    id_forma_pag = models.ForeignKey(CadTbCFpg, models.DO_NOTHING, db_column='id_forma_pag', blank=True, null=True)
    id_abertura = models.IntegerField(blank=True, null=True)
    vlr_cred_utilizado = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    id_cliente = models.ForeignKey(CadTbCCli, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    id_conta = models.IntegerField(blank=True, null=True)
    id_tipo_financeiro = models.IntegerField(blank=True, null=True)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    id_ccusto = models.IntegerField(blank=True, null=True)
    vlr_saldo_credito = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_credito_disponivel = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    id_responsavel = models.IntegerField(blank=True, null=True)
    dta_lancamento = models.DateField(blank=True, null=True)
    id_plano = models.CharField(max_length=11, blank=True, null=True)
    id_maquineta = models.ForeignKey(CadTbCMct, models.DO_NOTHING, db_column='id_maquineta', blank=True, null=True)
    id_recibo = models.IntegerField(blank=True, null=True, db_comment='Esse campo Ú utilizado para conter n║ do recibo')
    vlr_a_pagar = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_pago_ger = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_tot_ger = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    faz_conciliacao = models.BooleanField(blank=True, null=True, db_comment='Jß alimenta os dados ')

    class Meta:
        managed = False
        db_table = 'fin_tb_m_rbx'
        db_table_comment = 'Baixa de Contas a Receber'


class FinTbMRbxGer(models.Model):
    id_baixa = models.OneToOneField(FinTbMRbx, models.DO_NOTHING, db_column='id_baixa', primary_key=True)  # The composite primary key (id_baixa, id_controle) found, that is not supported. The first column is selected.
    id_controle = models.IntegerField()
    vlr_pagamento = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    dta_vencimento = models.DateField(blank=True, null=True)
    che_conta = models.IntegerField(blank=True, null=True)
    che_cheque = models.IntegerField(blank=True, null=True)
    che_banco = models.CharField(max_length=10, blank=True, null=True)
    che_emitente = models.CharField(max_length=50, blank=True, null=True)
    che_agencia = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fin_tb_m_rbx_ger'
        unique_together = (('id_baixa', 'id_controle'),)


class FinTbMRbxPpe(models.Model):
    id_baixa = models.IntegerField(primary_key=True)  # The composite primary key (id_baixa, id_pedido) found, that is not supported. The first column is selected.
    id_pedido = models.IntegerField()
    vlr_desc_pos_fat = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True, db_comment='Informe neste campo')

    class Meta:
        managed = False
        db_table = 'fin_tb_m_rbx_ppe'
        unique_together = (('id_baixa', 'id_pedido'),)
        db_table_comment = 'Pedidos que foram prestado conta na baixa do contas a receber. (sgq).'


class FinTbMRbxTit(models.Model):
    id_baixa = models.OneToOneField(FinTbMRbx, models.DO_NOTHING, db_column='id_baixa', primary_key=True)  # The composite primary key (id_baixa, id_titulo) found, that is not supported. The first column is selected.
    id_titulo = models.IntegerField()
    vlr_pagamento = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_juros = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_desconto = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_cred_utilizado = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    num_parcela = models.CharField(max_length=20, blank=True, null=True)
    per_desconto = models.FloatField(blank=True, null=True)
    vlr_a_pagar = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_titulo = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    atraso = models.IntegerField(blank=True, null=True)
    id_conta = models.IntegerField(blank=True, null=True)
    vlr_restante = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    dta_vencimento = models.DateField(blank=True, null=True)
    dta_novo_venc = models.DateField(blank=True, null=True)
    concilia = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fin_tb_m_rbx_tit'
        unique_together = (('id_baixa', 'id_titulo'),)


class FinTbMRcr(models.Model):
    id_credito = models.IntegerField(primary_key=True)
    id_empresa = models.ForeignKey(CadTbCPar, models.DO_NOTHING, db_column='id_empresa')
    origem = models.IntegerField(db_comment='0-Manual\r\n1-Baixa de Conta a Receber\r\n2-DevoluþÒo de vendas 3-Nota Fiscal de Venda; \r\n4 - Movimento de Caixa')
    num_documento = models.CharField(max_length=20)
    vlr_credito = models.DecimalField(max_digits=18, decimal_places=4)
    vlr_saldo = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    dta_credito = models.DateField()
    deb_cre = models.IntegerField(db_comment='0-Debito\n1-Credito')
    id_cliente = models.ForeignKey(CadTbCCli, models.DO_NOTHING, db_column='id_cliente')
    historico = models.CharField(max_length=100)
    id_forma_pag = models.ForeignKey(CadTbCFpg, models.DO_NOTHING, db_column='id_forma_pag', blank=True, null=True)
    pre_conta = models.IntegerField(blank=True, null=True)
    pre_cheque = models.IntegerField(blank=True, null=True)
    pre_banco = models.CharField(max_length=10, blank=True, null=True)
    pre_emitente = models.CharField(max_length=50, blank=True, null=True)
    pre_agencia = models.CharField(max_length=10, blank=True, null=True)
    id_conta = models.IntegerField(blank=True, null=True)
    car_parcelas = models.IntegerField(blank=True, null=True)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    id_baixa = models.IntegerField(blank=True, null=True)
    id_titulo = models.IntegerField(blank=True, null=True, db_comment='Campo utilizado pela nota fiscal de saÝda. Quando o cliente utiliza seu crÚdito o sitema deverß registrar a saÝda no FIN_TB_M_RCR.')
    id_fiscal = models.IntegerField(blank=True, null=True)
    id_maquineta = models.ForeignKey(CadTbCMct, models.DO_NOTHING, db_column='id_maquineta', blank=True, null=True)
    id_abertura = models.IntegerField(blank=True, null=True)
    dta_vencimento = models.DateField(blank=True, null=True)
    cancelado = models.BooleanField(blank=True, null=True)
    id_cta = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fin_tb_m_rcr'
        db_table_comment = 'Controle de CrÚdito de Cliente'


class FinTbMRec(models.Model):
    id_titulo = models.IntegerField(primary_key=True)
    id_empresa = models.ForeignKey(CadTbCPar, models.DO_NOTHING, db_column='id_empresa')
    id_cliente = models.ForeignKey(CadTbCCli, models.DO_NOTHING, db_column='id_cliente')
    num_parcela = models.CharField(max_length=20)
    dta_emissao = models.DateField()
    historico = models.CharField(max_length=100)
    vlr_parcela = models.DecimalField(max_digits=18, decimal_places=4)
    vlr_original = models.DecimalField(max_digits=18, decimal_places=4)
    dta_vencimento = models.DateField()
    dta_original = models.DateField()
    vlr_saldo = models.DecimalField(max_digits=18, decimal_places=4)
    id_fiscal = models.IntegerField(blank=True, null=True)
    origem = models.IntegerField(db_comment='0 - Manual\r\n1 - Baixa do contas a receber\r\n2 - Nota Fiscal de SaÝda\r\n3 - MovimentaþÒo de cheque 4- ConciliaþÒo Bancßria')
    id_forma_pag = models.ForeignKey(CadTbCFpg, models.DO_NOTHING, db_column='id_forma_pag')
    che_conta = models.IntegerField(blank=True, null=True)
    che_cheque = models.IntegerField(blank=True, null=True)
    che_banco = models.CharField(max_length=10, blank=True, null=True)
    che_emitente = models.CharField(max_length=50, blank=True, null=True)
    che_agencia = models.CharField(max_length=10, blank=True, null=True)
    tipo_lancamento = models.IntegerField(blank=True, null=True)
    id_local_titulo = models.ForeignKey(CadTbCLto, models.DO_NOTHING, db_column='id_local_titulo', blank=True, null=True)
    id_plano = models.ForeignKey(CadTbCPct, models.DO_NOTHING, db_column='id_plano', blank=True, null=True)
    bol_nosso_numero = models.CharField(max_length=30, blank=True, null=True)
    car_taxa = models.FloatField(blank=True, null=True)
    car_motivo_can = models.CharField(max_length=100, blank=True, null=True, db_comment='Movito de Cancelamento do CartÒo')
    car_dta_can = models.DateField(blank=True, null=True, db_comment='Data de Cancelamento')
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    seq_nosso_numero = models.IntegerField(blank=True, null=True)
    car_taxa_ope = models.FloatField(blank=True, null=True, db_comment='Campo utilizado pela tela de Fechamento de Caixa.')
    car_n_lote = models.CharField(max_length=30, blank=True, null=True, db_comment='Campo utilizado pela tela de Fechamento de Caixa.')
    car_n_lote_id_resp = models.IntegerField(blank=True, null=True, db_comment='Campo utilizado pela tela de Fechamento de Caixa.')
    car_n_lote_id_conta = models.IntegerField(blank=True, null=True, db_comment='Campo utilizado pela tela de Fechamento de Caixa.')
    id_baixa = models.IntegerField(blank=True, null=True, db_comment='Campo utilizando pela tela da baixa do contas a receber, quando preciso. Ex:  Caso a baixa seja com cartÒo de crÚdito o sistema terß de criar um novo registro no FIN_TB_M_REC.')
    situacao_chq = models.IntegerField(blank=True, null=True, db_comment='1 - Em aberto\n2 - Depositado\n3 - Devolvido\n4 - Parcial\n5 - Resgatado\n6 - Compensado')
    bol_chave = models.IntegerField(blank=True, null=True, db_comment='Campo utilizado pela geraþÒo de boleto.')
    bol_id_conta = models.IntegerField(blank=True, null=True, db_comment='Campo utilizado pela geraþÒo de boleto.')
    id_vendedor = models.IntegerField(blank=True, null=True, db_comment='Este campo serß alimentado no momento do faturamento da nota fiscal de venda.')
    car_id_maquineta = models.ForeignKey(CadTbCMct, models.DO_NOTHING, db_column='car_id_maquineta', blank=True, null=True)
    id_credito = models.IntegerField(blank=True, null=True, db_comment='Refere-se a tabela FIN_TB_M_RCR')
    id_mch = models.IntegerField(blank=True, null=True, db_comment='Campo utilizado pela tela de MovimentaþÒo de cheque')
    bol_banco = models.IntegerField(blank=True, null=True)
    id_obra = models.IntegerField(blank=True, null=True)
    dta_venc_original = models.DateField(blank=True, null=True)
    id_conciliacao = models.IntegerField(blank=True, null=True)
    dct_id_conta = models.IntegerField(blank=True, null=True, db_comment='Utilizado pela rotina Desconto de Titulos')
    dct_dta_descontado = models.DateField(blank=True, null=True)
    dct_id_local_titulo = models.IntegerField(blank=True, null=True)
    dct_id_desc = models.IntegerField(blank=True, null=True)
    vlr_saldo_anterior = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    bol_remessa_env = models.BooleanField(blank=True, null=True)
    bol_remessa_dta = models.DateField(blank=True, null=True)
    bol_remessa_id_func = models.IntegerField(blank=True, null=True)
    bol_remessa_nome_arq = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fin_tb_m_rec'
        db_table_comment = 'Contas a Receber'


class FinTbMRecHch(models.Model):
    id_titulo = models.OneToOneField(FinTbMRec, models.DO_NOTHING, db_column='id_titulo', primary_key=True)  # The composite primary key (id_titulo, id_mch) found, that is not supported. The first column is selected.
    id_mch = models.IntegerField()
    dta_movimento = models.DateField(blank=True, null=True)
    hor_movimento = models.TimeField(blank=True, null=True)
    situacao_chq = models.IntegerField(blank=True, null=True, db_comment='1 - Em aberto\n2 - Depositado\n3 - Devolvido\n4 - Parcial\n5 - Resgatado\n6 - Compensado')
    operacao = models.IntegerField(blank=True, null=True, db_comment='1 - Depositar;\n2 - Devolver;\n3 - Pagar parcial;\n4 - Resgatar;')
    id_responsavel = models.IntegerField(blank=True, null=True)
    situacao_chq_ant = models.IntegerField(blank=True, null=True, db_comment='Fica gravado a situaþÒo anterior do cheque.')

    class Meta:
        managed = False
        db_table = 'fin_tb_m_rec_hch'
        unique_together = (('id_titulo', 'id_mch'),)
        db_table_comment = 'Tabela de hist¾rico do cheque'


class FinTbMRecPag(models.Model):
    id_titulo = models.OneToOneField(FinTbMRec, models.DO_NOTHING, db_column='id_titulo', primary_key=True)  # The composite primary key (id_titulo, id_baixa) found, that is not supported. The first column is selected.
    id_baixa = models.IntegerField()
    dta_pagamento = models.DateField()
    vlr_pagamento = models.DecimalField(max_digits=18, decimal_places=2)
    per_juros = models.DecimalField(max_digits=18, decimal_places=2)
    vlr_juros = models.DecimalField(max_digits=18, decimal_places=2)
    vlr_desconto = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    historico = models.CharField(max_length=100)
    id_forma_pag = models.ForeignKey(CadTbCFpg, models.DO_NOTHING, db_column='id_forma_pag')
    id_plano = models.ForeignKey(CadTbCPct, models.DO_NOTHING, db_column='id_plano', blank=True, null=True)
    id_plano_juros = models.ForeignKey(CadTbCPct, models.DO_NOTHING, db_column='id_plano_juros', related_name='fintbmrecpag_id_plano_juros_set', blank=True, null=True)
    chp_id_situacao_chq = models.IntegerField(blank=True, null=True)
    chp_vlr_anterior = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    id_alinea = models.CharField(max_length=2, blank=True, null=True)
    chp_tipo_ocorrencia = models.CharField(max_length=1, blank=True, null=True)
    id_responsavel = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_responsavel', blank=True, null=True)
    com_substituicao = models.BooleanField(blank=True, null=True)
    id_ccusto = models.IntegerField(blank=True, null=True)
    id_plano_desconto = models.CharField(max_length=11, blank=True, null=True)
    id_fiscal = models.IntegerField(blank=True, null=True)
    origem = models.IntegerField(blank=True, null=True, db_comment='0 - Baixa do Contas a Receber;\r\n1 - Nota Fiscal de SaÝda;\r\n2 - Movimento de cheque;\r\n3 - Baixa automßtica de boleto (Rec);\r\n4 - Baixa de cart§es de crÚdito;\r\n5 - Desconto de TÝtulos')
    id_abertura = models.IntegerField(blank=True, null=True)
    vlr_cred_utilizado = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    id_mch = models.IntegerField(blank=True, null=True)
    id_cbx = models.IntegerField(blank=True, null=True)
    bol_nome_arq_ret = models.CharField(max_length=50, blank=True, null=True)
    vlr_acrescimo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True, db_comment='Este campo Ú utilizado no momento de baixar o arquivo retorno do banco, ele tem o mesmo sentido do campo VLR_JUROS.')
    id_empresa_bxa = models.IntegerField(blank=True, null=True, db_comment='Empresa que recebeu o pagamento.')
    id_dct_bxa = models.IntegerField(blank=True, null=True)
    vlr_tarifa = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fin_tb_m_rec_pag'
        unique_together = (('id_titulo', 'id_baixa'),)


class ObrTbCEqp(models.Model):
    id_equipamento = models.IntegerField(primary_key=True)
    controle = models.CharField(max_length=15, blank=True, null=True)
    descricao = models.CharField(max_length=50)
    especificacao = models.CharField(max_length=50, blank=True, null=True)
    modelo = models.CharField(max_length=30, blank=True, null=True)
    fabricante = models.CharField(max_length=30, blank=True, null=True)
    tipo = models.IntegerField()
    dta_compra = models.DateField()
    local_compra = models.CharField(max_length=30, blank=True, null=True)
    vlr_compra = models.DecimalField(max_digits=18, decimal_places=2)
    garantia = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'obr_tb_c_eqp'
        db_table_comment = 'Equipamentos'


class ObrTbCGru(models.Model):
    id_grupo_orca = models.CharField(primary_key=True, max_length=10)
    descricao = models.CharField(max_length=50)
    ativo = models.BooleanField()
    mes_cronograma = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'obr_tb_c_gru'
        db_table_comment = 'Grupo de Itens da Obra'


class ObrTbCObr(models.Model):
    id_obra = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=50)
    ativo = models.BooleanField()
    endereco = models.CharField(max_length=50)
    id_cidade = models.ForeignKey(CadTbCCid, models.DO_NOTHING, db_column='id_cidade', blank=True, null=True)
    cep = models.CharField(max_length=9, blank=True, null=True)
    tel_fixo = models.CharField(max_length=14, blank=True, null=True)
    fax = models.CharField(max_length=14, blank=True, null=True)
    obs = models.CharField(max_length=800, blank=True, null=True)
    dta_entrega = models.DateField()
    id_cliente = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'obr_tb_c_obr'
        db_table_comment = 'Cadastro de Obras'


class OfiTbCCat(models.Model):
    id_cat = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=60)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ofi_tb_c_cat'
        db_table_comment = 'Cadastro de Categorias'


class OfiTbCTio(models.Model):
    id_tipo_os = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=30, blank=True, null=True)
    tipo = models.IntegerField(blank=True, null=True, db_comment='0 - Normal\r\n1 - Garantia')

    class Meta:
        managed = False
        db_table = 'ofi_tb_c_tio'


class OfiTbMAge(models.Model):
    id_agenda = models.IntegerField(primary_key=True)
    id_empresa = models.IntegerField()
    nome_cliente = models.CharField(max_length=50, blank=True, null=True)
    dta_agenda = models.DateField(blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    observacao = models.CharField(max_length=800, blank=True, null=True)
    placa = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ofi_tb_m_age'
        db_table_comment = 'Agendamento de veiculos'


class OfiTbMCvl(models.Model):
    id_controle = models.IntegerField(primary_key=True)
    dta_controle = models.DateField()
    tipo_movimento = models.IntegerField(db_comment='0 - IPVA; 1 - Multa; 2 - Seguro')
    id_meq = models.ForeignKey('PcpTbCMeq', models.DO_NOTHING, db_column='id_meq')
    id_empresa = models.ForeignKey(CadTbCPar, models.DO_NOTHING, db_column='id_empresa')

    class Meta:
        managed = False
        db_table = 'ofi_tb_m_cvl'


class OfiTbMCvlIpv(models.Model):
    id_controle = models.OneToOneField(OfiTbMCvl, models.DO_NOTHING, db_column='id_controle', primary_key=True)  # The composite primary key (id_controle, id_ipva) found, that is not supported. The first column is selected.
    id_ipva = models.IntegerField()
    ano_exercicio = models.CharField(max_length=4)
    vlr_seguro_obg = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_ipva = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    dta_venc_unica = models.DateField(blank=True, null=True)
    dta_pag_unica = models.DateField(blank=True, null=True)
    dta_venc_cta01 = models.DateField(blank=True, null=True)
    dta_pag_cta01 = models.DateField(blank=True, null=True)
    valor_cta01 = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    dta_venc_cta02 = models.DateField(blank=True, null=True)
    dta_pag_cta02 = models.DateField(blank=True, null=True)
    valor_cta02 = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    dta_venc_cta03 = models.DateField(blank=True, null=True)
    dta_pag_cta03 = models.DateField(blank=True, null=True)
    valor_cta03 = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ofi_tb_m_cvl_ipv'
        unique_together = (('id_controle', 'id_ipva'),)


class OfiTbMCvlMlt(models.Model):
    id_controle = models.OneToOneField(OfiTbMCvl, models.DO_NOTHING, db_column='id_controle', primary_key=True)  # The composite primary key (id_controle, id_multa) found, that is not supported. The first column is selected.
    id_multa = models.IntegerField()
    local = models.CharField(max_length=100)
    cod_infracao = models.CharField(max_length=30)
    dta_vencimento = models.DateField(blank=True, null=True)
    vlr_multa = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_pago = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    dta_pagamento = models.DateField(blank=True, null=True)
    processo = models.CharField(max_length=30, blank=True, null=True)
    recurso = models.BooleanField(blank=True, null=True)
    recurso_aceito = models.BooleanField(blank=True, null=True)
    pago = models.BooleanField(blank=True, null=True)
    obs = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ofi_tb_m_cvl_mlt'
        unique_together = (('id_controle', 'id_multa'),)


class OfiTbMCvlSgr(models.Model):
    id_controle = models.OneToOneField(OfiTbMCvl, models.DO_NOTHING, db_column='id_controle', primary_key=True)
    id_seguro = models.IntegerField()
    dta_contrato = models.DateField(blank=True, null=True)
    dta_vigencia = models.DateField(blank=True, null=True)
    num_apolice = models.CharField(max_length=30)
    vlr_seguro = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_franquia = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_cobertura = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_danos_materiais = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_danos_corporais = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    corretor_nome = models.CharField(max_length=50, blank=True, null=True)
    corretor_telefone = models.CharField(max_length=15, blank=True, null=True)
    corretor_celular = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ofi_tb_m_cvl_sgr'


class OfiTbMOcq(models.Model):
    id_orcamento = models.IntegerField(primary_key=True)
    id_empresa = models.IntegerField()
    id_equipamento = models.IntegerField(blank=True, null=True)
    dta_orcamento = models.DateField(blank=True, null=True)
    dta_validade = models.DateField(blank=True, null=True)
    id_cliente = models.IntegerField(blank=True, null=True)
    nome_cliente = models.CharField(max_length=50, blank=True, null=True)
    id_funcionario = models.IntegerField(blank=True, null=True)
    id_analista = models.IntegerField(blank=True, null=True)
    id_condicao_pag = models.IntegerField(blank=True, null=True)
    vlr_servicos = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_produtos = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_terceiro = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    des_servicos = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    des_produtos = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_total = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True, db_comment='0 - Em aberto;\r\n1 - Importado;\r\n2 - Cancelado;')
    obs = models.CharField(max_length=100, blank=True, null=True)
    doc_cnpj_cpf = models.CharField(max_length=14, blank=True, null=True)
    hor_orcamento = models.TimeField(blank=True, null=True)
    can_motivo = models.CharField(max_length=100, blank=True, null=True)
    can_data = models.DateField(blank=True, null=True)
    can_hora = models.TimeField(blank=True, null=True)
    can_usuario = models.IntegerField(blank=True, null=True)
    serial = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ofi_tb_m_ocq'
        db_table_comment = 'Orþamento de Equipamentos'


class OfiTbMOcqIte(models.Model):
    id_orcamento = models.OneToOneField(OfiTbMOcq, models.DO_NOTHING, db_column='id_orcamento', primary_key=True)  # The composite primary key (id_orcamento, id_sequencia) found, that is not supported. The first column is selected.
    id_sequencia = models.IntegerField()
    id_item = models.IntegerField()
    id_busca_item = models.CharField(max_length=30, blank=True, null=True)
    qtde = models.FloatField()
    vlr_unitario = models.DecimalField(max_digits=18, decimal_places=4)
    vlr_bruto = models.DecimalField(max_digits=18, decimal_places=4)
    per_desconto = models.FloatField()
    vlr_desconto = models.DecimalField(max_digits=18, decimal_places=4)
    vlr_liquido = models.DecimalField(max_digits=18, decimal_places=4)
    id_terceiro = models.IntegerField(blank=True, null=True)
    vlr_unitario_orig = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True, db_comment='Este campo irß armazenar o preþo original (Que Ú calculado pelo sistema).  Assim o sistema saberß se o usußrio alterou o preþo no pedido ao verificar VLR_UNITARIO vs VLR_UNITARIO_ORIG')
    nome_ite = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ofi_tb_m_ocq_ite'
        unique_together = (('id_orcamento', 'id_sequencia'),)


class OfiTbMOcv(models.Model):
    id_orcamento = models.IntegerField(primary_key=True)
    id_empresa = models.IntegerField()
    placa = models.CharField(max_length=8, blank=True, null=True)
    km_atual = models.IntegerField(blank=True, null=True)
    dta_orcamento = models.DateField(blank=True, null=True)
    dta_validade = models.DateField(blank=True, null=True)
    id_cliente = models.IntegerField(blank=True, null=True)
    nome_cliente = models.CharField(max_length=50, blank=True, null=True)
    id_funcionario = models.IntegerField(blank=True, null=True)
    id_analista = models.IntegerField(blank=True, null=True)
    id_condicao_pag = models.IntegerField(blank=True, null=True)
    vlr_servicos = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_produtos = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_terceiro = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    des_servicos = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    des_produtos = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_total = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True, db_comment='0 - Em aberto;\n1 - Importado;\n2 - Cancelado;')
    obs = models.CharField(max_length=100, blank=True, null=True)
    doc_cnpj_cpf = models.CharField(max_length=14, blank=True, null=True)
    hor_orcamento = models.TimeField(blank=True, null=True)
    can_motivo = models.CharField(max_length=100, blank=True, null=True)
    can_data = models.DateField(blank=True, null=True)
    can_hora = models.TimeField(blank=True, null=True)
    can_usuario = models.IntegerField(blank=True, null=True)
    tipo_orcamento = models.IntegerField(blank=True, null=True, db_comment='1-VeÝculo;2-Tratores')
    chassi = models.CharField(max_length=20, blank=True, null=True)
    id_orcamento_mob = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ofi_tb_m_ocv'
        db_table_comment = 'Orþamento de Veiculos'


class OfiTbMOcvFot(models.Model):
    id_orcamento = models.OneToOneField(OfiTbMOcv, models.DO_NOTHING, db_column='id_orcamento', primary_key=True)  # The composite primary key (id_orcamento, id_sequencia) found, that is not supported. The first column is selected.
    id_sequencia = models.IntegerField()
    caminho_foto = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ofi_tb_m_ocv_fot'
        unique_together = (('id_orcamento', 'id_sequencia'),)


class OfiTbMOcvIte(models.Model):
    id_orcamento = models.OneToOneField(OfiTbMOcv, models.DO_NOTHING, db_column='id_orcamento', primary_key=True)  # The composite primary key (id_orcamento, id_sequencia) found, that is not supported. The first column is selected.
    id_sequencia = models.IntegerField()
    id_item = models.IntegerField()
    id_busca_item = models.CharField(max_length=30, blank=True, null=True)
    qtde = models.FloatField()
    vlr_unitario = models.DecimalField(max_digits=18, decimal_places=4)
    vlr_bruto = models.DecimalField(max_digits=18, decimal_places=4)
    per_desconto = models.FloatField()
    vlr_desconto = models.DecimalField(max_digits=18, decimal_places=4)
    vlr_liquido = models.DecimalField(max_digits=18, decimal_places=4)
    id_terceiro = models.IntegerField(blank=True, null=True)
    vlr_unitario_orig = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True, db_comment='Este campo irß armazenar o preþo original (Que Ú calculado pelo sistema).  Assim o sistema saberß se o usußrio alterou o preþo no pedido ao verificar VLR_UNITARIO vs VLR_UNITARIO_ORIG')
    nome_ite = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ofi_tb_m_ocv_ite'
        unique_together = (('id_orcamento', 'id_sequencia'),)


class OfiTbMOrv(models.Model):
    id_ordem = models.IntegerField(primary_key=True)
    id_empresa = models.IntegerField()
    dta_emissao = models.DateField(blank=True, null=True)
    dta_entrega = models.DateField(blank=True, null=True)
    id_cliente = models.IntegerField(blank=True, null=True)
    id_veiculo = models.IntegerField(blank=True, null=True)
    km_atual = models.IntegerField(blank=True, null=True)
    tanque_combus = models.IntegerField(blank=True, null=True)
    id_forma_pag = models.IntegerField(blank=True, null=True)
    id_condicao_pag = models.IntegerField(blank=True, null=True)
    id_analista = models.IntegerField(blank=True, null=True)
    id_orcamento = models.IntegerField(blank=True, null=True)
    obs_reclamacao = models.CharField(max_length=800, blank=True, null=True)
    obs_problema = models.CharField(max_length=800, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True, db_comment='0 û Aberta\n1 û Em Andamento\n2 û Fechada\n3 û Faturada\n4 - Cancelada')
    vlr_produtos = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_desc_produtos = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    per_desc_produtos = models.FloatField(blank=True, null=True)
    vlr_prod_liquido = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_serv_bruto = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_desc_servicos = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    per_desc_servicos = models.FloatField(blank=True, null=True)
    vlr_ser_liquido = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_terceiro = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_desc_terceiro = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    per_desc_terceiro = models.FloatField(blank=True, null=True)
    vlr_terc_liquido = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_despesas = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_credito = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_total = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    id_tipo_os = models.ForeignKey(OfiTbCTio, models.DO_NOTHING, db_column='id_tipo_os', blank=True, null=True)
    can_usuario = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='can_usuario', blank=True, null=True)
    can_data = models.DateField(blank=True, null=True)
    can_motivo = models.CharField(max_length=100, blank=True, null=True)
    can_hora = models.TimeField(blank=True, null=True)
    rea_usuario = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='rea_usuario', related_name='ofitbmorv_rea_usuario_set', blank=True, null=True)
    rea_data = models.DateField(blank=True, null=True)
    rea_hora = models.TimeField(blank=True, null=True)
    rea_motivo = models.CharField(max_length=100, blank=True, null=True)
    dta_fechamento = models.DateField(blank=True, null=True)
    id_almoxarifado = models.IntegerField(blank=True, null=True)
    vlr_cred_produtos = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_cred_servicos = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    observacoes = models.CharField(max_length=400, blank=True, null=True)
    status_painel = models.IntegerField(blank=True, null=True, db_comment='0 - Aguardando Ordem de Serviþo\n1 - Pr¾ximo Ordem de Serviþo\n2 - Em Serviþo\n3 - PrÚ-InspeþÒo\n4 - Aguardando Lavagem\n5 - InspeþÒo Final\n6 - Aguardando AprovaþÒo\n7 - Aguardando Peþas\n8 - Aguardando Serviþo\n9 - Aguardando PrÚ-Entrega\n10 - Aguardando Entrega\n11 - Entregue\n')
    hor_emissao = models.TimeField(blank=True, null=True)
    hor_fechamento = models.TimeField(blank=True, null=True)
    separa_prod_serv = models.BooleanField(blank=True, null=True)
    id_equipamento = models.ForeignKey(CadTbCEqp, models.DO_NOTHING, db_column='id_equipamento', blank=True, null=True)
    tipo_ordem = models.IntegerField(blank=True, null=True, db_comment='1-VeÝculo;2-Tratores;3-Equipamentos')
    chassi = models.CharField(max_length=20, blank=True, null=True)
    id_ordem_orig_gar = models.IntegerField(blank=True, null=True)
    id_fiscal_ref_entrada = models.IntegerField(blank=True, null=True)
    ordem_substituicao = models.BooleanField(blank=True, null=True)
    orv_gera_fin_separado = models.BooleanField(blank=True, null=True, db_comment='Campo preenchido automaticamente pelo parÔmetro da oficina. Indica se o financeiro da oficina serß gerado separado.')
    iss_valor_retido = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    id_ordem_mob = models.IntegerField(blank=True, null=True)
    id_meq = models.IntegerField(blank=True, null=True)
    horimetro = models.FloatField(blank=True, null=True)
    id_atendente = models.IntegerField(blank=True, null=True)
    id_mecanico = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ofi_tb_m_orv'
        db_table_comment = 'Ordem de Serviþos de Veiculos'


class OfiTbMOrvDes(models.Model):
    id_ordem = models.OneToOneField(OfiTbMOrv, models.DO_NOTHING, db_column='id_ordem', primary_key=True)  # The composite primary key (id_ordem, id_sequencia) found, that is not supported. The first column is selected.
    id_sequencia = models.IntegerField()
    dta_despesa = models.DateField(blank=True, null=True)
    local = models.CharField(max_length=50, blank=True, null=True)
    tipo = models.IntegerField(blank=True, null=True, db_comment='0 - Hotel\n1 - Almoþo  \n2 - Jantar\n3 - CombustÝvel\n4 - Outros')
    vlr_despesa = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ofi_tb_m_orv_des'
        unique_together = (('id_ordem', 'id_sequencia'),)


class OfiTbMOrvFot(models.Model):
    id_ordem = models.OneToOneField(OfiTbMOrv, models.DO_NOTHING, db_column='id_ordem', primary_key=True)  # The composite primary key (id_ordem, id_sequencia) found, that is not supported. The first column is selected.
    id_sequencia = models.IntegerField()
    caminho_foto = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ofi_tb_m_orv_fot'
        unique_together = (('id_ordem', 'id_sequencia'),)


class OfiTbMOrvIte(models.Model):
    id_ordem = models.OneToOneField(OfiTbMOrv, models.DO_NOTHING, db_column='id_ordem', primary_key=True)  # The composite primary key (id_ordem, id_sequencia) found, that is not supported. The first column is selected.
    id_sequencia = models.IntegerField()
    id_item = models.IntegerField()
    id_busca_item = models.CharField(max_length=30, blank=True, null=True)
    qtde = models.FloatField()
    vlr_unitario = models.DecimalField(max_digits=18, decimal_places=4)
    vlr_bruto = models.DecimalField(max_digits=18, decimal_places=4)
    per_desconto = models.FloatField()
    vlr_desconto = models.DecimalField(max_digits=18, decimal_places=4)
    vlr_liquido = models.DecimalField(max_digits=18, decimal_places=4)
    id_mecanico = models.IntegerField(blank=True, null=True)
    id_terceiro = models.IntegerField(blank=True, null=True)
    id_responsavel = models.IntegerField(blank=True, null=True)
    cancelada = models.BooleanField(blank=True, null=True)
    id_sequencia_ite_ocv = models.IntegerField(blank=True, null=True, db_comment='Campo utilizado no momento da ImportaþÒo do Orþamento da Oficina.')
    id_requisicao = models.IntegerField(blank=True, null=True, db_comment='Este campo serß alimentado pela tela OFI_FM_M_RQV')
    can_usuario = models.IntegerField(blank=True, null=True, db_comment='Campo utilizado pela tela OFI_FM_M_RQV no momento de cancelamento de peþa;')
    can_data = models.DateField(blank=True, null=True, db_comment='Campo utilizado pela tela OFI_FM_M_RQV no momento de cancelamento de peþa;')
    can_hora = models.TimeField(blank=True, null=True, db_comment='Campo utilizado pela tela OFI_FM_M_RQV no momento de cancelamento de peþa;')
    can_motivo = models.CharField(max_length=100, blank=True, null=True, db_comment='Campo utilizado pela tela OFI_FM_M_RQV no momento de cancelamento de peþa;')
    dta_requisicao = models.DateField(blank=True, null=True, db_comment='Este campo serß alimentado quando o campo id_requisicao for preenchido')
    id_cor = models.IntegerField(blank=True, null=True)
    id_tamanho = models.IntegerField(blank=True, null=True)
    vlr_unitario_orig = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True, db_comment='Este campo irß armazenar o preþo original (Que Ú calculado pelo sistema).  Assim o sistema saberß se o usußrio alterou o preþo no pedido ao verificar VLR_UNITARIO vs VLR_UNITARIO_ORIG')
    id_ordem_subst = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ofi_tb_m_orv_ite'
        unique_together = (('id_ordem', 'id_sequencia'),)


class OfiTbMOrvTit(models.Model):
    id_ordem = models.OneToOneField(OfiTbMOrv, models.DO_NOTHING, db_column='id_ordem', primary_key=True)  # The composite primary key (id_ordem, id_titulo) found, that is not supported. The first column is selected.
    id_titulo = models.IntegerField()
    dias = models.IntegerField()
    dta_vencimento = models.DateField()
    vlr_titulo = models.DecimalField(max_digits=18, decimal_places=4)
    che_banco = models.CharField(max_length=10, blank=True, null=True)
    che_agencia = models.CharField(max_length=10, blank=True, null=True)
    che_conta = models.IntegerField(blank=True, null=True)
    che_numero = models.IntegerField(blank=True, null=True)
    che_emitente = models.CharField(max_length=50, blank=True, null=True)
    id_forma_pag = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ofi_tb_m_orv_tit'
        unique_together = (('id_ordem', 'id_titulo'),)


class OfiTbMOrvTitSer(models.Model):
    id_ordem = models.OneToOneField(OfiTbMOrv, models.DO_NOTHING, db_column='id_ordem', primary_key=True)  # The composite primary key (id_ordem, id_titulo) found, that is not supported. The first column is selected.
    id_titulo = models.IntegerField()
    dias = models.IntegerField()
    dta_vencimento = models.DateField()
    vlr_titulo = models.DecimalField(max_digits=18, decimal_places=4)
    che_banco = models.CharField(max_length=10, blank=True, null=True)
    che_agencia = models.CharField(max_length=10, blank=True, null=True)
    che_conta = models.IntegerField(blank=True, null=True)
    che_numero = models.IntegerField(blank=True, null=True)
    che_emitente = models.CharField(max_length=50, blank=True, null=True)
    id_forma_pag = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ofi_tb_m_orv_tit_ser'
        unique_together = (('id_ordem', 'id_titulo'),)
        db_table_comment = 'Ordem de Serviþo - Titulos dos Serviþos'


class OfiTbMPos(models.Model):
    id_posvenda = models.IntegerField(primary_key=True)
    id_empresa = models.IntegerField(blank=True, null=True)
    dta_posvenda = models.DateField(blank=True, null=True)
    situacao = models.IntegerField(blank=True, null=True, db_comment='0 - Satisfeito;  1 - Insatisfeito;  2 - NÒo encontrado;')
    observaþÒo = models.CharField(max_length=100, blank=True, null=True)
    solucao = models.CharField(max_length=100, blank=True, null=True)
    id_responsavel = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_responsavel', blank=True, null=True)
    hor_posvenda = models.TimeField(blank=True, null=True)
    id_ordem = models.ForeignKey(OfiTbMOrv, models.DO_NOTHING, db_column='id_ordem', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ofi_tb_m_pos'
        db_table_comment = 'Tabela de P¾s Venda de Oficina'


class PcpTbCCdp(models.Model):
    id_item = models.OneToOneField(CadTbCIte, models.DO_NOTHING, db_column='id_item', primary_key=True)
    dta_lancamento = models.DateField()
    med_comp_01 = models.FloatField()
    med_comp_02 = models.FloatField()
    med_comp_03 = models.FloatField()
    med_comp_media = models.FloatField()
    med_largura_01 = models.FloatField()
    med_largura_02 = models.FloatField()
    med_largura_03 = models.FloatField()
    med_largura_media = models.FloatField()
    med_altura_01 = models.FloatField()
    med_altura_02 = models.FloatField()
    med_altura_03 = models.FloatField()
    med_altura_media = models.FloatField()
    situacao = models.BooleanField(db_comment='true - Aprovado  False - Reprovado')
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_c_cdp'
        db_table_comment = 'Controle Dimensional de Produto Acabado\nConforme Planilha: I 7.5.9-02'


class PcpTbCCdr(models.Model):
    id_cdr = models.IntegerField(primary_key=True)
    id_grupo = models.ForeignKey(CadTbCGru, models.DO_NOTHING, db_column='id_grupo')
    id_cor_grupo = models.IntegerField()
    tipo_cadarco = models.IntegerField(db_comment='1 - 18 mm\n2 - 35 mm\n3 - 40 mm')
    id_cor_cadarco = models.ForeignKey(CadTbCCor, models.DO_NOTHING, db_column='id_cor_cadarco')
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_c_cdr'
        db_table_comment = 'Tabela para uso de cadarþo'


class PcpTbCCin(models.Model):
    id_cin = models.IntegerField(primary_key=True)
    id_ins = models.ForeignKey('PcpTbCIns', models.DO_NOTHING, db_column='id_ins')
    id_num_seq = models.IntegerField(blank=True, null=True)
    tipo_mei = models.IntegerField(blank=True, null=True)
    requer_calibracao = models.IntegerField(blank=True, null=True)
    situacao_instrumento = models.IntegerField(blank=True, null=True, db_comment='0- Aprovado\n1- Retido nÒo usado\n2- Descartado\n3- Em calibraþÒo externa')
    cert_erro_admissivel = models.CharField(max_length=20, blank=True, null=True)
    cert_num = models.CharField(max_length=20, blank=True, null=True)
    cert_id_fornecedor = models.IntegerField(blank=True, null=True)
    cert_id_resp_inspecao = models.IntegerField(blank=True, null=True)
    cert_dta_verificacao = models.DateField(blank=True, null=True)
    num_seq = models.IntegerField(blank=True, null=True)
    tr_sit_encosto = models.IntegerField(blank=True, null=True)
    tr_sit_funcionamento = models.IntegerField(blank=True, null=True)
    tr_sit_escala = models.IntegerField(blank=True, null=True)
    tr_sit_aspecto_geral = models.IntegerField(blank=True, null=True)
    tr_sit_escala_padrao = models.IntegerField(blank=True, null=True)
    tr_resultado = models.IntegerField(blank=True, null=True)
    tr_sit_inspecao = models.IntegerField(blank=True, null=True)
    tr_id_resp_inspecao = models.IntegerField(blank=True, null=True)
    tr_dta_verificacao = models.DateField(blank=True, null=True)
    tr_reg_acao_tomada = models.CharField(max_length=200, blank=True, null=True)
    cal_efet_frequencia = models.CharField(max_length=10, blank=True, null=True)
    cal_efet_proxima = models.DateField(blank=True, null=True)
    numero_nfe = models.IntegerField(blank=True, null=True)
    historico_instrumento = models.CharField(max_length=100, blank=True, null=True)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_c_cin'
        db_table_comment = 'Controle do Instrumento\nConforme Planilha: P 7.6-01 (Controle de Instrumentos de MediþÒo)'


class PcpTbCCinLns(models.Model):
    id_cin = models.OneToOneField(PcpTbCCin, models.DO_NOTHING, db_column='id_cin', primary_key=True)  # The composite primary key (id_cin, id_cin_lns) found, that is not supported. The first column is selected.
    id_cin_lns = models.IntegerField()
    dta_cadastro = models.DateField()
    id_setor = models.ForeignKey(CadTbCSet, models.DO_NOTHING, db_column='id_setor')
    tolerancia_processo = models.CharField(max_length=30, blank=True, null=True)
    frequencia = models.CharField(max_length=15, blank=True, null=True)
    id_responsavel = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_responsavel')

    class Meta:
        managed = False
        db_table = 'pcp_tb_c_cin_lns'
        unique_together = (('id_cin', 'id_cin_lns'),)


class PcpTbCCle(models.Model):
    id_cle = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_c_cle'
        db_table_comment = 'Tabela de ClassificaþÒo de Etiqueta'


class PcpTbCCnf(models.Model):
    id_conformidade = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=50)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_c_cnf'
        db_table_comment = 'Conformidade'


class PcpTbCCrg(models.Model):
    id_cargo = models.IntegerField(primary_key=True)
    aprovador = models.CharField(max_length=50, blank=True, null=True)
    id_setor = models.ForeignKey(CadTbCSet, models.DO_NOTHING, db_column='id_setor')
    descricao = models.CharField(max_length=70)
    objetivo_cargo = models.CharField(max_length=200, blank=True, null=True)
    atribuicoes = models.CharField(max_length=300)
    requisitos = models.CharField(max_length=500)
    data_aprovacao = models.DateField()
    tipo = models.IntegerField(blank=True, null=True, db_comment='0 - Vendedor\n1 - Representante\n2 - Outros\n3 - MecÔnico')
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_c_crg'
        db_table_comment = 'Cargos'


class PcpTbCCue(models.Model):
    id_cue = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_c_cue'
        db_table_comment = 'Tabela de Cadastro Uso da Etiqueta\nex: Uso Geral;\n      Uso Infantil;'


class PcpTbCDis(models.Model):
    id_dis = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=80)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_c_dis'
        db_table_comment = 'Cadastro de DisposiþÒo'


class PcpTbCEsp(models.Model):
    id_especificacao = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=50)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_c_esp'


class PcpTbCFpi(models.Model):
    id_item = models.ForeignKey(CadTbCIte, models.DO_NOTHING, db_column='id_item')
    id_cor = models.IntegerField()
    id_tamanho = models.IntegerField()
    id_fpi = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_c_fpi'
        db_table_comment = 'Ficha TÚcnica de ProduþÒo do Item.'


class PcpTbCFpiFti(models.Model):
    id_item = models.ForeignKey(CadTbCIte, models.DO_NOTHING, db_column='id_item')
    id_cor = models.IntegerField()
    id_tamanho = models.IntegerField()
    tipo_acao = models.IntegerField(db_comment='1 - A requisitar\n2 - A executar')
    qtde = models.FloatField()
    id_setor = models.ForeignKey(CadTbCSet, models.DO_NOTHING, db_column='id_setor')
    id_fpi = models.OneToOneField(PcpTbCFpi, models.DO_NOTHING, db_column='id_fpi', primary_key=True)  # The composite primary key (id_fpi, id_fpi_fti) found, that is not supported. The first column is selected.
    id_fpi_fti = models.IntegerField()
    id_busca_item = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'pcp_tb_c_fpi_fti'
        unique_together = (('id_fpi', 'id_fpi_fti'),)
        db_table_comment = 'Itens da Ficha TÚcnica de ProduþÒo do Item.'


class PcpTbCFpiFtiIte(models.Model):
    id_fpi = models.OneToOneField(PcpTbCFpiFti, models.DO_NOTHING, db_column='id_fpi', primary_key=True)  # The composite primary key (id_fpi, id_fpi_fti, id_fpi_fti_ite) found, that is not supported. The first column is selected.
    id_fpi_fti = models.IntegerField()
    id_fpi_fti_ite = models.IntegerField()
    id_item = models.ForeignKey(CadTbCIte, models.DO_NOTHING, db_column='id_item')
    id_cor = models.IntegerField()
    id_tamanho = models.IntegerField()
    qtde = models.IntegerField()
    id_busca_item = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'pcp_tb_c_fpi_fti_ite'
        unique_together = (('id_fpi', 'id_fpi_fti', 'id_fpi_fti_ite'),)


class PcpTbCFte(models.Model):
    id_fte = models.IntegerField(primary_key=True)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    requisitos = models.CharField(max_length=300, blank=True, null=True)
    inf_contato = models.CharField(max_length=80, blank=True, null=True)
    inf_remocao = models.CharField(max_length=80, blank=True, null=True)
    inf_sac = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_c_fte'


class PcpTbCFteEtq(models.Model):
    id_fte = models.OneToOneField(PcpTbCFte, models.DO_NOTHING, db_column='id_fte', primary_key=True)  # The composite primary key (id_fte, id_fte_etq) found, that is not supported. The first column is selected.
    id_fte_etq = models.IntegerField()
    cod_int_etq = models.CharField(max_length=10)
    cod_int_etq_rev = models.CharField(max_length=5)
    descricao = models.CharField(max_length=60)
    especificacoes = models.CharField(max_length=200)
    img_modelo = models.BinaryField(blank=True, null=True)
    texto_livre1 = models.CharField(max_length=100, blank=True, null=True)
    texto_livre2 = models.CharField(max_length=100, blank=True, null=True)
    modelo_etq = models.IntegerField(blank=True, null=True, db_comment='1 û ColchÒo padrÒo\n2 û ColchÒo baby\n3 û ColchÒo bordado\n')
    etq_tecnica = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_c_fte_etq'
        unique_together = (('id_fte', 'id_fte_etq'),)


class PcpTbCIns(models.Model):
    id_ins = models.IntegerField(primary_key=True)
    sigla = models.CharField(max_length=20, blank=True, null=True)
    id_mde = models.ForeignKey('PcpTbCMde', models.DO_NOTHING, db_column='id_mde')
    id_fabricante = models.ForeignKey(CadTbCFor, models.DO_NOTHING, db_column='id_fabricante')
    nro_serie = models.CharField(max_length=20, blank=True, null=True)
    dta_cadastro = models.DateField()
    resolucao_menor_divisao = models.CharField(max_length=15, blank=True, null=True)
    id_tin = models.ForeignKey('PcpTbCTin', models.DO_NOTHING, db_column='id_tin')
    scala = models.CharField(max_length=20, blank=True, null=True)
    garantia = models.BooleanField(blank=True, null=True)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_c_ins'
        db_table_comment = 'Cadastro de Instrumentos\nConforme Planilha: P 7.6-01 (Controle de Instrumentos de MediþÒo)'


class PcpTbCLme(models.Model):
    id_lme = models.IntegerField(primary_key=True)
    data = models.DateField()
    id_responsavel = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_responsavel')
    observacao = models.CharField(max_length=200, blank=True, null=True)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_c_lme'


class PcpTbCLmeDoc(models.Model):
    id_lme = models.OneToOneField(PcpTbCLme, models.DO_NOTHING, db_column='id_lme', primary_key=True)  # The composite primary key (id_lme, id_lme_d) found, that is not supported. The first column is selected.
    id_lme_d = models.IntegerField()
    id_tlm = models.ForeignKey('PcpTbCTlm', models.DO_NOTHING, db_column='id_tlm')
    origem = models.IntegerField(db_comment='0 - Interna\n1 - Externa')
    descricao = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20, db_comment='Este c¾digo refere-se ao c¾digo da ISO.')
    revisao = models.CharField(max_length=5)
    data_aprovacao = models.DateField()
    id_setor = models.IntegerField(db_comment='0 - AdministraþÒo\n1 - ProduþÒo\n2 - Qualidade')
    distribuicao_tipo = models.IntegerField(db_comment='0 - FÝsico\n1 - Informatizado')
    observacao = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_c_lme_doc'
        unique_together = (('id_lme', 'id_lme_d'),)


class PcpTbCLmeDpg(models.Model):
    id_lme = models.OneToOneField(PcpTbCLmeDoc, models.DO_NOTHING, db_column='id_lme', primary_key=True)  # The composite primary key (id_lme, id_lme_d, id_lme_dp) found, that is not supported. The first column is selected.
    id_lme_d = models.IntegerField()
    id_lme_dp = models.IntegerField()
    data_cadastro = models.DateField()
    nome_formulario = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_c_lme_dpg'
        unique_together = (('id_lme', 'id_lme_d', 'id_lme_dp'),)


class PcpTbCLmeDrp(models.Model):
    id_lme = models.OneToOneField(PcpTbCLmeDoc, models.DO_NOTHING, db_column='id_lme', primary_key=True)  # The composite primary key (id_lme, id_lme_d, id_lme_dr) found, that is not supported. The first column is selected.
    id_lme_d = models.IntegerField()
    id_lme_dr = models.IntegerField()
    data = models.DateField()
    situacao = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_c_lme_drp'
        unique_together = (('id_lme', 'id_lme_d', 'id_lme_dr'),)


class PcpTbCLmeDrv(models.Model):
    id_lme = models.OneToOneField(PcpTbCLmeDoc, models.DO_NOTHING, db_column='id_lme', primary_key=True)  # The composite primary key (id_lme, id_lme_d, id_lme_dv) found, that is not supported. The first column is selected.
    id_lme_d = models.IntegerField()
    id_lme_dv = models.IntegerField()
    data_revisao = models.DateField()
    revisao = models.IntegerField()
    historico_alteracao = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_c_lme_drv'
        unique_together = (('id_lme', 'id_lme_d', 'id_lme_dv'),)


class PcpTbCMde(models.Model):
    id_mde = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=50)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_c_mde'
        db_table_comment = 'Modelo de Equipamento e Instrumentos'


class PcpTbCMeq(models.Model):
    id_meq = models.IntegerField(primary_key=True)
    id_empresa = models.ForeignKey(CadTbCPar, models.DO_NOTHING, db_column='id_empresa')
    cod_equipamento = models.CharField(max_length=15, blank=True, null=True)
    descricao = models.CharField(max_length=50, blank=True, null=True)
    id_mde = models.ForeignKey(PcpTbCMde, models.DO_NOTHING, db_column='id_mde', blank=True, null=True)
    id_fabricante = models.ForeignKey(CadTbCFor, models.DO_NOTHING, db_column='id_fabricante', blank=True, null=True)
    nro_serie = models.CharField(max_length=20, blank=True, null=True)
    dta_cadastro = models.DateField(blank=True, null=True)
    dta_compra = models.DateField(blank=True, null=True)
    numero_nf = models.IntegerField(blank=True, null=True)
    gara_validade = models.DateField(blank=True, null=True)
    gara_existe = models.BooleanField(blank=True, null=True)
    id_resp_lancto = models.IntegerField(blank=True, null=True)
    tipo_mei = models.IntegerField(blank=True, null=True, db_comment='0 - Mßquina  1 - Equipamento   2 - Outros')
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    id_setor = models.ForeignKey(CadTbCSet, models.DO_NOTHING, db_column='id_setor', blank=True, null=True)
    vlr_aquisicao = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    nome_fabricante = models.CharField(max_length=60, blank=True, null=True)
    vlr_hora = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    vlr_comissao = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    id_placa = models.CharField(max_length=8, blank=True, null=True)
    km_aquisicao = models.FloatField(blank=True, null=True)
    dta_aquisicao = models.DateField(blank=True, null=True)
    km_atual = models.FloatField(blank=True, null=True)
    chassi = models.CharField(max_length=20, blank=True, null=True)
    ano_modelo = models.CharField(max_length=4, blank=True, null=True)
    ano_fabricacao = models.CharField(max_length=4, blank=True, null=True)
    renavam = models.CharField(max_length=20, blank=True, null=True)
    alimentacao = models.IntegerField(blank=True, null=True, db_comment='0-InjeþÒo Eletr¶nica\n1-Carburador\n2-Bomba Injetora')
    combustivel = models.IntegerField(blank=True, null=True, db_comment='0-Gasolina\n1-Alcool\n2-Diesel\n3-Gas Natural\n4-Eletrico\n5-Flex')
    motor = models.CharField(max_length=11, blank=True, null=True)
    motor_num = models.CharField(max_length=20, blank=True, null=True)
    rastreado = models.BooleanField(blank=True, null=True)
    tipo = models.IntegerField(blank=True, null=True, db_comment='0-Veiculo\n1-Trator/Implemento')
    status = models.IntegerField(blank=True, null=True)
    id_cor = models.ForeignKey(CadTbCCor, models.DO_NOTHING, db_column='id_cor', blank=True, null=True)
    media_consumo = models.FloatField(blank=True, null=True, db_comment='media de consumo')
    eqp_terceiro = models.BooleanField(blank=True, null=True, db_comment='equipamento de terceiro')
    tipo_rodado = models.SmallIntegerField(blank=True, null=True, db_comment='0-NÒo Aplicavel, \n1-Truck, \n2-Toco, \n3-Cavalo Mecanico, \n4-VAN, \n5-Utilitario, \n6-Outros')
    tipo_carroceria = models.SmallIntegerField(blank=True, null=True, db_comment='0-NaoAplicavel, \n1-Aberta, \n2-Fechada, \n3-Graneleira, \n4-PortaContainer, \n5-Sider')
    cap_veiculo = models.FloatField(blank=True, null=True, db_comment='Capacidade do veiculo')
    tara = models.FloatField(blank=True, null=True)
    uf_licenciado = models.CharField(max_length=2, blank=True, null=True, db_comment='UF em que veÝculo estß licenciado.')

    class Meta:
        managed = False
        db_table = 'pcp_tb_c_meq'
        db_table_comment = 'Cadastro de Veiculos'


class PcpTbCMta(models.Model):
    id_motorista = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=80)
    placa = models.CharField(max_length=8)
    end_endereco = models.CharField(max_length=50)
    end_numero = models.CharField(max_length=10)
    end_cidade = models.CharField(max_length=30)
    end_bairro = models.CharField(max_length=30)
    end_cep = models.CharField(max_length=9)
    end_estado = models.CharField(max_length=2)
    fone = models.CharField(max_length=14, blank=True, null=True)
    celular = models.CharField(max_length=14, blank=True, null=True)
    email = models.CharField(max_length=80, blank=True, null=True)
    observacao = models.CharField(max_length=100, blank=True, null=True)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    doc_cpf = models.CharField(max_length=11, blank=True, null=True)
    mob_senha = models.CharField(max_length=100, blank=True, null=True)
    mob_login = models.CharField(max_length=30, blank=True, null=True)
    mob_id_empresa = models.IntegerField(blank=True, null=True)
    filiacao = models.CharField(max_length=100, blank=True, null=True)
    nome_contato_1 = models.CharField(max_length=50, blank=True, null=True)
    fone_contato_1 = models.CharField(max_length=14, blank=True, null=True)
    tipo_cnh = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_c_mta'


class PcpTbCOri(models.Model):
    id_ori = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=100, blank=True, null=True)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_c_ori'


class PcpTbCPrp(models.Model):
    id_grupo = models.OneToOneField(CadTbCGru, models.DO_NOTHING, db_column='id_grupo', primary_key=True)  # The composite primary key (id_grupo, id_item) found, that is not supported. The first column is selected.
    id_item = models.ForeignKey(CadTbCIte, models.DO_NOTHING, db_column='id_item')
    caract_inspecionada = models.CharField(max_length=300, blank=True, null=True)
    criterio_aceitacao = models.CharField(max_length=500, blank=True, null=True)
    metodo_verificacao = models.CharField(max_length=500, blank=True, null=True)
    amostragem = models.CharField(max_length=500, blank=True, null=True)
    manuseio_transporte = models.CharField(max_length=500, blank=True, null=True)
    armazenamento = models.CharField(max_length=500, blank=True, null=True)
    preservacao = models.CharField(max_length=500, blank=True, null=True)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_c_prp'
        unique_together = (('id_grupo', 'id_item'),)


class PcpTbCPrq(models.Model):
    id_grupo = models.OneToOneField(CadTbCGru, models.DO_NOTHING, db_column='id_grupo', primary_key=True)  # The composite primary key (id_grupo, id_item) found, that is not supported. The first column is selected.
    id_item = models.ForeignKey(CadTbCIte, models.DO_NOTHING, db_column='id_item')
    id_responsavel = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_responsavel')
    dta_cadastro = models.DateField()
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_c_prq'
        unique_together = (('id_grupo', 'id_item'),)


class PcpTbCPrqEsp(models.Model):
    id_grupo = models.OneToOneField(PcpTbCPrq, models.DO_NOTHING, db_column='id_grupo', primary_key=True)  # The composite primary key (id_grupo, id_item, id_prq_esp) found, that is not supported. The first column is selected.
    id_item = models.IntegerField()
    id_prq_esp = models.IntegerField()
    verif_texto = models.CharField(max_length=80, blank=True, null=True)
    verif_minimo = models.CharField(max_length=15, blank=True, null=True)
    vefif_maximo = models.CharField(max_length=15, blank=True, null=True)
    verif_metodo = models.CharField(max_length=80, blank=True, null=True)
    amostragem = models.CharField(max_length=80, blank=True, null=True)
    manuseio_transp = models.CharField(max_length=80, blank=True, null=True)
    armazenamento = models.CharField(max_length=80, blank=True, null=True)
    preservacao = models.CharField(max_length=80, blank=True, null=True)
    id_especificacao = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_c_prq_esp'
        unique_together = (('id_grupo', 'id_item', 'id_prq_esp'),)


class PcpTbCReg(models.Model):
    id_regiao = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=50)
    id_rota = models.ForeignKey('PcpTbCRot', models.DO_NOTHING, db_column='id_rota')
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    desc_perc = models.FloatField(blank=True, null=True)
    unifica_desc_reg = models.BooleanField(blank=True, null=True, db_comment='Se "true", ele irß somar o desconto do Pai + o registro do filho reg_ite')

    class Meta:
        managed = False
        db_table = 'pcp_tb_c_reg'


class PcpTbCRegIte(models.Model):
    id_regiao = models.OneToOneField(PcpTbCReg, models.DO_NOTHING, db_column='id_regiao', primary_key=True)  # The composite primary key (id_regiao, tipo, id_grupo, id_item) found, that is not supported. The first column is selected.
    tipo = models.IntegerField(db_comment='0 - Por Grupo de estoque;   1 - Por Item ')
    id_grupo = models.CharField(max_length=11)
    id_item = models.IntegerField()
    per_desconto = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_c_reg_ite'
        unique_together = (('id_regiao', 'tipo', 'id_grupo', 'id_item'),)


class PcpTbCRot(models.Model):
    id_rota = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=50)
    dis_inicial = models.FloatField()
    dis_final = models.FloatField()
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_c_rot'


class PcpTbCRpt(models.Model):
    id_rpt = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=50)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_c_rpt'
        db_table_comment = 'Recipiente'


class PcpTbCTin(models.Model):
    id_tin = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=50)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_c_tin'
        db_table_comment = 'Tipo de Instrumento'


class PcpTbCTlm(models.Model):
    id_tlm = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=80)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_c_tlm'
        db_table_comment = 'Tipo de Lista Mestre'


class PcpTbCTpp(models.Model):
    id_tpp = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=50)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_c_tpp'
        db_table_comment = 'Tipos de ProgramaþÒo da ProduþÒo'


class PcpTbCTppSet(models.Model):
    id_tpp = models.OneToOneField(PcpTbCTpp, models.DO_NOTHING, db_column='id_tpp', primary_key=True)  # The composite primary key (id_tpp, id_setor) found, that is not supported. The first column is selected.
    id_setor = models.ForeignKey(CadTbCSet, models.DO_NOTHING, db_column='id_setor')
    gera_estoque = models.BooleanField()
    grava_nro_lote = models.BooleanField()
    gera_nro_lote = models.BooleanField()
    executa_servico = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'pcp_tb_c_tpp_set'
        unique_together = (('id_tpp', 'id_setor'),)


class PcpTbMAcr(models.Model):
    id_acr = models.IntegerField(primary_key=True)
    id_empresa = models.ForeignKey(CadTbCPar, models.DO_NOTHING, db_column='id_empresa')
    data_atendimento = models.DateField()
    hora_atendimento = models.DateTimeField()
    cod_lme = models.CharField(max_length=20)
    rev_lme = models.CharField(max_length=5)
    nro_protocolo = models.CharField(max_length=25)
    tipo_cliente = models.IntegerField(db_comment='Neste campo Ú informado qual o tipo de cliente que ligou fazendo a reclamaþÒo.\n\n0 - Distribuidor / Logista\n1 - Consumidor\n2 - Representante')
    pessoa = models.IntegerField(db_comment='F - FÝsica\nJ - JurÝdica')
    id_cliente = models.ForeignKey(CadTbCCli, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True, db_comment='Este campo s¾ Ú preenchido se o campo TIPO_CLIENTE for 0 - Distribuidor / Logista.')
    id_representante = models.IntegerField(blank=True, null=True, db_comment='Este campo s¾ Ú preenchido se o campo TIPO_CLIENTE for 2 - Representante.')
    nome_consumidor = models.CharField(max_length=50)
    cnpj_cpf_consumidor = models.CharField(max_length=14)
    bairro_consumidor = models.CharField(max_length=40, blank=True, null=True)
    endereco_consumidor = models.CharField(max_length=50, blank=True, null=True)
    cep_consumidor = models.CharField(max_length=9, blank=True, null=True)
    fone_consumidor = models.CharField(max_length=14, blank=True, null=True)
    id_cidade = models.ForeignKey(CadTbCCid, models.DO_NOTHING, db_column='id_cidade')
    id_atendente = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_atendente')
    numero_nf = models.IntegerField(blank=True, null=True)
    observacao = models.CharField(max_length=200, blank=True, null=True, db_comment='Alguma observaþÒo do atendimento feito ao cliente.')
    nro_end_consumidor = models.CharField(max_length=10, blank=True, null=True)
    dta_nf = models.DateField(blank=True, null=True)
    id_busca_clirep = models.IntegerField(blank=True, null=True)
    atendimento_concluido = models.IntegerField(blank=True, null=True, db_comment='0-Em Aberto; 1-ConcluÝdo')
    id_pedido_venda = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_acr'


class PcpTbMAcrIte(models.Model):
    id_acr = models.OneToOneField(PcpTbMAcr, models.DO_NOTHING, db_column='id_acr', primary_key=True)  # The composite primary key (id_acr, id_acr_p) found, that is not supported. The first column is selected.
    id_acr_p = models.IntegerField()
    id_item = models.ForeignKey(CadTbCIte, models.DO_NOTHING, db_column='id_item')
    defeito_produto = models.CharField(max_length=800, blank=True, null=True)
    garantia = models.BooleanField(blank=True, null=True)
    data_validade = models.DateField(blank=True, null=True)
    data_fabricacao = models.DateField(blank=True, null=True)
    data_venda = models.DateField(blank=True, null=True)
    id_dis = models.ForeignKey(PcpTbCDis, models.DO_NOTHING, db_column='id_dis', blank=True, null=True, db_comment='aþÒo imediata para resolver o probema apresentado pelo cliente.')
    defeito_procede = models.BooleanField(blank=True, null=True)
    defeito_constatado = models.CharField(max_length=200, blank=True, null=True)
    motivo_nao_procede = models.CharField(max_length=200, blank=True, null=True, db_comment='Se nÒo procede, justicar.')
    comentarios = models.CharField(max_length=800, blank=True, null=True)
    data_monitor_abert = models.DateField(blank=True, null=True)
    hora_monitor_abert = models.DateTimeField(blank=True, null=True)
    data_monitor_encer = models.DateField(blank=True, null=True)
    hora_monitor_encer = models.DateTimeField(blank=True, null=True)
    id_resp_monitor = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_resp_monitor', blank=True, null=True, db_comment='Responsßvel pelo monitoramento.')
    id_busca_item = models.CharField(max_length=30, blank=True, null=True)
    id_cor = models.IntegerField(blank=True, null=True)
    id_tamanho = models.IntegerField(blank=True, null=True)
    id_resp_ana = models.IntegerField(blank=True, null=True)
    data_entrada_ana = models.DateField(blank=True, null=True)
    data_saida_ana = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_acr_ite'
        unique_together = (('id_acr', 'id_acr_p'),)


class PcpTbMAcrItePcn(models.Model):
    id_acr = models.OneToOneField(PcpTbMAcrIte, models.DO_NOTHING, db_column='id_acr', primary_key=True)  # The composite primary key (id_acr, id_acr_p, id_acr_pn) found, that is not supported. The first column is selected.
    id_acr_p = models.IntegerField()
    id_acr_pn = models.IntegerField()
    id_item = models.ForeignKey(CadTbCIte, models.DO_NOTHING, db_column='id_item')

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_acr_ite_pcn'
        unique_together = (('id_acr', 'id_acr_p', 'id_acr_pn'),)


class PcpTbMAcrItePcr(models.Model):
    id_acr = models.OneToOneField(PcpTbMAcrIte, models.DO_NOTHING, db_column='id_acr', primary_key=True)  # The composite primary key (id_acr, id_acr_p, id_acr_ph) found, that is not supported. The first column is selected.
    id_acr_p = models.IntegerField()
    id_acr_ph = models.IntegerField()
    id_item = models.ForeignKey(CadTbCIte, models.DO_NOTHING, db_column='id_item')

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_acr_ite_pcr'
        unique_together = (('id_acr', 'id_acr_p', 'id_acr_ph'),)


class PcpTbMAcrItePdt(models.Model):
    id_acr = models.OneToOneField(PcpTbMAcrIte, models.DO_NOTHING, db_column='id_acr', primary_key=True)  # The composite primary key (id_acr, id_acr_p, id_tdf) found, that is not supported. The first column is selected.
    id_acr_p = models.IntegerField()
    id_tdf = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_acr_ite_pdt'
        unique_together = (('id_acr', 'id_acr_p', 'id_tdf'),)


class PcpTbMAcrItePrc(models.Model):
    id_acr = models.OneToOneField(PcpTbMAcrIte, models.DO_NOTHING, db_column='id_acr', primary_key=True)  # The composite primary key (id_acr, id_acr_p, id_acr_pr) found, that is not supported. The first column is selected.
    id_acr_p = models.IntegerField()
    id_acr_pr = models.IntegerField()
    evento_ocorrido_reg_acao = models.CharField(max_length=200, blank=True, null=True)
    id_resp_reg_acao = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_resp_reg_acao', blank=True, null=True)
    situacao = models.IntegerField(blank=True, null=True, db_comment='0 - Em aberto\n1 - ConcluÝdo')
    data_reg_acao = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_acr_ite_prc'
        unique_together = (('id_acr', 'id_acr_p', 'id_acr_pr'),)


class PcpTbMCac(models.Model):
    id_cac = models.IntegerField(primary_key=True)
    id_empresa = models.ForeignKey(CadTbCPar, models.DO_NOTHING, db_column='id_empresa')
    dta_entrada = models.DateField()
    id_setor_origem = models.ForeignKey(CadTbCSet, models.DO_NOTHING, db_column='id_setor_origem')
    id_ori = models.ForeignKey(PcpTbCOri, models.DO_NOTHING, db_column='id_ori', db_comment='Refere-se a tabela PCP_TB_C_ORI')
    id_responsavel = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_responsavel')
    texto_nao_conformidade = models.CharField(max_length=200, blank=True, null=True)
    fec_dta_eficacia_apos = models.DateField()
    fec_dta_verificado = models.DateField()
    fec_situacao_n_conf = models.IntegerField(db_comment='0 - Sim   1 - Parcialmente    2 - NÒo ')
    fec_func_informados = models.BooleanField()
    fec_func_treinamento = models.BooleanField()
    fec_comentarios = models.CharField(max_length=100, blank=True, null=True)
    fec_id_responsavel = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='fec_id_responsavel', related_name='pcptbmcac_fec_id_responsavel_set')
    fec_id_resp_diretoria = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='fec_id_resp_diretoria', related_name='pcptbmcac_fec_id_resp_diretoria_set')
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    tipo_acao = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_cac'
        db_table_comment = 'Controle de AþÒo Corretiva/Preventiva\nDoc: P 8.5-02'


class PcpTbMCacAna(models.Model):
    id_cac = models.OneToOneField(PcpTbMCac, models.DO_NOTHING, db_column='id_cac', primary_key=True)  # The composite primary key (id_cac, id_cac_ana) found, that is not supported. The first column is selected.
    id_cac_ana = models.IntegerField()
    tipo_causa = models.IntegerField(db_comment='0 - MÚtodo - forma como o produto Ú fabricado, sequencia, padr§es,  organizaþÒo e informaþ§es.\n1 - Mßquina / Equipamento - recursos utilizados na execuþÒo do trabalho\n2 - Material / Insumos - caracterÝsticas necessßrias para a realizaþÒo do produto.\n3 - Meio de MediþÒo - forma como o resultado do processo ou produto Ú medido.\n4 - MÒo de Obra - qualificaþÒo; treinamento inadequado, descumprimento de regras ou prßticas.\n5 - Meio-Ambiente - interferÛncia do ambiente de trabalho no processo e produto (umidade, temperatura, ruÝdo, poeira, etc.).')
    subcausa = models.CharField(max_length=100, blank=True, null=True)
    motivo = models.CharField(max_length=200, blank=True, null=True)
    causa_raiz = models.CharField(max_length=200, blank=True, null=True)
    id_responsavel = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_responsavel')

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_cac_ana'
        unique_together = (('id_cac', 'id_cac_ana'),)


class PcpTbMCacPla(models.Model):
    id_cac = models.OneToOneField(PcpTbMCac, models.DO_NOTHING, db_column='id_cac', primary_key=True)  # The composite primary key (id_cac, id_cac_pla) found, that is not supported. The first column is selected.
    id_cac_pla = models.IntegerField()
    acao = models.CharField(max_length=100, blank=True, null=True)
    id_responsavel = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_responsavel')
    dta_prazo = models.DateField()
    dta_efetivo = models.DateField()

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_cac_pla'
        unique_together = (('id_cac', 'id_cac_pla'),)


class PcpTbMCme(models.Model):
    id_meq = models.IntegerField(primary_key=True)
    id_responsavel = models.IntegerField()
    dta_lancto = models.DateField()
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_cme'
        db_table_comment = 'Cronograma de ManutenþÒo de Mßquinas/Equipamentos\nPlanilha: P 6.3-02'


class PcpTbMCmeMeq(models.Model):
    id_meq = models.OneToOneField(PcpTbMCme, models.DO_NOTHING, db_column='id_meq', primary_key=True)  # The composite primary key (id_meq, id_cme_meq) found, that is not supported. The first column is selected.
    id_cme_meq = models.IntegerField()
    id_setor = models.ForeignKey(CadTbCSet, models.DO_NOTHING, db_column='id_setor', blank=True, null=True)
    nro_semana = models.IntegerField(blank=True, null=True)
    mes = models.IntegerField(blank=True, null=True)
    ano = models.IntegerField(blank=True, null=True)
    tipo_controle = models.IntegerField(blank=True, null=True, db_comment='0 - Planejado  1 - Executado   2 - Reprogramado')
    tipo_manutencao = models.IntegerField(blank=True, null=True, db_comment='0 - MecÔnica\n  1 - ElÚtrica/Eletronica\n  2 - Hidrßulica\n  3 - Pneumßtica\n  4 - Total')
    frequencia = models.IntegerField(blank=True, null=True)
    realizado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_cme_meq'
        unique_together = (('id_meq', 'id_cme_meq'),)


class PcpTbMCrp(models.Model):
    id_crp = models.IntegerField(primary_key=True)
    id_empresa = models.ForeignKey(CadTbCPar, models.DO_NOTHING, db_column='id_empresa')
    dta_emissao = models.DateField()
    num_lote_crp = models.CharField(max_length=15, blank=True, null=True)
    id_rpt = models.ForeignKey(PcpTbCRpt, models.DO_NOTHING, db_column='id_rpt')
    id_responsavel = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_responsavel')
    id_almoxarifado = models.ForeignKey(CadTbCAlm, models.DO_NOTHING, db_column='id_almoxarifado', blank=True, null=True)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    id_grupo = models.CharField(max_length=11, blank=True, null=True, db_comment='Este campo farß com que o controle de recipiente s¾ aceite itens do grupo informado. Ex.: Se o usußrio informar grupo POLIOU , recipiente s¾ aceitarß itens do grupo POLIOU.')

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_crp'
        db_table_comment = 'Controle de Recipientes'


class PcpTbMCrpIte(models.Model):
    id_crp = models.OneToOneField(PcpTbMCrp, models.DO_NOTHING, db_column='id_crp', primary_key=True)  # The composite primary key (id_crp, id_sequencia) found, that is not supported. The first column is selected.
    id_item = models.ForeignKey(CadTbCIte, models.DO_NOTHING, db_column='id_item')
    id_cor = models.IntegerField()
    id_tamanho = models.IntegerField()
    num_lote = models.CharField(max_length=15, blank=True, null=True, db_comment='Refere-se ao Nro do lote interno')
    qtde = models.FloatField()
    qtde_baixada = models.FloatField()
    id_sequencia = models.IntegerField()
    id_busca_item = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_crp_ite'
        unique_together = (('id_crp', 'id_sequencia'),)


class PcpTbMCrpIteBxi(models.Model):
    id_crp = models.OneToOneField(PcpTbMCrpIte, models.DO_NOTHING, db_column='id_crp', primary_key=True)  # The composite primary key (id_crp, id_sequencia, id_crp_bxi) found, that is not supported. The first column is selected.
    id_item = models.IntegerField()
    id_cor = models.IntegerField()
    id_tamanho = models.IntegerField()
    id_crp_bxi = models.IntegerField()
    num_lote = models.CharField(max_length=15, blank=True, null=True)
    qtde = models.FloatField()
    id_opb = models.IntegerField()
    id_opb_ope = models.IntegerField()
    id_opb_ibe = models.IntegerField()
    id_sequencia = models.IntegerField()
    dta_baixa = models.DateField()

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_crp_ite_bxi'
        unique_together = (('id_crp', 'id_sequencia', 'id_crp_bxi'),)


class PcpTbMCrq(models.Model):
    id_crq = models.IntegerField(primary_key=True)
    id_empresa = models.ForeignKey(CadTbCPar, models.DO_NOTHING, db_column='id_empresa')
    id_responsavel = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_responsavel')
    dta_criacao = models.DateField()
    dta_atualizacao = models.DateField()
    observacao = models.CharField(max_length=100, blank=True, null=True)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_crq'
        db_table_comment = 'Controle de Registros da Qualidade\nConforme planilha: P 4-2 R0'


class PcpTbMCrqReg(models.Model):
    id_crq = models.OneToOneField(PcpTbMCrq, models.DO_NOTHING, db_column='id_crq', primary_key=True)  # The composite primary key (id_crq, id_lme_d) found, that is not supported. The first column is selected.
    id_lme_d = models.IntegerField()
    id_setor = models.ForeignKey(CadTbCSet, models.DO_NOTHING, db_column='id_setor')
    forma = models.IntegerField(db_comment='0 - Pasta A-Z   1 - Rede  2- Eletr¶nico')
    indexacao = models.IntegerField(db_comment='0 - Por Data em Ordem Crescente')
    metodo_recuperacao = models.IntegerField(db_comment='0 - Data')
    tempo_retencao = models.IntegerField()
    disposicao_tempo = models.IntegerField(db_comment='0 - Ap¾s, Manter em Arquivo Morto')
    dta_cadastro = models.DateField()

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_crq_reg'
        unique_together = (('id_crq', 'id_lme_d'),)


class PcpTbMEpp(models.Model):
    id_epp = models.IntegerField(primary_key=True)
    id_empresa = models.ForeignKey(CadTbCPar, models.DO_NOTHING, db_column='id_empresa')
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    id_responsavel = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_responsavel')
    id_almoxarifado = models.IntegerField(blank=True, null=True)
    dta_entrada = models.DateField()
    hor_entrada = models.TimeField()
    tipo_entrada = models.IntegerField(blank=True, null=True, db_comment='0 - Entrada Normal\r\n1 - Entrada por Contagem')

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_epp'
        db_table_comment = 'Tabela: Entrada de Produtos da ProduþÒo'


class PcpTbMEppIte(models.Model):
    id_epp = models.OneToOneField(PcpTbMEpp, models.DO_NOTHING, db_column='id_epp', primary_key=True)  # The composite primary key (id_epp, id_epp_ite) found, that is not supported. The first column is selected.
    id_epp_ite = models.IntegerField()
    id_item = models.ForeignKey(CadTbCIte, models.DO_NOTHING, db_column='id_item', blank=True, null=True)
    id_busca_item = models.CharField(max_length=30, blank=True, null=True)
    id_cor = models.IntegerField(blank=True, null=True)
    id_tamanho = models.IntegerField(blank=True, null=True)
    cod_barra = models.CharField(max_length=50)
    qtde = models.FloatField(blank=True, null=True)
    id_func_colchoaria = models.IntegerField(blank=True, null=True)
    lancto_func_colch_manual = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_epp_ite'
        unique_together = (('id_epp', 'id_epp_ite'),)


class PcpTbMEtq(models.Model):
    id_opr = models.IntegerField()
    id_etq = models.IntegerField(primary_key=True)
    id_item = models.ForeignKey(CadTbCIte, models.DO_NOTHING, db_column='id_item')
    id_cor = models.IntegerField()
    id_tamanho = models.IntegerField()
    cod_barra = models.CharField(max_length=50)
    sequencia = models.IntegerField()
    dta_criacao = models.DateField()
    hor_criacao = models.TimeField()
    impressa = models.BooleanField()
    dta_entrada_est = models.DateField(blank=True, null=True, db_comment='Data que o item entrou no estoque.')
    hor_entrada_est = models.TimeField(blank=True, null=True, db_comment='Hora em que o item entrou no estoque.')
    id_funcionario_est = models.IntegerField(blank=True, null=True, db_comment='Funcionßrio responsßvel de dar entrada no estoque.')
    hor_impressa = models.TimeField(blank=True, null=True)
    dta_impressa = models.DateField(blank=True, null=True)
    id_func_impressa = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_func_impressa', blank=True, null=True)
    id_opr_origem = models.IntegerField(blank=True, null=True)
    id_empresa = models.IntegerField(blank=True, null=True)
    dta_saida = models.DateField(blank=True, null=True, db_comment='Data da saÝda do produto(etiqueta) do estoque')
    hor_saida = models.TimeField(blank=True, null=True, db_comment='Hora da saÝda do produto(etiqueta) do estoque')
    id_ors_saida = models.IntegerField(blank=True, null=True, db_comment='Ordem de Faturamento responsßvel pela saÝda do produto(etiqueta)')
    id_rom_saida = models.IntegerField(blank=True, null=True, db_comment='Romaneio que tem a conferÛncia desta etiqueta.')
    id_funcionario_sai = models.CharField(max_length=255, blank=True, null=True, db_comment='Responsßvel pela saÝda do produto(etiqueta) do estoque')
    id_epp = models.IntegerField(blank=True, null=True)
    pcp_obs_item = models.CharField(max_length=150, blank=True, null=True)
    temp_id_ors_saida_antigo = models.IntegerField(blank=True, null=True)
    dta_reimpressa = models.DateField(blank=True, null=True)
    hor_reimpressa = models.TimeField(blank=True, null=True)
    id_func_reimpressa = models.IntegerField(blank=True, null=True)
    motivo_reimpressa = models.CharField(max_length=80, blank=True, null=True)
    temp_id_epp_antigo = models.IntegerField(blank=True, null=True)
    temp_dta_entrada_est = models.DateField(blank=True, null=True)
    contagem = models.BooleanField(blank=True, null=True)
    dta_entrada_antes_contagem = models.DateField(blank=True, null=True)
    hor_entrada_antes_contagem = models.TimeField(blank=True, null=True)
    temp_obs_geral = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_etq'
        db_table_comment = 'Tabela de Etiquetas da Ordem de ProduþÒo'


class PcpTbMEtqTemp(models.Model):
    id_opr = models.IntegerField()
    id_etq = models.IntegerField(primary_key=True)
    id_item = models.ForeignKey(CadTbCIte, models.DO_NOTHING, db_column='id_item')
    id_cor = models.IntegerField()
    id_tamanho = models.IntegerField()
    cod_barra = models.CharField(max_length=50)
    sequencia = models.IntegerField()
    dta_criacao = models.DateField()
    hor_criacao = models.TimeField()
    impressa = models.BooleanField()
    dta_entrada_est = models.DateField(blank=True, null=True, db_comment='Data que o item entrou no estoque.')
    hor_entrada_est = models.TimeField(blank=True, null=True, db_comment='Hora em que o item entrou no estoque.')
    id_funcionario_est = models.IntegerField(blank=True, null=True, db_comment='Funcionßrio responsßvel de dar entrada no estoque.')
    hor_impressa = models.TimeField(blank=True, null=True)
    dta_impressa = models.DateField(blank=True, null=True)
    id_func_impressa = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_func_impressa', blank=True, null=True)
    id_opr_origem = models.IntegerField(blank=True, null=True)
    id_empresa = models.IntegerField(blank=True, null=True)
    dta_saida = models.DateField(blank=True, null=True, db_comment='Data da saÝda do produto(etiqueta) do estoque')
    hor_saida = models.TimeField(blank=True, null=True, db_comment='Hora da saÝda do produto(etiqueta) do estoque')
    id_ors_saida = models.IntegerField(blank=True, null=True, db_comment='Ordem de Faturamento responsßvel pela saÝda do produto(etiqueta)')
    id_rom_saida = models.IntegerField(blank=True, null=True, db_comment='Romaneio que tem a conferÛncia desta etiqueta.')
    id_funcionario_sai = models.CharField(max_length=255, blank=True, null=True, db_comment='Responsßvel pela saÝda do produto(etiqueta) do estoque')
    id_epp = models.IntegerField(blank=True, null=True)
    pcp_obs_item = models.CharField(max_length=150, blank=True, null=True)
    temp_id_ors_saida_antigo = models.IntegerField(blank=True, null=True)
    dta_reimpressa = models.DateField(blank=True, null=True)
    hor_reimpressa = models.TimeField(blank=True, null=True)
    id_func_reimpressa = models.IntegerField(blank=True, null=True)
    motivo_reimpressa = models.CharField(max_length=80, blank=True, null=True)
    temp_id_epp_antigo = models.IntegerField(blank=True, null=True)
    temp_dta_entrada_est = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_etq_temp'
        db_table_comment = 'Tabela de Etiquetas da Ordem de ProduþÒo'


class PcpTbMIqf(models.Model):
    id_fornecedor = models.OneToOneField(CadTbCFor, models.DO_NOTHING, db_column='id_fornecedor', primary_key=True)  # The composite primary key (id_fornecedor, ano_iqf) found, that is not supported. The first column is selected.
    ano_iqf = models.IntegerField()
    id_empresa = models.ForeignKey(CadTbCPar, models.DO_NOTHING, db_column='id_empresa')
    id_responsavel = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_responsavel')
    dta_semestre1 = models.DateField(blank=True, null=True, db_comment='Nome do campo: N·mero de entregas.\nEste campo refere-se a quantidade de notas fiscais do fornecedor no primeiro semestre.')
    qtde_nf_semestre1 = models.IntegerField()
    qtde_demeritos_semestre1 = models.IntegerField(db_comment='Nome do campo: Qtde de demÚritos\nSoma os demÚritos de todas as notas do fornecedor. Essa informaþÒo tß na tabela EST_TB_M_NFE_S.')
    qtde_plano_acao_semestre1 = models.IntegerField()
    iqf_semestre1 = models.FloatField()
    status_semestre1 = models.IntegerField(db_comment='1 - Sem fornecimento no semestre\n2 - Ruim\n3 - Regular\n4 - Bom')
    dta_semestre2 = models.DateField(blank=True, null=True)
    qtde_nf_semestre2 = models.IntegerField(db_comment='Nome do campo: N·mero de entregas.\nEste campo refere-se a quantidade de notas fiscais do fornecedor no segundo semestre.')
    qtde_demeritos_semestre2 = models.IntegerField(db_comment='Nome do campo: Qtde de demÚritos\nSoma os demÚritos de todas as notas do fornecedor. Essa informaþÒo tß na tabela EST_TB_M_NFE_S.')
    qtde_plano_acao_semestre2 = models.IntegerField()
    iqf_semestre2 = models.FloatField()
    status_semestre2 = models.IntegerField(db_comment='1 - Sem fornecimento no semestre\n2 - Ruim\n3 - Regular\n4 - Bom')
    ra_dta_prevista = models.DateField(blank=True, null=True, db_comment='Faz parte da re-qualificaþÒo anual.')
    ra_dta_realizada = models.DateField(blank=True, null=True, db_comment='Faz parte da re-qualificaþÒo anual.')
    ra_metodo1_media_anual = models.FloatField(blank=True, null=True)
    ra_metodo1_status = models.CharField(max_length=1, blank=True, null=True)
    ra_metodo2_especifico = models.CharField(max_length=150, blank=True, null=True)
    ra_metodo2_status = models.CharField(max_length=100, blank=True, null=True)
    ra_observacao = models.CharField(max_length=200, blank=True, null=True)
    observacao_geral = models.CharField(max_length=150, blank=True, null=True)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_iqf'
        unique_together = (('id_fornecedor', 'ano_iqf'),)
        db_table_comment = 'Indice de qualificaþÒo de fornecedores'


class PcpTbMLbe(models.Model):
    id_lbe = models.IntegerField(primary_key=True)
    id_empresa = models.ForeignKey(CadTbCPar, models.DO_NOTHING, db_column='id_empresa')
    tipo = models.CharField(max_length=1, blank=True, null=True, db_comment='H - Retangular - Mßquina horizontal   V - Retangular - Mßquina vertical   C - CilÝndrico')
    dta_laminacao = models.DateField()
    qtde = models.FloatField()
    id_setor = models.ForeignKey(CadTbCSet, models.DO_NOTHING, db_column='id_setor')
    id_item_acabado = models.ForeignKey(CadTbCIte, models.DO_NOTHING, db_column='id_item_acabado')
    id_item_lamina = models.ForeignKey(CadTbCIte, models.DO_NOTHING, db_column='id_item_lamina', related_name='pcptbmlbe_id_item_lamina_set')
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_lbe'
        db_table_comment = 'LaminaþÒo de Bloco Rentangular/CilÝnndrico'


class PcpTbMLbeBlo(models.Model):
    id_lbe = models.OneToOneField(PcpTbMLbe, models.DO_NOTHING, db_column='id_lbe', primary_key=True)  # The composite primary key (id_lbe, id_lbe_blo) found, that is not supported. The first column is selected.
    id_lbe_blo = models.IntegerField()
    num_lote = models.CharField(max_length=15, blank=True, null=True)
    qtde = models.FloatField()
    id_opb = models.IntegerField()
    id_opb_ope = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_lbe_blo'
        unique_together = (('id_lbe', 'id_lbe_blo'),)


class PcpTbMLpr(models.Model):
    id_lpr = models.IntegerField(primary_key=True)
    dta_presenca = models.DateField()
    hora = models.DateTimeField()
    id_responsavel = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_responsavel')
    id_resp_reuniao = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_resp_reuniao', related_name='pcptbmlpr_id_resp_reuniao_set')
    motivo_reuniao = models.CharField(max_length=300, blank=True, null=True)
    conteudo_reuniao = models.CharField(max_length=300, blank=True, null=True)
    observacao = models.CharField(max_length=100, blank=True, null=True)
    id_empresa = models.ForeignKey(CadTbCPar, models.DO_NOTHING, db_column='id_empresa')
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    hora_fin = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_lpr'
        db_table_comment = 'Tabela de lista de presenþa'


class PcpTbMLprFun(models.Model):
    id_lpr = models.OneToOneField(PcpTbMLpr, models.DO_NOTHING, db_column='id_lpr', primary_key=True)  # The composite primary key (id_lpr, id_funcionario) found, that is not supported. The first column is selected.
    id_funcionario = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_funcionario')

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_lpr_fun'
        unique_together = (('id_lpr', 'id_funcionario'),)


class PcpTbMMcp(models.Model):
    id_mcp = models.IntegerField(primary_key=True)
    id_empresa = models.ForeignKey(CadTbCPar, models.DO_NOTHING, db_column='id_empresa')
    problema = models.CharField(max_length=100, blank=True, null=True)
    id_setor = models.ForeignKey(CadTbCSet, models.DO_NOTHING, db_column='id_setor')
    id_meq = models.ForeignKey(PcpTbCMeq, models.DO_NOTHING, db_column='id_meq')
    id_cme_meq = models.IntegerField()
    total_pecas = models.DecimalField(max_digits=18, decimal_places=4)
    total_mobra = models.DecimalField(max_digits=18, decimal_places=4)
    total_pecas_garantia = models.DecimalField(max_digits=18, decimal_places=4)
    total_servicos_garantia = models.DecimalField(max_digits=18, decimal_places=4)
    total_garantia = models.DecimalField(max_digits=18, decimal_places=4)
    total_pecas_mobra = models.DecimalField(max_digits=18, decimal_places=4)
    id_responsavel = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_responsavel')
    id_resp_autorizou = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_resp_autorizou', related_name='pcptbmmcp_id_resp_autorizou_set')
    dta_autorizacao = models.DateField()
    dta_inicio_atend = models.DateField()
    hora_inicio_atend = models.DateTimeField()
    dta_termino_atend = models.DateField()
    hora_termino_atend = models.DateTimeField()
    tipo_acao = models.IntegerField(blank=True, null=True)
    tipo_manutencao = models.IntegerField(blank=True, null=True, db_comment='0 - Corretiva   1 - Preventiva')
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_mcp'
        db_table_comment = 'Registro de ManutenþÒo Corretiva e Preventiva\nConforme DOC: P 6.3-01'


class PcpTbMMcpIve(models.Model):
    id_mcp = models.OneToOneField(PcpTbMMcp, models.DO_NOTHING, db_column='id_mcp', primary_key=True)  # The composite primary key (id_mcp, id_mcp_ive) found, that is not supported. The first column is selected.
    id_mcp_ive = models.IntegerField()
    texto_verificado = models.CharField(max_length=100, blank=True, null=True)
    verificado = models.BooleanField()
    substituido = models.BooleanField()
    lubrificado = models.BooleanField()
    ajustado = models.BooleanField()
    completado = models.BooleanField()
    trocado = models.BooleanField()
    limpado = models.BooleanField()
    reparado = models.BooleanField()
    outros = models.BooleanField()
    texto_outros = models.CharField(max_length=60, blank=True, null=True)
    observacao = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_mcp_ive'
        unique_together = (('id_mcp', 'id_mcp_ive'),)


class PcpTbMMcpSer(models.Model):
    id_mcp = models.OneToOneField(PcpTbMMcp, models.DO_NOTHING, db_column='id_mcp', primary_key=True)  # The composite primary key (id_mcp, id_mcp_ser) found, that is not supported. The first column is selected.
    id_mcp_ser = models.IntegerField()
    id_item = models.ForeignKey(CadTbCIte, models.DO_NOTHING, db_column='id_item')

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_mcp_ser'
        unique_together = (('id_mcp', 'id_mcp_ser'),)


class PcpTbMNcf(models.Model):
    id_ncf = models.IntegerField(primary_key=True)
    id_setor_origem = models.ForeignKey(CadTbCSet, models.DO_NOTHING, db_column='id_setor_origem')
    id_empresa = models.ForeignKey(CadTbCPar, models.DO_NOTHING, db_column='id_empresa', blank=True, null=True)
    texto_nao_conformidade = models.CharField(max_length=200, blank=True, null=True)
    id_item_motivo = models.ForeignKey(CadTbCIte, models.DO_NOTHING, db_column='id_item_motivo', db_comment='Caso o produto exista no cadastro , o usußrio poderß informar seu c¾digo neste campo.')
    id_cor = models.ForeignKey(CadTbCCor, models.DO_NOTHING, db_column='id_cor')
    id_tamanho = models.IntegerField()
    motivo = models.CharField(max_length=100, blank=True, null=True, db_comment='Caso nÒo tenha o produto cadastro o usußrio poderß digitar o Motivo do lanþamento de nÒo conformidade')
    qtde_total_lote = models.FloatField()
    qtde_nao_conforme = models.FloatField()
    perc_nao_conforme = models.FloatField()
    qtde_troca_dev = models.FloatField()
    id_responsavel = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_responsavel', blank=True, null=True)
    dta_emissao = models.DateField()
    re_satisfatoria = models.BooleanField()
    re_especificacao = models.CharField(max_length=100, blank=True, null=True)
    re_id_responsavel = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='re_id_responsavel', related_name='pcptbmncf_re_id_responsavel_set', blank=True, null=True)
    ana_prazo_eficaz = models.IntegerField()
    ana_disp_eficaz = models.IntegerField()
    ana_racp = models.IntegerField()
    ana_func_informados = models.IntegerField()
    ana_func_treinamento = models.IntegerField()
    ana_comentarios = models.CharField(max_length=100, blank=True, null=True)
    ana_id_responsavel = models.IntegerField()
    ana_id_resp_diretoria = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='ana_id_resp_diretoria', related_name='pcptbmncf_ana_id_resp_diretoria_set')
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    re_dta_resp = models.DateField(blank=True, null=True)
    ana_dta_resp = models.DateField(blank=True, null=True)
    ana_dta_diretoria = models.DateField(blank=True, null=True)
    ana_dta_racp = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_ncf'
        db_table_comment = 'Controle de NÒo Conformidade\nDoc: P-8.3-01'


class PcpTbMNcfDis(models.Model):
    id_ncf = models.OneToOneField(PcpTbMNcf, models.DO_NOTHING, db_column='id_ncf', primary_key=True)  # The composite primary key (id_ncf, id_ncf_dis) found, that is not supported. The first column is selected.
    id_ncf_dis = models.IntegerField()
    id_dis = models.ForeignKey(PcpTbCDis, models.DO_NOTHING, db_column='id_dis')
    id_responsavel = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_responsavel')
    prazo = models.IntegerField()
    efetivo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_ncf_dis'
        unique_together = (('id_ncf', 'id_ncf_dis'),)


class PcpTbMOpb(models.Model):
    id_opb = models.IntegerField(primary_key=True)
    id_responsavel = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_responsavel')
    id_empresa = models.ForeignKey(CadTbCPar, models.DO_NOTHING, db_column='id_empresa')
    dta_emissao = models.DateField()
    obs_administrativa = models.CharField(max_length=200, blank=True, null=True)
    obs_producao = models.CharField(max_length=200, blank=True, null=True)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    origem = models.IntegerField(blank=True, null=True, db_comment='0 - Gerado Manualmente; \r\n1 - Gerado por Ordem de ProduþÒo;')
    id_opr = models.IntegerField(blank=True, null=True)
    id_almoxarifado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_opb'
        db_table_comment = 'Ordem de ProduþÒo de Bloco de Espuma'


class PcpTbMOpbBlo(models.Model):
    id_opb = models.OneToOneField(PcpTbMOpb, models.DO_NOTHING, db_column='id_opb', primary_key=True)  # The composite primary key (id_opb, num_lote) found, that is not supported. The first column is selected.
    num_lote = models.CharField(max_length=15)
    dta_emissao = models.DateField()
    hor_emissao = models.TimeField()
    id_item_bloco = models.ForeignKey(CadTbCIte, models.DO_NOTHING, db_column='id_item_bloco')
    id_cor = models.IntegerField(blank=True, null=True)
    id_tamanho = models.IntegerField(blank=True, null=True)
    bloco_aprovado = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_opb_blo'
        unique_together = (('id_opb', 'num_lote'),)
        db_table_comment = 'Blocos produzidos da Ordem de ProduþÒo'


class PcpTbMOpbObl(models.Model):
    id_opb = models.OneToOneField(PcpTbMOpb, models.DO_NOTHING, db_column='id_opb', primary_key=True)  # The composite primary key (id_opb, id_opb_obl) found, that is not supported. The first column is selected.
    id_opb_obl = models.IntegerField()
    id_item = models.ForeignKey(CadTbCIte, models.DO_NOTHING, db_column='id_item')
    id_cor = models.IntegerField()
    id_tamanho = models.IntegerField()
    cubagem_a_produzir = models.FloatField()
    obs = models.CharField(max_length=100, blank=True, null=True)
    qtde_abater_sld = models.FloatField(blank=True, null=True, db_comment='A qtde deste campo serß utilizada para abater na tabela de saldo do item.')
    op_espumacao_impressa = models.BooleanField(blank=True, null=True)
    op_impressa_por = models.IntegerField(blank=True, null=True)
    op_impressa_em = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_opb_obl'
        unique_together = (('id_opb', 'id_opb_obl'),)
        db_table_comment = 'Blocos de espuma para serem produzidos.'


class PcpTbMOpbOpe(models.Model):
    id_opb = models.OneToOneField(PcpTbMOpb, models.DO_NOTHING, db_column='id_opb', primary_key=True)  # The composite primary key (id_opb, id_opb_ope) found, that is not supported. The first column is selected.
    id_opb_ope = models.IntegerField()
    id_item_semi = models.ForeignKey(CadTbCIte, models.DO_NOTHING, db_column='id_item_semi')
    id_cor = models.ForeignKey(CadTbCCor, models.DO_NOTHING, db_column='id_cor')
    id_tamanho = models.IntegerField()
    dta_producao = models.DateField()
    hora_producao = models.DateField()
    num_lote = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_opb_ope'
        unique_together = (('id_opb', 'id_opb_ope'),)


class PcpTbMOpbOpeIbe(models.Model):
    id_opb = models.OneToOneField(PcpTbMOpbOpe, models.DO_NOTHING, db_column='id_opb', primary_key=True)  # The composite primary key (id_opb, id_opb_ope, id_opb_ibe) found, that is not supported. The first column is selected.
    id_opb_ope = models.IntegerField()
    id_opb_ibe = models.IntegerField()
    id_item = models.ForeignKey(CadTbCIte, models.DO_NOTHING, db_column='id_item')
    id_cor = models.ForeignKey(CadTbCCor, models.DO_NOTHING, db_column='id_cor')
    id_tamanho = models.IntegerField()
    qtde = models.FloatField()
    num_lote_crp = models.CharField(max_length=15, blank=True, null=True)
    num_lote_item = models.CharField(max_length=15, blank=True, null=True)
    id_crp = models.ForeignKey(PcpTbMCrp, models.DO_NOTHING, db_column='id_crp')

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_opb_ope_ibe'
        unique_together = (('id_opb', 'id_opb_ope', 'id_opb_ibe'),)


class PcpTbMOpbOpeOpr(models.Model):
    id_opb = models.OneToOneField(PcpTbMOpbOpe, models.DO_NOTHING, db_column='id_opb', primary_key=True)  # The composite primary key (id_opb, id_opb_ope, id_opr) found, that is not supported. The first column is selected.
    id_opb_ope = models.IntegerField()
    id_opr = models.ForeignKey('PcpTbMOpr', models.DO_NOTHING, db_column='id_opr')
    dta_utilizado = models.DateField()
    hor_utilizado = models.TimeField()

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_opb_ope_opr'
        unique_together = (('id_opb', 'id_opb_ope', 'id_opr'),)
        db_table_comment = 'O.P.Rs que utilizaram este bloco.'


class PcpTbMOpbOpr(models.Model):
    id_opb = models.OneToOneField(PcpTbMOpb, models.DO_NOTHING, db_column='id_opb', primary_key=True)  # The composite primary key (id_opb, id_opr) found, that is not supported. The first column is selected.
    id_opr = models.ForeignKey('PcpTbMOpr', models.DO_NOTHING, db_column='id_opr')

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_opb_opr'
        unique_together = (('id_opb', 'id_opr'),)


class PcpTbMOpr(models.Model):
    id_opr = models.IntegerField(primary_key=True)
    dta_emissao = models.DateField()
    obs_administrativa = models.CharField(max_length=800, blank=True, null=True)
    obs_producao = models.CharField(max_length=800, blank=True, null=True)
    id_responsavel = models.IntegerField()
    situacao = models.IntegerField(db_comment='0 - EM ABERTO   1 - INICIADA   2 - ENCERRADA    3 - CANCELADA')
    id_empresa = models.ForeignKey(CadTbCPar, models.DO_NOTHING, db_column='id_empresa')
    id_tpp = models.ForeignKey(PcpTbCTpp, models.DO_NOTHING, db_column='id_tpp')
    cub_produzir = models.FloatField()
    cub_pedidos = models.FloatField()
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    id_almoxarifado = models.IntegerField(blank=True, null=True)
    id_setor = models.ForeignKey(CadTbCSet, models.DO_NOTHING, db_column='id_setor', blank=True, null=True)
    num_lote = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_opr'
        db_table_comment = 'Ordem de ProduþÒo de Produtos Acabado'


class PcpTbMOprIpa(models.Model):
    id_opr = models.OneToOneField(PcpTbMOpr, models.DO_NOTHING, db_column='id_opr', primary_key=True)  # The composite primary key (id_opr, id_opr_opp, id_opr_ipa) found, that is not supported. The first column is selected.
    id_opr_opp = models.IntegerField()
    id_opr_ipa = models.IntegerField()
    id_item = models.ForeignKey(CadTbCIte, models.DO_NOTHING, db_column='id_item')
    id_cor = models.ForeignKey(CadTbCCor, models.DO_NOTHING, db_column='id_cor')
    id_tamanho = models.IntegerField()
    qtde = models.FloatField()

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_opr_ipa'
        unique_together = (('id_opr', 'id_opr_opp', 'id_opr_ipa'),)


class PcpTbMOprOpp(models.Model):
    id_opr = models.OneToOneField(PcpTbMOpr, models.DO_NOTHING, db_column='id_opr', primary_key=True)  # The composite primary key (id_opr, id_opr_opp) found, that is not supported. The first column is selected.
    id_opr_opp = models.IntegerField()
    id_item = models.ForeignKey(CadTbCIte, models.DO_NOTHING, db_column='id_item')
    id_cor = models.ForeignKey(CadTbCCor, models.DO_NOTHING, db_column='id_cor')
    id_tamanho = models.IntegerField()
    qtde_a_produzir = models.FloatField()
    qtde_produzida = models.FloatField()
    qtde_a_produzir_orig = models.FloatField(db_comment='Este campo nÒo pode ser alterado pelo usußrio.\nNo momento da criaþÒo deste registro, este campo terß o mesmo valor do campo QTDE_A_PRODUZIR.')
    id_resp_alt = models.IntegerField(blank=True, null=True, db_comment='Este campo Ú preenchido no momento em que o usußrio altera o valor do campo QTDE_A_PRODUZIR.')
    dta_alt = models.DateField(blank=True, null=True, db_comment='Este campo Ú preenchido no momento em que o usußrio altera o valor do campo QTDE_A_PRODUZIR.')
    hora_alt = models.TimeField(blank=True, null=True, db_comment='Este campo Ú preenchido no momento em que o usußrio altera o valor do campo QTDE_A_PRODUZIR.')
    qtde_atender_opr = models.FloatField(db_comment='Este campo tem a funþÒo de informar Ó O.P.R a qtde real que serß utilizada para ela. De inicio ela pode ter mandado Produzir 100, mas depois teve pedido com desistÛncia , onde a qtde a produzir baixaria pra 80, mas o usußrio resolveu deixar a Produzir 100, com isso a O.P.R terß um saldo de 20 que servirß para demais O.P.R.')
    qtde_atender_opr_ext = models.FloatField(db_comment='Toda vez que uma O.P.R externa utiliza o saldo disponÝvel de uma O.P.R, ela deverß quardar a qtde utilizada neste campo.   \n\tImagine que: QTDE_A_PRODUZIR = 70 \n                                      QTDE_ATENDER_OPR = 60 \n                                      QTD_ATENDER_OPR_EXT = 4\n                                      SALDO_DISPONIVEL = 6 \n e a O.P.R Externa estß precisando de 2.  \n               EntÒo  ficarß:   QTDE_A_PRODUZIR = 70 \n                                      QTDE_ATENDER_OPR = 60 \n                                      QTD_ATENDER_OPR_EXT = 6\n                                      SALDO_DISPONIVEL = 4 \n')
    saldo_disponivel = models.FloatField(db_comment='SALDO_DISPONIVEL:  float    QTDE_A_PRODUZIR û ( QTD_ATENDER_OPR +  QTD_ATENDER_OPR_EXT)')
    reg_alt = models.BooleanField(blank=True, null=True)
    historico_alt = models.CharField(max_length=500, blank=True, null=True, db_comment='Cada vez que houver alguma alteraþÒo neste registro o sistema irß guardando o conte·do do campo Motivo da alteraþÒo.')
    motivo_alt = models.CharField(max_length=100, blank=True, null=True)
    gerado_aut = models.BooleanField(blank=True, null=True, db_comment='Serß TRUE quando for gerado pela ImportaþÒo do Pedido de Venda. Caso for inserido manualmente, serß FALSE;')
    motivo_ger_man = models.CharField(max_length=100, blank=True, null=True, db_comment='Motivo do por quÛ que estß inserido o produto manualmente na ordem de produþÒo.')
    id_resp_man = models.IntegerField(blank=True, null=True)
    dta_man = models.DateField(blank=True, null=True)
    hor_man = models.TimeField(blank=True, null=True)
    id_busca_item = models.CharField(max_length=20, blank=True, null=True)
    obs_producao = models.CharField(max_length=800, blank=True, null=True)
    saldo_fisico_momento = models.FloatField(blank=True, null=True)
    saldo_pendente = models.FloatField(blank=True, null=True)
    saldo_disponivel_est = models.FloatField(blank=True, null=True)
    saldo_disp_outras_opr = models.FloatField(blank=True, null=True)
    temp_qtde_produzida = models.FloatField(blank=True, null=True)
    pcp_desc_item_person = models.CharField(max_length=150, blank=True, null=True)
    bloco_gerado = models.IntegerField(blank=True, null=True, db_comment='Se foi gerado a ordem de produþÒo de bloco para espuma do produto.\r\n0 - NÒo necessita de criaþÒo de bloco;\r\n1 - Ord. de produþÒo do bloco nÒo gerada;\r\n2 - Gerado a ordem de produþÒo;\r\n3 - GeraþÒo de bloco cancelada;')
    id_opb = models.IntegerField(blank=True, null=True, db_comment='Ao gerar a Ordem de produþÒo dos blocos de espuma , o sistema irß gravar o c¾digo da O.P.B.')
    criado_em = models.DateField(blank=True, null=True, db_comment='Data quando o registro do opp foi criado.')
    hora_criado = models.TimeField(blank=True, null=True, db_comment='Hora quando o registro do opp foi criado.')

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_opr_opp'
        unique_together = (('id_opr', 'id_opr_opp'),)


class PcpTbMOprOpp030318(models.Model):
    id_opr = models.OneToOneField(PcpTbMOpr, models.DO_NOTHING, db_column='id_opr', primary_key=True)  # The composite primary key (id_opr, id_opr_opp) found, that is not supported. The first column is selected.
    id_opr_opp = models.IntegerField()
    id_item = models.ForeignKey(CadTbCIte, models.DO_NOTHING, db_column='id_item')
    id_cor = models.ForeignKey(CadTbCCor, models.DO_NOTHING, db_column='id_cor')
    id_tamanho = models.IntegerField()
    qtde_a_produzir = models.FloatField()
    qtde_produzida = models.FloatField()
    qtde_a_produzir_orig = models.FloatField(db_comment='Este campo nÒo pode ser alterado pelo usußrio.\nNo momento da criaþÒo deste registro, este campo terß o mesmo valor do campo QTDE_A_PRODUZIR.')
    id_resp_alt = models.IntegerField(blank=True, null=True, db_comment='Este campo Ú preenchido no momento em que o usußrio altera o valor do campo QTDE_A_PRODUZIR.')
    dta_alt = models.DateField(blank=True, null=True, db_comment='Este campo Ú preenchido no momento em que o usußrio altera o valor do campo QTDE_A_PRODUZIR.')
    hora_alt = models.TimeField(blank=True, null=True, db_comment='Este campo Ú preenchido no momento em que o usußrio altera o valor do campo QTDE_A_PRODUZIR.')
    qtde_atender_opr = models.FloatField(db_comment='Este campo tem a funþÒo de informar Ó O.P.R a qtde real que serß utilizada para ela. De inicio ela pode ter mandado Produzir 100, mas depois teve pedido com desistÛncia , onde a qtde a produzir baixaria pra 80, mas o usußrio resolveu deixar a Produzir 100, com isso a O.P.R terß um saldo de 20 que servirß para demais O.P.R.')
    qtde_atender_opr_ext = models.FloatField(db_comment='Toda vez que uma O.P.R externa utiliza o saldo disponÝvel de uma O.P.R, ela deverß quardar a qtde utilizada neste campo.   \n\tImagine que: QTDE_A_PRODUZIR = 70 \n                                      QTDE_ATENDER_OPR = 60 \n                                      QTD_ATENDER_OPR_EXT = 4\n                                      SALDO_DISPONIVEL = 6 \n e a O.P.R Externa estß precisando de 2.  \n               EntÒo  ficarß:   QTDE_A_PRODUZIR = 70 \n                                      QTDE_ATENDER_OPR = 60 \n                                      QTD_ATENDER_OPR_EXT = 6\n                                      SALDO_DISPONIVEL = 4 \n')
    saldo_disponivel = models.FloatField(db_comment='SALDO_DISPONIVEL:  float    QTDE_A_PRODUZIR û ( QTD_ATENDER_OPR +  QTD_ATENDER_OPR_EXT)')
    reg_alt = models.BooleanField(blank=True, null=True)
    historico_alt = models.CharField(max_length=500, blank=True, null=True, db_comment='Cada vez que houver alguma alteraþÒo neste registro o sistema irß guardando o conte·do do campo Motivo da alteraþÒo.')
    motivo_alt = models.CharField(max_length=100, blank=True, null=True)
    gerado_aut = models.BooleanField(blank=True, null=True, db_comment='Serß TRUE quando for gerado pela ImportaþÒo do Pedido de Venda. Caso for inserido manualmente, serß FALSE;')
    motivo_ger_man = models.CharField(max_length=100, blank=True, null=True, db_comment='Motivo do por quÛ que estß inserido o produto manualmente na ordem de produþÒo.')
    id_resp_man = models.IntegerField(blank=True, null=True)
    dta_man = models.DateField(blank=True, null=True)
    hor_man = models.TimeField(blank=True, null=True)
    id_busca_item = models.CharField(max_length=20, blank=True, null=True)
    obs_producao = models.CharField(max_length=800, blank=True, null=True)
    pcp_desc_item_person = models.CharField(max_length=150, blank=True, null=True)
    saldo_fisico_momento = models.FloatField(blank=True, null=True)
    saldo_pendente = models.FloatField(blank=True, null=True)
    saldo_disponivel_est = models.FloatField(blank=True, null=True)
    saldo_disp_outras_opr = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_opr_opp_030318'
        unique_together = (('id_opr', 'id_opr_opp'),)


class PcpTbMOprOppCopy(models.Model):
    id_opr = models.OneToOneField(PcpTbMOpr, models.DO_NOTHING, db_column='id_opr', primary_key=True)  # The composite primary key (id_opr, id_opr_opp) found, that is not supported. The first column is selected.
    id_opr_opp = models.IntegerField()
    id_item = models.ForeignKey(CadTbCIte, models.DO_NOTHING, db_column='id_item')
    id_cor = models.ForeignKey(CadTbCCor, models.DO_NOTHING, db_column='id_cor')
    id_tamanho = models.IntegerField()
    qtde_a_produzir = models.FloatField()
    qtde_produzida = models.FloatField()
    qtde_a_produzir_orig = models.FloatField(db_comment='Este campo nÒo pode ser alterado pelo usußrio.\nNo momento da criaþÒo deste registro, este campo terß o mesmo valor do campo QTDE_A_PRODUZIR.')
    id_resp_alt = models.IntegerField(blank=True, null=True, db_comment='Este campo Ú preenchido no momento em que o usußrio altera o valor do campo QTDE_A_PRODUZIR.')
    dta_alt = models.DateField(blank=True, null=True, db_comment='Este campo Ú preenchido no momento em que o usußrio altera o valor do campo QTDE_A_PRODUZIR.')
    hora_alt = models.TimeField(blank=True, null=True, db_comment='Este campo Ú preenchido no momento em que o usußrio altera o valor do campo QTDE_A_PRODUZIR.')
    qtde_atender_opr = models.FloatField(db_comment='Este campo tem a funþÒo de informar Ó O.P.R a qtde real que serß utilizada para ela. De inicio ela pode ter mandado Produzir 100, mas depois teve pedido com desistÛncia , onde a qtde a produzir baixaria pra 80, mas o usußrio resolveu deixar a Produzir 100, com isso a O.P.R terß um saldo de 20 que servirß para demais O.P.R.')
    qtde_atender_opr_ext = models.FloatField(db_comment='Toda vez que uma O.P.R externa utiliza o saldo disponÝvel de uma O.P.R, ela deverß quardar a qtde utilizada neste campo.   \n\tImagine que: QTDE_A_PRODUZIR = 70 \n                                      QTDE_ATENDER_OPR = 60 \n                                      QTD_ATENDER_OPR_EXT = 4\n                                      SALDO_DISPONIVEL = 6 \n e a O.P.R Externa estß precisando de 2.  \n               EntÒo  ficarß:   QTDE_A_PRODUZIR = 70 \n                                      QTDE_ATENDER_OPR = 60 \n                                      QTD_ATENDER_OPR_EXT = 6\n                                      SALDO_DISPONIVEL = 4 \n')
    saldo_disponivel = models.FloatField(db_comment='SALDO_DISPONIVEL:  float    QTDE_A_PRODUZIR û ( QTD_ATENDER_OPR +  QTD_ATENDER_OPR_EXT)')
    reg_alt = models.BooleanField(blank=True, null=True)
    historico_alt = models.CharField(max_length=500, blank=True, null=True, db_comment='Cada vez que houver alguma alteraþÒo neste registro o sistema irß guardando o conte·do do campo Motivo da alteraþÒo.')
    motivo_alt = models.CharField(max_length=100, blank=True, null=True)
    gerado_aut = models.BooleanField(blank=True, null=True, db_comment='Serß TRUE quando for gerado pela ImportaþÒo do Pedido de Venda. Caso for inserido manualmente, serß FALSE;')
    motivo_ger_man = models.CharField(max_length=100, blank=True, null=True, db_comment='Motivo do por quÛ que estß inserido o produto manualmente na ordem de produþÒo.')
    id_resp_man = models.IntegerField(blank=True, null=True)
    dta_man = models.DateField(blank=True, null=True)
    hor_man = models.TimeField(blank=True, null=True)
    id_busca_item = models.CharField(max_length=20, blank=True, null=True)
    obs_producao = models.CharField(max_length=800, blank=True, null=True)
    pcp_desc_item_person = models.CharField(max_length=150, blank=True, null=True)
    saldo_fisico_momento = models.FloatField(blank=True, null=True)
    saldo_pendente = models.FloatField(blank=True, null=True)
    saldo_disponivel_est = models.FloatField(blank=True, null=True)
    saldo_disp_outras_opr = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_opr_opp_copy'
        unique_together = (('id_opr', 'id_opr_opp'),)


class PcpTbMOprOppSop(models.Model):
    id_opr = models.OneToOneField(PcpTbMOprOpp, models.DO_NOTHING, db_column='id_opr', primary_key=True)  # The composite primary key (id_opr, id_opr_opp, id_opr_sop) found, that is not supported. The first column is selected.
    id_opr_opp = models.IntegerField()
    id_opr_sop = models.IntegerField()
    id_opr_ext = models.ForeignKey(PcpTbMOprOpp, models.DO_NOTHING, db_column='id_opr_ext', related_name='pcptbmoproppsop_id_opr_ext_set')
    id_opr_opp_ext = models.IntegerField(blank=True, null=True)
    dta_utilizado = models.DateField()
    hor_utilizado = models.TimeField()
    qtd_utilizado = models.FloatField()

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_opr_opp_sop'
        unique_together = (('id_opr', 'id_opr_opp', 'id_opr_sop'),)
        db_table_comment = 'Saldo utilizado por outras O.P.Rs.'


class PcpTbMOprOps(models.Model):
    id_opr = models.OneToOneField(PcpTbMOpr, models.DO_NOTHING, db_column='id_opr', primary_key=True)  # The composite primary key (id_opr, id_opr_ops) found, that is not supported. The first column is selected.
    id_opr_ops = models.IntegerField()
    id_setor = models.ForeignKey(CadTbCSet, models.DO_NOTHING, db_column='id_setor')
    id_item = models.ForeignKey(CadTbCIte, models.DO_NOTHING, db_column='id_item')
    id_cor = models.ForeignKey(CadTbCCor, models.DO_NOTHING, db_column='id_cor')
    id_tamanho = models.IntegerField()
    qtde = models.FloatField()
    tamanho = models.CharField(max_length=15, blank=True, null=True)
    referencias = models.CharField(max_length=100, blank=True, null=True)
    num_lote = models.CharField(max_length=150, blank=True, null=True, db_comment='O usußrio poderß informar N lotes.')
    id_item_acabado = models.ForeignKey(CadTbCIte, models.DO_NOTHING, db_column='id_item_acabado', related_name='pcptbmoprops_id_item_acabado_set')
    id_cor_acabado = models.IntegerField()
    id_tamanho_acabado = models.IntegerField()
    num_lote_bordadeira = models.CharField(max_length=150, blank=True, null=True)
    num_lote_espuma = models.CharField(max_length=150, blank=True, null=True)
    num_lote_tecido = models.CharField(max_length=150, blank=True, null=True)
    num_lote_tnt = models.CharField(max_length=150, blank=True, null=True)
    qtde_acabado = models.FloatField(blank=True, null=True)
    obs_producao = models.CharField(max_length=800, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_opr_ops'
        unique_together = (('id_opr', 'id_opr_ops'),)


class PcpTbMOprOpsIps(models.Model):
    id_opr = models.OneToOneField(PcpTbMOprOps, models.DO_NOTHING, db_column='id_opr', primary_key=True)  # The composite primary key (id_opr, id_opr_ops, id_opr_ops_ips) found, that is not supported. The first column is selected.
    id_opr_ops = models.IntegerField()
    id_opr_ops_ips = models.IntegerField()
    id_item = models.ForeignKey(CadTbCIte, models.DO_NOTHING, db_column='id_item')
    id_cor = models.ForeignKey(CadTbCCor, models.DO_NOTHING, db_column='id_cor')
    id_tamanho = models.IntegerField()
    qtde = models.FloatField()
    num_lote = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_opr_ops_ips'
        unique_together = (('id_opr', 'id_opr_ops', 'id_opr_ops_ips'),)


class PcpTbMOprOpsLot(models.Model):
    id_opr = models.OneToOneField(PcpTbMOprOps, models.DO_NOTHING, db_column='id_opr', primary_key=True)  # The composite primary key (id_opr, id_opr_ops, id_opr_lot) found, that is not supported. The first column is selected.
    id_opr_ops = models.IntegerField()
    id_opr_lot = models.IntegerField()
    qtde = models.FloatField(blank=True, null=True)
    num_lote = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_opr_ops_lot'
        unique_together = (('id_opr', 'id_opr_ops', 'id_opr_lot'),)
        db_table_comment = 'Lotes da O.P.S'


class PcpTbMOprPed(models.Model):
    id_opr = models.OneToOneField(PcpTbMOpr, models.DO_NOTHING, db_column='id_opr', primary_key=True)  # The composite primary key (id_opr, id_pedido) found, that is not supported. The first column is selected.
    id_pedido = models.ForeignKey(FatTbMPed, models.DO_NOTHING, db_column='id_pedido')
    remanejado = models.BooleanField(db_comment='Este campo receberß TRUE automaticamente quando outra O.P.R pegar este pedido de venda, senÒo terß o valor FALSE.')
    id_opr_ori = models.IntegerField(blank=True, null=True, db_comment='Este campo Ú preenchido no momento da importaþÒo do pedido. Este campos serß preenchido quando o pedido de venda for oriundo de outra O.P.R.')
    id_opr_dest = models.IntegerField(blank=True, null=True, db_comment='Este campo serß preenchido automaticamente no momento em que outra O.P.R pegar este pedido de venda.')
    origem_insercao = models.IntegerField(blank=True, null=True, db_comment='0 - Pedido inserido por importacao;\r\n1 - Pedido inserido por pedido automßtico(Quando  o pedido Ú gerado partindo de um pedido jß em produþÒo);')
    id_responsavel = models.IntegerField(blank=True, null=True)
    dta_importacao = models.DateField(blank=True, null=True)
    hor_importacao = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_opr_ped'
        unique_together = (('id_opr', 'id_pedido'),)


class PcpTbMOprReq(models.Model):
    id_opr = models.OneToOneField(PcpTbMOpr, models.DO_NOTHING, db_column='id_opr', primary_key=True)  # The composite primary key (id_opr, id_opr_req) found, that is not supported. The first column is selected.
    id_opr_req = models.IntegerField()
    dta_emissao = models.DateField()
    id_funcionario_canc = models.IntegerField(blank=True, null=True)
    dta_canc = models.DateField(blank=True, null=True)
    hor_canc = models.TimeField(blank=True, null=True)
    id_responsavel = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_responsavel', blank=True, null=True)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    cancelado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_opr_req'
        unique_together = (('id_opr', 'id_opr_req'),)


class PcpTbMOprReqIte(models.Model):
    id_opr = models.OneToOneField(PcpTbMOprReq, models.DO_NOTHING, db_column='id_opr', primary_key=True)  # The composite primary key (id_opr, id_opr_req, id_opr_req_ite) found, that is not supported. The first column is selected.
    id_opr_req = models.IntegerField()
    id_opr_req_ite = models.IntegerField()
    id_item = models.ForeignKey(CadTbCIte, models.DO_NOTHING, db_column='id_item')
    id_cor = models.ForeignKey(CadTbCCor, models.DO_NOTHING, db_column='id_cor')
    id_tamanho = models.IntegerField()
    qtde = models.FloatField()
    qtde_atendida = models.FloatField(blank=True, null=True)
    dta_canc = models.DateField(blank=True, null=True)
    hor_canc = models.TimeField(blank=True, null=True)
    id_funcionario_canc = models.IntegerField(blank=True, null=True)
    situacao = models.IntegerField(blank=True, null=True, db_comment='1 - Em aberto\r\n2 - Atendido parcial\r\n3 - Atendido total')
    id_setor = models.ForeignKey(CadTbCSet, models.DO_NOTHING, db_column='id_setor')
    id_busca_item = models.CharField(max_length=30, blank=True, null=True)
    num_lote = models.CharField(max_length=15, blank=True, null=True)
    gerado_automatico = models.BooleanField(blank=True, null=True)
    cancelado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_opr_req_ite'
        unique_together = (('id_opr', 'id_opr_req', 'id_opr_req_ite'),)


class PcpTbMOrs(models.Model):
    id_ors = models.IntegerField(primary_key=True)
    id_empresa = models.ForeignKey(CadTbCPar, models.DO_NOTHING, db_column='id_empresa')
    dta_emissao = models.DateField()
    id_responsavel = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_responsavel')
    observacao = models.CharField(max_length=200, blank=True, null=True)
    id_pedido = models.IntegerField(blank=True, null=True)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    id_motorista = models.ForeignKey(PcpTbCMta, models.DO_NOTHING, db_column='id_motorista', blank=True, null=True)
    id_rom = models.IntegerField(blank=True, null=True, db_comment='Este campo Ú alimentado no momento em que o usußrio digita o c¾digo do pedido de venda. Este campo Ú alimentado automaticamente.')
    id_tipo_mov_estoque = models.IntegerField(blank=True, null=True)
    id_almoxarifado = models.IntegerField(blank=True, null=True)
    vlr_bruto = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    vlr_desconto = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    per_desconto = models.FloatField(blank=True, null=True)
    vlr_liquido = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    hor_emissao = models.TimeField(blank=True, null=True)
    id_abertura = models.IntegerField(blank=True, null=True)
    fin_gerado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_ors'
        db_table_comment = 'Tabela de Ordem de SaÝdas'


class PcpTbMOrsIco(models.Model):
    id_ors = models.OneToOneField(PcpTbMOrs, models.DO_NOTHING, db_column='id_ors', primary_key=True)  # The composite primary key (id_ors, id_sequencia) found, that is not supported. The first column is selected.
    id_sequencia = models.IntegerField()
    id_item = models.ForeignKey(CadTbCIte, models.DO_NOTHING, db_column='id_item')
    id_cor = models.IntegerField()
    id_tamanho = models.IntegerField()
    qtde = models.FloatField()
    vlr_unitario = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_bruto = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_liquido = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    vlr_desconto = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    per_desconto = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_ors_ico'
        unique_together = (('id_ors', 'id_sequencia'),)


class PcpTbMOrsIte(models.Model):
    id_ors = models.OneToOneField(PcpTbMOrs, models.DO_NOTHING, db_column='id_ors', primary_key=True)  # The composite primary key (id_ors, id_sequencia) found, that is not supported. The first column is selected.
    id_sequencia = models.IntegerField()
    id_item = models.ForeignKey(CadTbCIte, models.DO_NOTHING, db_column='id_item')
    id_cor = models.IntegerField()
    id_tamanho = models.IntegerField()
    qtde = models.FloatField()
    vlr_unitario = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    vlr_bruto = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    id_sequencia_ped = models.IntegerField(blank=True, null=True)
    vlr_liquido = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    vlr_desconto = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    per_desconto = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_ors_ite'
        unique_together = (('id_ors', 'id_sequencia'),)


class PcpTbMOrsTit(models.Model):
    id_ors = models.OneToOneField(PcpTbMOrs, models.DO_NOTHING, db_column='id_ors', primary_key=True)  # The composite primary key (id_ors, id_ors_tit) found, that is not supported. The first column is selected.
    id_ors_tit = models.IntegerField()
    id_forma_pag = models.ForeignKey(CadTbCFpg, models.DO_NOTHING, db_column='id_forma_pag')
    num_parcela = models.CharField(max_length=20, blank=True, null=True)
    dias = models.IntegerField()
    dta_vencimento = models.DateField()
    che_banco = models.CharField(max_length=10, blank=True, null=True)
    che_agencia = models.CharField(max_length=10, blank=True, null=True)
    che_conta = models.IntegerField(blank=True, null=True)
    che_numero = models.IntegerField(blank=True, null=True)
    che_emitente = models.CharField(max_length=50, blank=True, null=True)
    vlr_titulo = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_ors_tit'
        unique_together = (('id_ors', 'id_ors_tit'),)


class PcpTbMPsc(models.Model):
    id_psc = models.IntegerField(primary_key=True)
    id_empresa = models.ForeignKey(CadTbCPar, models.DO_NOTHING, db_column='id_empresa')
    nome_cliente = models.CharField(max_length=80, blank=True, null=True)
    data = models.DateField()
    cidade = models.CharField(max_length=30, blank=True, null=True)
    estado = models.CharField(max_length=2, blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    celular = models.CharField(max_length=15, blank=True, null=True)
    observacao = models.CharField(max_length=100, blank=True, null=True)
    pergunta_1 = models.IntegerField(db_comment='(1)\nVocÛ comprarß ou utilizarß o colchÒo GLOBO novamente?\n\n0 - NÒo\n1 - Sim')
    pergunta_2 = models.IntegerField(db_comment='(2)\nVocÛ recomendaria colchÒo GLOBO para outras pessoas?\n\n0 - NÒo\n1 - Sim')
    pergunta_3 = models.IntegerField(db_comment='(3)\nHß quanto tempo o Sr.(a) vem utilizando o colchÒo de Espuma da GLOBO?\n\n0 - menos de 1 ano\n1 - mais de 1 ano')
    pergunta_4 = models.IntegerField(db_comment='(4)\nEm comparaþÒo com outras alternativas de colch§es, o colchÒo GLOBO Ú:\n\n0 - Melhor\n1 - Igual\n2 - Pior')
    pergunta_1_resposta = models.CharField(max_length=80, blank=True, null=True, db_comment='Este campo Ú utilizado quando o valor do campo PERGUNTA_4 for = N├O.')
    pergunta_5 = models.IntegerField(db_comment='(5)\nQual Ú o seu grau de satisfaþÒo geral com o seu colchÒo GLOBO?\n\n0 - Excelente\n1 - Bom \n2 - Razoßvel\n3 - Ruim')
    pergunta_2_resposta = models.CharField(max_length=80, blank=True, null=True, db_comment='Este campo Ú utilizado quando o valor do campo PERGUNTA_5 for = N├O.')
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    id_responsavel = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_psc'


class PcpTbMRaa(models.Model):
    id_raa = models.IntegerField(primary_key=True)
    id_empresa = models.ForeignKey(CadTbCPar, models.DO_NOTHING, db_column='id_empresa')
    dta_emissao = models.DateField()
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    nro_raa = models.CharField(max_length=15, blank=True, null=True, db_comment='Este campo terß a mesma sequencia do nro do lote interno do produto que Ú utilizado pela NF de entrada.')
    id_item = models.ForeignKey(CadTbCIte, models.DO_NOTHING, db_column='id_item')
    dta_recebimento_item = models.DateField()
    codigo_fabrica = models.CharField(max_length=30, blank=True, null=True)
    id_fornecedor = models.ForeignKey(CadTbCFor, models.DO_NOTHING, db_column='id_fornecedor')
    id_fabricante = models.ForeignKey(CadTbCFor, models.DO_NOTHING, db_column='id_fabricante', related_name='pcptbmraa_id_fabricante_set')
    qtde_amostra = models.FloatField()
    id_setor = models.ForeignKey(CadTbCSet, models.DO_NOTHING, db_column='id_setor')
    pergunta_1 = models.IntegerField(db_comment='Pergunta padrÒo:\nQuantidade da amostra Ú suficiente para os testes?\n\n0 - NÒo\n1 - Sim\n2 - NÒo aplicßvel')
    pergunta_2 = models.IntegerField(db_comment='Pergunta padrÒo:\nQualidade do produto esta de acordo com o solicitado?\n\n0 - NÒo\n1 - Sim\n2 - NÒo aplicßvel')
    pergunta_3 = models.IntegerField(db_comment='Pergunta padrÒo:\nO Material atendeu as expectativas?\n\n0 - NÒo\n1 - Sim\n2 - NÒo aplicßvel')
    pergunta_4 = models.IntegerField(db_comment='Pergunta padrÒo:\nO material precisa de alguma adaptaþÒo?\n\n0 - NÒo\n1 - Sim\n2 - NÒo aplicßvel')
    pergunta_5 = models.IntegerField(db_comment='Pergunta padrÒo:\nNecessita de mais amostra para concluir os testes?\n\n0 - NÒo\n1 - Sim\n2 - NÒo aplicßvel')
    pergunta_6 = models.IntegerField(db_comment='Pergunta padrÒo:\nNecessidade de anßlise em laborat¾rio?\n\n0 - NÒo\n1 - Sim\n2 - NÒo aplicßvel')
    pergunta_7 = models.IntegerField(db_comment='Pergunta padrÒo:\nEspessura X Largura X Comprimento estÒo de acordo com o especificado?\n\n0 - NÒo\n1 - Sim\n2 - NÒo aplicßvel')
    pergunta_8 = models.IntegerField(db_comment='Pergunta padrÒo:\nGramatura/peso estÒo de acordo com o especificado?\n\n0 - NÒo\n1 - Sim\n2 - NÒo aplicßvel')
    resultado = models.IntegerField(db_comment='0 - Reprovado\n1 - Aprovado')
    incorpora_item = models.IntegerField(db_comment='Incorpora o item na estrutura do produto?\n\n0 - NÒo\n1 - Sim')
    id_analista = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_analista')
    dta_analise = models.DateField(blank=True, null=True)
    observacao = models.CharField(max_length=80, blank=True, null=True)
    id_cor = models.IntegerField(blank=True, null=True)
    id_tamanho = models.IntegerField(blank=True, null=True)
    qtde_nf = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_raa'
        db_table_comment = 'Relat¾rio de Anßlise de Amostra.'


class PcpTbMRaaIte(models.Model):
    id_raa = models.OneToOneField(PcpTbMRaa, models.DO_NOTHING, db_column='id_raa', primary_key=True)  # The composite primary key (id_raa, id_raa_ite) found, that is not supported. The first column is selected.
    id_raa_ite = models.IntegerField()
    acao_necessaria = models.CharField(max_length=150, blank=True, null=True)
    id_responsavel = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_responsavel')
    dta_prazo = models.DateField(db_comment='Prazo')
    dta_executado = models.DateField(blank=True, null=True, db_comment='Executado em')
    observacao = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_raa_ite'
        unique_together = (('id_raa', 'id_raa_ite'),)
        db_table_comment = 'Relat¾rio de Anßlise de Amostra - Itens'


class PcpTbMRec(models.Model):
    id_protocolo = models.IntegerField(primary_key=True)
    id_empresa = models.IntegerField()
    dta_reclamacao = models.DateField()
    id_cliente = models.IntegerField()
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_rec'


class PcpTbMRecIpp(models.Model):
    id_protocolo = models.OneToOneField(PcpTbMRec, models.DO_NOTHING, db_column='id_protocolo', primary_key=True)  # The composite primary key (id_protocolo, id_sequencia) found, that is not supported. The first column is selected.
    id_sequencia = models.IntegerField()
    id_pedido = models.IntegerField()
    id_item = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_rec_ipp'
        unique_together = (('id_protocolo', 'id_sequencia'),)


class PcpTbMRom(models.Model):
    id_rom = models.IntegerField(primary_key=True)
    id_empresa = models.ForeignKey(CadTbCPar, models.DO_NOTHING, db_column='id_empresa')
    dta_emissao = models.DateField()
    id_responsavel = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_responsavel')
    id_motorista = models.ForeignKey(PcpTbCMta, models.DO_NOTHING, db_column='id_motorista')
    observacao = models.CharField(max_length=200, blank=True, null=True)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)
    placa = models.CharField(max_length=8, blank=True, null=True)
    lot_qtde_total = models.FloatField(blank=True, null=True, db_comment='Neste campo acumula o total das qtde do lote, da tabela PCP_TB_M_ROM_LOT.')
    hor_emissao = models.TimeField(blank=True, null=True)
    hor_alt = models.TimeField(blank=True, null=True, db_comment='Utilizado no momento em que o usußrio altera o romaneio.')
    id_resp_alt = models.IntegerField(blank=True, null=True, db_comment='Usußrio responsßvel por fazer alteraþ§es no Romaneio(Relat¾rio de Cargas).')
    dta_alt = models.DateField(blank=True, null=True)
    hor_fin = models.TimeField(blank=True, null=True)
    dta_fin = models.DateField(blank=True, null=True)
    id_resp_fin = models.IntegerField(blank=True, null=True, db_comment='Usußrio responsßvel pela finalizaþÒo do Romaneio(Relat¾rio de Cargas).')
    ped_ite_qtde_total = models.IntegerField(blank=True, null=True, db_comment='Neste campo acumula o total das qtde dos itens do pedido de venda, da tabela PCP_TB_M_ROM_PED_ITE.')
    id_pca = models.IntegerField(blank=True, null=True)
    qtde_total_ite_conf = models.FloatField(blank=True, null=True, db_comment='Ficarß neste campo qtde total de itens pistolados.')
    seq_pca_carreg_anual = models.IntegerField(blank=True, null=True, db_comment='C¾digo do campo seq_carreg_anual')

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_rom'
        db_table_comment = 'Tabela de Romaneio de Carga'


class PcpTbMRomIcf(models.Model):
    id_rom = models.OneToOneField(PcpTbMRom, models.DO_NOTHING, db_column='id_rom', primary_key=True)  # The composite primary key (id_rom, id_rom_icf) found, that is not supported. The first column is selected.
    id_rom_icf = models.IntegerField()
    id_item = models.ForeignKey(CadTbCIte, models.DO_NOTHING, db_column='id_item')
    id_cor = models.IntegerField()
    id_tamanho = models.IntegerField()
    cod_barra = models.CharField(max_length=50)
    id_responsavel = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_responsavel')
    dta_conferencia = models.DateField()
    hor_conferencia = models.TimeField()
    id_opr_etq = models.IntegerField()
    item_conjugado = models.BooleanField(blank=True, null=True, db_comment='Quando o valor deste campo for TRUE quer dizer , que este item Ú um item conjugado. Pois existe itens do pedido que tem o CAD_TB_C_ITE_COJ preenchido.')
    temp_cod_barra_antigo = models.CharField(max_length=50, blank=True, null=True)
    id_pedido = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_rom_icf'
        unique_together = (('id_rom', 'id_rom_icf'),)
        db_table_comment = 'Tabela de Itens Conferido do Romaneio'


class PcpTbMRomIte(models.Model):
    id_rom = models.OneToOneField(PcpTbMRom, models.DO_NOTHING, db_column='id_rom', primary_key=True)  # The composite primary key (id_rom, id_rom_ite) found, that is not supported. The first column is selected.
    id_rom_ite = models.IntegerField()
    id_item = models.ForeignKey(CadTbCIte, models.DO_NOTHING, db_column='id_item')
    id_cor = models.IntegerField(blank=True, null=True)
    id_tamanho = models.IntegerField(blank=True, null=True)
    qtde = models.FloatField(blank=True, null=True)
    qtde_conferida = models.FloatField(blank=True, null=True)
    qtde_conj = models.FloatField(blank=True, null=True)
    qtde_conj_conf = models.FloatField(blank=True, null=True)
    nome_ite = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_rom_ite'
        unique_together = (('id_rom', 'id_rom_ite'),)
        db_table_comment = 'Itens do romaneio'


class PcpTbMRomLot(models.Model):
    id_rom = models.OneToOneField(PcpTbMRom, models.DO_NOTHING, db_column='id_rom', primary_key=True)  # The composite primary key (id_rom, nro_lote_caminhao) found, that is not supported. The first column is selected.
    nro_lote_caminhao = models.IntegerField()
    qtde = models.FloatField()
    observacao = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_rom_lot'
        unique_together = (('id_rom', 'nro_lote_caminhao'),)


class PcpTbMRomPed(models.Model):
    id_rom = models.OneToOneField(PcpTbMRom, models.DO_NOTHING, db_column='id_rom', primary_key=True)  # The composite primary key (id_rom, id_pedido) found, that is not supported. The first column is selected.
    id_pedido = models.ForeignKey(FatTbMPed, models.DO_NOTHING, db_column='id_pedido')
    status = models.IntegerField(blank=True, null=True, db_comment='0-Pendente\r\n1-Em Andamento\r\n2-Conferido')
    qtde_total_item_conj = models.FloatField(blank=True, null=True)
    qtde_total_item_conj_conf = models.FloatField(blank=True, null=True)
    importado = models.BooleanField(blank=True, null=True, db_comment='Se true, quer dizer que foi importado do Carregamento do Pedido.')

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_rom_ped'
        unique_together = (('id_rom', 'id_pedido'),)
        db_table_comment = 'Pedidos do Romaneio'


class PcpTbMRomPedIcf(models.Model):
    id_rom = models.OneToOneField(PcpTbMRomPed, models.DO_NOTHING, db_column='id_rom', primary_key=True)  # The composite primary key (id_rom, id_pedido, id_sequencia) found, that is not supported. The first column is selected.
    id_pedido = models.IntegerField()
    id_sequencia = models.IntegerField()
    id_item = models.ForeignKey(CadTbCIte, models.DO_NOTHING, db_column='id_item')
    id_cor = models.IntegerField()
    id_tamanho = models.IntegerField()
    cod_barra = models.CharField(max_length=50)
    id_responsavel = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_responsavel')
    dta_conferencia = models.DateField()
    hor_conferencia = models.TimeField()
    id_opr_etq = models.IntegerField()
    item_conjugado = models.BooleanField(blank=True, null=True, db_comment='Quando o valor deste campo for TRUE quer dizer , que este item Ú um item conjugado. Pois existe itens do pedido que tem o CAD_TB_C_ITE_COJ preenchido.')
    temp_cod_barra_antigo = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_rom_ped_icf'
        unique_together = (('id_rom', 'id_pedido', 'id_sequencia'),)
        db_table_comment = 'Tabela de Itens Conferido do Pedido do Romaneio'


class PcpTbMRomPedIcfCopy(models.Model):
    id_rom = models.IntegerField(primary_key=True)  # The composite primary key (id_rom, id_pedido, id_sequencia) found, that is not supported. The first column is selected.
    id_pedido = models.IntegerField()
    id_sequencia = models.IntegerField()
    id_item = models.ForeignKey(CadTbCIte, models.DO_NOTHING, db_column='id_item')
    id_cor = models.IntegerField()
    id_tamanho = models.IntegerField()
    cod_barra = models.CharField(max_length=50)
    id_responsavel = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_responsavel')
    dta_conferencia = models.DateField()
    hor_conferencia = models.TimeField()
    id_opr_etq = models.IntegerField()
    item_conjugado = models.BooleanField(blank=True, null=True, db_comment='Quando o valor deste campo for TRUE quer dizer , que este item Ú um item conjugado. Pois existe itens do pedido que tem o CAD_TB_C_ITE_COJ preenchido.')

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_rom_ped_icf_copy'
        unique_together = (('id_rom', 'id_pedido', 'id_sequencia'),)
        db_table_comment = 'Tabela de Itens Conferido do Pedido do Romaneio'


class PcpTbMRomPedIcj(models.Model):
    id_rom = models.OneToOneField(PcpTbMRomPed, models.DO_NOTHING, db_column='id_rom', primary_key=True)  # The composite primary key (id_rom, id_pedido, id_ped_ite, id_sequencia) found, that is not supported. The first column is selected.
    id_pedido = models.IntegerField()
    id_sequencia = models.IntegerField()
    id_item = models.ForeignKey(CadTbCIte, models.DO_NOTHING, db_column='id_item')
    id_cor = models.IntegerField()
    id_tamanho = models.IntegerField()
    id_responsavel = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_responsavel')
    dta_conferencia = models.DateField()
    hor_conferencia = models.TimeField()
    id_ped_ite = models.IntegerField(db_comment='Este campo se refere ao mesmo campo da tabela PCP_TB_M_ROM_PED_ITE')
    qtde_a_inserir = models.FloatField(blank=True, null=True)
    qtde_conf = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_rom_ped_icj'
        unique_together = (('id_rom', 'id_pedido', 'id_ped_ite', 'id_sequencia'),)
        db_table_comment = 'Tabela de Itens Conferido do Pedido do Romaneio'


class PcpTbMRomPedIte(models.Model):
    id_rom = models.OneToOneField(PcpTbMRomPed, models.DO_NOTHING, db_column='id_rom', primary_key=True)  # The composite primary key (id_rom, id_pedido, id_ped_ite) found, that is not supported. The first column is selected.
    id_pedido = models.IntegerField()
    id_ped_ite = models.IntegerField()
    id_item = models.ForeignKey(CadTbCIte, models.DO_NOTHING, db_column='id_item')
    id_cor = models.IntegerField(blank=True, null=True)
    id_tamanho = models.IntegerField(blank=True, null=True)
    qtde = models.FloatField(blank=True, null=True)
    qtde_conferida = models.FloatField(blank=True, null=True)
    qtde_conj = models.FloatField(blank=True, null=True)
    qtde_conj_conf = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_rom_ped_ite'
        unique_together = (('id_rom', 'id_pedido', 'id_ped_ite'),)
        db_table_comment = 'Itens dos pedidos no romaneio'


class PcpTbMRvc(models.Model):
    id_rvc = models.IntegerField(primary_key=True)
    dta_revisao = models.DateField()
    id_empresa = models.ForeignKey(CadTbCPar, models.DO_NOTHING, db_column='id_empresa')
    col_tot_ite_rev = models.IntegerField()
    col_tot_def_ide = models.IntegerField()
    col_tot_col = models.IntegerField()
    col_num_maior_def = models.IntegerField()
    def_maior_nro_ocor = models.IntegerField()
    indice_defeitos = models.FloatField()
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_rvc'
        db_table_comment = 'CONTROLE DE DEFEITOS NA REVIS├O DOS COLCHıES\nConforme a planilha C¾d. I 7.5-9-01'


class PcpTbMRvcIte(models.Model):
    id_rvc = models.OneToOneField(PcpTbMRvc, models.DO_NOTHING, db_column='id_rvc', primary_key=True)  # The composite primary key (id_rvc, id_rvc_ite) found, that is not supported. The first column is selected.
    id_rvc_ite = models.IntegerField()
    id_item = models.ForeignKey(CadTbCIte, models.DO_NOTHING, db_column='id_item')
    id_cor = models.ForeignKey(CadTbCCor, models.DO_NOTHING, db_column='id_cor')
    id_tamanho = models.IntegerField()
    id_responsavel = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_responsavel')
    observacao = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_rvc_ite'
        unique_together = (('id_rvc', 'id_rvc_ite'),)


class PcpTbMRvcIteSet(models.Model):
    id_rvc = models.OneToOneField(PcpTbMRvcIte, models.DO_NOTHING, db_column='id_rvc', primary_key=True)  # The composite primary key (id_rvc, id_rvc_ite, id_setor) found, that is not supported. The first column is selected.
    id_rvc_ite = models.IntegerField()
    id_setor = models.ForeignKey(CadTbCSet, models.DO_NOTHING, db_column='id_setor')

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_rvc_ite_set'
        unique_together = (('id_rvc', 'id_rvc_ite', 'id_setor'),)


class PcpTbMRvcIteSetDef(models.Model):
    id_rvc = models.OneToOneField(PcpTbMRvcIteSet, models.DO_NOTHING, db_column='id_rvc', primary_key=True)  # The composite primary key (id_rvc, id_rvc_ite, id_setor, id_tdf) found, that is not supported. The first column is selected.
    id_rvc_ite = models.IntegerField()
    id_setor = models.IntegerField()
    id_tdf = models.ForeignKey(CadTbCTdf, models.DO_NOTHING, db_column='id_tdf')

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_rvc_ite_set_def'
        unique_together = (('id_rvc', 'id_rvc_ite', 'id_setor', 'id_tdf'),)


class PcpTbMVve(models.Model):
    id_vve = models.IntegerField(primary_key=True)
    id_veiculo = models.ForeignKey(CadTbCVei, models.DO_NOTHING, db_column='id_veiculo', blank=True, null=True)
    dta_cadastro = models.DateField()
    situacao_limpeza = models.BooleanField()
    situacao_revestimento = models.BooleanField()
    situacao_madeiramento = models.BooleanField()
    situacao_bau = models.BooleanField()
    id_responsavel = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_responsavel')
    texto_nao_conformidade = models.CharField(max_length=800, blank=True, null=True)
    cod_lme = models.CharField(max_length=20, blank=True, null=True)
    rev_lme = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcp_tb_m_vve'


class ProTbMPmb(models.Model):
    dta_rec = models.DateField(blank=True, null=True)
    hor_rec = models.TimeField(blank=True, null=True)
    pacote_mobile = models.BinaryField(blank=True, null=True)
    id_funcionario = models.IntegerField(blank=True, null=True)
    pacote_utilizado = models.BooleanField(blank=True, null=True, db_comment='Caso for TRUE quer dizer que o pacote foi utilizado com sucesso para a geraþÒo das visitas, pedido, etc.')
    id_pmb = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'pro_tb_m_pmb'
        db_table_comment = 'Tabela de Pacote de Dados do Mobile'


class ProTbMVis(models.Model):
    id_vis = models.IntegerField(primary_key=True)
    semana = models.IntegerField()
    id_vendedor = models.ForeignKey(CadTbCFun, models.DO_NOTHING, db_column='id_vendedor')
    fechada = models.BooleanField(blank=True, null=True)
    id_empresa = models.IntegerField(blank=True, null=True)
    ano = models.IntegerField(blank=True, null=True)
    dta_criacao = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pro_tb_m_vis'
        db_table_comment = 'Tabela de Vistas a serem feitas aos produtores'


class ProTbMVisCli(models.Model):
    id_vis = models.OneToOneField(ProTbMVis, models.DO_NOTHING, db_column='id_vis', primary_key=True)  # The composite primary key (id_vis, id_vis_cli) found, that is not supported. The first column is selected.
    id_vis_cli = models.IntegerField()
    doc_cnpj_cpf = models.CharField(max_length=14, blank=True, null=True)
    dta_visita = models.DateField(blank=True, null=True)
    id_cliente = models.ForeignKey(CadTbCCli, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pro_tb_m_vis_cli'
        unique_together = (('id_vis', 'id_vis_cli'),)
        db_table_comment = 'Tabela de clientes da vista ao produtor por semana.'


class TbSaldoFinal2020Fea(models.Model):
    id_item = models.IntegerField(blank=True, null=True)
    id_cor = models.IntegerField(blank=True, null=True)
    qtde_tot_entradas = models.FloatField(blank=True, null=True)
    qtde_tot_saidas = models.FloatField(blank=True, null=True)
    saldo = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_saldo_final_2020_fea'


class Teste(models.Model):
    nome = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teste'
