class KunaException(Exception):
    def __init__(self, result):
        try:
            self.message = result["error"]["message"]
            self.code = result["error"].get("code")
        except:
            self.message = result

        Exception.__init__(self, self.message)
