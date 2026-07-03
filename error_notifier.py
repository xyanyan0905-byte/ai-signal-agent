# error_notifier.py
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os

def send_error_email(step_name, error):
    sender = os.environ.get("EMAIL_SENDER")
    password = os.environ.get("EMAIL_PASSWORD")
    receiver = os.environ.get("EMAIL_RECEIVER")
    smtp_server = os.environ.get("SMTP_SERVER", "smtp.qq.com")
    smtp_port = int(os.environ.get("SMTP_PORT", 465))

    subject = f"[ai-signal-agent] {step_name} 失败"
    body = f"步骤: {step_name}\n错误信息: {error}"

    msg = MIMEText(body, "plain", "utf-8")
    msg["Subject"] = Header(subject, "utf-8")
    msg["From"] = sender
    msg["To"] = receiver

    try:
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(sender, password)
            server.sendmail(sender, [receiver], msg.as_string())
        print(f"✅ 错误邮件已发送: {step_name}")
    except Exception as e:
        print(f"⚠️ 发送错误邮件失败: {e}")