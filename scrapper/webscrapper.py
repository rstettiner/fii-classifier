import codecs
import re
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

def get_data_from_link(file_name: str):
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    
    result = []
    
    with open(file_name, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',', skipinitialspace=True)
        for row in csv_reader:
            driver.get(row['url'])

            get_url = driver.current_url
            wait.until(EC.url_to_be(row['url']))

            if get_url == row['url']:
                soup = BeautifulSoup(driver.page_source, features="html.parser")
                nome_do_titulo = row['ticker']
                worth_it = row['worth_it']
                
                nome_do_fundo = soup.find('span', class_='titulo-dado', string = 'Nome do Fundo: ').parent.findNext('td').contents[0].text
                data_da_analise = soup.find('span', class_='titulo-dado', string = 'Competência: ').parent.findNext('td').contents[0].text
                
                numeroTotalDeCotistas = int(soup.find('b', string = 'Número de cotistas ').parent.findNext('td').contents[0].text.replace('.', ''))
                n_cotistas_pessoa_fisica = int(soup.find('td', string = re.compile('Pessoa física')).findNext('td').contents[0].text.replace('.', ''))
                n_cotistas_pessoa_juridica_nao_financeira = int(soup.find('td', string = re.compile('Pessoa jurídica não financeira')).findNext('td').contents[0].text.replace('.', ''))
                n_cotistas_banco_comercial = int(soup.find('td', string = re.compile('Banco comercial')).findNext('td').contents[0].text.replace('.', ''))
                n_cotistas_corretora_ou_distribuidora = int(soup.find('td', string = re.compile('Corretora ou distribuidora')).findNext('td').contents[0].text.replace('.', ''))
                n_cotistas_outras_pessoas_juridicas_financeiras = int(soup.find('td', string = re.compile('Outras pessoas jurídicas financeiras')).findNext('td').contents[0].text.replace('.', ''))
                n_cotistas_investidores_nao_residentes = int(soup.find('td', string = re.compile('Investidores não residentes')).findNext('td').contents[0].text.replace('.', ''))
                n_cotistas_entidade_aberta_de_previdencia = int(soup.find('td', string = re.compile('Entidade aberta de previdência complementar')).findNext('td').contents[0].text.replace('.', ''))
                n_cotistas_entidade_fechada_de_previdencia = int(soup.find('td', string = re.compile('Entidade fechada de previdência complementar')).findNext('td').contents[0].text.replace('.', ''))
                n_cotistas_regime_proprio_de_previdencia = int(soup.find('td', string = re.compile('Regime próprio de previdência dos servidores públicos')).findNext('td').contents[0].text.replace('.', ''))
                n_cotistas_sociedade_seguradora = int(soup.find('td', string = re.compile('Sociedade seguradora ou resseguradora')).findNext('td').contents[0].text.replace('.', ''))
                n_cotistas_sociedade_de_capitalizacao = int(soup.find('td', string = re.compile('Sociedade de capitalização e de arrendamento mercantil')).findNext('td').contents[0].text.replace('.', ''))
                n_cotistas_fiis = int(soup.find('td', string = re.compile('Fundos de investimento imobiliário')).findNext('td').contents[0].text.replace('.', ''))
                n_cotistas_outros_fundos_de_investimento = int(soup.find('td', string = re.compile('Outros fundos de investimento')).findNext('td').contents[0].text.replace('.', ''))
                n_cotistas_distribuidores_de_fundo = int(soup.find('td', string = re.compile('distribuição por conta e ordem')).findNext('td').contents[0].text.replace('.', ''))
                n_cotistas_nao_relacionados = int(soup.find('td', string = re.compile('Outros tipos de cotistas não relacionados')).findNext('td').contents[0].text.replace('.', ''))
                
                ativos = float(soup.find('b', string = 'Ativo – R$ ').parent.findNext('td').findChild('span').text.replace('.', '').replace(',', '.'))
                patrimonio_liquido = float(soup.find('b', string = 'Patrimônio Líquido – R$ ').parent.findNext('td').findChild('span').text.replace('.', '').replace(',', '.'))
                n_de_cotas_emitidas = float(soup.find('b', string = 'Número de Cotas Emitidas ').parent.findNext('td').findChild('span').text.replace('.', '').replace(',', '.'))
                valor_patrimonial_das_cotas = float(soup.find('b', string = 'Valor Patrimonial das Cotas – R$ ').parent.findNext('td').findChild('span').text.replace('.', '').replace(',', '.'))
                despesas_com_taxas_de_adm_em_relacao_ao_patrimonio = float(soup.find('b', string = 'Valor Patrimonial das Cotas – R$ ').parent.parent.findNext('tr').findChild('span').text.replace('%', '').replace(',', '.'))
                despesas_com_agente_custodiante_em_relacao_ao_patrimonio = float(soup.find('b', string = 'Despesas com o agente custodiante em relação ao patrimônio líquido do mês (%) ').parent.findNext('td').findChild('span').text.replace('%', '').replace(',', '.'))
                rentabilidade_efetiva_mensal = float(soup.find('b', string = 'Rentabilidade Efetiva Mensal (%) ').parent.findNext('td').findChild('span').text.replace('%', '').replace(',', '.'))
                rentabilidade_patrimonial = float(soup.find('td', string = re.compile('Rentabilidade Patrimonial do Mês de Referência')).findNext('td').findChild('span').text.replace('%', '').replace(',', '.'))
                dividend_yield = float(soup.find('td', string = re.compile('Dividend Yield do Mês de Referência')).findNext('td').findChild('span').text.replace('%', '').replace(',', '.'))
                amortizacoes_de_cotas_no_mes_ref = float(soup.find('b', string = re.compile('Amortizações de cotas do Mês de Referência')).parent.findNext('td').findChild('span').text.replace('%', '').replace(',', '.'))
                
                total_mantido_para_necessidade_de_liquidez = float(soup.find('b', string = re.compile('Total mantido para as Necessidades de Liquidez')).parent.findNext('td').findChild('span').text.replace('.', '').replace(',', '.'))
                total_mantido_para_necessidade_de_liquidez_disponibilidade = float(soup.find('td', string = re.compile('Disponibilidades')).findNext('td').findChild('span').text.replace('.', '').replace(',', '.'))
                total_mantido_para_necessidade_de_liquidez_titulos_publicos = float(soup.find('td', string = re.compile('Títulos Públicos')).findNext('td').findChild('span').text.replace('.', '').replace(',', '.'))
                total_mantido_para_necessidade_de_liquidez_titulos_privados = float(soup.find('td', string = re.compile('Títulos Privados')).findNext('td').findChild('span').text.replace('.', '').replace(',', '.'))
                total_mantido_para_necessidade_de_liquidez_fundos_de_renda_fixa = float(soup.find('td', string = re.compile('Fundos de Renda Fixa')).findNext('td').findChild('span').text.replace('.', '').replace(',', '.'))
                
                total_investido = float(soup.find('b', string = re.compile('Total investido')).parent.findNext('td').findChild('span').text.replace('.', '').replace(',', '.'))
                total_investido_direitos_reais_sobre_bens = float(soup.find('td', string = re.compile('Direitos reais sobre bens imóveis')).findNext('td').findChild('span').text.replace('.', '').replace(',', '.'))
                total_investido_direitos_reais_sobre_bens_terrenos = float(soup.find('td', string = re.compile('Terrenos')).findNext('td').findChild('span').text.replace('.', '').replace(',', '.'))
                total_investido_direitos_reais_sobre_bens_imoveis_para_renda_acabados = float(soup.find('td', string = re.compile('Imóveis para Renda Acabados')).findNext('td').findChild('span').text.replace('.', '').replace(',', '.'))
                total_investido_direitos_reais_sobre_bens_imoveis_para_renda_em_construcao = float(soup.find('td', string = re.compile('Imóveis para Renda em Construção')).findNext('td').findChild('span').text.replace('.', '').replace(',', '.'))
                total_investido_direitos_reais_sobre_bens_imoveis_para_venda_acabados = float(soup.find('td', string = re.compile('Imóveis para Venda Acabados')).findNext('td').findChild('span').text.replace('.', '').replace(',', '.'))
                total_investido_direitos_reais_sobre_bens_imoveis_para_venda_em_construcao = float(soup.find('td', string = re.compile('Imóveis para Venda em Construção')).findNext('td').findChild('span').text.replace('.', '').replace(',', '.'))
                total_investido_direitos_reais_sobre_bens_outros_direitos_reais = float(soup.find('td', string = re.compile('Outros direitos reais')).findNext('td').findChild('span').text.replace('.', '').replace(',', '.'))
                total_investido_acoes = float(soup.find('td', string = re.compile('Ações')).findNext('td').findChild('span').text.replace('.', '').replace(',', '.'))
                total_investido_debentures = float(soup.find('td', string = re.compile('Debêntures')).findNext('td').findChild('span').text.replace('.', '').replace(',', '.'))
                total_investido_subscricao = float(soup.find('td', string = re.compile('Bônus de Subscrição, seus cupons, direitos, recibos de subscrição e certificados de desdobramentos')).findNext('td').findChild('span').text.replace('.', '').replace(',', '.'))
                total_investido_depositos_de_valores_mobiliarios = float(soup.find('td', string = re.compile('Certificados de Depósitos de Valores Mobiliários')).findNext('td').findChild('span').text.replace('.', '').replace(',', '.'))
                total_investido_cedulas_debentures = float(soup.find('td', string = re.compile('Cédulas de Debêntures')).findNext('td').findChild('span').text.replace('.', '').replace(',', '.'))
                total_investido_fia = float(soup.find('td', string = re.compile('Fundo de Ações')).findNext('td').findChild('span').text.replace('.', '').replace(',', '.'))
                total_investido_fip = float(soup.find('td', string = re.compile('Fundo de Investimento em Participações')).findNext('td').findChild('span').text.replace('.', '').replace(',', '.'))
                total_investido_fii = float(soup.find('td', string = re.compile('Fundo de Investimento Imobiliário')).findNext('td').findChild('span').text.replace('.', '').replace(',', '.'))
                total_investido_fidc = float(soup.find('td', string = re.compile('Fundo de Investimento em Direitos Creditórios')).findNext('td').findChild('span').text.replace('.', '').replace(',', '.'))
                total_investido_outras_cotas_de_fundos = float(soup.find('td', string = re.compile('Outras cotas de Fundos de Investimento')).findNext('td').findChild('span').text.replace('.', '').replace(',', '.'))
                total_investido_notas_promissorias = float(soup.find('td', string = re.compile('Notas Promissórias')).findNext('td').findChild('span').text.replace('.', '').replace(',', '.'))
                total_investido_acoes_de_sociedades = float(soup.find('td', string = re.compile('Ações de Sociedades cujo único propósito se enquadra entre as atividades permitidas aos FII')).findNext('td').findChild('span').text.replace('.', '').replace(',', '.'))
                total_investido_cotas_de_sociedades = float(soup.find('td', string = re.compile('Cotas de Sociedades que se enquadre entre as atividades permitidas aos FII')).findNext('td').findChild('span').text.replace('.', '').replace(',', '.'))
                total_investido_cepac = float(soup.find('td', string = re.compile('CEPAC')).findNext('td').findChild('span').text.replace('.', '').replace(',', '.'))
                total_investido_cri_ou_cra = float(soup.find('td', string = re.compile('CRI')).findNext('td').findChild('span').text.replace('.', '').replace(',', '.'))
                total_investido_letras_hipotecarias = float(soup.find('td', string = re.compile('Letras Hipotecárias')).findNext('td').findChild('span').text.replace('.', '').replace(',', '.'))
                total_investido_lci_ou_lca = float(soup.find('td', string = re.compile('LCI')).findNext('td').findChild('span').text.replace('.', '').replace(',', '.'))
                total_investido_lig = float(soup.find('td', string = re.compile('LIG')).findNext('td').findChild('span').text.replace('.', '').replace(',', '.'))
                total_investido_outros_valores_mobiliarios = float(soup.find('td', string = re.compile('Outros Valores Mobiliários')).findNext('td').findChild('span').text.replace('.', '').replace(',', '.'))
                valores_a_receber = float(soup.find('b', string = re.compile('Valores a Receber')).parent.findNext('td').findChild('span').text.replace('.', '').replace(',', '.'))
                valores_a_receber_por_alugueis = float(soup.find('td', string = re.compile('Contas a Receber por Aluguéis')).findNext('td').findChild('span').text.replace('.', '').replace(',', '.'))
                valores_a_receber_por_venda_de_imoveis = float(soup.find('td', string = re.compile('Contas a Receber por Venda de Imóveis')).findNext('td').findChild('span').text.replace('.', '').replace(',', '.'))
                valores_a_receber_por_outros = float(soup.find('td', string = re.compile('Outros Valores a Receber')).findNext('td').findChild('span').text.replace('.', '').replace(',', '.'))
                
                passivo_rendimentos_a_distribuir = float(soup.find('b', string = re.compile('Rendimentos a distribuir')).parent.findNext('td').findChild('span').text.replace('.', '').replace(',', '.'))
                passivo_taxa_de_adm = float(soup.find('b', string = re.compile('Taxa de administração a pagar')).parent.findNext('td').findChild('span').text.replace('.', '').replace(',', '.'))
                passivo_taxa_de_performance = float(soup.find('b', string = re.compile('Taxa de performance a pagar')).parent.findNext('td').findChild('span').text.replace('.', '').replace(',', '.'))
                passivo_obrigacoes_por_aquisicao_de_imoveis = float(soup.find('b', string = re.compile('Obrigações por aquisição de imóveis')).parent.findNext('td').findChild('span').text.replace('.', '').replace(',', '.'))
                passivo_adiantamento_por_venda_de_imoveis = float(soup.find('b', string = re.compile('Adiantamento por venda de imóveis')).parent.findNext('td').findChild('span').text.replace('.', '').replace(',', '.'))
                passivo_adiantamento_de_valores_de_alugueis = float(soup.find('b', string = re.compile('Adiantamento de valores de aluguéis')).parent.findNext('td').findChild('span').text.replace('.', '').replace(',', '.'))
                passivo_obrigacoes_por_securitizacao_de_recebiveis = float(soup.find('b', string = re.compile('Obrigações por securitização de recebíveis')).parent.findNext('td').findChild('span').text.replace('.', '').replace(',', '.'))
                passivo_instrumentos_financeiros_derivativos = float(soup.find('b', string = re.compile('Instrumentos financeiros derivativos')).parent.findNext('td').findChild('span').text.replace('.', '').replace(',', '.'))
                passivo_provisoes_para_contingencias = float(soup.find('b', string = re.compile('Provisões para contingências')).parent.findNext('td').findChild('span').text.replace('.', '').replace(',', '.'))
                passivo_outros_valores_a_pagar = float(soup.find('b', string = re.compile('Outros valores a pagar')).parent.findNext('td').findChild('span').text.replace('.', '').replace(',', '.'))
                passivo_total = float(soup.find('b', string = re.compile('Total do passivo')).parent.findNext('td').findChild('span').text.replace('.', '').replace(',', '.'))
                
                rowParsed = {
                    'nome_do_titulo': nome_do_titulo,
                    'worth_it': worth_it,
                    'nome_do_fundo': nome_do_fundo,
                    'data_da_analise': data_da_analise,
                    'numeroTotalDeCotistas': numeroTotalDeCotistas,
                    'n_cotistas_pessoa_fisica': n_cotistas_pessoa_fisica,
                    'n_cotistas_pessoa_juridica_nao_financeira': n_cotistas_pessoa_juridica_nao_financeira,
                    'n_cotistas_banco_comercial': n_cotistas_banco_comercial,
                    'n_cotistas_corretora_ou_distribuidora': n_cotistas_corretora_ou_distribuidora,
                    'n_cotistas_outras_pessoas_juridicas_financeiras': n_cotistas_outras_pessoas_juridicas_financeiras,
                    'n_cotistas_investidores_nao_residentes': n_cotistas_investidores_nao_residentes,
                    'n_cotistas_entidade_aberta_de_previdencia': n_cotistas_entidade_aberta_de_previdencia,
                    'n_cotistas_entidade_fechada_de_previdencia': n_cotistas_entidade_fechada_de_previdencia,
                    'n_cotistas_regime_proprio_de_previdencia': n_cotistas_regime_proprio_de_previdencia,
                    'n_cotistas_sociedade_seguradora': n_cotistas_sociedade_seguradora,
                    'n_cotistas_sociedade_de_capitalizacao': n_cotistas_sociedade_de_capitalizacao,
                    'n_cotistas_fiis': n_cotistas_fiis,
                    'n_cotistas_outros_fundos_de_investimento': n_cotistas_outros_fundos_de_investimento,
                    'n_cotistas_distribuidores_de_fundo': n_cotistas_distribuidores_de_fundo,
                    'n_cotistas_nao_relacionados': n_cotistas_nao_relacionados,
                    'ativos': ativos,
                    'patrimonio_liquido': patrimonio_liquido,
                    'n_de_cotas_emitidas': n_de_cotas_emitidas,
                    'valor_patrimonial_das_cotas': valor_patrimonial_das_cotas,
                    'despesas_com_taxas_de_adm_em_relacao_ao_patrimonio': despesas_com_taxas_de_adm_em_relacao_ao_patrimonio,
                    'despesas_com_agente_custodiante_em_relacao_ao_patrimonio': despesas_com_agente_custodiante_em_relacao_ao_patrimonio,
                    'rentabilidade_efetiva_mensal': rentabilidade_efetiva_mensal,
                    'rentabilidade_patrimonial': rentabilidade_patrimonial,
                    'dividend_yield': dividend_yield,
                    'amortizacoes_de_cotas_no_mes_ref': amortizacoes_de_cotas_no_mes_ref,
                    'total_mantido_para_necessidade_de_liquidez': total_mantido_para_necessidade_de_liquidez,
                    'total_mantido_para_necessidade_de_liquidez_disponibilidade': total_mantido_para_necessidade_de_liquidez_disponibilidade,
                    'total_mantido_para_necessidade_de_liquidez_titulos_publicos': total_mantido_para_necessidade_de_liquidez_titulos_publicos,
                    'total_mantido_para_necessidade_de_liquidez_titulos_privados': total_mantido_para_necessidade_de_liquidez_titulos_privados,
                    'total_mantido_para_necessidade_de_liquidez_fundos_de_renda_fixa': total_mantido_para_necessidade_de_liquidez_fundos_de_renda_fixa,
                    'total_investido': total_investido,
                    'total_investido_direitos_reais_sobre_bens': total_investido_direitos_reais_sobre_bens,
                    'total_investido_direitos_reais_sobre_bens_terrenos': total_investido_direitos_reais_sobre_bens_terrenos,
                    'total_investido_direitos_reais_sobre_bens_imoveis_para_renda_acabados': total_investido_direitos_reais_sobre_bens_imoveis_para_renda_acabados,
                    'total_investido_direitos_reais_sobre_bens_imoveis_para_renda_em_construcao': total_investido_direitos_reais_sobre_bens_imoveis_para_renda_em_construcao,
                    'total_investido_direitos_reais_sobre_bens_imoveis_para_venda_acabados': total_investido_direitos_reais_sobre_bens_imoveis_para_venda_acabados,
                    'total_investido_direitos_reais_sobre_bens_imoveis_para_venda_em_construcao': total_investido_direitos_reais_sobre_bens_imoveis_para_venda_em_construcao,
                    'total_investido_direitos_reais_sobre_bens_outros_direitos_reais': total_investido_direitos_reais_sobre_bens_outros_direitos_reais,
                    'total_investido_acoes': total_investido_acoes,
                    'total_investido_debentures': total_investido_debentures,
                    'total_investido_subscricao': total_investido_subscricao,
                    'total_investido_depositos_de_valores_mobiliarios': total_investido_depositos_de_valores_mobiliarios,
                    'total_investido_cedulas_debentures': total_investido_cedulas_debentures,
                    'total_investido_fia': total_investido_fia,
                    'total_investido_fip': total_investido_fip,
                    'total_investido_fii': total_investido_fii,
                    'total_investido_fidc': total_investido_fidc,
                    'total_investido_outras_cotas_de_fundos': total_investido_outras_cotas_de_fundos,
                    'total_investido_notas_promissorias': total_investido_notas_promissorias,
                    'total_investido_acoes_de_sociedades': total_investido_acoes_de_sociedades,
                    'total_investido_cotas_de_sociedades': total_investido_cotas_de_sociedades,
                    'total_investido_cepac': total_investido_cepac,
                    'total_investido_cri_ou_cra': total_investido_cri_ou_cra,
                    'total_investido_letras_hipotecarias': total_investido_letras_hipotecarias,
                    'total_investido_lci_ou_lca': total_investido_lci_ou_lca,
                    'total_investido_lig': total_investido_lig,
                    'total_investido_outros_valores_mobiliarios': total_investido_outros_valores_mobiliarios,
                    'valores_a_receber': valores_a_receber,
                    'valores_a_receber_por_alugueis': valores_a_receber_por_alugueis,
                    'valores_a_receber_por_venda_de_imoveis': valores_a_receber_por_venda_de_imoveis,
                    'valores_a_receber_por_outros': valores_a_receber_por_outros,
                    'passivo_rendimentos_a_distribuir': passivo_rendimentos_a_distribuir,
                    'passivo_taxa_de_adm': passivo_taxa_de_adm,
                    'passivo_taxa_de_performance': passivo_taxa_de_performance,
                    'passivo_obrigacoes_por_aquisicao_de_imoveis': passivo_obrigacoes_por_aquisicao_de_imoveis,
                    'passivo_adiantamento_por_venda_de_imoveis': passivo_adiantamento_por_venda_de_imoveis,
                    'passivo_adiantamento_de_valores_de_alugueis': passivo_adiantamento_de_valores_de_alugueis,
                    'passivo_obrigacoes_por_securitizacao_de_recebiveis': passivo_obrigacoes_por_securitizacao_de_recebiveis,
                    'passivo_instrumentos_financeiros_derivativos': passivo_instrumentos_financeiros_derivativos,
                    'passivo_provisoes_para_contingencias': passivo_provisoes_para_contingencias,
                    'passivo_outros_valores_a_pagar': passivo_outros_valores_a_pagar,
                    'passivo_total': passivo_total
                }
                
                result.append(rowParsed)
                
    
    driver.quit()
            
    return result

def main():
    result = get_data_from_link('links.csv')
                
    with open('../data_filter/raw_dataset.csv', mode='w', encoding='utf-8') as dataset_file:
        dataset_writer = csv.DictWriter(dataset_file, fieldnames=result[0].keys(), delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator = '\n')
        
        dataset_writer.writeheader()
        
        for line in result:
            dataset_writer.writerow(line)
            
if __name__ == "__main__": main()