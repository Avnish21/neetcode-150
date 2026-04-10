class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            if s == "":
                encoded.append("")
            else:
                encoded.append(s.encode("utf-8").hex())
        print(encoded)
        return "%__%" + "%__%".join(encoded) if len(strs) > 0 else ''

    def decode(self, s: str) -> List[str]:
        sList = s.split("%__%") if len(s) > 0 else []
        print(sList, len(s), s)
        result = []
        for st in sList:
            bytes_object = bytes.fromhex(st)
            result.append(bytes_object.decode("utf-8"))
        return result[1:]