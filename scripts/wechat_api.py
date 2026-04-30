#!/usr/bin/env python3
"""
微信公众号文章发布工具
使用 wx.limyai.com 第三方代理服务发布到微信草稿箱
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

import markdown
import requests

API_BASE = "https://wx.limyai.com/api/openapi"


def get_api_key():
    """获取API密钥"""
    api_key = os.environ.get("WECHAT_API_KEY")
    if not api_key:
        print("错误: 未设置 WECHAT_API_KEY 环境变量", file=sys.stderr)
        sys.exit(1)
    return api_key


def get_headers(api_key):
    """构建请求头"""
    return {
        "X-API-Key": api_key,
        "Content-Type": "application/json",
    }


def list_accounts(api_key):
    """列出已授权的微信公众号"""
    headers = get_headers(api_key)
    resp = requests.post(
        f"{API_BASE}/wechat-accounts",
        headers=headers,
        json={},
        timeout=30,
    )
    data = resp.json()
    if data.get("code") != 0 and data.get("success") is not True:
        # Try alternative response format
        if "accounts" not in data and "data" not in data:
            print(f"获取账号列表失败: {json.dumps(data, ensure_ascii=False)}", file=sys.stderr)
            return []
    # Handle different response formats
    accounts = data.get("accounts", data.get("data", []))
    if isinstance(accounts, dict):
        accounts = accounts.get("list", [accounts])
    return accounts


def md_to_wechat_html(md_content):
    """将Markdown转换为微信公众号兼容的HTML"""
    html_body = markdown.markdown(
        md_content,
        extensions=["tables", "fenced_code"],
    )

    styled_html = f"""<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 16px; line-height: 1.8; color: #333; max-width: 100%; word-wrap: break-word;">

{html_body}

</div>"""

    styled_html = styled_html.replace("<table>", '<table style="border-collapse: collapse; width: 100%; margin: 16px 0; font-size: 14px;">')
    styled_html = styled_html.replace("<th>", '<th style="border: 1px solid #ddd; padding: 8px 12px; background-color: #f5f5f5; text-align: left;">')
    styled_html = styled_html.replace("<td>", '<td style="border: 1px solid #ddd; padding: 8px 12px;">')
    styled_html = styled_html.replace("<h1>", '<h1 style="font-size: 24px; font-weight: bold; margin: 24px 0 16px; color: #1a1a1a;">')
    styled_html = styled_html.replace("<h2>", '<h2 style="font-size: 20px; font-weight: bold; margin: 20px 0 12px; color: #1a1a1a;">')
    styled_html = styled_html.replace("<h3>", '<h3 style="font-size: 18px; font-weight: bold; margin: 16px 0 10px; color: #1a1a1a;">')
    styled_html = styled_html.replace("<p>", '<p style="margin: 10px 0;">')
    styled_html = styled_html.replace("<blockquote>", '<blockquote style="border-left: 4px solid #ddd; padding: 8px 16px; margin: 16px 0; color: #666;">')
    styled_html = styled_html.replace("<code>", '<code style="background-color: #f5f5f5; padding: 2px 6px; border-radius: 3px; font-size: 14px;">')
    styled_html = styled_html.replace("<strong>", '<strong style="font-weight: bold; color: #1a1a1a;">')
    styled_html = styled_html.replace("<a ", '<a style="color: #576b95; text-decoration: none;" ')

    return styled_html


def extract_title(md_content):
    """从Markdown内容中提取标题"""
    lines = md_content.strip().split("\n")
    for line in lines:
        line = line.strip()
        if line.startswith("# "):
            title = re.sub(r'^#\s*', '', line).strip()
            # 清理emoji
            title = re.sub(r'[\U0001F4F0-\U0001F9FF]', '', title).strip()
            if title:
                return title[:64]  # 微信标题最长64字符
    return "GitHub Agent/Skills 日报"


def extract_digest(md_content):
    """从Markdown内容中提取摘要"""
    lines = md_content.strip().split("\n")
    for line in lines:
        line = line.strip()
        if line.startswith(">") and "数据来源" in line:
            continue
        if line.startswith(">") and line.strip() != ">":
            digest = re.sub(r'^>\s*', '', line).strip()
            return digest[:120]
    for line in lines:
        line = line.strip()
        if not line.startswith("#") and not line.startswith(">") and not line.startswith("---") and line:
            return line[:120]
    return "GitHub Agent/Skills 热门项目日报"


def publish_article(api_key, appid, title, content, digest="", content_format="html", article_type="news"):
    """发布文章到微信公众号草稿箱"""
    headers = get_headers(api_key)
    payload = {
        "wechatAppid": appid,
        "title": title,
        "content": content,
        "summary": digest[:120] if digest else "",
        "contentFormat": content_format,
        "articleType": article_type,
    }

    resp = requests.post(
        f"{API_BASE}/wechat-publish",
        headers=headers,
        json=payload,
        timeout=60,
    )
    data = resp.json()
    return data


def cmd_list_accounts(args):
    """列出已授权账号"""
    api_key = get_api_key()
    accounts = list_accounts(api_key)
    if not accounts:
        print("未找到已授权的微信公众号")
        return
    print(f"找到 {len(accounts)} 个已授权账号:")
    for acc in accounts:
        appid = acc.get("wechatAppid", acc.get("appid", "N/A"))
        name = acc.get("name", acc.get("nickname", "N/A"))
        acc_type = acc.get("type", acc.get("serviceType", "N/A"))
        verified = acc.get("verified", acc.get("isVerified", False))
        status = acc.get("status", "N/A")
        print(f"  - {name} (AppID: {appid}, 类型: {acc_type}, 认证: {verified}, 状态: {status})")


def cmd_publish(args):
    """发布文章到草稿箱"""
    api_key = get_api_key()

    # 读取文件
    if args.markdown:
        file_path = Path(args.markdown)
        content_format = "markdown"
    elif args.html:
        file_path = Path(args.html)
        content_format = "html"
    else:
        print("错误: 请指定 --markdown 或 --html 文件", file=sys.stderr)
        sys.exit(1)

    if not file_path.exists():
        print(f"错误: 文件不存在: {file_path}", file=sys.stderr)
        sys.exit(1)

    file_content = file_path.read_text(encoding="utf-8")

    # 提取标题和摘要
    title = extract_title(file_content)
    digest = extract_digest(file_content)

    # 确定内容格式
    if content_format == "markdown":
        # 使用HTML格式发布（微信兼容性更好）
        html_content = md_to_wechat_html(file_content)
        publish_content = html_content
        publish_format = "html"
    else:
        publish_content = file_content
        publish_format = "html"

    article_type = getattr(args, "type", "news") or "news"

    print(f"📝 标题: {title}")
    print(f"📋 摘要: {digest[:80]}...")
    print(f"📄 内容格式: {publish_format}")
    print(f"📂 文章类型: {article_type}")

    # 发布
    print("\n📤 正在发布到草稿箱...")
    try:
        result = publish_article(
            api_key=api_key,
            appid=args.appid,
            title=title,
            content=publish_content,
            digest=digest,
            content_format=publish_format,
            article_type=article_type,
        )

        # 检查结果
        if result.get("code") == 0 or result.get("success") is True or "media_id" in result:
            media_id = result.get("media_id", result.get("data", {}).get("media_id", "N/A"))
            print(f"✅ 发布成功! media_id: {media_id}")
        else:
            error_msg = result.get("message", result.get("msg", json.dumps(result, ensure_ascii=False)))
            print(f"❌ 发布失败: {error_msg}", file=sys.stderr)
            sys.exit(1)
    except Exception as e:
        print(f"❌ 发布异常: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="微信公众号文章发布工具")
    subparsers = parser.add_subparsers(dest="command")

    # list-accounts 命令
    subparsers.add_parser("list-accounts", help="列出已授权的微信公众号")

    # publish 命令
    publish_parser = subparsers.add_parser("publish", help="发布文章到草稿箱")
    publish_parser.add_argument("--appid", required=True, help="微信公众号AppID")
    publish_parser.add_argument("--markdown", help="Markdown文件路径")
    publish_parser.add_argument("--html", help="HTML文件路径")
    publish_parser.add_argument("--type", choices=["news", "newspic"], default="news", help="文章类型")

    args = parser.parse_args()

    if args.command == "list-accounts":
        cmd_list_accounts(args)
    elif args.command == "publish":
        cmd_publish(args)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
