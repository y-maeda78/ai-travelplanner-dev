"""
概要    OpenAiのAPIを用いた旅行プランナー 
"""

import json
import requests
import os
# flaskモジュールからFlaskクラス、requestオブジェクト、render_template関数をインポートする
from flask import Flask, request, render_template
from dotenv import load_dotenv

# Flaskクラスのインスタンスを作成する
app = Flask(__name__)

# FlaskアプリのルートURL（"/"）にアクセスしたときの処理
@app.route("/", methods=["GET", "POST"])
def index():
	# OpenAIのAPIキー
	api_key = os.getenv("OPENAI_API_KEY")

	# OpenAI APIのエンドポイント
	url = "https://api.openai.com/v1/chat/completions"

	# HTTPヘッダーの内容
	headers = {
		"Content-Type": "application/json",
		"Authorization": f"Bearer {api_key}"
	}

	# HTTPリクエストのPOSTメソッドで送信するデータ
	plan = None
	if request.method == "POST":
		# フォームからデータを受け取る（Fletのinputに対応）
		loc = request.form.get("location")
		ppl = request.form.get("people")
		stay = request.form.get("stay_type")
		prc = request.form.get("price")
		obj = request.form.get("objective")

		# 元のコードのプロンプトをそのまま活用
		prompt = f"""You are an experienced travel planner. Please propose a detailed travel plan in Japanese based on the information below.
		場所: {loc}, 人数: {ppl}, 滞在日数: {stay}, 予算: {prc}, 旅行の目的: {obj}
		提案は、以下の要素を含んでください。
		- 全体的なコンセプトや魅力（どのような旅行になりそうか）
		- 日ごとの詳細なスケジュール（n日目、午前、ランチ、午後、ディナー、夜の過ごし方、など活動内容に分けて、おすすめのお店や場所、交通手段を提案）
		- おすすめの食事場所（お店の店名、小休憩のための道の駅など、施設名を明確にしてください）
		- おすすめの宿泊施設（宿泊の場合）
		- 各アクティビティや場所の簡単な説明（なぜそこがおすすめか）
		- 提案された予算内での実現可能性を考慮すること
		- ユーザーにとって分かりやすく、読みやすい形式で記述してください。
		- 丁寧な言葉遣いで記述してください。
		- **提案する施設や場所は、実際に存在し、訪問可能であることを前提としてください。存在が不確かな情報や、架空の場所は提案しないでください。**
		- **具体的な電話番号やウェブサイトのURL、料金の厳密な数値は含めないでください。（目安としての料金は可）**
		- 旅行プラン以外の余計な情報（例：はじめまして、ありがとうございます、太字装飾など）は含めないでください。
		- 各項目のタイトルには【】かっこをつけて目立たせてください。
		"""

		# OpenAI APIに送るデータ（辞書型）
		data = {
			"model": "gpt-3.5-turbo",
			"messages": [
				{"role": "system", "content": "You are a travel advisor."},
				{"role": "user", "content": prompt}
			]
		}

		try:
			# 修正：data=json.dumps(data) で辞書をJSON文字列に変換して送信します
			response = requests.post(url, headers=headers, data=json.dumps(data))
			response.raise_for_status()
			
			result = response.json()
			if "error" in result:
				plan = f"APIエラー: {result['error'].get('message', '原因不明')}"
			else:
				# 修正：結果を return するのではなく plan 変数に代入して画面に渡します
				plan = result.get("choices", [{}])[0].get("message", {}).get("content")
					
		except requests.exceptions.RequestException as e:
			plan = f"HTTPリクエストエラー: {str(e)}"

    # 修正：最後に必ず render_template を呼び出して画面を表示させます
	return render_template("index.html", plan=plan)

# このファイルが直接実行された場合、Flaskアプリとして起動する（デフォルトではポート番号5000）
if __name__ == "__main__":
    app.run(debug=True)
