import random
from typing import Tuple, Dict, List

import matplotlib.pyplot as plt
import numpy as np


class Individual:
    '''各個体のクラス
        args: 個体の持つ遺伝子情報(np.array)'''
    def __init__(self, genom_size):
        self.body_hair = np.random.randint(0, 2, genom_size).tolist()
        self.body_size = np.random.randint(0, 2, genom_size).tolist()
        self.herd_num = np.random.randint(0, 2, genom_size).tolist()
        self.eating = np.random.randint(0, 2, genom_size).tolist()
        self.body_color = np.random.randint(0, 2, genom_size).tolist()
        self.ferocity = np.random.randint(0, 2, genom_size).tolist()

        self.all_genoms = {
            "body_hair": self.body_hair,
            "body_size": self.body_size,
            "herd_num": self.herd_num,
            "eating": self.eating,
            "body_color": self.body_color,
            "ferocity": self.ferocity,
        }
        self.fitness = {
            "body_hair": 0,
            "body_size": 0,
            "herd_num": 0,
            "eating": 0,
            "body_color": 0,
            "ferocity": 0,
        }  # 個体の適応度(set_fitness関数で設定)
        self.set_fitness()
        self.set_all_genoms()

    def set_fitness(self):
        '''個体に対する目的関数(OneMax)の値をself.fitnessに代入'''
        self.fitness = {key: sum(value) for key, value in self.all_genoms.items()}

    def get_fitness(self):
        '''self.fitnessを出力'''
        return self.fitness

    def set_all_genoms(self):
        '''self.all_parameterの中身をself.body_hair以下に代入する'''
        self.body_hair = self.all_genoms["body_hair"]
        self.body_size = self.all_genoms["body_size"]
        self.herd_num = self.all_genoms["herd_num"]
        self.eating = self.all_genoms["eating"]
        self.body_color = self.all_genoms["body_color"]
        self.ferocity = self.all_genoms["ferocity"]

    def mutate(self):
        '''遺伝子の突然変異'''
        for i, (parameter, genom) in enumerate(self.all_genoms.items()):

            tmp = genom.copy()
            i = np.random.randint(0, len(genom) - 1)
            tmp[i] = float(not genom[i])
            self.all_genoms[parameter] = tmp

        self.set_all_genoms()
        self.set_fitness()

def random_temperature() -> float:
    """
        火星の気温20℃〜-140℃の範囲でrandomにfloat値を返す

        args
            times (int): 試行回数
        return
            float: ランダムに作成した 火星の気温
    """

    temperature = random.uniform(-140, 30)

    return temperature

def random_food_volume(food_volume):
    """
        餌の量

        args
            times (int): 試行回数
        return
            float: ランダムに作成した 火星の気温
    """
    
    food_volume += random.randint(-100, 100)
    if food_volume < 0:
        food_volume = 0
    
    return food_volume

def create_generation(POPURATIONS, GENOMS_SIZE):
    '''初期世代の作成
        return: 個体クラスのリスト'''
    generation = {}
    for i in range(POPURATIONS):
        individual = Individual(GENOMS_SIZE)
        generation[individual] = 0
    return generation

def select_tournament(
    generation_: List[Tuple[Individual, int]], TOUNAMENT_NUM
    ) -> List[Tuple[Individual, int]]:

    """
        選択の関数(トーナメント方式)。すべてのgenerationから3つ選び、強い(scoreが最も高い)genomを１つ選ぶ。これをgenerationのサイズだけ繰り返す

        args
            generation List[Tuple[Individual, int]]: Individual で作成したゲノム情報 [["body_hair"], ["body_size"], ["herd_num"]] , 評価score
        return
            List[Tuple[Individual, int]] : トーナメント戦で生き残ったゲノム1つ
    """

    selected_genoms = []

    for i in range(len(generation_)):

        # 最もスコアのよいgeneration を採用
        tournament = random.sample(generation_, TOUNAMENT_NUM)
        max_genom = max(tournament, key=lambda x: x[1])

        selected_genoms.append(max_genom)

    return selected_genoms

def cross_two_point_copy(child1, child2):
    '''二点交叉'''

    new_child1 = {}
    new_child2 = {}

    for parameter_genom_1, parameter_genom_2 in zip(child1[0].all_genoms.items(), child2[0].all_genoms.items()):

        size = len(parameter_genom_1[1])

        tmp_child_parameter1 = parameter_genom_1[0]
        tmp_child_parameter2 = parameter_genom_2[0]

        tmp_child_genom1 = parameter_genom_1[1].copy()
        tmp_child_genom2 = parameter_genom_2[1].copy()

        cxpoint1 = np.random.randint(1, size)
        cxpoint2 = np.random.randint(1, size - 1)

        if cxpoint2 >= cxpoint1:
            cxpoint2 += 1
        else:
            cxpoint1, cxpoint2 = cxpoint2, cxpoint1

        tmp_child_genom1[cxpoint1:cxpoint2], tmp_child_genom2[cxpoint1:cxpoint2] = tmp_child_genom2[cxpoint1:cxpoint2].copy(), tmp_child_genom1[cxpoint1:cxpoint2].copy()

        child1[0].all_genoms[tmp_child_parameter1] = tmp_child_genom1
        child2[0].all_genoms[tmp_child_parameter2] = tmp_child_genom2

        child1[0].set_all_genoms()
        child1[0].set_fitness()
        child2[0].set_all_genoms()
        child2[0].set_fitness()

    return child1, child2

def crossover(selected, POPURATIONS, CROSSOVER_PB):
    '''交叉の関数'''
    children = []
    if POPURATIONS % 2:
        selected.append(selected[0])
    for child1, child2 in zip(selected[::2], selected[1::2]):
        if np.random.rand() < CROSSOVER_PB:
            child1, child2 = cross_two_point_copy(child1, child2)
        children.append(child1)
        children.append(child2)
    children = children[:POPURATIONS]
    return children


def mutate(children, MUTATION_PB):

    tmp_children = []

    for child in children:
        individual, score = child[0], child[1]
        if np.random.rand() < MUTATION_PB:
            individual.mutate()

        tmp_children.append((individual, score))

    return tmp_children

def reset_generation_score(generation_):

    for i, (individual, score) in enumerate(generation_):
        generation_[i] = (individual, 0)

    return generation_

def scoring(generation_, temperature, food_volume):
    
    MAX_NUM = 4 # fitness の最大値
    THREASHOLD_TEMPRETURE = 10 # score の判定に用いる気温のしきい値
    THREASHOLD_FOOD_VOLUME = 3000 # score の判定に用いる食料のしきい値

    generation_ = reset_generation_score(generation_)

    # scoring を実施
    for i, (individual, score) in enumerate(generation_):

        # 各パラメーターの特性値を探索
        for parameter, fitness in individual.get_fitness().items():

            # 気温が高い 
            if temperature > THREASHOLD_TEMPRETURE:
                if parameter == "body_hair": # body_hair が小さいほうが有利、大きいほうが不利
                    score += MAX_NUM - fitness
                elif parameter == "body_size": # body_size が小さいほうが有利、大きいほうが不利
                    score += MAX_NUM - fitness
                elif parameter == "body_color": # body_color が暗い方が有利、明るいほうが不利
                    score += fitness
            
            # 気温が低い
            else:
                if parameter == "body_hair": # body_hair が大きいほうが有利、小さいほうが不利
                    score += fitness
                elif parameter == "body_size": # body_size が大きいほうが有利、小さいほうが不利
                    score += fitness
                elif parameter == "body_color": # body_color が明るい方が有利、暗いほうが不利
                    score += MAX_NUM - fitness

            # エサが多い
            if food_volume > THREASHOLD_FOOD_VOLUME:
                if parameter == "body_size": # body_size が大きいほうが有利、小さいほうが不利
                    score += fitness
                elif parameter == "herd_num": # herd_num が大きいほうが有利、小さいほうが不利
                    score += fitness
                elif parameter == "eating": # eating が大きい(肉食)ほうが有利、小さい(草食)ほうが不利
                    score += fitness

            # エサが少ない
            else:
                if parameter == "body_size": # body_size が小さいほうが有利、大きいほうが不利
                    score += MAX_NUM - fitness
                elif parameter == "herd_num": # herd_num が小さいほうが有利、大きいほうが不利
                    score += MAX_NUM - fitness
                elif parameter == "eating": # eating が小さい(草食)ほうが有利、大さい(肉食)ほうが不利
                    score += MAX_NUM - fitness


            # 強さ
            if parameter == "body_size": # body_size が大きいほうが有利、小さい方が不利
                score += fitness
            elif parameter == "herd_num":
                score += fitness
            elif parameter == "ferocity": # ferocity が大きい(凶暴)ほうが有利、小さい(おとなしい)ほうが不利
                score += fitness
            

        # score を更新
        generation_[i] = (individual, int(score))

    return generation_

def ga_solve(generation, NUM_GENERATION, POPURATIONS, TOUNAMENT_NUM, CROSSOVER_PB, MUTATION_PB):
    '''遺伝的アルゴリズムのソルバー
        return: 最終世代の最高適応値の個体、最低適応値の個体'''

    best = []
    worst = []

    temperature_transition = []
    food_volume = 500
    food_volume_transition = []

    parameter_transiton = {
        "body_size" : [],
        "body_hair" : [],
        "herd_num" : [],
        "eating" : [],
        "body_color" : [],
        "ferocity" : [],
    }

    # --- Generation loop
    print('Generation loop start.')

    # Dict[Individual, int] から List[Tuple(individual, int)]へ変換
    # Dict だと Key の重複ができないため
    generation_ = [(individual, score) for individual, score in generation.items()]

    for i in range(NUM_GENERATION):

        temperature = random_temperature()
        temperature_transition.append(temperature)
        food_volume = random_food_volume(food_volume)
        food_volume_transition.append(food_volume)

        # スコアリング
        generation_ = scoring(generation_, temperature, food_volume)


        # --- Step1. Print fitness in the generation
        best_individual_score = max(generation_, key=lambda x: x[1])

        best.append(best_individual_score[0].fitness)
        worst_individual_score = min(generation_, key=lambda x: x[1])

        worst.append(worst_individual_score[0].fitness)
        # print("Generation: " + str(i) \
        #         + ": Best fitness: " + str(best_individual_score[0].fitness) + "Best fitness score: " + str(best_individual_score[1]) \
        #         + ". Worst fitness: " + str(worst_individual_score[0].fitness) + "Worst fitness score: " + str(worst_individual_score[1]) 
        #         )

        # --- Step2. Selection (Roulette)
        selected_genoms = select_tournament(generation_, TOUNAMENT_NUM)

        # --- Step3. Crossover (two_point_copy)
        children = crossover(selected_genoms, POPURATIONS, CROSSOVER_PB)

        # --- Step4. Mutation
        generation_ = mutate(children, MUTATION_PB)

        for parameter, genom in best_individual_score[0].all_genoms.items():
            parameter_transiton[parameter].append(sum(genom))

        best_individual_score[0].set_all_genoms()
        best_individual_score[0].set_fitness()

    print("Generation loop ended. The best individual: ")
    print(best_individual_score[0].all_genoms)

    plt.figure(figsize=(20, 5))
    plt.title("temperature")
    plt.plot(temperature_transition)
    plt.ylabel("temperature Celsius")
    plt.xlabel("generation")
    plt.savefig("simlation_tempreture.png")

    plt.figure(figsize=(20, 5))
    plt.title("food volume")
    plt.plot(food_volume_transition)
    plt.ylim(0);
    plt.ylabel("food volume")
    plt.xlabel("generation")
    plt.savefig("simlation_food_volume.png")

    plt.figure(figsize=(20, 16))
    for i, (parameter, transition) in enumerate(parameter_transiton.items()):
        plt.subplot(6, 1, i+1)
        plt.title(parameter)
        plt.plot(transition, label=parameter)
        plt.legend()
        plt.ylim(0, 4)
    plt.tight_layout()
    plt.savefig("each_parameter_transition.png")

    return best, worst

def get_word_for_image_generate(word_dict, best, index):

    # アルゴリズムの結果に対応するwordを抽出
    word_list = [word_dict[parameter][int(fitness)] for parameter, fitness in best[index].items()]

    # 最終的な I/F 補足: スペース区切りの文字列 を渡す, 英語もありうる
    word = " ".join(word_list)
    return word