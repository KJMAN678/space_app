## Space App Toyohashi in Japan / 豊橋

### [Team X Alien (チーム星人)](https://2022.spaceappschallenge.org/challenges/2022-challenges/space-biology-superhero/teams/team-x-alien/project)

- Mr. Takeo (竹尾さん)
- Mr. Matsubara (松原さん)
- Me, Shimizu (清水(記))

### Choice Theme / 選択したテーマ

- [BUILD A SPACE BIOLOGY SUPERHERO](https://2022.spaceappschallenge.org/challenges/2022-challenges/space-biology-superhero/details)

### Discription / 注意書き

- 簡単な火星の環境をシミュレートした遺伝的アルゴリズムにより導き出した究極生命体の特徴（=画像生成に与えるキーワード)を画像生成プログラムに与えて未来に生き残る究極生命体の画像を生成する。
- The image generation program is given the characteristics of the ultimate life form (= keywords for image generation) derived by a genetic algorithm that simulates a simple Martian environment to generate images of the ultimate life form that will survive in the future.

- [Slide (Sorry, Only Japanese) / スライド(日本語のみ)](https://docs.google.com/presentation/d/1Umq53JqME-GUJN6TgCDA7Fu1CcQhMJTG/edit#slide=id.g15d379b926a_3_0)

### Output Images by Image Generation / 画像生成により出力した画像

##### left: first Generation! Very Furry Tall Herd of No teeth Lighter skin Ferocious alien from Mars  
##### center: 500th Generation! Pair Carnivorous  Gentle alien from Mars  
##### right: 1000th Generation! Pair Herbivorous  Ferocious alien from Mars   

<div align="center">
<img src="./images/first_generation.png" alt="エビフライトライアングル" title="サンプル"  style="width:240px;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img src="./images/500th_generation.png" alt="エビフライトライアングル" title="サンプル"  style="width:240px;"/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img src="./images/1000th_generation.png" alt="エビフライトライアングル" title="サンプル"  style="width:240px;"/>
</div>

### File Organization / ファイル構成

- StableDiffusionSample.ipynb
  - An executable file that performs image generation. Sory You Need to Login Hugging Face Infomation!
  - 画像生成を行う実行ファイル。Hugging Face へのログイン情報が必要。
- simulation.py 
  - A file with a genetic algorithm simulation running in StableDiffusionSample.ipynb
  - StableDiffusionSample.ipynb で実行する、遺伝的アルゴリズムによるシミュレーションを行っているファイル。
- images
  - Folder containing the Output image described above.
  - 上述のOutput画像が入ったフォルダ

### Reference material / 参考資料
- [StableDiffusionSample.ipynb on Colab](https://colab.research.google.com/drive/1Uaqmq3ibMmEwepnn4OWHf2TVboUVa14O?usp=sharing))