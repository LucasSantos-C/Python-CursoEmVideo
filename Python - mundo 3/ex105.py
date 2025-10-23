def notas(*n, sit=False):
    maior= menor= 0
    '''
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    '''
    nt = dict()
    nt['total'] = len(n)
    nt['maior'] = max(n)
    nt['menor'] = min(n)
    nt['média'] = sum(n)/len(n)
    if sit:
        if nt['média'] > 7.00:
            nt['situação'] = "Boa"
        elif nt['média'] >= 5:
            nt['situação'] = "Média"
        else:
            nt['situação'] = "Ruim"
    return nt

resp = notas(10,9,8, sit=True)
print(resp)