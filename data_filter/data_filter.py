import pandas as pd
import numpy as np

def main():
    df = pd.read_csv("raw_dataset.csv")
    
    df = df.drop(columns=['nome_do_fundo', 'data_da_analise'])
    
    grp = df.groupby('nome_do_titulo').agg(
                                            worth_it = ('worth_it', 'mean'),
                                            numeroTotalDeCotistas_mean = ('numeroTotalDeCotistas', 'mean'),
                                            numeroTotalDeCotistas_std = ('numeroTotalDeCotistas', 'std'),
                                            n_cotistas_pessoa_fisica_mean = ('n_cotistas_pessoa_fisica', 'mean'),
                                            n_cotistas_pessoa_fisica_std = ('n_cotistas_pessoa_fisica', 'std'),
                                            n_cotistas_pessoa_juridica_nao_financeira_mean = ('n_cotistas_pessoa_juridica_nao_financeira', 'mean'),
                                            n_cotistas_pessoa_juridica_nao_financeira_std = ('n_cotistas_pessoa_juridica_nao_financeira', 'std'),
                                            n_cotistas_banco_comercial_mean = ('n_cotistas_banco_comercial', 'mean'),
                                            n_cotistas_banco_comercial_std = ('n_cotistas_banco_comercial', 'std'),
                                            n_cotistas_corretora_ou_distribuidora_mean = ('n_cotistas_corretora_ou_distribuidora', 'mean'),
                                            n_cotistas_corretora_ou_distribuidora_std = ('n_cotistas_corretora_ou_distribuidora', 'std'),
                                            n_cotistas_outras_pessoas_juridicas_financeiras_mean = ('n_cotistas_outras_pessoas_juridicas_financeiras', 'mean'),
                                            n_cotistas_outras_pessoas_juridicas_financeiras_std = ('n_cotistas_outras_pessoas_juridicas_financeiras', 'std'),
                                            n_cotistas_investidores_nao_residentes_mean = ('n_cotistas_investidores_nao_residentes', 'mean'),
                                            n_cotistas_investidores_nao_residentes_std = ('n_cotistas_investidores_nao_residentes', 'std'),
                                            n_cotistas_entidade_aberta_de_previdencia_mean = ('n_cotistas_entidade_aberta_de_previdencia', 'mean'),
                                            n_cotistas_entidade_aberta_de_previdencia_std = ('n_cotistas_entidade_aberta_de_previdencia', 'std'),
                                            n_cotistas_entidade_fechada_de_previdencia_mean = ('n_cotistas_entidade_fechada_de_previdencia', 'mean'),
                                            n_cotistas_entidade_fechada_de_previdencia_std = ('n_cotistas_entidade_fechada_de_previdencia', 'std'),
                                            n_cotistas_regime_proprio_de_previdencia_mean = ('n_cotistas_regime_proprio_de_previdencia', 'mean'),
                                            n_cotistas_regime_proprio_de_previdencia_std = ('n_cotistas_regime_proprio_de_previdencia', 'std'),
                                            n_cotistas_sociedade_seguradora_mean = ('n_cotistas_sociedade_seguradora', 'mean'),
                                            n_cotistas_sociedade_seguradora_std = ('n_cotistas_sociedade_seguradora', 'std'),
                                            n_cotistas_sociedade_de_capitalizacao_mean = ('n_cotistas_sociedade_de_capitalizacao', 'mean'),
                                            n_cotistas_sociedade_de_capitalizacao_std = ('n_cotistas_sociedade_de_capitalizacao', 'std'),
                                            n_cotistas_fiis_mean = ('n_cotistas_fiis', 'mean'),
                                            n_cotistas_fiis_std = ('n_cotistas_fiis', 'std'),
                                            n_cotistas_outros_fundos_de_investimento_mean = ('n_cotistas_outros_fundos_de_investimento', 'mean'),
                                            n_cotistas_outros_fundos_de_investimento_std = ('n_cotistas_outros_fundos_de_investimento', 'std'),
                                            n_cotistas_distribuidores_de_fundo_mean = ('n_cotistas_distribuidores_de_fundo', 'mean'),
                                            n_cotistas_distribuidores_de_fundo_std = ('n_cotistas_distribuidores_de_fundo', 'std'),
                                            n_cotistas_nao_relacionados_mean = ('n_cotistas_nao_relacionados', 'mean'),
                                            n_cotistas_nao_relacionados_std = ('n_cotistas_nao_relacionados', 'std'),
                                            ativos_mean = ('ativos', 'mean'),
                                            ativos_std = ('ativos', 'std'),
                                            patrimonio_liquido_mean = ('patrimonio_liquido', 'mean'),
                                            patrimonio_liquido_std = ('patrimonio_liquido', 'std'),
                                            n_de_cotas_emitidas_mean = ('n_de_cotas_emitidas', 'mean'),
                                            n_de_cotas_emitidas_std = ('n_de_cotas_emitidas', 'std'),
                                            valor_patrimonial_das_cotas_mean = ('valor_patrimonial_das_cotas', 'mean'),
                                            valor_patrimonial_das_cotas_std = ('valor_patrimonial_das_cotas', 'std'),
                                            despesas_com_taxas_de_adm_em_relacao_ao_patrimonio_mean = ('despesas_com_taxas_de_adm_em_relacao_ao_patrimonio', 'mean'),
                                            despesas_com_taxas_de_adm_em_relacao_ao_patrimonio_std = ('despesas_com_taxas_de_adm_em_relacao_ao_patrimonio', 'std'),
                                            despesas_com_agente_custodiante_em_relacao_ao_patrimonio_mean = ('despesas_com_agente_custodiante_em_relacao_ao_patrimonio', 'mean'),
                                            despesas_com_agente_custodiante_em_relacao_ao_patrimonio_std = ('despesas_com_agente_custodiante_em_relacao_ao_patrimonio', 'std'),
                                            rentabilidade_efetiva_mensal_mean = ('rentabilidade_efetiva_mensal', 'mean'),
                                            rentabilidade_efetiva_mensal_std = ('rentabilidade_efetiva_mensal', 'std'),
                                            rentabilidade_patrimonial_mean = ('rentabilidade_patrimonial', 'mean'),
                                            rentabilidade_patrimonial_std = ('rentabilidade_patrimonial', 'std'),
                                            dividend_yield_mean = ('dividend_yield', 'mean'),
                                            dividend_yield_std = ('dividend_yield', 'std'),
                                            amortizacoes_de_cotas_no_mes_ref_mean = ('amortizacoes_de_cotas_no_mes_ref', 'mean'),
                                            amortizacoes_de_cotas_no_mes_ref_std = ('amortizacoes_de_cotas_no_mes_ref', 'std'),
                                            total_mantido_para_necessidade_de_liquidez_mean = ('total_mantido_para_necessidade_de_liquidez', 'mean'),
                                            total_mantido_para_necessidade_de_liquidez_std = ('total_mantido_para_necessidade_de_liquidez', 'std'),
                                            total_mantido_para_necessidade_de_liquidez_disponibilidade_mean = ('total_mantido_para_necessidade_de_liquidez_disponibilidade', 'mean'),
                                            total_mantido_para_necessidade_de_liquidez_disponibilidade_std = ('total_mantido_para_necessidade_de_liquidez_disponibilidade', 'std'),
                                            total_mantido_para_necessidade_de_liquidez_titulos_publicos_mean = ('total_mantido_para_necessidade_de_liquidez_titulos_publicos', 'mean'),
                                            total_mantido_para_necessidade_de_liquidez_titulos_publicos_std = ('total_mantido_para_necessidade_de_liquidez_titulos_publicos', 'std'),
                                            total_mantido_para_necessidade_de_liquidez_titulos_privados_mean = ('total_mantido_para_necessidade_de_liquidez_titulos_privados', 'mean'),
                                            total_mantido_para_necessidade_de_liquidez_titulos_privados_std = ('total_mantido_para_necessidade_de_liquidez_titulos_privados', 'std'),
                                            total_mantido_para_necessidade_de_liquidez_fundos_de_renda_fixa_mean = ('total_mantido_para_necessidade_de_liquidez_fundos_de_renda_fixa', 'mean'),
                                            total_mantido_para_necessidade_de_liquidez_fundos_de_renda_fixa_std = ('total_mantido_para_necessidade_de_liquidez_fundos_de_renda_fixa', 'std'),
                                            total_investido_mean = ('total_investido', 'mean'),
                                            total_investido_std = ('total_investido', 'std'),
                                            total_investido_direitos_reais_sobre_bens_mean = ('total_investido_direitos_reais_sobre_bens', 'mean'),
                                            total_investido_direitos_reais_sobre_bens_std = ('total_investido_direitos_reais_sobre_bens', 'std'),
                                            total_investido_direitos_reais_sobre_bens_terrenos_mean = ('total_investido_direitos_reais_sobre_bens_terrenos', 'mean'),
                                            total_investido_direitos_reais_sobre_bens_terrenos_std = ('total_investido_direitos_reais_sobre_bens_terrenos', 'std'),
                                            total_investido_direitos_reais_sobre_bens_imoveis_para_renda_acabados_mean = ('total_investido_direitos_reais_sobre_bens_imoveis_para_renda_acabados', 'mean'),
                                            total_investido_direitos_reais_sobre_bens_imoveis_para_renda_acabados_std = ('total_investido_direitos_reais_sobre_bens_imoveis_para_renda_acabados', 'std'),
                                            total_investido_direitos_reais_sobre_bens_imoveis_para_renda_em_construcao_mean = ('total_investido_direitos_reais_sobre_bens_imoveis_para_renda_em_construcao', 'mean'),
                                            total_investido_direitos_reais_sobre_bens_imoveis_para_renda_em_construcao_std = ('total_investido_direitos_reais_sobre_bens_imoveis_para_renda_em_construcao', 'std'),
                                            total_investido_direitos_reais_sobre_bens_imoveis_para_venda_acabados_mean = ('total_investido_direitos_reais_sobre_bens_imoveis_para_venda_acabados', 'mean'),
                                            total_investido_direitos_reais_sobre_bens_imoveis_para_venda_acabados_std = ('total_investido_direitos_reais_sobre_bens_imoveis_para_venda_acabados', 'std'),
                                            total_investido_direitos_reais_sobre_bens_imoveis_para_venda_em_construcao_mean = ('total_investido_direitos_reais_sobre_bens_imoveis_para_venda_em_construcao', 'mean'),
                                            total_investido_direitos_reais_sobre_bens_imoveis_para_venda_em_construcao_std = ('total_investido_direitos_reais_sobre_bens_imoveis_para_venda_em_construcao', 'std'),
                                            total_investido_direitos_reais_sobre_bens_outros_direitos_reais_mean = ('total_investido_direitos_reais_sobre_bens_outros_direitos_reais', 'mean'),
                                            total_investido_direitos_reais_sobre_bens_outros_direitos_reais_std = ('total_investido_direitos_reais_sobre_bens_outros_direitos_reais', 'std'),
                                            total_investido_acoes_mean = ('total_investido_acoes', 'mean'),
                                            total_investido_acoes_std = ('total_investido_acoes', 'std'),
                                            total_investido_debentures_mean = ('total_investido_debentures', 'mean'),
                                            total_investido_debentures_std = ('total_investido_debentures', 'std'),
                                            total_investido_subscricao_mean = ('total_investido_subscricao', 'mean'),
                                            total_investido_subscricao_std = ('total_investido_subscricao', 'std'),
                                            total_investido_depositos_de_valores_mobiliarios_mean = ('total_investido_depositos_de_valores_mobiliarios', 'mean'),
                                            total_investido_depositos_de_valores_mobiliarios_std = ('total_investido_depositos_de_valores_mobiliarios', 'std'),
                                            total_investido_cedulas_debentures_mean = ('total_investido_cedulas_debentures', 'mean'),
                                            total_investido_cedulas_debentures_std = ('total_investido_cedulas_debentures', 'std'),
                                            total_investido_fia_mean = ('total_investido_fia', 'mean'),
                                            total_investido_fia_std = ('total_investido_fia', 'std'),
                                            total_investido_fip_mean = ('total_investido_fip', 'mean'),
                                            total_investido_fip_std = ('total_investido_fip', 'std'),
                                            total_investido_fii_mean = ('total_investido_fii', 'mean'),
                                            total_investido_fii_std = ('total_investido_fii', 'std'),
                                            total_investido_fidc_mean = ('total_investido_fidc', 'mean'),
                                            total_investido_fidc_std = ('total_investido_fidc', 'std'),
                                            total_investido_outras_cotas_de_fundos_mean = ('total_investido_outras_cotas_de_fundos', 'mean'),
                                            total_investido_outras_cotas_de_fundos_std = ('total_investido_outras_cotas_de_fundos', 'std'),
                                            total_investido_notas_promissorias_mean = ('total_investido_notas_promissorias', 'mean'),
                                            total_investido_notas_promissorias_std = ('total_investido_notas_promissorias', 'std'),
                                            total_investido_acoes_de_sociedades_mean = ('total_investido_acoes_de_sociedades', 'mean'),
                                            total_investido_acoes_de_sociedades_std = ('total_investido_acoes_de_sociedades', 'std'),
                                            total_investido_cotas_de_sociedades_mean = ('total_investido_cotas_de_sociedades', 'mean'),
                                            total_investido_cotas_de_sociedades_std = ('total_investido_cotas_de_sociedades', 'std'),
                                            total_investido_cepac_mean = ('total_investido_cepac', 'mean'),
                                            total_investido_cepac_std = ('total_investido_cepac', 'std'),
                                            total_investido_cri_ou_cra_mean = ('total_investido_cri_ou_cra', 'mean'),
                                            total_investido_cri_ou_cra_std = ('total_investido_cri_ou_cra', 'std'),
                                            total_investido_letras_hipotecarias_mean = ('total_investido_letras_hipotecarias', 'mean'),
                                            total_investido_letras_hipotecarias_std = ('total_investido_letras_hipotecarias', 'std'),
                                            total_investido_lci_ou_lca_mean = ('total_investido_lci_ou_lca', 'mean'),
                                            total_investido_lci_ou_lca_std = ('total_investido_lci_ou_lca', 'std'),
                                            total_investido_lig_mean = ('total_investido_lig', 'mean'),
                                            total_investido_lig_std = ('total_investido_lig', 'std'),
                                            total_investido_outros_valores_mobiliarios_mean = ('total_investido_outros_valores_mobiliarios', 'mean'),
                                            total_investido_outros_valores_mobiliarios_std = ('total_investido_outros_valores_mobiliarios', 'std'),
                                            valores_a_receber_mean = ('valores_a_receber', 'mean'),
                                            valores_a_receber_std = ('valores_a_receber', 'std'),
                                            valores_a_receber_por_alugueis_mean = ('valores_a_receber_por_alugueis', 'mean'),
                                            valores_a_receber_por_alugueis_std = ('valores_a_receber_por_alugueis', 'std'),
                                            valores_a_receber_por_venda_de_imoveis_mean = ('valores_a_receber_por_venda_de_imoveis', 'mean'),
                                            valores_a_receber_por_venda_de_imoveis_std = ('valores_a_receber_por_venda_de_imoveis', 'std'),
                                            valores_a_receber_por_outros_mean = ('valores_a_receber_por_outros', 'mean'),
                                            valores_a_receber_por_outros_std = ('valores_a_receber_por_outros', 'std'),
                                            passivo_rendimentos_a_distribuir_mean = ('passivo_rendimentos_a_distribuir', 'mean'),
                                            passivo_rendimentos_a_distribuir_std = ('passivo_rendimentos_a_distribuir', 'std'),
                                            passivo_taxa_de_adm_mean = ('passivo_taxa_de_adm', 'mean'),
                                            passivo_taxa_de_adm_std = ('passivo_taxa_de_adm', 'std'),
                                            passivo_taxa_de_performance_mean = ('passivo_taxa_de_performance', 'mean'),
                                            passivo_taxa_de_performance_std = ('passivo_taxa_de_performance', 'std'),
                                            passivo_obrigacoes_por_aquisicao_de_imoveis_mean = ('passivo_obrigacoes_por_aquisicao_de_imoveis', 'mean'),
                                            passivo_obrigacoes_por_aquisicao_de_imoveis_std = ('passivo_obrigacoes_por_aquisicao_de_imoveis', 'std'),
                                            passivo_adiantamento_por_venda_de_imoveis_mean = ('passivo_adiantamento_por_venda_de_imoveis', 'mean'),
                                            passivo_adiantamento_por_venda_de_imoveis_std = ('passivo_adiantamento_por_venda_de_imoveis', 'std'),
                                            passivo_adiantamento_de_valores_de_alugueis_mean = ('passivo_adiantamento_de_valores_de_alugueis', 'mean'),
                                            passivo_adiantamento_de_valores_de_alugueis_std = ('passivo_adiantamento_de_valores_de_alugueis', 'std'),
                                            passivo_obrigacoes_por_securitizacao_de_recebiveis_mean = ('passivo_obrigacoes_por_securitizacao_de_recebiveis', 'mean'),
                                            passivo_obrigacoes_por_securitizacao_de_recebiveis_std = ('passivo_obrigacoes_por_securitizacao_de_recebiveis', 'std'),
                                            passivo_instrumentos_financeiros_derivativos_mean = ('passivo_instrumentos_financeiros_derivativos', 'mean'),
                                            passivo_instrumentos_financeiros_derivativos_std = ('passivo_instrumentos_financeiros_derivativos', 'std'),
                                            passivo_provisoes_para_contingencias_mean = ('passivo_provisoes_para_contingencias', 'mean'),
                                            passivo_provisoes_para_contingencias_std = ('passivo_provisoes_para_contingencias', 'std'),
                                            passivo_outros_valores_a_pagar_mean = ('passivo_outros_valores_a_pagar', 'mean'),
                                            passivo_outros_valores_a_pagar_std = ('passivo_outros_valores_a_pagar', 'std'),
                                            passivo_total_mean = ('passivo_total', 'mean'),
                                            passivo_total_std = ('passivo_total', 'std')
                                           )
    
    correlacao_dados = grp.corr()
    
    correlacao_dados = correlacao_dados.dropna(how="all")

    # Remover as colunas
    agrupado_sem_colinearidade = grp.drop(columns=[coluna for coluna in grp.columns if coluna not in correlacao_dados.columns])
    
    correlacao_dados.to_csv('../colineriade.csv')
    
    agrupado_sem_colinearidade.dropna()
    
    agrupado_sem_colinearidade.to_csv('../dataset.csv', index=True)
    
    agrupado_sem_colinearidade = agrupado_sem_colinearidade.drop('worth_it', axis=1)
    
    cov = agrupado_sem_colinearidade.corr()
    
    cov = cov.dropna(axis=0, how="all").dropna(axis=1, how="all")
    
    U, s, Vt = np.linalg.svd(cov, full_matrices=False)

    # Passo 2: Determinar a tolerância para considerar uma singularidade zero
    tol = 1e-10

    # Passo 3: Encontrar colunas linearmente dependentes
    rank = np.sum(s > tol)
    independent_columns = Vt[:rank].T

    # Passo 4: Remover colunas dependentes
    cov = cov.iloc[:, :rank]
    
    agrupado_sem_colinearidade = agrupado_sem_colinearidade.drop(columns=[coluna for coluna in agrupado_sem_colinearidade.columns if coluna not in cov.columns])
    
    cov = agrupado_sem_colinearidade.corr()
    
    covariancia_dados_array = cov.to_numpy()
    determinante_covariancia = np.linalg.det(covariancia_dados_array)
    
    print(determinante_covariancia)
    
            
if __name__ == "__main__": main()