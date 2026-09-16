#!/usr/bin/env python3
"""
Random Joke Generator
Fetches jokes from multiple external APIs
"""

import requests
import json
import sys
from typing import Dict, List, Optional
from datetime import datetime
import time

# API 配置
APIS = {
    'jokapi': {
        'url': 'https://v2.jokeapi.dev/joke/Any',
        'params': {'format': 'json'},
        'parser': 'parse_jokapi'
    },
    'random_joke': {
        'url': 'https://random-joke-api.herokuapp.com/jokes/random',
        'params': {},
        'parser': 'parse_random_joke'
    },
    'official_joke': {
        'url': 'https://official-joke-api.appspot.com/random_joke',
        'params': {},
        'parser': 'parse_official_joke'
    },
    'uselessfacts': {
        'url': 'https://uselessfacts.jsondatabase.com/random',
        'params': {},
        'parser': 'parse_useless_fact'
    },
    'dadjoke': {
        'url': 'https://icanhazdadjoke.com/slack',
        'params': {},
        'parser': 'parse_dadjoke'
    }
}

class JokeGenerator:
    """随机笑话生成器"""
    
    def __init__(self, timeout: int = 5):
        self.timeout = timeout
        self.session = requests.Session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    
    def parse_jokapi(self, data: Dict) -> str:
        """解析 JokeAPI 响应"""
        if data.get('type') == 'twopart':
            return f"{data.get('setup')}\n{data.get('delivery')}"
        return data.get('joke', '')
    
    def parse_random_joke(self, data: List) -> str:
        """解析 Random Joke API 响应"""
        if isinstance(data, list) and len(data) > 0:
            return data[0].get('joke', '')
        return ''
    
    def parse_official_joke(self, data: Dict) -> str:
        """解析 Official Joke API 响应"""
        setup = data.get('setup', '')
        punchline = data.get('punchline', '')
        return f"{setup}\n{punchline}"
    
    def parse_useless_fact(self, data: Dict) -> str:
        """解析 Useless Facts API 响应"""
        return data.get('data', '')
    
    def parse_dadjoke(self, data: Dict) -> str:
        """解析 Dad Joke API 响应"""
        blocks = data.get('blocks', [])
        if blocks:
            elements = blocks[0].get('elements', [])
            if elements:
                text_elements = elements[0].get('elements', [])
                if text_elements:
                    return text_elements[0].get('text', '')
        return ''
    
    def fetch_from_api(self, api_name: str) -> Optional[str]:
        """从指定 API 获取笑话"""
        if api_name not in APIS:
            return None
        
        api_info = APIS[api_name]
        try:
            response = self.session.get(
                api_info['url'],
                params=api_info.get('params', {}),
                headers=self.headers,
                timeout=self.timeout
            )
            response.raise_for_status()
            
            data = response.json()
            parser_name = api_info['parser']
            parser = getattr(self, parser_name)
            joke = parser(data)
            
            return joke if joke else None
        except requests.RequestException as e:
            print(f"[Error] {api_name}: {str(e)}")
            return None
        except Exception as e:
            print(f"[Error] 解析 {api_name} 失败: {str(e)}")
            return None
    
    def get_joke(self, api_name: Optional[str] = None) -> Optional[str]:
        """获取单个笑话"""
        if api_name:
            return self.fetch_from_api(api_name)
        
        # 如果没有指定 API，尝试所有 API
        for name in APIS.keys():
            joke = self.fetch_from_api(name)
            if joke:
                return joke
        
        return None
    
    def get_multiple_jokes(self, count: int = 5, api_name: Optional[str] = None) -> List[Dict]:
        """获取多个笑话"""
        jokes = []
        for i in range(count):
            joke = self.get_joke(api_name)
            if joke:
                jokes.append({
                    'id': i + 1,
                    'joke': joke,
                    'timestamp': datetime.now().isoformat(),
                    'api': api_name or 'random'
                })
            time.sleep(0.5)  # 防止请求过于频繁
        
        return jokes
    
    def get_joke_category(self, category: str = 'Any') -> Optional[str]:
        """按分类获取笑话（仅 JokeAPI 支持）"""
        params = {'format': 'json', 'type': 'single'}
        try:
            response = self.session.get(
                f'https://v2.jokeapi.dev/joke/{category}',
                params=params,
                headers=self.headers,
                timeout=self.timeout
            )
            response.raise_for_status()
            data = response.json()
            return self.parse_jokapi(data)
        except Exception as e:
            print(f"[Error] 获取分类笑话失败: {str(e)}")
            return None
    
    def list_apis(self) -> List[str]:
        """列出所有可用的 API"""
        return list(APIS.keys())
    
    def save_jokes_to_file(self, jokes: List[Dict], filename: str = 'jokes.json'):
        """将笑话保存到文件"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(jokes, f, ensure_ascii=False, indent=2)
            print(f"✅ 已保存 {len(jokes)} 个笑话到 {filename}")
        except Exception as e:
            print(f"❌ 保存失败: {str(e)}")
    
    def load_jokes_from_file(self, filename: str = 'jokes.json') -> List[Dict]:
        """从文件加载笑话"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"文件不存在: {filename}")
            return []
        except Exception as e:
            print(f"加载失败: {str(e)}")
            return []


def print_joke(joke: Dict):
    """美化打印笑话"""
    print("\n" + "="*60)
    print(f"🎭 笑话 #{joke['id']}")
    print(f"📝 {joke['joke']}")
    print(f"🔗 来源: {joke.get('api', 'unknown')}")
    print("="*60 + "\n")


def main_menu():
    """主菜单"""
    generator = JokeGenerator()
    
    while True:
        print("\n" + "="*50)
        print("  🎭 随机笑话生成器")
        print("="*50)
        print("  1. 获取单个笑话")
        print("  2. 获取多个笑话")
        print("  3. 按分类获取笑话")
        print("  4. 从指定 API 获取")
        print("  5. 查看可用 API")
        print("  6. 保存笑话")
        print("  7. 加载笑话")
        print("  0. 退出")
        print("="*50)
        
        choice = input("请选择功能: ").strip()
        
        if choice == '1':
            print("⏳ 正在获取笑话...")
            joke = generator.get_joke()
            if joke:
                print_joke({'id': 1, 'joke': joke, 'api': 'random'})
            else:
                print("❌ 获取笑话失败，请检查网络连接")
        
        elif choice == '2':
            try:
                count = int(input("要获取多少个笑话? (默认5): ") or "5")
                print(f"⏳ 正在获取 {count} 个笑话...")
                jokes = generator.get_multiple_jokes(count)
                for joke in jokes:
                    print_joke(joke)
            except ValueError:
                print("❌ 输入的数字无效")
        
        elif choice == '3':
            print("\n可用分类: Any, Miscellaneous, Programming, Knock-Knock, General, Christmas")
            category = input("选择分类 (默认Any): ").strip() or "Any"
            print("⏳ 正在获取笑话...")
            joke = generator.get_joke_category(category)
            if joke:
                print_joke({'id': 1, 'joke': joke, 'api': f'jokapi ({category})'})
            else:
                print("❌ 获取笑话失败")
        
        elif choice == '4':
            apis = generator.list_apis()
            print(f"\n可用 API: {', '.join(apis)}")
            api_name = input("选择 API: ").strip().lower()
            if api_name in apis:
                print("⏳ 正在获取笑话...")
                joke = generator.get_joke(api_name)
                if joke:
                    print_joke({'id': 1, 'joke': joke, 'api': api_name})
                else:
                    print("❌ 从该 API 获取笑话失败")
            else:
                print("❌ API 不存在")
        
        elif choice == '5':
            apis = generator.list_apis()
            print("\n可用的 API 列表:")
            for api in apis:
                print(f"  • {api}: {APIS[api]['url']}")
        
        elif choice == '6':
            try:
                count = int(input("要保存多少个笑话? (默认10): ") or "10")
                print(f"⏳ 正在获取 {count} 个笑话...")
                jokes = generator.get_multiple_jokes(count)
                if jokes:
                    generator.save_jokes_to_file(jokes)
            except ValueError:
                print("❌ 输入的数字无效")
        
        elif choice == '7':
            filename = input("输入文件名 (默认jokes.json): ").strip() or "jokes.json"
            jokes = generator.load_jokes_from_file(filename)
            if jokes:
                for joke in jokes:
                    print_joke(joke)
            else:
                print("❌ 没有笑话")
        
        elif choice == '0':
            print("\n👋 再见！")
            break
        
        else:
            print("❌ 无效的选择")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        # CLI 模式
        generator = JokeGenerator()
        
        if sys.argv[1] == 'single':
            joke = generator.get_joke()
            if joke:
                print(joke)
            else:
                print("Error: Failed to fetch joke")
        
        elif sys.argv[1] == 'multiple':
            count = int(sys.argv[2]) if len(sys.argv) > 2 else 5
            jokes = generator.get_multiple_jokes(count)
            for j in jokes:
                print(f"\n{j['joke']}")
        
        elif sys.argv[1] == 'category':
            category = sys.argv[2] if len(sys.argv) > 2 else 'Any'
            joke = generator.get_joke_category(category)
            if joke:
                print(joke)
            else:
                print("Error: Failed to fetch joke")
        
        else:
            print("Usage: python joke_generator.py [single|multiple|category] [args]")
    else:
        # 交互模式
        main_menu()
