## TouchGal 的非官方 MCP 服务器。

### 导入到 AstrBot：
```
{
    "command": "env",
    "args": [
        "touchgal_base_url=https://www.touchgal.top",
        "touchgal_cookies=your-touchgal-cookies-or-blank",
        "uvx",
        "touchgal-mcp-server"
    ]
}
```

### 导入到其它支持的客户端中：
```
{
    "mcpServers": {
        "touchgal-mcp-server": {
            "command": "uvx",
            "args": [
                "touchgal-mcp-server"
            ],
            "env" : {
                "touchgal_base_url":"https://www.touchgal.top",
                "touchgal_cookies":"your-touchgal-cookies-or-blank"
            }
        }
    }
}
```