import io
import os
import random
import sys

import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import torch
from diffusers import StableDiffusionPipeline

# from dotenv import load_dotenv
from huggingface_hub import notebook_login
from PIL import Image

# ローカル実行用 .envファイルから環境変数読み込み
# load_dotenv(".env")
# ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")

# Hugging SpaceのSecret Repoから環境変数読み取り
ACCESS_TOKEN = st.secrets["ACCESS_TOKEN"]

sys.path.append("./")
from simulation import *

# シード値の固定
SEED = 42
np.random.seed(seed=SEED)
random.seed(SEED)


def main():

    # 生息地を表すワード
    HABITAT_WORDS = " Alien from Mars"

    # パラメーター
    GENOMS_SIZE = 4  # 遺伝配列 0, 1 のどちらかを要素とした配列のサイズ
    TOUNAMENT_NUM = 10  # トーナメント方式で競わせる数
    CROSSOVER_PB = 0.8  # cross over(交差) する確率
    MUTATION_PB = 0.5  # mutation(突然変異)する確率

    # グローバル変数
    global best

    POPURATIONS = st.slider(
        label="人口数",
        min_value=3,
        max_value=3000,
        value=500,
    )

    NUM_GENERATION = st.slider(
        label="世代数",
        min_value=10,
        max_value=10000,
        value=1000,
    )

    # キーワード候補
    word_dict = {
        "body_size": ["Fingertip sized", "Palm sized", "", "Tall", "Giant"],
        "body_hair": ["Bald", "Smooth", "", "Furry", "Very Furry"],
        "herd_num": ["Lone", "Pair", "", "Herd of", "Swarm of"],
        "eating": ["No teeth", "Herbivorous", "Omnivorous", "Carnivorous", "Fang"],
        "body_color": [
            "Lightest skin",
            "Lighter skin",
            "",
            "Darker skin",
            "Darkest skin",
        ],
        "ferocity": ["Peaceful", "Gentle", "", "Ferocious", "Tyrannical"],
    }

    if st.button("実行", key="ga"):

        st.write("遺伝アルゴリズムの実行")

        progress_bar_ga = st.progress(0)

        # create first genetarion
        generation = create_generation(POPURATIONS, GENOMS_SIZE)

        progress_bar_ga.progress(50)

        # アルゴリズムの実行
        best, worst = ga_solve(
            generation,
            NUM_GENERATION,
            POPURATIONS,
            TOUNAMENT_NUM,
            CROSSOVER_PB,
            MUTATION_PB,
        )

        progress_bar_ga.progress(100)

        st.write("遺伝アルゴリズム処理の終了")

        st.write("画像生成の実行")

        progress_bar_image = st.progress(0)

        progress_bar_image.progress(0)

        pipe = StableDiffusionPipeline.from_pretrained(
            "CompVis/stable-diffusion-v1-4", use_auth_token=ACCESS_TOKEN
        )
        pipe.enable_attention_slicing()

        progress_bar_image.progress(7)

        device = "gpu" if torch.cuda.is_available() else "cpu"

        print("used device is", device)
        pipe.to(device)

        # NSFWフィルターの回避
        def null_safety(images, **kwargs):
            return images, False

        pipe.safety_checker = null_safety

        last_generation = NUM_GENERATION - 1

        plt.figure(figsize=(8, 8))
        plt.rcParams["font.size"] = 9

        words = (
            get_word_for_image_generate(word_dict, best, last_generation)
            + HABITAT_WORDS
        )

        image = pipe(words)["sample"][0]

        plt.title(f"{last_generation + 1}th\n{words}.")
        plt.xticks([])
        plt.yticks([])
        plt.imshow(image)

        progress_bar_image.progress(100)

        plt.tight_layout()
        buf = io.BytesIO()
        plt.savefig(buf, format="png")

        buf.seek(0)
        im = Image.open(buf)
        numpy_image = np.array(im)
        st.image(numpy_image)


if __name__ == "__main__":

    main()
