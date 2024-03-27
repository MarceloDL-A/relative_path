import os
import pandas as pd

def load(file, folder="../../datasets/banks", sep=";"):
    """
    Carrega um arquivo CSV localizado em um subdiretório específico e o retorna como um DataFrame do pandas.
    
    A função constrói o caminho absoluto para o arquivo CSV combinando o diretório atual do script, o nome do subdiretório e o nome do arquivo fornecido. O arquivo CSV é então lido e retornado como um DataFrame.
    
    Parameters
    ----------
    file : str
        Nome do arquivo CSV a ser carregado. A função assume que este arquivo está localizado dentro do subdiretório especificado pelo parâmetro `folder` no diretório atual do script.
    folder : str, optional
        Nome do subdiretório dentro do qual o arquivo CSV está localizado, relativo ao diretório atual do script. O valor padrão é "banks".
    sep : str, optional
        Delimitador utilizado no arquivo CSV. O valor padrão é ";".
        
    Returns
    -------
    pandas.DataFrame
        DataFrame contendo os dados lidos do arquivo CSV.
        
    Raises
    ------
    FileNotFoundError
        Se o arquivo especificado não for encontrado no caminho construído.
    pd.errors.EmptyDataError
        Se o arquivo CSV estiver vazio.
    pd.errors.ParserError
        Se ocorrer um erro durante a análise do arquivo CSV, por exemplo, se o delimitador especificado não for encontrado.
    
    Examples
    --------
    >>> df = load("example.csv")
    Carrega o arquivo 'example.csv' localizado no subdiretório 'banks' do diretório atual do script, utilizando ";" como delimitador.
    
    >>> df = load("data.csv", folder="data", sep=",")
    Carrega o arquivo 'data.csv' localizado no subdiretório 'data' do diretório atual do script, utilizando "," como delimitador.
    """
    current_dir = os.path.dirname(__file__)  # Diretório atual onde este script está localizado
    csv_file_path = os.path.join(current_dir, folder, file)  # Caminho absoluto para o arquivo CSV
    return pd.read_csv(csv_file_path, sep=sep)  # Leitura do arquivo CSV e retorno como DataFrame
