class FireBase:
    def company_products(self, phone):
        import firebase_admin
        firebase_admin._apps.clear()
        from firebase_admin import credentials, initialize_app, db
        if not firebase_admin._apps:
            try:
                cred = credentials.Certificate("credential/farmzon-abdcb-c4c57249e43b.json")
                initialize_app(cred, {'databaseURL': 'https://farmzon-abdcb.firebaseio.com/'})
                store = db.reference("Shoppy").child("Company").child(phone).child('products')
                stores = store.get()
                print(stores)
                return stores
            except:
                return "No Internet!"

    def get_sellers(self):
        import firebase_admin
        firebase_admin._apps.clear()
        from firebase_admin import credentials, initialize_app, db
        if not firebase_admin._apps:
            try:
                cred = credentials.Certificate("credential/farmzon-abdcb-c4c57249e43b.json")
                initialize_app(cred, {'databaseURL': 'https://farmzon-abdcb.firebaseio.com/'})
                store = db.reference("Users")
                stores = store.get()
                print(stores)
                return stores
            except:
                return "No Internet!"

#FireBase.get_sellers(FireBase())
