import flet as ft
from supabase_client import supabase


def main(page: ft.Page):
    # 页面基础设置
    page.title = "Supabase + Flet 乐器列表"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 30

    # 从 Supabase 查询数据
    try:
        response = supabase.table("instruments").select("*").execute()
        instruments = response.data
    except Exception as e:
        page.add(ft.Text(f"查询失败: {e}", color=ft.Colors.RED))
        return

    # 构建界面元素
    items = []
    for item in instruments:
        items.append(
            ft.ListTile(
                leading=ft.Icon(ft.Icons.MUSIC_NOTE),
                title=ft.Text(item["name"]),
                subtitle=ft.Text(f"ID: {item['id']}")
            )
        )

    # 将组件添加到页面
    page.add(
        ft.Text("乐器列表", size=32, weight=ft.FontWeight.BOLD),
        ft.Divider(),
        ft.Column(items)
    )

# 启动 Flet 应用
ft.run(main)