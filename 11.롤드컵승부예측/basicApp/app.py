# 플라스크   -------------------------------------------
from flask import Flask, Blueprint, render_template
from flask import redirect, url_for, request
import os
from pydoc import html

# 데이터 가져오기 및 기능 구현 -----------------------------
from simulate import df, simulate_one, simulate_total
from tqdm import tqdm
from collections import Counter





##############################################################################
#####  플라스크 연결
##############################################################################
template_dir = os.path.join(os.path.dirname(__file__),'templates')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict.html')
def predict():
    return render_template('predict.html')


@app.route('/probal.html')
def probal():
    _name = request.args.get("name")
    
##########################################
    # 우승 확률
    lst1 = []
    for _ in tqdm(range(1000)):
        lst1.append(simulate_total(df)[0])
    value_counts = Counter(lst1)
    prob_ = str(round(value_counts[_name]/1000,2) * 100) + '%' if _name in value_counts.keys() else '0%'

    # 이길 확률
    lst2 = []
    for i in df[~df.Name.isin([_name])].Name:
        lst2.append(simulate_one(_name,i))
    lst2 = [' '.join(map(str, lst2[i])) for i in range(len(lst2))]

    # 예상 우승팀
    champion_ = max(value_counts, key=value_counts.get)
    
    # 중꺾마
    miracle_ = [item[0] for item in value_counts.most_common()[-3:]]

##########################################

    return render_template('probal.html',button_name=_name, win_team=lst2, prob_team =prob_, champion=champion_, miracle = miracle_)


@app.route('/probal/<button_name>')
def probal_with_button(button_name):
    return render_template('probal.html', button_name=button_name)



@app.route('/play.html')
def play():
    winTeam, teamList = simulate_total(df)
    return render_template('play.html', team_list=teamList, win = winTeam)


if __name__ == '__main__':
    app.run()

