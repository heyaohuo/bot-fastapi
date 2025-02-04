# 使用官方的 Python 作为基础镜像
FROM python:3.11

# 设置工作目录
WORKDIR /app

# 复制当前目录的所有文件到工作目录中
COPY . /app/

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 暴露应用运行的端口
EXPOSE 8080

# 运行 FastAPI 应用
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
