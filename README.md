# 🏠 服务导航页

个人服务器聚合导航页面，支持多服务管理、搜索、明暗主题。

## ✨ 功能

- **🔐 密码保护** — 首次访问需输入密码，验证后 30 天免密
- **🌗 明暗主题** — 自动跟随系统，支持手动切换
- **🔍 聚合搜索** — 集成百度、Google、Bing，一键多引擎搜索
- **🌐 网络模式** — 自动检测局域网/远程，支持手动切换域名、IPv6
- **🏘️ 网上邻居** — 支持添加邻居服务器服务
- **🙈 地址隐藏** — 服务地址默认模糊遮挡，点击显示
- **📱 响应式** — 完美适配手机、平板、桌面

## 📦 部署

```bash
# 1. 克隆仓库
git clone https://github.com/你的用户名/nav-page.git
cd nav-page

# 2. 创建配置文件
cp config.example.js config.js
# 编辑 config.js 填入你的实际配置

# 3. 启动服务
python3 server.py

# 4. 或使用 systemd
sudo cp nav-page.service /etc/systemd/system/
sudo systemctl enable --now nav-page
```

## 📁 文件结构

```
├── index.html          # 主页面（HTML + CSS + JS）
├── config.example.js   # 配置模板
├── config.js           # 实际配置（gitignore）
├── server.py           # Python 双栈 HTTP 服务器
├── nav-page.service    # systemd 服务文件
└── .gitignore
```

## ⚙️ 配置说明

编辑 `config.js`：

```javascript
const CONFIG = {
  LAN_IP: '192.168.1.100',        // 本机局域网 IP
  DOMAIN: 'example.com',           // 域名
  IPV6: '::1',                     // IPv6 地址
  NEIGHBOR_LAN: '192.168.1.101',   // 邻居服务器 IP
  NEIGHBOR_DOMAIN: 'nas.example.com',
  AUTH_PASSWORD: 'your_password',  // 访问密码
  SERVICES: [                      // 本机服务
    { icon:'🔧', name:'Service', desc:'Description', port:8080, tags:['tag'] }
  ],
  NEIGHBOR_SERVICES: []            // 邻居服务
};
```

## 🔒 安全说明

- `config.js` 包含敏感信息，已在 `.gitignore` 中排除
- 密码验证为前端实现，适合个人使用场景
- 建议配合反向代理 + HTTPS 使用

## 📄 License

MIT
