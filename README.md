# 說明
這是一個幣別轉換器
使用Python3.10以及Django4.2.2版完成

api路徑在/currency-converter/currency-converter/底下
使用get方法
後面的參數帶入source, target, amount

檔案都在CurrencyConverter底下
我將他細分為validator(驗證參數用)以及usecase(實際轉換用)

# 實際使用
若要在本機執行
我有提供一個Dockerfile
下以下的指令即可執行
```bash
docker build -t [your-image-name] .
docker run -p 8000:8000 [your-image-name]
```

之後使用api測試工具、直接使用瀏覽器拜訪、寫程式測試
格式如下
```
yourServerURL/currency-converter/currency-converter/?source=USD&target=JPY&amount=$1,525
```
後面的參數帶入source, target, amount即可看到回應
失敗時會告知原因，成功即可看到資訊
以上述為例
會得到
```
{
    "msg": "Success",
    "amount": "$170,496.53"
}
```

# 單元測試
如想測試function是否正常運作，可以到manage.py的同層目錄使用以下指令
```
python manage.py test
```
