from random import randint

def calc_Prob(dados, target):
    um_and_true = 0
    zero_and_true = 0
    num_dados = len(dados)
    for i in range(0, num_dados-1):
        if dados[i] == 1 and target[i] == 1:
            um_and_true += 1
        elif dados[i] == 0 and target[i] == 1:
            zero_and_true += 1
    return float(um_and_true)/num_dados, float(zero_and_true)/num_dados

def analisar(animais_teste, todas_as_probs):
    for animal_teste in animais_teste:
        probs_animal_teste = []
        i = 0
        for feature in animal_teste:
            if feature == 1:
                probs_animal_teste.append(todas_as_probs[i][0])
            else:
                probs_animal_teste.append(todas_as_probs[i][1])
            i += 1

        prob_final = probs_animal_teste[0]*probs_animal_teste[1]*probs_animal_teste[2]

        num_aleatorio = randint(0,1)
        if num_aleatorio > prob_final:
            print("Nao")
        else:
            print("Sim")

# Declarar alguns dados
animal_1 = [1, 1, 1]
animal_2 = [1, 1, 0]
animal_3 = [0, 0, 0]
animal_4 = [0, 0, 1]
animal_5 = [1, 0, 1]
animal_6 = [1, 1, 0]
animal_7 = [0, 1, 0]
animal_8 = [1, 0, 0]
animais = [animal_1, animal_2, animal_3, animal_4, animal_5, animal_6, animal_7, animal_8]
target = [1, 1, 0, 0, 1, 0, 1, 0]

#Separar as features
features_1 = []
features_2 = []
features_3 = []
for animal in animais:
    features_1.append(animal[0])
    features_2.append(animal[1])
    features_3.append(animal[2])

todas_as_features = [features_1, features_2, features_3]

#Separar as probabilidades
prob_atender_e_ser = 0
prob_nao_atender_e_ser = 0
todas_as_probs = []

for feature in todas_as_features:
    prob_atender_e_ser, prob_nao_atender_e_ser = calc_Prob(feature, target)
    probs_Feature = [prob_atender_e_ser, prob_nao_atender_e_ser]
    todas_as_probs.append(probs_Feature)

#Testar
animais_teste = [[1, 1, 1],[0, 0, 0],[1, 0, 0]]
analisar(animais_teste, todas_as_probs)

