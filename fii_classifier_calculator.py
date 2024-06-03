import pandas as pd
import numpy as np

def main():
    df = pd.read_csv("dataset.csv")
    
    df_only_numbers = df.drop('nome_do_titulo', axis=1)
    
    valued_group = df_only_numbers.query('worth_it == 1').drop('worth_it', axis=1)
    nonvalued_group = df_only_numbers.query('worth_it == 0').drop('worth_it', axis=1)
    
    valued_group_percentage = len(valued_group.index) / len(df_only_numbers.index)
    nonvalued_group_percentage = len(nonvalued_group.index) / len(df_only_numbers.index)
    
    valued_group_mean = valued_group.mean(axis = 0)
    nonvalued_group_mean = nonvalued_group.mean(axis = 0)
    
    valued_group_covariance = valued_group.cov()
    nonvalued_group_covariance = valued_group.cov()
    
    valued_group_mean_array = valued_group_mean.to_numpy()
    nonvalued_group_mean_array = nonvalued_group_mean.to_numpy()
    
    valued_group_covariance_array = valued_group_covariance.to_numpy()
    nonvalued_group_covariance_array = nonvalued_group_covariance.to_numpy()
    
    determinante = np.linalg.det((valued_group_percentage * valued_group_covariance_array) + (nonvalued_group_percentage * nonvalued_group_covariance_array))
    
    print(determinante)
    print((valued_group_percentage * valued_group_covariance_array) + (nonvalued_group_percentage * nonvalued_group_covariance_array))
    
    # determinante_fisher = (valued_group_mean_array - nonvalued_group_mean_array) * (np.linalg.inv((valued_group_percentage * valued_group_covariance_array) + (nonvalued_group_percentage * nonvalued_group_covariance_array)))
    
    # fronteira_fisher = 0.5 * (determinante_fisher * valued_group_mean_array + determinante_fisher * nonvalued_group_mean_array)
    
    # print(fronteira_fisher)
    
    # fudeu, determinante eh zero porque as linhas das matrizes tem dependencia linear entre elas, preciso rever o uso das colunas!!!
    
            
if __name__ == "__main__": main()