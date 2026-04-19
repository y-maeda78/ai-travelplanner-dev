# AI Travel Planner
AI（OpenAI API）を活用した、パーソナライズ旅行プラン生成アプリケーション。

## URL
https://ai-travelplanner-app-v1-fc07674f29c0.herokuapp.com/

## 概要
「旅行の計画を立てるのが大変」「どこに行けばいいか迷う」という悩みを解決するためのWebアプリです。
目的地、人数、期間、予算、そして個人のこだわり（「海鮮を食べたい」「歴史を巡りたい」など）を入力するだけで、AIが最適なスケジュールを提案します。

## 特徴
- **AIによるプラン生成**: OpenAI API (GPT-3.5) を使用し、具体的で実現可能な旅程を提案。
- **モバイル対応**: Bootstrap 5 を使用したレスポンシブデザイン。
- **印刷機能**: 生成されたプランをA4サイズで綺麗に印刷・保存できる機能を搭載。

## 使用技術 (Tech Stack)
### Backend
- Python 3.x
- Flask (Web Framework)
- Gunicorn (WSGI Server)

### Frontend
- HTML5 / CSS3
- Bootstrap 5
- Lucide (Icons)

### API / Infrastructure
- OpenAI API
- Heroku (Hosting)
- Git / GitHub
