from .excepts import UnSupportedException

def preprecess(code: str):
    if code.startswith(('51', '600', '601', '602')):
        prefix = "sh"
    elif code.startswith(('15','16', '000')):
        prefix = "sz"
    elif code[0].isalpha():
        prefix = ""
    else:
        raise UnSupportedException(f"暂不支持当前类型的股票: {code}")
    return f"{prefix}{code}"
