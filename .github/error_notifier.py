import smtplib
import traceback
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
import os


# Signal Agent 用环境变量读取，不依赖 config.py
# 在 GitHub Actions secrets 里配置这三个变量：
# GMAIL_SENDER / GMAIL_PASSWORD / GMAIL_RECEIVER
EMAIL_SENDER   = os.getenv("GMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("GMAIL_PASSWORD")
EMAIL_RECEIVER = os.getenv("GMAIL_RECEIVER")


def send_error_email(step: str, error: Exception):
    """
    程序任意位置报错时，发邮件通知。
    step: 出错的步骤名，比如 "RSS抓取" / "AI评分筛选" / "推文生成"
    error: 捕获到的异常对象
    """
    if not all([EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECEIVER]):
        print("❌ 邮件环境变量未配置，无法发送报错通知")
        print(f"报错步骤：{step}，错误：{error}")
        return

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    error_type = type(error).__name__
    error_msg = str(error)
    tb = traceback.format_exc()

    html = f"""
    <html><body style="font-family:Arial,sans-serif;max-width:700px;margin:auto;padding:20px">
    <h2 style="color:#e94560;border-bottom:2px solid #e94560;padding-bottom:10px">
        🚨 AI Signal Agent · 运行报错通知
    </h2>
    <table style="width:100%;border-collapse:collapse;margin:20px 0">
        <tr style="background:#f9f9f9">
            <td style="padding:10px;font-weight:bold;width:120px">报错时间</td>
            <td style="padding:10px">{now}</td>
        </tr>
        <tr>
            <td style="padding:10px;font-weight:bold">出错步骤</td>
            <td style="padding:10px;color:#e94560"><b>{step}</b></td>
        </tr>
        <tr style="background:#f9f9f9">
            <td style="padding:10px;font-weight:bold">错误类型</td>
            <td style="padding:10px">{error_type}</td>
        </tr>
        <tr>
            <td style="padding:10px;font-weight:bold">错误信息</td>
            <td style="padding:10px">{error_msg}</td>
        </tr>
    </table>
    <div style="background:#1a1a2e;padding:15px;border-radius:8px">
        <p style="color:#e94560;margin:0 0 10px 0;font-weight:bold">完整报错堆栈：</p>
        <pre style="color:#f0f0f0;font-size:12px;white-space:pre-wrap;margin:0">{tb}</pre>
    </div>
    <p style="color:#999;font-size:12px;margin-top:20px">
        由 AI Signal Agent 自动发送 · 请及时处理
    </p>
    </body></html>
    """

    msg = MIMEMultipart('alternative')
    msg['Subject'] = f"🚨 Signal Agent报错 · {step} · {now}"
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECEIVER
    msg.attach(MIMEText(html, 'html'))

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
        print(f"🚨 报错通知已发送至 {EMAIL_RECEIVER}")
    except Exception as e:
        print(f"❌ 报错通知发送失败：{e}")