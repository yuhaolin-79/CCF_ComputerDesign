import os  #操作系统接口库，用于读取环境变量（如 .env 文件）
import requests   #发送 HTTP 请求的库（调用 OpenWeatherMap API）
from flask import Flask, render_template, request #创建 Web 应用实例,渲染 HTML 模板,处理用户输入（表单数据）
from dotenv import load_dotenv  #加载.env的

# ===== 核心修复：必须最先执行！ =====
load_dotenv()  # ← 自动加载项目根目录的 .env 文件
app = Flask(__name__)

# ===== 城市名智能映射（解决中文显示问题）=====
CITY_MAPPING = {
    # 中国主要城市（已扩展至20+城市）
    '北京': 'beijing,cn', '上海': 'shanghai,cn', '广州': 'guangzhou,cn',  #这里的cn是国家码，查询更准确
    '深圳': 'shenzhen,cn', '成都': 'chengdu,cn', '杭州': 'hangzhou,cn',
    '重庆': 'chongqing,cn', '武汉': 'wuhan,cn', '西安': 'xian,cn',
    '南京': 'nanjing,cn', '天津': 'tianjin,cn', '苏州': 'suzhou,cn',
    '郑州': 'zhengzhou,cn', '长沙': 'changsha,cn', '宁波': 'ningbo,cn',
    '青岛': 'qingdao,cn', '沈阳': 'shenyang,cn', '大连': 'dalian,cn',
    '厦门': 'xiamen,cn', '福州': 'fuzhou,cn', '昆明': 'kunming,cn',
    '哈尔滨': 'haerbin,cn', '济南': 'jinan,cn', '合肥': 'hefei,cn'
}

# 反向映射：API返回的英文名 → 显示中文
REVERSE_MAPPING = {v.split(',')[0].lower(): k for k, v in CITY_MAPPING.items()}
#因为API这玩意就会给你返回一个英文名，如beijing

def get_display_city(api_city_name):
    """智能转换：API返回的英文名 → 显示为中文（如 'beijing' → '北京'）"""
    city_lower = api_city_name.lower()
    return REVERSE_MAPPING.get(city_lower, api_city_name)  #找不到就拿拼音凑合一下


def get_weather_tips(condition):
    cond = condition.lower()
    if '雨' in cond or 'rain' in cond: return "🌧️ 出门记得带伞！"
    if '云' in cond or 'cloud' in cond: return "☁️ 多云天气，注意防晒。"
    if '晴' in cond or 'sun' in cond or 'clear' in cond: return "☀️ 晴天，适合户外活动。"
    if 'snow' in cond or '雪' in cond: return "❄️ 降雪天气，注意防滑保暖。"
    return "🌤️ 天气舒适～"


@app.route('/')
def index():
    # 调试信息：终端打印密钥状态（安全：只显示前4位）
    api_key = os.getenv('WEATHER_API_KEY', '')  #安全获取密钥
    if api_key:
        print(f"🔑 API密钥已加载（前4位）: {api_key[:4]}***")   #对了我也就打印四位
    else:
        print("❌ 警告：.env文件未加载！请检查文件名和位置")    #不对就算了
    return render_template('index.html')


@app.route('/weather', methods=['POST'])   #将URL路径 /weather 绑定到 get_weather 函数，限定只能通过 POST 方法访问（防止直接在浏览器输入URL）
def get_weather():
    raw_city = request.form.get('city', '').strip()   #从 index.html 的 <input name="city"> 获取值
    if not raw_city:
        return render_template('index.html', error="⚠️ 请输入城市名称")

    # 智能转换城市名（中文→拼音+国家码）
    city = CITY_MAPPING.get(raw_city, raw_city)  # 优先匹配中文，否则原样返回  CITY_MAPPING匹配
    api_key = os.getenv('WEATHER_API_KEY')    #从环境变量读取密钥（安全：密钥不写在代码中）

    if not api_key:
        return render_template('index.html',
                               error="🔑 未检测到API密钥！<br>请确认项目根目录有 .env 文件，内容：<br><code>WEATHER_API_KEY=你的密钥</code>",
                               show_help=True)

    try:   #构建API请求
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=zh_cn"
        print(f"🌐 正在查询: {url.split('q=')[1].split('&')[0]}")  # 终端打印实际查询名

        response = requests.get(url, timeout=8)
        if response.status_code == 200:
            data = response.json()    #成功分支
            # ===== 核心修复：显示时转回中文 =====
            display_city = get_display_city(data['name'])

            return render_template('index.html',
                                   city=display_city,  # ← 关键：使用中文显示
                                   temp=round(data['main']['temp'], 1),
                                   condition=data['weather'][0]['description'],
                                   icon=f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}@2x.png",
                                   tips=get_weather_tips(data['weather'][0]['description']))
        else:   #没成功就走这里（这里的输入是不合规的，比如不能输入省份浙江，要输入市级地区）
            err = response.json().get('message', '未知错误')
            # 智能提示：教用户正确输入
            if 'city not found' in err.lower():
                return render_template('index.html',
                                       error=f"📍 未找到「{raw_city}」<br>✅ 成功案例：<br>- 中国城市：北京 / beijing / Shanghai<br>- 国外城市：Tokyo / Paris / London<br>- 拼音更可靠：输入 beijing 代替 北京",
                                       show_help=True)
            return render_template('index.html', error=f"⚠️ API错误({response.status_code})：{err}", show_help=True)


    except requests.exceptions.Timeout:   #突发事件就走这里
        return render_template('index.html', error="⏱️ 网络超时！请检查WiFi", show_help=True)
    except Exception as e:
        return render_template('index.html', error=f"❌ 错误：{str(e)}", show_help=True)


if __name__ == '__main__':
    print("\n" + "🚀" * 25)
    print("✅ 天气系统启动成功！支持全球城市（中/英文/拼音）")
    print("💡 输入示例：北京 / beijing / Shanghai / Tokyo / Paris")
    print("🔍 终端会打印实际查询的城市名（方便调试）")
    print("🚀" * 25 + "\n")
    app.run(host='0.0.0.0', port=5000, debug=True)