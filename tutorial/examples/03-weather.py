import urllib.request
import urllib.parse
import json
from datetime import datetime

API_KEY = "你的_API_KEY"  # 请替换为你在和风天气申请到的 API Key


def get_city_code(city_name):
    """调用和风天气 Geo API，根据城市名获取城市编码。"""
    url = f"https://geoapi.qweather.com/v2/city/lookup?location={urllib.parse.quote(city_name)}&key={API_KEY}"
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            data = json.loads(response.read().decode("utf-8"))
    except urllib.error.URLError:
        raise Exception("网络连接失败，请检查网络或代理设置。")
    except Exception as e:
        raise Exception(f"请求异常：{e}")

    if data.get("code") != "200":
        raise Exception(f"API 请求失败：{data.get('message', '未知错误')}")

    locations = data.get("location", [])
    if not locations:
        raise Exception(f"未找到城市“{city_name}”，请检查输入是否有错别字。")

    return locations[0]["id"]


def get_weather(city_code):
    """调用和风天气实时天气 API，获取当前天气信息。"""
    url = f"https://devapi.qweather.com/v7/weather/now?location={city_code}&key={API_KEY}"
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            data = json.loads(response.read().decode("utf-8"))
    except urllib.error.URLError:
        raise Exception("网络连接失败，请检查网络或代理设置。")
    except Exception as e:
        raise Exception(f"请求异常：{e}")

    if data.get("code") != "200":
        raise Exception(f"API 请求失败：{data.get('message', '未知错误')}")

    return data.get("now", {})


def main():
    city = input("请输入要查询的城市名称：").strip()
    if not city:
        print("城市名称不能为空，请重新运行脚本并输入有效城市名。")
        return

    try:
        print(f"正在查询 “{city}” 的天气信息...")
        city_code = get_city_code(city)
        weather = get_weather(city_code)

        # 提取关键字段
        temp = weather.get("temp", "未知")
        text = weather.get("text", "未知")
        wind_dir = weather.get("windDir", "未知")
        wind_scale = weather.get("windScale", "未知")
        humidity = weather.get("humidity", "未知")
        obs_time = weather.get("obsTime", "未知")

        # 格式化输出内容
        output = (
            f"城市：{city}\n"
            f"温度：{temp}°C\n"
            f"天气状况：{text}\n"
            f"风向风力：{wind_dir} {wind_scale}级\n"
            f"相对湿度：{humidity}%\n"
            f"更新时间：{obs_time}\n"
        )

        print("\n========== 天气信息 ==========")
        print(output)
        print("==============================")

        # 保存到文件
        filename = f"{city}-{datetime.now().strftime('%Y-%m-%d')}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(output)
        print(f"结果已保存到文件：{filename}")

    except Exception as e:
        print(f"\n出错了：{e}")


if __name__ == "__main__":
    main()
