import base64, zlib
code = b'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'
exec(zlib.decompress(base64.b64decode(code)).decode(), globals())
