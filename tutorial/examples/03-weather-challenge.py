import urllib.request
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


def get_weather_3d(city_code):
    """调用和风天气 3 日预报 API，获取未来 3 天天气信息。"""
    url = f"https://devapi.qweather.com/v7/weather/3d?location={city_code}&key={API_KEY}"
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            data = json.loads(response.read().decode("utf-8"))
    except urllib.error.URLError:
        raise Exception("网络连接失败，请检查网络或代理设置。")
    except Exception as e:
        raise Exception(f"请求异常：{e}")

    if data.get("code") != "200":
        raise Exception(f"API 请求失败：{data.get('message', '未知错误')}")

    return data.get("daily", [])


def main():
    city = input("请输入要查询的城市名称：").strip()
    if not city:
        print("城市名称不能为空，请重新运行脚本并输入有效城市名。")
        return

    try:
        print(f"正在查询 “{city}” 的未来 3 天天气预报...")
        city_code = get_city_code(city)
        daily_list = get_weather_3d(city_code)

        if not daily_list:
            print("未能获取到预报数据，请稍后再试。")
            return

        lines = [f"城市：{city}\n", f"预报时间：{datetime.now().strftime('%Y-%m-%d')}\n", "=" * 30 + "\n"]

        for day in daily_list:
            date = day.get("fxDate", "未知")
            temp_max = day.get("tempMax", "未知")
            temp_min = day.get("tempMin", "未知")
            text_day = day.get("textDay", "未知")
            text_night = day.get("textNight", "未知")
            wind_dir = day.get("windDirDay", "未知")
            wind_scale = day.get("windScaleDay", "未知")

            lines.append(
                f"日期：{date}\n"
                f"最高温：{temp_max}°C / 最低温：{temp_min}°C\n"
                f"白天天气：{text_day}\n"
                f"夜间天气：{text_night}\n"
                f"风向风力：{wind_dir} {wind_scale}级\n"
                f"-" * 30 + "\n"
            )

        output = "".join(lines)

        print("\n========== 3 日天气预报 ==========")
        print(output)
        print("==================================")

        # 保存到文件
        filename = f"{city}-{datetime.now().strftime('%Y-%m-%d')}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(output)
        print(f"结果已保存到文件：{filename}")

    except Exception as e:
        print(f"\n出错了：{e}")


if __name__ == "__main__":
    main()
