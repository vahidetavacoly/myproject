class userauth():
    def __init__(self):
        self.state=False#دو تا پراپرتری دو تابع سازنده ساختیم یکی به نام وضعیت و دیگری به نام مشخصات حساب
        self.user=None#تو این تابع خودمون میسازیم که این دو تا پراپرتی را قانون میکنیم.انگار اولی وضعیت لاگین ما رو داره دومی مشخصات حساب رو داره

    def state_and_login(self,request):
        if request.user.is_authenticated:#ایا کاربر لاگین هست یا نه
            self.user=request.user#حلا بیا مشخصات کاربر رو بریز توی این متغیر
            self.state=True
            dic={"state": self.state,"user":self.user}
            return dic
        else:
            self.user = None
            self.state = False

            dic={"state": self.state,"user":self.user}
            return dic