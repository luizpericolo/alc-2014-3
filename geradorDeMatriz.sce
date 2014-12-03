// Algoritmo: Gerador de Matriz
// Entrada: Pasta de arquivo "training_set"
// Saída: Matriz R 943x1682

// A matriz do artigo é montada no seguinte esquema:
// Cada coluna equivale a um filme
// Cada linha equivale a um usuário
// Logo a matriz R contém 1682 colunas (filmes) e 943 linhas (usuários)

// Cada arquivo da pasta "training_set" é relativo a um filme
// O que faço é gerar um vetor coluna para cada arquivo da pasta
// gerando a matriz R final

// Foi criado também um vetor coluna chamado USUARIO que linka o 
// numero do usuário com o número da linha que ele ocupará na matriz, 
// por exemplo: USUARIO = [1488844 ; 822109 ; 885013];
// Significa que o Usuario 1488844 que corresponde ao índice 1 da matriz usuário
// corresponderá à primeira linha da matriz, sempre.

clear; 

// Função que transforma o contador atual no nome correto do arquivo
function [nome] = parseNomeArquivo(contador)
    numero = string(contador);
    nome = "mv_" + '000000' + numero;
    if contador > 9 then
        nome = "mv_" + "00000" + numero;
    end
    if contador > 99 then
        nome = "mv_" + "0000" + numero;
    end
    if contador > 999 then
        nome = "mv_" + "000" + numero;
    end
    if contador > 9999 then
        nome = "mv_" + "00" + numero;
    end
    if contador > 99999 then
        nome = "mv_" + "0" + numero;
    end
    if contador > 999999 then
        nome = "mv_" + numero;
    end
    return nome;
endfunction

USUARIO = [];
R = [];
TEMP = "C:\FILMES\"; // Diretorio onde deixei os arquivos

//for arquivo = 1:1682
for arquivo_contador = 1:1
    // Abre o arquivo correspondente
    nomeArquivo = parseNomeArquivo(arquivo_contador);
    
    // Os dados estão separados por coluna no formato:
    // id_usuario ; avaliação ; data
    M = csvRead(TEMP + nomeArquivo + ".cvs", ascii(44), []);
        
end


