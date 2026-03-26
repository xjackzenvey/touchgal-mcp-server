from fastmcp import FastMCP
from typing import Annotated
import os

from .backends import TouchgalSession

mcp = FastMCP(name="TouchGal-MCP-Server", instructions='该工具可以搜索，查看TouchGal上的Galgame信息')
touchgalSession = TouchgalSession(
    os.getenv('touchgal_base_url', 'https://www.touchgal.top'),
    os.getenv('touchgal_cookies', '')
)


@mcp.tool(
    name='search_games',
    description='使用（部分）关键字搜索galgame。返回检索到的所有游戏的id和相关信息。',
)
def touchgal_search_games(keyword: Annotated[str, '游戏关键字']) -> list:
    return touchgalSession.do_search(keyword=keyword)

