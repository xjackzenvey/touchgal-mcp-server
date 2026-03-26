import requests
import json


class TouchgalSession:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    


    def __init__(self, base_url: str, cookies: str):
        self.session = requests.Session()
        self.base_url = base_url
        self.search_api = base_url + '/api/search'
        self._setup_session(cookies)


    def _setup_session(self, cookies: str):
        '''设置请求头信息'''
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0',
            'Referer': 'https://www.touchgal.top/search',
            'Cookie': cookies
        })

    def _build_search_params(self, keyword: str, limit: int = 12, page: int = 1, **kwargs) -> dict:
        return {
            "queryString": json.dumps(
                [{"type": "keyword", "name": keyword}], ensure_ascii=False
            ),
            "limit": limit,
            "searchOption": {
                "searchInIntroduction": False,
                "searchInAlias": True,
                "searchInTag": False,
            },
            "page": page,
            "selectedType": "all",
            "selectedLanguage": kwargs.get('selected_language', 'all'),
            "selectedPlatform": kwargs.get('selectedPlatform', 'all'),
            "sortField": "resource_update_time",
            "sortOrder": kwargs.get('sortOrder', 'desc'),
            "selectedYears": ["all"],
            "selectedMonths": ["all"],
            
        }


    def do_search(self, keyword: str, limit: int = 12, page: int = 1, **kwargs):
        '''搜索游戏'''
        assert limit < 30, "获取项目的数量应在30以下"
        assert page > 0, "页数必须是正整数"

        search_params = self._build_search_params(keyword=keyword, limit=limit, page=page, **kwargs)
        response  = self.session.post(
            url=self.search_api,
            data=json.dumps(search_params, ensure_ascii=False),
            headers={'Content-Type': 'text/plain;charset=UTF-8'}
        )

        response.raise_for_status()

        datas = json.loads(response.content.decode()).get('galgames', [])
        important_datas = []

        ## 筛选出我们需要的信息
        for item in datas:
            important_datas.append({
                'unique_id': item['unique_id'],
                'name': item['name'],
                'view': item['view'],
                'download': item['download'],
                'language': item['language'],
                'platform': item['platform'],
                'tags': item['tags'],
                'rating': item['averageRating'],
                'banner': item['banner']
            })

        return important_datas


if __name__ == '__main__':
    base_url = 'https://www.touchgal.top'
    cookies = ''
    session = TouchgalSession(base_url=base_url, cookies=cookies)
    content = session.do_search(keyword='千')

    with open('debug.json', 'w', encoding='utf-8') as f:
        json.dump(content, f, ensure_ascii=False, indent=4)