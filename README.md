---
title: Alien on Mars
emoji: 👽
colorFrom: pink
colorTo: blue
sdk: streamlit
sdk_version: 1.2.0
app_file: app.py
pinned: false
---

## Space App Toyohashi in Japan / 豊橋

### [Team X Alien (チーム星人)](https://2022.spaceappschallenge.org/challenges/2022-challenges/space-biology-superhero/teams/team-x-alien/project)

- Mr. Takeo (竹尾さん)
- Mr. Matsubara (松原さん)
- Me, Shimizu (清水(記))

### Choice Theme / 選択したテーマ

- [BUILD A SPACE BIOLOGY SUPERHERO](https://2022.spaceappschallenge.org/challenges/2022-challenges/space-biology-superhero/details)

### Explanation / 説明書き

- 簡単な火星の環境をシミュレートした遺伝的アルゴリズムにより導き出した究極生命体の特徴（=画像生成に与えるキーワード)を画像生成プログラムに与えて未来に生き残る究極生命体の画像を生成する。
- The image generation program is given the characteristics of the ultimate life form (= keywords for image generation) derived by a genetic algorithm that simulates a simple Martian environment to generate images of the ultimate life form that will survive in the future.

- [Slide (Sorry, Only Japanese) / スライド(日本語のみ)](https://docs.google.com/presentation/d/1Umq53JqME-GUJN6TgCDA7Fu1CcQhMJTG/edit#slide=id.g15d379b926a_3_0)

- [Movie in YouTube / 紹介動画 YouTube](https://www.youtube.com/watch?v=CmSESCkDMz4)

### Output Images by Image Generation / 画像生成により出力した画像

##### left: first Generation! Very Furry Tall Herd of No teeth Lighter skin Ferocious alien from Mars

##### center: 500th Generation! Pair Carnivorous Gentle alien from Mars

##### right: 1000th Generation! Pair Herbivorous Ferocious alien from Mars

<div align="center">
<img src="./sample_output_images/first_generation.png" alt="エビフライトライアングル" title="サンプル"  style="width:240px;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img src="./sample_output_images/500th_generation.png" alt="エビフライトライアングル" title="サンプル"  style="width:240px;"/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img src="./sample_output_images/1000th_generation.png" alt="エビフライトライアングル" title="サンプル"  style="width:240px;"/>
</div>

### How to Execute / 実行方法

- Verify execution with M1 Mac, Python 3.7.13

- On Colab

  - Open [StableDiffusionSample.ipynb on Colab](https://colab.research.google.com/drive/1Uaqmq3ibMmEwepnn4OWHf2TVboUVa14O?usp=sharing)
  - Upload simulation.py to the current directory of Colab

- On Local
  - Install requirements.txt library in a virtual environment, etc.

### Command Example (Mac)

```
# Create a virtual environment
python -m venv .venv

# Activate your virtual environment.
source .venv/bin/activate

# Upgrade pip
python -m pip install --upgrade pip

# Install library
pip install -r requirements.txt
```

- Launch notebook StableDiffusionByCpu.ipynb.

- Common
  - Create a [Hugging Face](https://huggingface.co/) account.
  - Create an access token in [Hugging Face Setting](https://huggingface.co/settings/tokens).
    ![スクリーンショット 2022-10-05 21 30 00](https://user-images.githubusercontent.com/45703844/194060690-574e4ee2-be14-48f9-aa76-887ef32e737c.png)
  - Allow the use of the model you want to use (e.g. CompVis/stable-diffusion-v1-4), referring to the explanation on the official site.
  - Run a Colab or Local notebook, enter the Hugging Face token into the notebook, login and run the notebook.
    ![スクリーンショット 2022-10-05 21 33 06](https://user-images.githubusercontent.com/45703844/194061128-92b76dc0-cf2a-48c7-8930-8b3b3ab60405.png)

---

- M1 Mac, Python 3.7.13 で実行を確認

- グーグルコラボ

  - [StableDiffusionSample.ipynb on Colab](https://colab.research.google.com/drive/1Uaqmq3ibMmEwepnn4OWHf2TVboUVa14O?usp=sharing)を開く
  - Colab のカレントディレクトリに simulation.py をアップロードする

- ローカル環境
  - 仮想環境などに requirements.txt のライブラリをインストールする

### コマンド例(Mac)

```
# 仮想環境の作成
python -m venv .venv

# 仮想環境のアクティベート
source .venv/bin/activate

# pip のアップグレード
python -m pip install --upgrade pip

# ライブラリのインストール
pip install -r requirements.txt
```

- stable_diffusion_cpu.ipynb を立ち上げる

- 共通
  - [Hugging Face](https://huggingface.co/)のアカウントを作成する
  - [Hugging Face の Setting](https://huggingface.co/settings/tokens)でアクセストークンを作成する
    ![スクリーンショット 2022-10-05 21 30 00](https://user-images.githubusercontent.com/45703844/194060690-574e4ee2-be14-48f9-aa76-887ef32e737c.png)
  - [公式サイトの解説](https://huggingface.co/docs/hub/security-tokens)を参考に、使用するモデル(例: CompVis/stable-diffusion-v1-4)の使用を許可する
  - Colab または Local のノートブックを実行し、Hugging Face のトークンをノートブックに入力しログインしてノートブックを実行する。
    ![スクリーンショット 2022-10-05 21 33 06](https://user-images.githubusercontent.com/45703844/194061128-92b76dc0-cf2a-48c7-8930-8b3b3ab60405.png)

### File Organization / ファイル構成

- stable_diffusion_cpu.ipynb
  - An executable file that performs image generation locally.
  - ローカルで画像生成を行う実行ファイル。
- simulation.py
  - File with genetic algorithm simulations, required for both Colab and local.
  - 遺伝的アルゴリズムによるシミュレーションを行っているファイル。Colab、ローカルいずれの場合も必要。
- sample_output_images
  - Folder containing the Output image described above.
  - 上述の Output 画像が入ったフォルダ

### Reference site / 参考サイト

- [【python】遺伝的アルゴリズム(Genetic Algorithm)を実装してみる](https://mori-memo.hateblo.jp/entry/2022/06/16/232644)
- [CompVis/stable-diffusion の環境を Apple Silicon で構築する](https://zenn.dev/laiso/articles/7af434269ffa1b)
