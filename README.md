# 实验室管理系统

基于 Vue 和 FastAPI 的实验室管理系统，提供实验室与设备管理、预约及审核、用户管理和 AI 助手等功能。

## 环境要求

- Python（建议使用虚拟环境）
- Node.js `^22.18.0` 或 `>=24.12.0`，以及 npm
- MySQL 数据库
- 兼容 OpenAI API 的模型服务

## 启动后端

1. 创建 MySQL 数据库，例如 `lab_agent`。
2. 将 `backend/.env.example` 复制为 `backend/.env`，填写数据库连接、JWT 密钥和模型服务配置。`JWT_ALGORITHM` 和 `JWT_EXPIRE_HOURS` 有默认值；其他配置项需要填写。
3. 在项目根目录运行：

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

首次启动会创建数据表，并尝试加载 `BAAI/bge-small-zh-v1.5` 向量模型，可能需要下载模型文件。后端 API 文档位于 <http://127.0.0.1:8000/docs>。

## 启动前端

在另一个终端中，从项目根目录运行：

```powershell
cd frontend
npm install
npm run dev
```

浏览器访问终端显示的地址（通常为 <http://localhost:5173>）。开发服务器默认将 `/api` 和 `/uploads` 转发到 `http://127.0.0.1:8000`。如需指定其他 API 地址，可在 `frontend/.env.local` 中设置 `VITE_API_BASE_URL`。

## 数据与文件

- `backend/data/kb/`：知识库 Markdown 文件；向量库首次为空时会读取其中的 `.md` 文件。
- `backend/data/chroma/`：本地向量库数据。
- `backend/uploads/`：上传的文件。

这些运行时数据和本地环境配置不应提交到版本控制。前端生产构建可在 `frontend` 目录运行 `npm run build`。
