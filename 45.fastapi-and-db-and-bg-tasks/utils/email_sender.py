from asyncio import sleep


async def send_email(
    send_to: str,
    subject: str,
    text: str,
):
    print(f"send email to {send_to!r}, subj: {subject!r}")
    print(text)
    await sleep(1)
    print("email sent")
