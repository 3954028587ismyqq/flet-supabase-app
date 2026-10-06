import os
from typing import Optional
from dotenv import load_dotenv
from supabase import create_client, Client


load_dotenv()

# 从环境变量读取配置
SUPABASE_URL: Optional[str] = os.environ.get("SUPABASE_URL")
SUPABASE_KEY: Optional[str] = os.environ.get("SUPABASE_KEY")

# 创建并导出 Supabase 客户端实例
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

print(f"Supabase 客户端已初始化，连接至 {SUPABASE_URL}")